from src.utils.logger import setup_logger
from src.controllers.data_controller import DataController
from src.controllers.eda_controller import EDAController
from src.controllers.model_controller import ModelController
from src.views.sidebar import render_sidebar
from src.views.eda_view import render_eda_view
from src.views.model_view import render_model_view
from src.views.download_view import DownloadDataset
from src.views.machine_learning import classificacao_sentimento, regressao_housing, clusterizacao_clientes
import streamlit as st

# Set up logging
logger = setup_logger()

def main():
    st.title("Aplicativo Streamlit para Kaggle")
    
    # Inicializa os controllers
    data_controller = DataController(logger)
    eda_controller = EDAController()
    model_controller = ModelController()
    
    # Renderiza a barra lateral para seleção de funcionalidade e obtém opções
    opcao_principal, subtipo = render_sidebar()
    
    if opcao_principal == "Download Dataset":
        DownloadDataset(data_controller)
    elif opcao_principal == "EDA":
        render_eda_view()
    elif opcao_principal == "Treinamento de Modelos":
        render_model_view(model_controller)
    elif opcao_principal == "Machine Learning":
        if subtipo == "Classificação":
            st.header("🔠 Classificação: Análise de Sentimento (IMDB)")
            modelo, vectorizer, acuracia = classificacao_sentimento()
            st.write(f"**Acurácia do modelo:** {acuracia:.2%}")
            review_nova = st.text_input("Digite uma nova resenha para classificar:")
            if review_nova:
                vetor_novo = vectorizer.transform([review_nova])
                pred = modelo.predict(vetor_novo)[0]
                st.success(f"Sentimento previsto: **{pred}**")
        elif subtipo == "Regressão":
            st.header("📈 Regressão: Previsão de Valor de Casas")
            modelo, rmse = regressao_housing()
            st.write(f"**Erro quadrático médio (RMSE):** {rmse:.3f}")
        elif subtipo == "Clusterização":
            st.header("👥 Clusterização: Segmentação de Clientes")
            k = st.slider("Escolha o número de clusters:", 2, 10, 3)
            df, clusters = clusterizacao_clientes(k)
            st.write("🔎 Resultado com os clusters:")
            st.write(df)
    # Se "Selecione uma opção", não faz nada

if __name__ == "__main__":
    main()