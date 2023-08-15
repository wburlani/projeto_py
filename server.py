#server.py
from flask import Flask
import logging
import os

app = Flask(__name__)

# Configuração do logging
log_file = os.path.join('logs', 'app.log')
if not os.path.exists('logs'):
    os.makedirs('logs')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Importação das rotas após a configuração do logging
from route import *

if __name__ == "__main__":
    app.run(debug=True)