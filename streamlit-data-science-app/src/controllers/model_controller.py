from src.utils.logger import setup_logger

logger = setup_logger()

class ModelController:
    def __init__(self):
        logger.info("ModelController initialized")

    def select_model(self, model_type):
        logger.info(f"Model selected: {model_type}")
        # Logic for selecting a model based on model_type
        pass

    def train_model(self, model, X_train, y_train):
        logger.info("Training model")
        # Logic for training the model
        pass

    def evaluate_model(self, model, X_test, y_test):
        logger.info("Evaluating model")
        # Logic for evaluating the model
        pass

    def save_model(self, model, model_name):
        logger.info(f"Saving model: {model_name}")
        # Logic for saving the trained model
        pass

    def load_model(self, model_name):
        logger.info(f"Loading model: {model_name}")
        # Logic for loading a saved model
        pass