class ResultModel:
    def __init__(self):
        self.results = {}

    def save_result(self, model_name, metrics):
        """Save the training results for a given model."""
        self.results[model_name] = metrics
        # Here you would implement the logic to save results to a file or database

    def get_result(self, model_name):
        """Retrieve the training results for a given model."""
        return self.results.get(model_name, None)

    def save_results_to_file(self, file_path):
        """Save all results to a specified file."""
        with open(file_path, 'w') as file:
            for model_name, metrics in self.results.items():
                file.write(f"{model_name}: {metrics}\n")

    def load_results_from_file(self, file_path):
        """Load results from a specified file."""
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    model_name, metrics = line.strip().split(': ')
                    self.results[model_name] = eval(metrics)  # Be cautious with eval
        except FileNotFoundError:
            print(f"No results file found at {file_path}.")