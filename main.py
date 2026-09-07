from fastapi import FastAPI

app = FastAPI(title="PRASA Cape Town Transit API")

@app.get("/")
def home():
    return {"message": "PRASA Cape Town Transit API is live"}

@app.get("/stations")
def get_stations():
    return [
        {"id": 1, "name": "Cape Town Central", "zone": "Metro Central"},
        {"id": 2, "name": "Bellville", "zone": "Northern Line"},
        {"id": 3, "name": "Simon's Town", "zone": "Southern Line"}
    ]