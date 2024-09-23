@app.get("/")
async def hello():
    return {"message": "Testing FastAPI for the ABB Hackathon!"}