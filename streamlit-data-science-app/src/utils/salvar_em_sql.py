import pandas as pd
import os
import sqlite3

imdb = pd.read_csv("streamlit-data-science-app\dados\imdb.csv")
housing = pd.read_csv("streamlit-data-science-app\dados\california_housing.csv")
clientes = pd.read_csv("streamlit-data-science-app\dados\customers.csv")

db_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "DB",
    "projeto_ml.db"
)
conn = sqlite3.connect(db_path)
imdb.to_sql("sentimentos", conn, if_exists="replace", index=False)
housing.to_sql("regressao", conn, if_exists="replace", index=False)
clientes.to_sql("clientes", conn, if_exists="replace", index=False)
conn.close()
print("Dados salvos com sucesso no SQLite.")
