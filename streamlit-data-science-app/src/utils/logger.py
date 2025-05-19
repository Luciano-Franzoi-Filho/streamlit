def setup_logger(log_file='logs/app.log'):
    import logging
    import os

    log_dir = os.path.dirname(log_file)
    if log_dir:  # Só cria se não for string vazia
        os.makedirs(log_dir, exist_ok=True)

    # Configure the logger
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Create a console handler for logging to stdout
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logging.getLogger().addHandler(console_handler)

    return logging.getLogger(__name__)