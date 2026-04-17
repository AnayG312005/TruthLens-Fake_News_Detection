# TruthLens: Fake News Detection Web Application

## 1. Introduction

In the digital era, information spreads faster than ever before. While this rapid dissemination of news has many advantages, it also comes with a significant downside—the widespread circulation of misinformation and fake news. False or misleading information can influence public opinion, create panic, manipulate markets, and even impact democratic processes. To address this growing concern, **TruthLens: Fake News Detection** has been developed as an intelligent, AI-powered web application designed to help users verify the authenticity of news content quickly and efficiently.

TruthLens leverages machine learning techniques to analyze textual data and determine whether a given news headline or article is likely to be real or fake. The application provides users with an intuitive interface where they can input news content and receive instant predictions along with supporting insights. Additionally, the system enhances credibility by showing related live headlines, enabling users to cross-check information with real-time sources.

This project combines the power of **Python**, **Machine Learning**, **Flask**, and **modern frontend technologies like Tailwind CSS** to create a seamless and visually appealing experience. The goal is not only to provide accurate predictions but also to promote awareness and critical thinking among users when consuming online information.

---

## 2. Objectives

The primary objectives of the TruthLens application are:

* To detect fake news using machine learning algorithms.
* To provide real-time prediction results based on user input.
* To create a user-friendly and responsive web interface.
* To help users verify information using related live news sources.
* To reduce the spread of misinformation by empowering users with AI tools.

---

## 3. Key Features

### 3.1 AI-Powered News Classification

TruthLens uses a trained machine learning model to classify news as:

* Real News
* Likely Real News
* Fake News

The classification is based on patterns learned from large datasets of labeled news articles.

### 3.2 Real-Time Prediction

Users can input any news headline and instantly receive a prediction. The system processes the input in real time, ensuring minimal delay and a smooth experience.

### 3.3 Live News Matching

To enhance credibility, the application fetches related live headlines. This feature allows users to compare their input with actual news articles available online.

### 3.4 Modern UI/UX Design

The interface is designed using Tailwind CSS, ensuring:

* Clean layout
* Responsive design
* Smooth animations
* Professional look and feel

### 3.5 Clear and Interactive Dashboard

The application includes:

* Input field for news text
* Prediction result section with color indicators
* Related headlines section
* Testimonials and user trust indicators

---

## 4. System Architecture

TruthLens follows a simple yet effective architecture consisting of three main components:

### 4.1 Frontend

The frontend is built using:

* HTML5
* Tailwind CSS
* JavaScript

It handles user interaction, form submission, and dynamic UI updates.

### 4.2 Backend

The backend is developed using Flask, a lightweight Python web framework. It is responsible for:

* Handling HTTP requests
* Processing user input
* Communicating with the machine learning model
* Rendering templates with prediction results

### 4.3 Machine Learning Model

The ML component includes:

* A trained classification model (e.g., Logistic Regression or Naive Bayes)
* A vectorizer (such as TF-IDF) for text transformation

The model processes textual input and outputs a prediction label.

---

## 5. Technology Stack

The application uses the following technologies:

### Backend:

* Python
* Flask

### Machine Learning:

* Scikit-learn
* Pandas
* NumPy

### Frontend:

* HTML
* Tailwind CSS
* JavaScript

### Deployment (optional):

* Render / Heroku / AWS

---

## 6. Working of the Application

The workflow of TruthLens can be described step-by-step:

1. The user enters a news headline into the input field.
2. The form sends a POST request to the Flask backend.
3. The backend receives the input and preprocesses it.
4. The text is transformed using a vectorizer.
5. The processed input is passed to the trained model.
6. The model predicts whether the news is real or fake.
7. The result is sent back to the frontend.
8. The UI updates dynamically to display:

   * Prediction result
   * Input text
   * Related headlines (if available)

---

## 7. Machine Learning Approach

### 7.1 Data Collection

The model is trained on datasets containing labeled news articles categorized as real or fake. These datasets may include:

* News headlines

### 7.2 Data Preprocessing

Steps include:

* Removing punctuation
* Converting text to lowercase
* Removing stopwords
* Tokenization

### 7.3 Feature Extraction

The text is converted into numerical format using:

* TF-IDF Vectorization

### 7.4 Model Training

Common algorithms used:

* Logistic Regression
* Naive Bayes
* Passive Aggressive Classifier

### 7.5 Model Evaluation

Metrics used:

* Accuracy
* Precision
* Recall
* F1 Score

---

## 8. User Interface Overview

### 8.1 Home Page

The home page introduces the platform and includes:

* Hero section
* Call-to-action button
* Statistics (accuracy, usage)
* Testimonials

### 8.2 Prediction Page

This is the core functionality page where users:

* Enter news text
* Get prediction results
* View related headlines

### 8.3 Result Visualization

The result section uses color coding:

* Green → Real News
* Red → Fake News
* Yellow → Uncertain / Likely

---

## 9. Advantages of the System

* Fast and accurate predictions
* Easy-to-use interface
* Real-time processing
* Helps combat misinformation
* Scalable and extendable

---

## 10. Limitations

While TruthLens is powerful, it has some limitations:

* Accuracy depends on training data quality
* Cannot verify extremely new or unseen topics perfectly
* May struggle with sarcasm or complex language
* Relies on text input only (no image/video verification)

---

## 11. Future Enhancements

The system can be improved by adding:

* Deep learning models (LSTM, BERT)
* Multilingual support
* Image and video fake detection
* Browser extension integration
* API for third-party usage
* Confidence score display
* User authentication and history tracking

---

## 12. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone [https://github.com/AnayG312005/TruthLens-Fake_News_Detection.git]
cd fake_news_detection
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

```
http://127.0.0.1:5000/
```

---

## 13. Project Structure

```
truthlens/
│
├── static/
├── templates/
│   ├── index.html
│   ├── prediction.html
│
├── model/
│   ├── model.pkl
│   ├── vectorizer.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 14. Use Cases

TruthLens can be used by:

* Students for research verification
* Journalists for fact-checking
* General users to verify news
* Researchers studying misinformation
* Social media users to validate viral posts

---

## 15. Conclusion

TruthLens is a practical and impactful application designed to address one of the most pressing challenges of the digital age—fake news. By integrating machine learning with a user-friendly web interface, it empowers individuals to verify information quickly and confidently.

The system demonstrates how AI can be used responsibly to improve information reliability and promote digital literacy. Although it is not a complete replacement for professional fact-checking, it serves as a powerful first step in identifying potentially misleading content.

As misinformation continues to evolve, tools like TruthLens will play a crucial role in building a more informed and aware society. With further enhancements and scalability, the platform has the potential to become a comprehensive solution for news verification across multiple domains and formats.

---

## 16 . Output

<img width="1335" height="625" alt="home" src="https://github.com/user-attachments/assets/af7097da-336c-4d27-84d4-af7ff27dcbb5" />

<img width="1338" height="629" alt="home1" src="https://github.com/user-attachments/assets/60140e30-e4b9-44b8-8879-1e4d1f7bc888" />

<img width="1336" height="609" alt="prediction" src="https://github.com/user-attachments/assets/7981517e-05a8-4b4d-a853-4adc76421498" />

<img width="1299" height="625" alt="Screenshot (1020)" src="https://github.com/user-attachments/assets/7f919bea-950d-4f7c-a575-f2165c1e3c4f" />

<img width="1299" height="609" alt="Screenshot (1021)" src="https://github.com/user-attachments/assets/be8619ea-313f-423f-a6e7-1db9d0e2ac30" />


**TruthLens — See the truth clearly.**
