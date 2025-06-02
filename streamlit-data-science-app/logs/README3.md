# Results of Model Training and Evaluation

This directory contains the results generated from the machine learning models trained and evaluated in the Streamlit Data Science App. 

## Contents

- **Model Performance Metrics**: This includes various metrics such as accuracy, precision, recall, F1 score, and AUC for classification models, as well as RMSE, MAE, and R² for regression models.

- **Visualizations**: Graphs and charts that illustrate the performance of the models, including confusion matrices, ROC curves, and feature importance plots.

- **Model Predictions**: Sample predictions made by the trained models on the test dataset.

- **Logs**: Any relevant logs related to the model training process, including warnings or errors encountered during training.

## Usage

The results can be accessed programmatically through the `ResultModel` class in the `src/models/result_model.py` file, which provides methods for saving and retrieving results.

## Future Work

- Enhance the reporting of results by including more detailed visualizations.
- Implement functionality to compare results across different models.
- Automate the generation of summary reports for each model trained.