from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "UADE project is running"}
