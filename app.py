import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer


ps = PorterStemmer()



tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

st.markdown("""
<style>
    input[type="text"] {
        height: 100px;
    }
</style>
""", unsafe_allow_html=True)

input_sms = st.text_input("Enter the message", value="", key="message_input", type="default")

# input_sms = st.text_input("Enter the message",height=100)


# Define a function to perform text transformation
def transform_text(text):
    # Step 1: Lowercasing
    text = text.lower()

    # Step 2: Tokenization
    text = nltk.word_tokenize(text)
    
    # Create an empty list to store the filtered tokens
    y = []
    
    # Step 3: Removing Special Characters
    for i in text:
        if i.isalnum():
            y.append(i)
    
    # Copy the filtered tokens back to the 'text' variable
    text = y[:]
    
    # Clear the 'y' list for the next step
    y.clear()
    
    # Step 4: Removing Stop Words and Punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    # Copy the filtered tokens back to the 'text' variable
    text = y[:]
    
    # Clear the 'y' list for the next step
    y.clear()
    
    # Step 5: Stemming
    for i in text:
        y.append(ps.stem(i))
    
    # Combine the stemmed tokens into a single string
    return " ".join(y)

if st.button('Predict'):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. Predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
