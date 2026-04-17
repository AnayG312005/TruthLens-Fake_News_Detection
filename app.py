from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

import requests
import xml.etree.ElementTree as ET
import re
from urllib.parse import quote_plus
from difflib import SequenceMatcher

app = Flask(__name__)

with open("finalized_model.pk1", "rb") as f:
    model = pickle.load(f)

df = pd.read_csv("news.csv")
labels = df.label

x_train, x_test, y_train, y_test = train_test_split(
    df["text"], labels, test_size=0.2, random_state=20
)

vector = TfidfVectorizer(stop_words="english", max_df=0.7)
vector.fit(x_train)


def normalize_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def similarity(a, b):
    a_norm = normalize_text(a)
    b_norm = normalize_text(b)

    seq_score = SequenceMatcher(None, a_norm, b_norm).ratio()

    a_tokens = set(a_norm.split())
    b_tokens = set(b_norm.split())

    if not a_tokens or not b_tokens:
        return seq_score

    jaccard_score = len(a_tokens & b_tokens) / len(a_tokens | b_tokens)

    return (0.65 * seq_score) + (0.35 * jaccard_score)


def get_live_headline_matches(query, max_items=8):
    rss_url = (
        "https://news.google.com/rss/search?q="
        f"{quote_plus(query)}&hl=en-IN&gl=IN&ceid=IN:en"
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(rss_url, headers=headers, timeout=10)
    response.raise_for_status()

    root = ET.fromstring(response.content)

    matches = []
    items = root.findall(".//item")[:max_items]

    for item in items:
        title = item.findtext("title", default="")
        link = item.findtext("link", default="")
        score = similarity(query, title)

        matches.append({
            "title": title,
            "link": link,
            "score": round(score, 3)
        })

    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches


def model_predict(text):
    text_vector = vector.transform([text])
    prediction = model.predict(text_vector)[0]

    if str(prediction).upper() == "REAL" or prediction == 1:
        return "Real News"
    return "Fake News"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predictions", methods=["GET", "POST"])
def predictions():
    if request.method == "POST":
        news = request.form.get("news", "").strip()

        if not news:
            return render_template(
                "predictions.html",
                prediction_text="Please enter some news text.",
                news_text="",
                live_matches=[]
            )

        model_result = model_predict(news)

        live_matches = []
        best_live_score = 0.0

        try:
            live_matches = get_live_headline_matches(news)
            if live_matches:
                best_live_score = live_matches[0]["score"]
        except Exception:
            live_matches = []

        # Hybrid decision logic
        if best_live_score >= 0.65:
            final_result = "Real News"
        elif best_live_score >= 0.45:
            if model_result == "Real News":
                final_result = "Likely Real News"
            else:
                final_result = "Unverified News"
        else:
            if model_result == "Real News":
                final_result = "Real News"
            else:
                final_result = "Fake News"

        return render_template(
            "predictions.html",
            prediction_text=final_result,
            news_text=news,
            live_matches=live_matches
        )

    return render_template(
        "predictions.html",
        prediction_text="",
        news_text="",
        live_matches=[]
    )


if __name__ == "__main__":
    app.run(debug=True)
