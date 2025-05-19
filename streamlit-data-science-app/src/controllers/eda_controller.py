from src.utils.logger import setup_logger
import ydata_profiling
import dtale
import sweetviz
import pandas as pd

class EDAController:
    def __init__(self):
        self.logger = setup_logger("eda_controller")

    def perform_ydata_eda(self, dataframe):
        self.logger.info("Performing EDA using ydata profiling.")
        profile = ydata_profiling.ProfileReport(dataframe)
        return profile

    def perform_dtale_eda(self, dataframe):
        self.logger.info("Performing EDA using dtale.")
        d = dtale.show(dataframe)
        return d

    def perform_sweetviz_eda(self, dataframe, target=None):
        self.logger.info("Performing EDA using sweetviz.")
        report = sweetviz.analyze(dataframe, target_feat=target)
        return report

    def load_data(self, file_path):
        self.logger.info(f"Loading data from {file_path}.")
        dataframe = pd.read_csv(file_path)
        return dataframe

    def save_report(self, report, report_name):
        self.logger.info(f"Saving report as {report_name}.")
        report.save_html(report_name)