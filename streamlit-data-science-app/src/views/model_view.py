from src.controllers.model_controller import ModelController
import streamlit as st
import logging

logger = logging.getLogger(__name__)

def render_model_view():
    st.title("Selecção de Modelo e Treinamento")

    model_controller = ModelController()

    # Model selection
    model_type = st.selectbox("Selecione o tipo do modelo", ["Regressão", "Classificação"])
    
    if model_type == "Regressão":
        regression_models = model_controller.get_regression_models()
        selected_model = st.selectbox("Selecionado o modelo de Regressão", regression_models)
    else:
        classification_models = model_controller.get_classification_models()
        selected_model = st.selectbox("Selecionado o modelo de Classificação", classification_models)

    # Input features
    features = st.text_area("Entre com os features para a predição(comma-separated)")

    if st.button("Treinar Modelo"):
        if features:
            features_list = [feature.strip() for feature in features.split(",")]
            results = model_controller.train_model(selected_model, features_list)
            st.success("Modelo treinado com sucesso!")
            st.write("Resultados:", results)
            logger.info(f"Modelo {selected_model} treinado com os features: {features_list}")
        else:
            st.error("Por Favor selecione o features para a previsão.")