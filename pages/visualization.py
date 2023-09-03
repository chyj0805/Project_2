import streamlit as st
import os
import joblib
from colabs.Yujie.Class.SMTPc import StockModelTrainerPredictor

import streamlit as st
import os
from colabs.Yujie.Class.SMTPc import StockModelTrainerPredictor

# Create a Streamlit app
st.title("Stock Prediction Model")

# Allow the user to upload the pre-trained model file
model_file = st.file_uploader("Upload Pretrained Model", type=["h5"])

# Check if a model file is uploaded
if model_file:
    # Initialize the predictor object with a dummy ticker symbol
    predictor = StockModelTrainerPredictor("DUMMY")

    # Load the pre-trained model
    if predictor.load_model(model_file):
        st.write("Model loaded successfully.")

        # Create a download button for the model
        st.markdown("### Download Trained Model")
        with st.spinner("Preparing the model for download..."):
            # Define the model path
            model_path = "trained_model.h5"

            # Save the loaded model to the specified path
            predictor.save_model(model_path)

        # Create a download link for the model file
        st.markdown(f"Download the trained model: [Trained Model](/{model_path})")

    else:
        st.write("Failed to load the model. Please check the model file.")
