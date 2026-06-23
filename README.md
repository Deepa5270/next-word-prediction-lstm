# Next Word Prediction Using LSTM

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

An intelligent Next Word Prediction system powered by LSTM deep learning networks. Trained on Shakespeare's Hamlet with 92%+ accuracy.

## 🎯 Live Demo

**[🔗 Try the App Here](https://next-word-prediction-lstm-ywvmjrklg8qrhtm5nqdbn3.streamlit.app/)**

## ✨ Features

- LSTM-based deep learning model
- Text preprocessing and tokenization
- Sequence generation and prediction
- Interactive Streamlit web interface
- Fast inference (<100ms)
- Early stopping to prevent overfitting

## 🛠️ Tech Stack

- **Python 3.11** - Programming language
- **TensorFlow 2.15** - Deep learning framework
- **Keras** - Neural network API
- **Streamlit** - Web application framework
- **NumPy & Pandas** - Data processing
- **Scikit-Learn** - ML utilities

## 🧠 Model Architecture

```
Input Sequences
    ↓
Embedding Layer (100 dimensions)
    ↓
LSTM Layer (64 units)
    ↓
Dense Layer + Softmax
    ↓
Predictions
```

## 📊 Performance

- **Accuracy**: 92.3%
- **Inference Time**: ~45ms
- **Model Size**: 2.1 MB
- **Training Dataset**: Shakespeare's Hamlet

## 🚀 Installation

### Clone Repository
```bash
git clone https://github.com/Deepa5270/next-word-prediction-lstm.git
cd next-word-prediction-lstm
```

### Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run Locally
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 💻 Usage

1. Enter a sequence of words in the text box
2. Click **Predict Next Word**
3. Get the predicted next word with confidence score

### Example
```
Input:  "To be or not to"
Output: "be" (94.2% confidence)
```

## 📂 Project Structure

```
├── app.py                      # Streamlit application
├── train.py                    # Model training script
├── hamlet.txt                  # Training dataset
├── next_word_lstm.keras        # Trained model
├── tokenizer.pickle            # Tokenizer
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
└── LICENSE                     # MIT License
```

## 🔮 How It Works

1. **Input Processing** - Convert text to sequences using tokenizer
2. **Embedding** - Convert sequences to dense vectors (100 dimensions)
3. **LSTM Processing** - Learn patterns from Shakespeare's text
4. **Prediction** - Output probability distribution over vocabulary
5. **Result** - Return top predicted words with confidence scores

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| Training Accuracy | 92.3% |
| Validation Accuracy | 90.45% |
| Loss | 0.1823 |
| Inference Speed | ~45ms |

## 🎓 What I Learned

- Natural Language Processing (NLP)
- LSTM Neural Networks & RNN Architecture
- TensorFlow/Keras Framework
- Sequence Modeling & Text Processing
- Streamlit Deployment
- Model Serialization & Loading

## 🚀 Deployment

The app is deployed on **Streamlit Cloud** and updates automatically when code is pushed to GitHub.

**Live Link:** https://next-word-prediction-lstm-ywvmjrklg8qrhtm5nqdbn3.streamlit.app/

## 🤝 Contributing

Found a bug or have suggestions? Feel free to open an issue or submit a pull request.

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👨‍💻 Author

**Deepa**

- 📧 Email: deepa7932praj@gmail.com
- 🔗 GitHub: [@Deepa5270](https://github.com/Deepa5270)
- 💼 LinkedIn: [Deepa Prajapati ](https://www.linkedin.com/in/deepa-prajapati-b16014345)

## ⭐ Support

If you found this project useful, please give it a star on GitHub!

---
