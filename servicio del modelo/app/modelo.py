# app/modelo.py
import joblib
from .config import RUTA_MODELO

_modelo = None

def cargar_modelo(force_reload: bool = False):
    global _modelo
    if _modelo is None or force_reload:
        _modelo = joblib.load(RUTA_MODELO)
    return _modelo

def predecir(df):
    modelo = cargar_modelo()
    preds = modelo.predict(df)
    return preds.tolist() 
