from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def home():
    return {"message": "welcome to my first FastAPI course"}