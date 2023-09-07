import streamlit as st
import os
from colabs.Yujie.Class.SMTPc import StockModelTrainerPredictor

# Create an instance of the StockModelTrainerPredictor class
model_predictor = StockModelTrainerPredictor(ticker=None)

# Define Streamlit app
def main():
    st.title("Stock Price Prediction")

    # List all the model files in the directory
    model_directory = r"C:\Users\scott\OneDrive\Documents\GitHub\Project_2\assests"  # Update with your model directory
    model_files = [f for f in os.listdir(model_directory) if f.endswith(".h5")]

    # Create a dropdown to select the model
    selected_model = st.selectbox("Select a pretrained model:", model_files)

    # Extract the ticker symbol from the selected model filename
    default_ticker = selected_model.split("_")[0]

    # Load the selected pretrained model
    if st.button("Predict"):
        model_path = os.path.join(model_directory, selected_model)
        model_predictor.load_model(model_path)

        # Use the extracted ticker symbol as the ticker
        model_predictor.ticker = default_ticker

        # Get combined data and preprocess it
        combined_data = model_predictor.get_combined_data()

        if combined_data is not None:
            x_train_actual, y_train_actual, x_val, y_val, x_test = model_predictor.preprocess_data()

            # Make predictions
            predictions = model_predictor.predict_with_pretrained_model()
            st.write("Predictions:", predictions)

            # Calculate KPIs
            average_rmse = model_predictor.calculate_average_rmse()
            average_mape = model_predictor.calculate_average_mape()
            average_corr = model_predictor.calculate_average_pearson_corr()

            # Display KPIs as text
            st.markdown(f'**Average RMSE:** {average_rmse}')
            st.markdown(f'**Average MAPE:** {average_mape}')
            st.markdown(f'**Average Pearson Correlation Coefficient:** {average_corr}')
        # Visualize results
            st.write("Visualizations:")
            model_predictor.visualize_results_whole()
            model_predictor.visualize_results_60days()
            model_predictor.predict_next_60_days()
        else:
            st.write("Error: Unable to fetch combined data.")

if __name__ == "__main__":
    main()


