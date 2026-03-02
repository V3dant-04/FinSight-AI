from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Simple training data
texts = [
    "uber ride", "ola cab", "bus ticket",
    "pizza", "burger", "swiggy order",
    "movie ticket", "netflix subscription",
    "electricity bill", "water bill",
    "gym membership", "medical bill",
    "amazon shopping", "flipkart order"
]

labels = [
    "Transport", "Transport", "Transport",
    "Food", "Food", "Food",
    "Entertainment", "Entertainment",
    "Utilities", "Utilities",
    "Health", "Health",
    "Shopping", "Shopping"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_category(description: str):
    X_test = vectorizer.transform([description])
    return model.predict(X_test)[0]
