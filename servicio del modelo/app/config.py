# Rutas de archivos y configuración general
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "modelo"
RUTA_MODELO = MODELS_DIR / "modelo_California_housing_prices.pkl"
