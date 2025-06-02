from src.utils.logger import setup_logger
from src.controllers.kaggle_authenticator import autenticar_kaggle
import streamlit as st
import os

logger = setup_logger()

def DownloadDataset(data_controller):
    try:
        st.title("Download Dataset")
        st.write("Baixe o dataset desejado do Kaggle.")
        dataset_name = st.text_input("Digite o nome do dataset do Kaggle (ex: zynicide/wine-reviews)")
        if st.button("Baixar Dataset"):
            if dataset_name:
                api = autenticar_kaggle()
                if api is None:
                    st.error("Erro ao autenticar no Kaggle. Verifique suas credenciais.")
                    return
                data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "dados")
                try:
                    api.dataset_download_files(dataset_name, path=data_dir, unzip=True)
                    st.success(f"Dataset '{dataset_name}' baixado com sucesso e salvo na pasta 'dados'!")
                except Exception as e:
                    logger.error(f"Erro ao baixar dataset: {e}")
                    st.error("Falha ao baixar o dataset. Verifique o nome e tente novamente.")
            else:
                st.warning("Por favor, insira o nome do dataset.")
    except Exception as e:
        logger.error("Error in dataset download view: %s", e)
        st.error("An error occurred while downloading dataset.")