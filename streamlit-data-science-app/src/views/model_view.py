from src.controllers.model_controller import ModelController
import streamlit as st
import logging

logger = logging.getLogger(__name__)

def render_model_view():
    st.title("Model Selection and Training")

    model_controller = ModelController()

    # Model selection
    model_type = st.selectbox("Select Model Type", ["Regression", "Classification"])
    
    if model_type == "Regression":
        regression_models = model_controller.get_regression_models()
        selected_model = st.selectbox("Select Regression Model", regression_models)
    else:
        classification_models = model_controller.get_classification_models()
        selected_model = st.selectbox("Select Classification Model", classification_models)

    # Input features
    features = st.text_area("Enter features for prediction (comma-separated)")

    if st.button("Train Model"):
        if features:
            features_list = [feature.strip() for feature in features.split(",")]
            results = model_controller.train_model(selected_model, features_list)
            st.success("Model trained successfully!")
            st.write("Training Results:", results)
            logger.info(f"Model {selected_model} trained with features: {features_list}")
        else:
            st.error("Please enter features for prediction.")