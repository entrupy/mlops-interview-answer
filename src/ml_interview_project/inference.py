from pathlib import Path
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

MODEL_DIR = Path("model")
MODEL_PATH = MODEL_DIR / "text_classifier.joblib"

def train_and_save_model():
    texts = [
        "this is a positive example",
        "great content, really enjoyed it",
        "excellent work, very helpful",
        "this is a negative example",
        "terrible experience, waste of time",
        "poor quality, would not recommend"
    ]
    labels = ["positive"] * 3 + ["negative"] * 3
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    pipeline.fit(texts, labels)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)

def load_model():
    if not MODEL_PATH.exists():
        train_and_save_model()
    return joblib.load(MODEL_PATH)

def predict_text(text, model):
    return model.predict([text])[0]