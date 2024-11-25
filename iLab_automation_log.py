import logging
import colorlog
from logging.handlers import RotatingFileHandler
from datetime import datetime
from iLab_automation_helper import Helper

class LoggerConfig:
    @staticmethod
    def setup_logger():
        # Create logs directory if it doesn't exist
        log_directory = Helper.get_automation_log_path()
        # Get the current date for the log file name
        current_date = datetime.now().strftime("%Y-%m-%d")
        log_file = f"{log_directory}/knexus-automation-log_{current_date}.log"

        # Set up rotating file handler for log files
        file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=30)
        
        # Set up color logging for console output
        color_formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s [%(levelname)s] %(message)s",
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(color_formatter)

        # Set up the logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)  # Adjust the level as needed
        logger.addHandler(file_handler)  # Log to file
        logger.addHandler(console_handler)  # Log to console with color

        # File formatter without colors (plain text)
        file_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(file_formatter)

        return logger
