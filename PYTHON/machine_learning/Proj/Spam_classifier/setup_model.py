"""
Script to export the trained model and vectorizer from the notebook
Run this after training your model in the notebook
"""

import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def transform_text(text):
    """
    Transform text using the same preprocessing steps as in model training
    """
    ps = PorterStemmer()
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize
    text = nltk.word_tokenize(text)
    
    # Remove non-alphanumeric characters
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y.copy()
    y.clear()
    
    # Remove stopwords and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text = y.copy()
    y.clear()
    
    # Apply stemming
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

def create_and_save_model():
    """
    Create and save the model if model files don't exist
    """
    print("Creating model from scratch...")
    
    # You would need to add your dataset path here
    # For now, this is a placeholder
    print("Please run your Model_training.ipynb notebook first to generate model.pkl and tfidf.pkl files")
    print("Or place your spam.csv dataset in the Data folder and uncomment the code below:")
    
    """
    # Load data
    df = pd.read_csv("./Data/spam.csv", encoding='latin1')
    
    # Clean data
    df = df.drop(["Unnamed: 4", "Unnamed: 3", "Unnamed: 2"], axis=1)
    df.rename(columns={"v1": "target", "v2": "text"}, inplace=True)
    
    # Encode target
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    df['target'] = encoder.fit_transform(df['target'])
    
    # Transform text
    df['transformed_text'] = df['text'].apply(transform_text)
    
    # Create TF-IDF vectorizer
    tfidf = TfidfVectorizer(max_features=3000)
    X = tfidf.fit_transform(df['transformed_text']).toarray()
    y = df['target'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2, test_size=0.2)
    
    # Train model
    mnb = MultinomialNB()
    mnb.fit(X_train, y_train)
    
    # Save model and vectorizer
    with open('model.pkl', 'wb') as model_file:
        pickle.dump(mnb, model_file)
    
    with open('tfidf.pkl', 'wb') as tfidf_file:
        pickle.dump(tfidf, tfidf_file)
    
    print("Model and vectorizer saved successfully!")
    """

def check_model_files():
    """
    Check if model files exist
    """
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('tfidf.pkl', 'rb') as f:
            tfidf = pickle.load(f)
        print("✅ Model files found and loaded successfully!")
        return True
    except FileNotFoundError:
        print("❌ Model files not found!")
        return False

if __name__ == "__main__":
    print("Spam Classifier Model Setup")
    print("=" * 40)
    
    if not check_model_files():
        create_and_save_model()
    else:
        print("Model files are ready! You can now run the Streamlit app.")
        print("Run: streamlit run Main.py")
