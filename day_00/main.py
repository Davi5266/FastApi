from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def test():
	print("PL")
	return {"message":"OK"}
