class DatasetModel:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = None

    def load_dataset(self):
        import pandas as pd
        try:
            self.data = pd.read_csv(self.dataset_path)
            return self.data
        except Exception as e:
            print(f"Error loading dataset: {e}")
            return None

    def save_dataset(self, save_path):
        try:
            self.data.to_csv(save_path, index=False)
            print(f"Dataset saved to {save_path}")
        except Exception as e:
            print(f"Error saving dataset: {e}")