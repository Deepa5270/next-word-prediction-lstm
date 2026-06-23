import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

#Load the LSTM Model
model = load_model('next_word_lstm.h5', compile=False)



#3 Laod the tokenizer
with open('tokenizer.pickle','rb') as handle:
    tokenizer=pickle.load(handle)

# Function to predict the next word
def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len-1):]  # Ensure the sequence length matches max_sequence_len-1
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(predicted, axis=1)
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

# streamlit app
# Sidebar
st.sidebar.header("About")
st.sidebar.write(
    "This application predicts the next word using an LSTM model trained on Shakespeare's Hamlet."
)

# Title
st.title("Next Word Prediction Using LSTM")

# Example text
st.write("Example: To be or not to")

# Input box
input_text = st.text_input(
    "Enter the sequence of Words",
    "To be or not to"
)

# Prediction button
if st.button("Predict Next Word"):
    max_sequence_len = model.input_shape[1] + 1

    next_word = predict_next_word(
        model,
        tokenizer,
        input_text,
        max_sequence_len
    )

    st.success(f"Predicted Word: {next_word}")
    
