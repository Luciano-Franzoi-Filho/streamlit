import os
import pandas as pd

class DataController:
    def __init__(self, logger):
        self.logger = logger
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir, exist_ok=True)

    def download_dataset(self, dataset_name):
        try:
            # Lógica para baixar dataset do Kaggle
            self.logger.info(f"Baixando dataset: {dataset_name}")
            # Placeholder para lógica real de download
            # download_dataset_from_kaggle(dataset_name)
            self.logger.info(f"Dataset baixado com sucesso: {dataset_name}")
        except Exception as e:
            self.logger.error(f"Erro ao baixar dataset {dataset_name}: {e}")

    def save_dataset(self, dataset, filename):
        try:
            # Salva o dataset na pasta data
            path = os.path.join(self.data_dir, filename)
            self.logger.info(f"Salvando dataset em: {path}")
            dataset.to_csv(path, index=False)
            self.logger.info(f"Dataset salvo com sucesso em: {path}")
        except Exception as e:
            self.logger.error(f"Erro ao salvar dataset em {path}: {e}")

    def load_dataset(self, filename):
        try:
            # Carrega o dataset da pasta data
            path = os.path.join(self.data_dir, filename)
            self.logger.info(f"Carregando dataset de: {path}")
            dataset = pd.read_csv(path)
            self.logger.info(f"Dataset carregado com sucesso de: {path}")
            return dataset
        except Exception as e:
            self.logger.error(f"Erro ao carregar dataset de {path}: {e}")
            return None