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
        st.title("Exploratory Data Analysis (EDA)")

        # Caminho para a pasta de dados
        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "dados")
        result_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "results")
        arquivos = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

        if not arquivos:
            st.warning("Nenhum dataset encontrado na pasta 'dados'.")
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
        st.write(f"Total de linhas: {dataset.shape[0]}")
        st.write(f"Total de colunas: {dataset.shape[1]}")
        st.write(f"Colunas: {', '.join(dataset.columns)}")
        st.write(f"Valores ausentes:\n{dataset.isnull().sum()}")
        st.write(f"Valores únicos:\n{dataset.nunique()}")
        st.write(f"Colunas categóricas:\n{dataset.select_dtypes(include=['object']).columns.tolist()}")
        st.write(f"Colunas numéricas:\n{dataset.select_dtypes(include=['number']).columns.tolist()}")


        # Seção de seleção do tipo de relatório
        st.subheader("Escolha o tipo de relatório que deseja gerar:")

        report_type = st.selectbox(
            "Selecione o tipo de relatório:",
            ("YData Profiling", "D-Tale", "Sweetviz")
        )

        if report_type == "YData Profiling":
            if st.button("Gerar relatório YData Profiling"):
                with st.spinner("Gerando relatório YData Profiling..."):
                    profile = ydp.ProfileReport(dataset)
                    profile_path = os.path.join(result_dir, "ydata_profile_report.html")
                    profile.to_file(profile_path)
                    with open(profile_path, "r", encoding="utf-8") as f:
                        html = f.read()
                        components.html(html, height=800, width=1000, scrolling=True)

        elif report_type == "D-Tale":
            if st.button("Lançar D-Tale"):
                d = dtale.show(dataset)
                st.write(f"D-Tale está em execução. Clique [aqui]({d._url}) para visualizar.")

        elif report_type == "Sweetviz":
            if st.button("Gerar relatório Sweetviz"):
                with st.spinner("Gerando relatório Sweetviz..."):
                    report = sv.analyze(dataset)
                    report_path = os.path.join(result_dir, 'sweetviz_report.html')
                    report.show_html(report_path)
                    st.write(f"Relatório Sweetviz gerado. Verifique o arquivo: [sweetviz_report.html](./results/sweetviz_report.html)")


    except Exception as e:
        logger.error("Erro na visualização EDA: %s", e)
        st.error("Ocorreu um erro ao gerar os relatórios de EDA.")