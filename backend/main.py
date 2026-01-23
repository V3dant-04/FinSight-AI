from fastapi import FastAPI

app = FastAPI(title="FinSight AI")

@app.get("/")
def root():
    return {"status": "FinSight AI backend running"}
