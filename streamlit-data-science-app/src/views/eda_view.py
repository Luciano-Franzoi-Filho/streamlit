from src.utils.logger import setup_logger
import streamlit.components.v1 as components
import streamlit as st
import ydata_profiling as ydp
import dtale
import sweetviz as sv
import os
import pandas as pd

logger = setup_logger()

def render_eda_view():
    try:
        st.title("Exploratory Data Analysis")

        # Caminho para a pasta de dados
        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
        result_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "results")
        arquivos = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

        if not arquivos:
            st.warning("Nenhum dataset encontrado na pasta 'data'.")
            return

        # Adiciona uma opção vazia no início
        arquivos_opcoes = ["Selecione um arquivo"] + arquivos
        arquivo_escolhido = st.selectbox("Selecione o dataset para análise:", arquivos_opcoes)

        # Só continua se o usuário selecionar um arquivo válido
        if arquivo_escolhido == "Selecione um arquivo":
            st.info("Selecione um arquivo para continuar.")
            return

        # Carregar dataset selecionado
        dataset_path = os.path.join(data_dir, arquivo_escolhido)
        dataset = pd.read_csv(dataset_path)
        st.success(f"Dataset '{arquivo_escolhido}' carregado com sucesso.")
        st.dataframe(dataset.head())

        # Seção de seleção do tipo de relatório
        st.subheader("Escolha o tipo de relatório que deseja gerar:")

        # YData Profiling
        if st.checkbox("Gerar relatório com YData Profiling"):
            profile = ydp.ProfileReport(dataset)
            with st.spinner("Gerando relatório YData Profiling..."):
                profile_path = os.path.join(result_dir, "ydata_profile_report.html")
                profile.to_file(profile_path)
                with open(profile_path, "r", encoding="utf-8") as f:
                    html = f.read()
                    components.html(html, height=800, width=1000, scrolling=True)

        # D-Tale
        if st.checkbox("Lançar D-Tale"):
            d = dtale.show(dataset)
            st.write("D-Tale está em execução. Clique [aqui](%s) para visualizar." % d._url)

        # Sweetviz
        if st.checkbox("Gerar relatório com Sweetviz"):
            report = sv.analyze(dataset)
            report_path = os.path.join(result_dir, 'sweetviz_report.html')
            report.show_html(report_path)
            st.write(f"Relatório Sweetviz gerado. Verifique o arquivo: [sweetviz_report.html](./results/sweetviz_report.html)")

    except Exception as e:
        logger.error("Erro na visualização EDA: %s", e)
        st.error("Ocorreu um erro ao gerar os relatórios de EDA.")