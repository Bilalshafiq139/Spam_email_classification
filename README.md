# Spam_email_classification
This project is a **machine learning-based spam email classifier** built using **Streamlit**, `scikit-learn`, and `NLTK`. It allows users to upload a CSV file containing emails, processes the text data, trains a **Naïve Bayes model**, and provides a **real-time spam detection feature**.



Here is a **properly formatted** README file for your **Spam Email Classification** project. You can **copy and paste** this into a `README.md` file for your GitHub repository.  

---

### **README.md**
```markdown
# Spam Email Classification with Streamlit

This project is a **machine learning-based spam email classifier** built using **Streamlit**, `scikit-learn`, and `NLTK`. It allows users to upload a CSV file containing emails, processes the text data, trains a **Naïve Bayes model**, and provides a **real-time spam detection feature**.

---

## Features
- Upload a **CSV file** containing email data
- Perform **text preprocessing** (tokenization, stemming, stopword removal)
- Generate **data visualizations** for spam vs. ham distribution
- Train a **Multinomial Naïve Bayes** classification model
- Predict if a given message is **spam or not** in real time using the trained model

---

## Project Structure
```
Spam-Email-Classifier/
│── app.py             # Main Streamlit application
│── requirements.txt   # Dependencies
│── README.md          # Project documentation
│── data/              # Directory for sample email datasets
```

---

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/Spam-Email-Classifier.git
cd Spam-Email-Classifier
```

### 2. Create a Virtual Environment (Optional)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

---

## How to Run the Application

### 1. Start the Streamlit App
```sh
streamlit run app.py
```

### 2. Upload a CSV File
- The dataset must contain columns `v1` (spam/ham labels) and `v2` (email text).  
- The app **automatically processes** the uploaded data.

### 3. Real-Time Spam Detection
- Enter an email message into the text box.
- Click "Check Spam".
- The model will classify the message as **SPAM** or **NOT SPAM**.

---

## Technologies Used
- **Python 3.8+**
- **Streamlit** – Interactive Web App
- **NLTK** – Text Preprocessing (Tokenization, Stemming, Stopword Removal)
- **Scikit-Learn** – Machine Learning Model (Naïve Bayes Classifier)
- **Matplotlib & Seaborn** – Data Visualization
- **Pandas & NumPy** – Data Processing

---

## Example Spam Message for Testing
Try entering the following message to test the classifier:
```
Congratulations! You have won a FREE iPhone! Click the link to claim your prize: http://spam-link.com
```

Expected output: **SPAM**

---

## Contributing
1. Fork the repository  
2. Create a new branch  
3. Submit a pull request  




