import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Page Config
st.set_page_config(
    page_title="Job Recommendation System",
    page_icon="💼",
    layout="centered"
)

MAX_LEN = 200

# Cache model loading
@st.cache_resource
def load_resources():
    model = load_model("job_model.h5")

    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    with open("label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)

    return model, tokenizer, label_encoder

try:
    model, tokenizer, label_encoder = load_resources()
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# Title
st.title("💼 Job Recommendation System")

st.write(
    "Enter your skills or resume summary to get a recommended job role."
)

# Input
user_input = st.text_area(
    "Enter Skills / Resume Summary",
    height=200,
    placeholder="Python, Machine Learning, SQL, TensorFlow..."
)

# Prediction
if st.button("🚀 Recommend Job"):

    if not user_input.strip():
        st.warning("Please enter skills.")
    else:
        try:
            seq = tokenizer.texts_to_sequences([user_input])

            padded = pad_sequences(
                seq,
                maxlen=MAX_LEN,
                padding="post"
            )

            pred = model.predict(padded, verbose=0)

            best_index = np.argmax(pred)
            confidence = pred[0][best_index] * 100

            job_role = label_encoder.inverse_transform(
                [best_index]
            )[0]

            st.success(
                f"🎯 Recommended Job: {job_role}"
            )

            st.info(
                f"📊 Confidence Score: {confidence:.2f}%"
            )

            st.subheader("🏆 Top 5 Recommendations")

            top5 = np.argsort(pred[0])[-5:][::-1]

            for i in top5:
                role = label_encoder.inverse_transform([i])[0]
                score = pred[0][i] * 100
                st.write(
                    f"✅ {role} — {score:.2f}%"
                )

        except Exception as e:
            st.error(f"Prediction Error: {e}")