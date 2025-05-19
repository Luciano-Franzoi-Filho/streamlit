from src.utils.logger import setup_logger
import streamlit as st
import ydata_profiling as ydp
import dtale
import sweetviz as sv

logger = setup_logger()

def render_eda_view(dataset):
    try:
        st.title("Download Dataset")
        st.write("Baixe o dataset desejado do Kaggle.")
        dataset_name = st.text_input("Digite o nome do dataset do Kaggle (ex: zynicide/wine-reviews)")
        if st.button("Baixar Dataset") and dataset_name:
            # Placeholder para lógica real de download
            # download_dataset_from_kaggle(dataset_name)
            st.success(f"Dataset '{dataset_name}' baixado com sucesso!")    
        else:
            st.warning("Por favor, insira o nome do dataset.")
    except Exception as e:
        logger.error("Error in dataset download view: %s", e)
        st.error("An error occurred while downloading dataset.")