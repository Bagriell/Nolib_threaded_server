"""Module for logging config"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# handle logfile
file_handler = logging.FileHandler("customer_events.log")
file_handler.setLevel(logging.INFO)
fh_formatter = logging.Formatter("%(asctime)s - %(message)s")
file_handler.setFormatter(fh_formatter)
file_logger = logging.getLogger("file_loger")
file_logger.addHandler(file_handler)
file_logger.propagate = False
