import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get(path="/")
def main():
    return {'message': "Hello FastAPI!"}



@app.get("/home")
def home():
     return {"message": "This codes covers the API-Desigining"}





if __name__ == "__main__":
    uvicorn.run(
        app= "101main:app",
        host= "127.0.0.1",
        port= 8000,
        reload= True,
        log_level= "info"
    )


