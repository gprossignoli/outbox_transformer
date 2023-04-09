import logging
import os
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

ROOT_DIR = os.path.dirname((os.path.realpath(__file__)))
ENV_FILE = os.path.abspath(os.path.join(ROOT_DIR, "../.env"))

load_dotenv(ENV_FILE)
# LOGGING CONFIG

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('transformer')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# to log debug messages
debug_logger = logging.StreamHandler()
debug_logger.setLevel(logging.DEBUG)
debug_logger.setFormatter(formatter)

# to log general messages
# x2 files of 2mb
info_logger = RotatingFileHandler(filename='../transformer.log', maxBytes=2097152, backupCount=2)
info_logger.setLevel(logging.INFO)
info_logger.setFormatter(formatter)

# to log errors messages
error_logger = RotatingFileHandler(filename='../transformer_errors.log', maxBytes=2097152, backupCount=2)
error_logger.setLevel(logging.ERROR)
error_logger.setFormatter(formatter)

logger.addHandler(debug_logger)
logger.addHandler(info_logger)
logger.addHandler(error_logger)

publication_data_logger = logging.getLogger("publication_data")
# x2 files of 2mb
publication_data_handler = RotatingFileHandler(filename='../publication_data.log', maxBytes=2097152, backupCount=2)
publication_data_logger.addHandler(publication_data_handler)

# database connection
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy()

SECRET_KEY = os.getenv("SECRET_KEY")


# KAFKA
KAFKA_SERVERS = os.getenv("KAFKA_SERVERS")
KAFKA_CLIENT_ID = os.getenv("SERVICE_NAME")
OUTBOX_CDC_TOPIC = os.getenv("OUTBOX_CDC_TOPIC")
