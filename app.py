from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

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
                news_text=""
            )

        news_vector = vector.transform([news])

        prediction = model.predict(news_vector)[0]

        if str(prediction).upper() == "REAL" or prediction == 1:
            result = "Real News"
        else:
            result = "Fake News"

        return render_template(
            "predictions.html",
            prediction_text=result,
            news_text=news
        )

    return render_template("predictions.html")


if __name__ == "__main__":
    app.run(debug=True)