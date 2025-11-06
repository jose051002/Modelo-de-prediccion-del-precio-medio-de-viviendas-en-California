from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .esquemas import PredictRequest, PredictResponse, PredictResponseItem
from .preprocesar import dict_a_dataframe
from .modelo import predecir, cargar_modelo
from .utils import configurar_logger

logger = configurar_logger()
app = FastAPI(title="California Housing Price Predictor", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST","GET","OPTIONS"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    cargar_modelo()
    logger.info("Modelo cargado.")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    try:
        data_obj = request.data
        df = dict_a_dataframe(data_obj.dict())
        results = predecir(df)
        response_items = [PredictResponseItem(prediction=float(p)) for p in results]
        response = PredictResponse(predictions=response_items, model="California Housing Prices Model", n=len(response_items))
        return response
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.exception("Error interno al procesar la predicción")
        raise HTTPException(status_code=500, detail="Error interno en el servidor")
