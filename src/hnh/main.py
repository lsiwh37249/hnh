from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict")
async def root():
    return {"predict_result": random.choice(["hotdog","not hotdog"])}

