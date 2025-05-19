from streamlit import sidebar

def render_sidebar():
    sidebar.title("Aplicativo Streamlit para Kaggle")
    sidebar.markdown("### Sobre")
    sidebar.markdown("Este aplicativo permite baixar conjuntos de dados do Kaggle, realizar análise exploratória de dados (EDA) e selecionar modelos para regressão e classificação.")
    return