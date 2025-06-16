from streamlit import sidebar

def render_sidebar():
    sidebar.title("Aplicativo Streamlit para Kaggle")
    sidebar.markdown("### Sobre")
    sidebar.markdown(
        "Este aplicativo permite baixar conjuntos de dados do Kaggle, "
        "realizar análise exploratória de dados (EDA) e selecionar modelos para regressão e classificação."
    )
    opcoes = [
        "Selecione uma opção",
        "Download Dataset",
        "EDA",
        # "Treinamento de Modelos",
        "Machine Learning"
    ]
    opcao_principal = sidebar.selectbox("Selecione uma funcionalidade:", opcoes)
    subtipo = None
    if opcao_principal == "Machine Learning":
        subtipo = sidebar.radio(
            "Escolha o tipo de análise de ML:",
            ["Classificação", "Regressão", "Clusterização"]
        )
    return opcao_principal, subtipo