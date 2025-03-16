import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nltk.download('stopwords')
nltk.download('punkt')

st.title(" Spam Email Classification")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin-1')

    df = df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1)

    df.rename(columns={"v1": "target", "v2": "text"}, inplace=True)

    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    df['target'] = encoder.fit_transform(df['target'])

    ps = PorterStemmer()

    def transform_text(text):
        text = text.lower()
        text = nltk.word_tokenize(text)
        y = [ps.stem(i) for i in text if i.isalnum() and i not in stopwords.words('english') and i not in string.punctuation]
        return " ".join(y)

    df["transformed_text"] = df["text"].apply(transform_text)

    st.write("###  Processed Data Sample:")
    st.write(df.head())

    st.write("###  Spam vs Ham Distribution")
    fig, ax = plt.subplots()
    plt.pie(df["target"].value_counts(), labels=["Ham", "Spam"], autopct="%0.2f")
    st.pyplot(fig)

    cv = CountVectorizer()
    X = cv.fit_transform(df["transformed_text"]).toarray()
    y = df["target"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

    mnb = MultinomialNB()
    mnb.fit(X_train, y_train)
    y_pred = mnb.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    st.write("###  Model Performance:")
    st.write(f"**MultinomialNB Accuracy:** {accuracy:.2f}")

    st.write("## Check if a Message is Spam")

    user_input = st.text_area("Enter a message:", "")

    if st.button("Check Spam"):
        if user_input:
            transformed_input = transform_text(user_input)

            input_features = cv.transform([transformed_input]).toarray()

            prediction = mnb.predict(input_features)[0]

            if prediction == 1:
                st.error(" This message is **SPAM**!")
            else:
                st.success(" This message is **NOT SPAM**.")
        else:
            st.warning(" Please enter a message to check.")
