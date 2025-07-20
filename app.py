# app.py
from fastapi import FastAPI, UploadFile
import pandas as pd

app = FastAPI()

@app.post("/upload")
async def upload_excel(file: UploadFile):
    df = pd.read_excel(file.file, engine="openpyxl")
    result = {
        row["localDate"]: row["enhancedWeatherDescription"]
        for _, row in df.iterrows()
    }
    return result
