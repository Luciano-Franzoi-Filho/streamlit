from src.utils.logger import setup_logger
from src.controllers.data_controller import DataController
from src.controllers.eda_controller import EDAController
from src.controllers.model_controller import ModelController
from src.views.sidebar import render_sidebar
from src.views.eda_view import render_eda_view
from src.views.model_view import render_model_view
from src.views.download_view import DownloadDataset
import streamlit as st

# Set up logging
logger = setup_logger()

def main():
    st.title("Aplicativo Streamlit para Kaggle")
    
    # Inicializa os controllers
    data_controller = DataController(logger)
    eda_controller = EDAController()
    model_controller = ModelController()
    
    # Renderiza a barra lateral para seleção de funcionalidade
    render_sidebar()
    
    # Seleção de funcionalidade principal
    option = st.sidebar.selectbox("Selecione uma opção", ["Selecione uma opção", "Download Dataset", "EDA", "Treinamento de Modelos"])
    
    if option == "Download Dataset":
        DownloadDataset(data_controller)
    elif option == "EDA":
        render_eda_view()
    elif option == "Treinamento de Modelos":
        render_model_view(model_controller)

if __name__ == "__main__":
    main()