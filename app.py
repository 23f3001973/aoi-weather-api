from fastapi import FastAPI

app = FastAPI()

@app.get("/weather")
def get_weather():
    return {
        "2024-07-21": "Light rain showers",
        "2024-07-22": "Sunny intervals",
        "2024-07-23": "Heavy rain"
    }
