# app/esquemas.py
from pydantic import BaseModel, Field
from typing import List, Literal, Dict

#Datos de entrada
class PredictData(BaseModel):
    longitude: float = Field(..., description="Longitud geográfica de la vivienda")
    latitude: float = Field(..., description="Latitud geográfica de la vivienda")
    housing_median_age: float = Field(..., description="Edad media de las viviendas")
    total_rooms: float = Field(..., description="Número total de habitaciones en el bloque")
    total_bedrooms: float = Field(..., description="Número total de dormitorios en el bloque")
    population: float = Field(..., description="Número total de habitantes en el bloque")
    households: float = Field(..., description="Número total de hogares en el bloque")
    median_income: float = Field(..., description="Ingreso medio del bloque")
    ocean_proximity: Literal["INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"] = Field(..., description="Proximidad al océano")

#Request principal
class PredictRequest(BaseModel):
    data: PredictData

# Respuesta individual
class PredictResponseItem(BaseModel):
    prediction: float

# Respuesta completa
class PredictResponse(BaseModel):
    predictions: List[PredictResponseItem]
    model: str
    n: int
