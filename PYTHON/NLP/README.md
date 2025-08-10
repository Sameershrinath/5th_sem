# 🧠 NLTK Operations - NLP Text Analysis App

This is a simple and interactive Natural Language Processing (NLP) app built using **Streamlit** and **NLTK (Natural Language Toolkit)**. It allows users to perform essential text processing operations like ASCII value checking, tokenization, and text analysis — all in one place with a clean and easy-to-use UI.

🌐 **Live Demo:** [Click to Use the App](https://sam-nltk.streamlit.app/)

---

## 🚀 Features

🔹 **ASCII Value Checker** – Check ASCII values of individual characters with a comprehensive reference table  
🔹 **Word Tokenization** – Split your text into individual words using NLTK  
🔹 **Sentence Tokenization** – Break paragraphs into individual sentences  
🔹 **Text to ASCII Converter** – Convert entire sentences to their ASCII representations  
🔹 **Text Capitalization** – Properly capitalize your sentences with first letter uppercase  

---

## 📸 App Interface

The app features 5 interactive tabs:

1. **Check word ASCII** - Individual character ASCII value lookup with reference table
2. **Word Tokenizer** - NLTK-powered word tokenization
3. **Sentence Tokenizer** - Paragraph-to-sentence breakdown
4. **What computer see** - ASCII representation of entire text
5. **Capitalize** - Text capitalization tool

---

## 🛠️ How to Run Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Sameershrinath/NLTK_operations.git
   cd NLTK_operations
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download required NLTK data:**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

4. **Run the app:**
   ```bash
   streamlit run main.py
   ```

---

## 📁 Project Structure

```
NLTK_operations/
├── main.py              # Main Streamlit app
├── requirements.txt     # List of dependencies
└── README.md            # This file
```

---

## 📦 Dependencies

* **Streamlit** - Web app framework
* **NLTK** - Natural Language Toolkit
* **Pandas** - Data manipulation and analysis

Create a `requirements.txt` file with:
```
streamlit==1.28.0
nltk==3.8.1
pandas==2.1.4
```

To install everything manually:
```bash
pip install streamlit nltk pandas
```

---

## 🎯 Usage Examples

### ASCII Value Checker
- Enter any single character to get its ASCII value
- Browse the comprehensive ASCII reference table (characters 33-126)

### Word Tokenizer
- Input: "Hello world! How are you?"
- Output: ['Hello', 'world', '!', 'How', 'are', 'you', '?']

### Sentence Tokenizer
- Input: "This is sentence one. This is sentence two! Is this sentence three?"
- Output: ['This is sentence one.', 'This is sentence two!', 'Is this sentence three?']

### Text to ASCII
- Input: "Hi"
- Output: [{'H': 72}, {'i': 105}]

### Text Capitalization
- Input: "hello world"
- Output: "Hello world"

---

## 🔧 Technical Details

The app uses NLTK's built-in tokenizers:
- `nltk.word_tokenize()` for word-level tokenization
- `nltk.sent_tokenize()` for sentence-level tokenization

ASCII operations use Python's built-in `ord()` function to convert characters to their ASCII values.

---

## 🌟 Features Breakdown

| Feature | Description | Use Case |
|---------|-------------|----------|
| ASCII Checker | Get ASCII value of any character | Character encoding analysis |
| Word Tokenizer | Split text into words | Text preprocessing |
| Sentence Tokenizer | Split text into sentences | Document analysis |
| ASCII Converter | Convert text to ASCII representation | Understanding character encoding |
| Text Capitalizer | Proper text capitalization | Text formatting |

---

## 🚀 Deployment

This app is deployed on **Streamlit Cloud** and accessible at:
🌐 [https://sam-nltk.streamlit.app/](https://sam-nltk.streamlit.app/)

To deploy your own version:
1. Fork this repository
2. Connect your GitHub account to Streamlit Cloud
3. Deploy directly from the repository

---

## 🔮 Future Enhancements

- [ ] Add stemming and lemmatization features
- [ ] Include stopword removal functionality
- [ ] Add frequency distribution analysis
- [ ] Implement part-of-speech tagging
- [ ] Add text preprocessing pipeline
- [ ] Include word cloud generation
- [ ] Add sentiment analysis capabilities

---

## 🙋‍♂️ Author

**Sameer Shrinath**  
📫 [Connect on LinkedIn](https://www.linkedin.com/in/sameershrinath/)  
🐍 Passionate about NLP, Python, and building AI-powered tools.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute.

```
MIT License

Copyright (c) 2025 Sameer Shrinath

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🏷️ Tags

`nlp` `nltk` `streamlit` `python` `text-processing` `tokenization` `ascii` `natural-language-processing` `text-analysis` `web-app`

---

**⭐ If you found this project helpful, please give it a star!**
