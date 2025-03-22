from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"hello":"world"}

@app.get("/2")
async def root2():
    return {"message":"hello world"}