from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is Mariah Counter project backend"}