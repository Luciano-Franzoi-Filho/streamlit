def download_dataset(dataset_name, destination_folder):
    import os
    import subprocess
    import logging

    logger = logging.getLogger(__name__)

    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            logger.info(f"Created directory: {destination_folder}")

        command = f"kaggle datasets download -d {dataset_name} -p {destination_folder}"
        logger.info(f"Executing command: {command}")
        subprocess.run(command, shell=True, check=True)
        logger.info(f"Downloaded dataset: {dataset_name} to {destination_folder}")

        # Unzip the dataset if it's in zip format
        zip_file_path = os.path.join(destination_folder, f"{dataset_name.split('/')[-1]}.zip")
        if os.path.exists(zip_file_path):
            import zipfile
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(destination_folder)
            os.remove(zip_file_path)  # Remove the zip file after extraction
            logger.info(f"Extracted dataset: {zip_file_path}")

    except Exception as e:
        logger.error(f"Error downloading dataset: {e}")
        raise e