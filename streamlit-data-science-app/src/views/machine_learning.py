from src.utils.logger import setup_logger
import streamlit as st
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.cluster import KMeans
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, r2_score, mean_absolute_error


# Set up logging
logger = setup_logger()

def render_ML_view(subtipo):
    st.header("Machine Learning")
    dados_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "dados")
    arquivos = [f for f in os.listdir(dados_dir) if f.endswith('.csv')]
    if not arquivos:
        st.warning("Nenhum arquivo CSV encontrado na pasta de dados.")
        return

    arquivo_escolhido = st.selectbox("Selecione o dataset:", arquivos)
    df = pd.read_csv(os.path.join(dados_dir, arquivo_escolhido))

    if subtipo == "Classificação":
        st.subheader("Classificação")
        colunas = df.columns.tolist()
        target = st.selectbox("Selecione a variável alvo (target):", colunas)
        features = [col for col in colunas if col != target]
        selected_features = st.multiselect("Selecione as variáveis preditoras:", features, default=features)
        if st.button("Treinar modelo de Classificação"):
            X = df[selected_features]
            y = df[target]
            # Verifica se y é categórico (menos de 10 valores únicos ou tipo objeto)
            if (np.issubdtype(y.dtype, np.number) and y.nunique() > 10) or y.dtype.kind == 'f':
                st.error("A variável alvo parece ser contínua. Por favor, selecione uma variável categórica para classificação.")
            else:
                X = pd.get_dummies(X)
                if y.dtype == 'O':
                    y = pd.factorize(y)[0]
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                model = LogisticRegression(max_iter=1000)
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                acc = accuracy_score(y_test, y_pred)
                st.success(f"Acurácia do modelo: {acc:.2%}")

                # Matriz de confusão como imagem
                st.subheader("Matriz de Confusão")
                fig, ax = plt.subplots()
                ConfusionMatrixDisplay.from_predictions(y_test, y_pred, ax=ax)
                st.pyplot(fig)

                # Relatório de classificação
                st.subheader("Relatório de Classificação")
                st.text(classification_report(y_test, y_pred))

                review_nova = st.text_input("Digite valores para uma nova amostra (separados por vírgula):")
                if review_nova:
                    try:
                        valores = [float(x) for x in review_nova.split(",")]
                        pred = model.predict([valores])[0]
                        st.info(f"Classe prevista: {pred}")
                    except Exception as e:
                        st.error(f"Erro ao prever: {e}")

    elif subtipo == "Regressão":
        st.subheader("Regressão")
        colunas = df.columns.tolist()
        target = st.selectbox("Selecione a variável alvo (target):", colunas)
        features = [col for col in colunas if col != target]
        selected_features = st.multiselect("Selecione as variáveis preditoras:", features, default=features)
        if st.button("Treinar modelo de Regressão"):
            X = df[selected_features]
            y = df[target]
            # Verifica se y é numérico e contínuo
            if not np.issubdtype(y.dtype, np.number) or y.nunique() <= 10:
                st.error("A variável alvo parece ser categórica. Por favor, selecione uma variável contínua para regressão.")
            else:
                X = pd.get_dummies(X)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                model = LinearRegression()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                rmse = mean_squared_error(y_test, y_pred, squared=False)
                r2 = r2_score(y_test, y_pred)
                mae = mean_absolute_error(y_test, y_pred)
                st.success(f"RMSE do modelo: {rmse:.3f}")
                st.info(f"R²: {r2:.3f} | MAE: {mae:.3f}")

                # Gráfico de dispersão real vs previsto
                st.subheader("Valores Reais vs. Previsto")
                fig, ax = plt.subplots()
                ax.scatter(y_test, y_pred, alpha=0.7)
                ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
                ax.set_xlabel("Valor Real")
                ax.set_ylabel("Valor Previsto")
                st.pyplot(fig)

                valores_novos = st.text_input("Digite valores para uma nova amostra (separados por vírgula):")
                if valores_novos:
                    try:
                        valores = [float(x) for x in valores_novos.split(",")]
                        pred = model.predict([valores])[0]
                        st.info(f"Valor previsto: {pred:.2f}")
                    except Exception as e:
                        st.error(f"Erro ao prever: {e}")

    elif subtipo == "Clusterização":
        st.subheader("Clusterização")
        colunas = df.columns.tolist()
        selected_features = st.multiselect("Selecione as variáveis para clusterização:", colunas, default=colunas)
        k = st.slider("Escolha o número de clusters:", 2, 10, 3)
        if st.button("Executar Clusterização"):
            X = df[selected_features]
            X = pd.get_dummies(X)
            model = KMeans(n_clusters=k, random_state=42, n_init=10)
            clusters = model.fit_predict(X)
            df_result = df.copy()
            df_result['Cluster'] = clusters
            st.success("Clusterização realizada!")
            st.write(df_result)

            # Exibe o número de amostras por cluster
            st.subheader("Distribuição dos Clusters")
            st.bar_chart(df_result['Cluster'].value_counts().sort_index())

            # Gráfico de dispersão dos clusters (se possível)
            if X.shape[1] >= 2:
                st.subheader("Visualização dos Clusters")
                fig, ax = plt.subplots()
                # Pega as duas primeiras features para plotar
                x_axis = X.columns[0]
                y_axis = X.columns[1]
                scatter = ax.scatter(X[x_axis], X[y_axis], c=clusters, cmap='tab10', alpha=0.7)
                # Plota centróides
                centers = model.cluster_centers_
                ax.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centróides')
                ax.set_xlabel(x_axis)
                ax.set_ylabel(y_axis)
                ax.legend()
                st.pyplot(fig)
            else:
                st.info("Selecione pelo menos duas variáveis numéricas para visualizar")
