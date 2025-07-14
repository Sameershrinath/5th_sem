import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
import numpy as np

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Initialize Porter Stemmer
ps = PorterStemmer()

# Page configuration
st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #FF6B6B;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #4ECDC4;
        font-size: 1.3rem;
        margin-bottom: 2rem;
    }
    .spam-result {
        background-color: #FFE5E5;
        color: #D32F2F;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #F44336;
        margin-top: 1rem;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .ham-result {
        background-color: #E8F5E8;
        color: #2E7D32;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin-top: 1rem;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2196F3;
        margin-bottom: 2rem;
    }
    .warning-box {
        background-color: #FFF3E0;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #FF9800;
        margin-bottom: 1rem;
    }
    .example-box {
        background-color: #F5F5F5;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #9E9E9E;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def transform_text(text):
    """
    Transform text using the same preprocessing steps as in model training
    """
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

@st.cache_resource
def load_model():
    """Load the trained model and vectorizer"""
    try:
        with open('model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        
        with open('tfidf.pkl', 'rb') as tfidf_file:
            tfidf = pickle.load(tfidf_file)
        
        return model, tfidf
    except FileNotFoundError:
        st.error("Model files not found! Please make sure 'model.pkl' and 'tfidf.pkl' are in the same directory.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.stop()

def predict_spam(text, model, tfidf):
    """Predict if the text is spam or ham"""
    # Transform the text
    transformed_text = transform_text(text)
    
    # Vectorize the text
    vectorized_text = tfidf.transform([transformed_text])
    
    # Make prediction
    prediction = model.predict(vectorized_text)[0]
    probability = model.predict_proba(vectorized_text)[0]
    
    return prediction, probability

# Main header
st.markdown('<h1 class="main-header">📧 Spam Email Classifier</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Detect spam emails using Machine Learning</p>', unsafe_allow_html=True)

# Load model
model, tfidf = load_model()

# Sidebar information
st.sidebar.title("📊 Model Information")
st.sidebar.markdown("""
**Model Details:**
- **Algorithm**: Multinomial Naive Bayes
- **Vectorizer**: TF-IDF (max 3000 features)
- **Preprocessing**: Tokenization, Stemming, Stop word removal
- **Training Data**: SMS Spam Collection Dataset

**Performance:**
- High accuracy in spam detection
- Optimized for precision to minimize false positives
""")

# Info box
st.markdown("""
<div class="info-box">
    <h3>🔍 How it works:</h3>
    <p>This classifier uses Natural Language Processing and Machine Learning to analyze text messages and emails. 
    It processes the text through several steps including tokenization, stemming, and feature extraction using TF-IDF, 
    then uses a Multinomial Naive Bayes algorithm to classify the message as spam or legitimate (ham).</p>
</div>
""", unsafe_allow_html=True)

# Create tabs for different functionalities
tab1, tab2, tab3 = st.tabs(["🔍 Single Message", "📄 Batch Processing", "📈 Examples"])

with tab1:
    st.header("Enter a Message to Classify")
    
    # Text input area
    input_text = st.text_area(
        "Enter your message here:",
        height=150,
        placeholder="Type your email or SMS message here...",
        help="Enter the complete message you want to classify"
    )
    
    # Prediction button
    if st.button("🔍 Classify Message", type="primary", use_container_width=True):
        if input_text.strip():
            with st.spinner("Analyzing message..."):
                try:
                    # Get prediction
                    prediction, probability = predict_spam(input_text, model, tfidf)
                    
                    # Display results
                    if prediction == 1:  # Spam
                        st.markdown(f"""
                        <div class="spam-result">
                            <h3>🚨 SPAM DETECTED!</h3>
                            <p>This message is classified as <strong>SPAM</strong></p>
                            <p>Confidence: {probability[1]:.2%}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:  # Ham
                        st.markdown(f"""
                        <div class="ham-result">
                            <h3>✅ LEGITIMATE MESSAGE</h3>
                            <p>This message is classified as <strong>HAM (Not Spam)</strong></p>
                            <p>Confidence: {probability[0]:.2%}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Show prediction probabilities
                    st.subheader("📊 Prediction Probabilities")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("Ham (Not Spam)", f"{probability[0]:.2%}")
                    
                    with col2:
                        st.metric("Spam", f"{probability[1]:.2%}")
                    
                    # Show processed text
                    with st.expander("🔧 Processed Text", expanded=False):
                        processed_text = transform_text(input_text)
                        st.text("Processed text:")
                        st.code(processed_text, language="text")
                        
                        st.markdown("**Processing Steps:**")
                        st.markdown("""
                        1. Convert to lowercase
                        2. Tokenize words
                        3. Remove non-alphanumeric characters
                        4. Remove stopwords and punctuation
                        5. Apply stemming
                        6. Vectorize using TF-IDF
                        """)
                
                except Exception as e:
                    st.error(f"Error during prediction: {str(e)}")
        else:
            st.warning("Please enter a message to classify.")

with tab2:
    st.header("Batch Processing")
    st.markdown("Upload a CSV file or enter multiple messages for batch classification.")
    
    # File upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Preview of uploaded data:")
            st.dataframe(df.head())
            
            # Select column for classification
            text_column = st.selectbox("Select the column containing text messages:", df.columns)
            
            if st.button("🔍 Classify All Messages"):
                with st.spinner("Processing all messages..."):
                    predictions = []
                    probabilities = []
                    
                    for text in df[text_column]:
                        try:
                            pred, prob = predict_spam(str(text), model, tfidf)
                            predictions.append("Spam" if pred == 1 else "Ham")
                            probabilities.append(prob[1])  # Spam probability
                        except:
                            predictions.append("Error")
                            probabilities.append(0.0)
                    
                    # Add results to dataframe
                    df['Prediction'] = predictions
                    df['Spam_Probability'] = probabilities
                    
                    # Display results
                    st.subheader("📊 Results")
                    st.dataframe(df)
                    
                    # Summary statistics
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        spam_count = sum(1 for p in predictions if p == "Spam")
                        st.metric("Spam Messages", spam_count)
                    
                    with col2:
                        ham_count = sum(1 for p in predictions if p == "Ham")
                        st.metric("Ham Messages", ham_count)
                    
                    with col3:
                        total_messages = len(predictions)
                        st.metric("Total Messages", total_messages)
                    
                    # Download results
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results",
                        data=csv,
                        file_name="spam_classification_results.csv",
                        mime="text/csv"
                    )
        
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    
    # Manual batch input
    st.subheader("Manual Batch Input")
    batch_text = st.text_area(
        "Enter multiple messages (one per line):",
        height=200,
        placeholder="Message 1\nMessage 2\nMessage 3\n..."
    )
    
    if st.button("🔍 Classify Batch Messages"):
        if batch_text.strip():
            messages = [msg.strip() for msg in batch_text.split('\n') if msg.strip()]
            
            with st.spinner("Processing batch messages..."):
                results = []
                
                for i, message in enumerate(messages, 1):
                    try:
                        pred, prob = predict_spam(message, model, tfidf)
                        results.append({
                            "Message #": i,
                            "Message": message[:50] + "..." if len(message) > 50 else message,
                            "Full Message": message,
                            "Prediction": "Spam" if pred == 1 else "Ham",
                            "Spam Probability": f"{prob[1]:.2%}"
                        })
                    except Exception as e:
                        results.append({
                            "Message #": i,
                            "Message": message[:50] + "..." if len(message) > 50 else message,
                            "Full Message": message,
                            "Prediction": "Error",
                            "Spam Probability": "N/A"
                        })
                
                # Display results
                results_df = pd.DataFrame(results)
                st.dataframe(results_df[["Message #", "Message", "Prediction", "Spam Probability"]])
                
                # Summary
                spam_count = sum(1 for r in results if r["Prediction"] == "Spam")
                ham_count = sum(1 for r in results if r["Prediction"] == "Ham")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Spam Messages", spam_count)
                with col2:
                    st.metric("Ham Messages", ham_count)

with tab3:
    st.header("📈 Example Messages")
    
    # Example messages
    examples = {
        "Spam Examples": [
            "FREE! Win a £1000 cash prize! Text WIN to 85233 now!",
            "URGENT! Your account will be closed. Click here to verify immediately.",
            "Congratulations! You've won a free iPhone! Claim now at freephone.com",
            "Hot singles in your area! Meet them tonight! Register free!",
            "WINNER! You've been selected for a £500 shopping voucher. Reply STOP to opt out."
        ],
        "Ham (Legitimate) Examples": [
            "Hi, are we still meeting for lunch tomorrow at 12pm?",
            "Your appointment is confirmed for Monday at 3pm. Please arrive 10 minutes early.",
            "Thanks for your help today. The presentation went really well!",
            "Can you pick up some milk on your way home? Thanks!",
            "Meeting has been rescheduled to 2pm in conference room B."
        ]
    }
    
    # Display examples with predictions
    for category, messages in examples.items():
        st.subheader(f"🔍 {category}")
        
        for i, example in enumerate(messages, 1):
            with st.expander(f"Example {i}: {example[:50]}..."):
                st.write(f"**Full Message:** {example}")
                
                # Get prediction for example
                pred, prob = predict_spam(example, model, tfidf)
                
                if pred == 1:
                    st.markdown(f"""
                    <div class="spam-result">
                        <strong>Prediction: SPAM</strong><br>
                        Confidence: {prob[1]:.2%}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="ham-result">
                        <strong>Prediction: HAM</strong><br>
                        Confidence: {prob[0]:.2%}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Show processed text
                processed = transform_text(example)
                st.text("Processed text:")
                st.code(processed, language="text")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🛡️ This spam classifier is for educational and demonstration purposes.</p>
    <p>Built with Streamlit and scikit-learn | Powered by Multinomial Naive Bayes</p>
</div>
""", unsafe_allow_html=True)

# Warning box
st.markdown("""
<div class="warning-box">
    <h4>⚠️ Important Notes:</h4>
    <ul>
        <li>This model is trained on SMS/email data and may not work perfectly on all types of messages</li>
        <li>Always verify important messages manually, especially if they seem suspicious</li>
        <li>The model's performance depends on the quality and diversity of training data</li>
        <li>Consider the context and sender when evaluating messages</li>
    </ul>
</div>
""", unsafe_allow_html=True)