from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}


