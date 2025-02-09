from fastapi import FastAPI

app = FastAPI()

@app.get("/process")
def process_data():
    telemetry_data = {"temperature": 22.5, "pressure": 1.8}
    result = orion_ai_pipeline(telemetry_data)
    return {"message": result}

