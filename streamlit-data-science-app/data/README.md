# This file contains documentation about the datasets used in the project.

## Datasets Overview

This project utilizes various datasets for performing exploratory data analysis (EDA) and training machine learning models. The datasets are sourced from Kaggle and are intended for regression and classification tasks.

## Dataset Structure

Each dataset is organized in a structured format, typically including the following components:

- **Features**: The input variables used for training the models.
- **Target**: The output variable that the models aim to predict.
- **Data Types**: Information about the types of data present in each feature (e.g., numerical, categorical).
- **Missing Values**: Details on any missing values in the dataset and how they are handled.

## Dataset Storage

Datasets are stored in the `data` directory. Each dataset is saved in a separate file, and the naming convention follows the pattern `dataset_name.csv`. Ensure that the datasets are properly formatted and cleaned before use.

## Usage

To load a dataset, use the `DatasetModel` class from the `src/models/dataset_model.py` file. This class provides methods for loading and saving datasets, ensuring that the data is accessible for analysis and model training.

## Acknowledgments

Datasets used in this project are sourced from Kaggle. Please refer to the respective dataset pages for licensing and usage restrictions.