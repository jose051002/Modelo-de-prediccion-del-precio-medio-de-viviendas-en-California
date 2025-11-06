import pandas as pd

def dict_a_dataframe(data_dict):
    df = pd.DataFrame([data_dict])

    # Ingenieria de características
    df["habitaciones_por_hogar"] = df["total_rooms"] / df["households"]
    df["habitaciones_por_persona"] = df["total_rooms"] / df["population"]
    df["habitantes_por_hogar"] = df["population"] / df["households"]

    # One-hot encoding de ocean_proximity
    categorias = ["INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
    for cat in categorias:
        df[f"ocean_proximity_{cat}"] = (df["ocean_proximity"] == cat).astype(int)
    df.drop(columns=["ocean_proximity"], inplace=True)

    # Orden final
    columnas_finales = [
        "longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms",
        "population", "households", "median_income",
        "habitaciones_por_hogar", "habitaciones_por_persona", "habitantes_por_hogar",
        "ocean_proximity_INLAND", "ocean_proximity_ISLAND",
        "ocean_proximity_NEAR BAY", "ocean_proximity_NEAR OCEAN"
    ]
    df = df[columnas_finales]

    return df
