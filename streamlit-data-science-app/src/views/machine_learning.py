import pandas as pd
import sqlite3
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def carregar_dados(nome_tabela):
    # Caminho absoluto para o banco de dados
    db_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "DB",
        "projeto_ml.db"
    )
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {nome_tabela}", conn)
    conn.close()
    return df

def classificacao_sentimento():
    df = carregar_dados("sentimentos")
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["review"])
    y = df["sentiment"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)
    return modelo, vectorizer, acuracia

def regressao_housing():
    df = carregar_dados("regressao")
    X = df.drop("MedHouseVal", axis=1)
    y = df["MedHouseVal"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    return modelo, rmse

def clusterizacao_clientes(k=3):
    df = carregar_dados("clientes")
    X = df.drop("CustomerID", axis=1)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    modelo = KMeans(n_clusters=k, random_state=42)
    clusters = modelo.fit_predict(X_scaled)
    df["Cluster"] = clusters
    return df, clusters