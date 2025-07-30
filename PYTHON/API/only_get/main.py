from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"Message": "Welcome to calculator"}

@app.get("/add/{a}/{b}")
def addition(a: int, b: int):
    return {"Solution": (a + b)}

@app.get("/subtract/{a}/{b}")
def subtraction(a: int, b: int):
    return {"Solution": (a - b)}

@app.get("/multiply/{a}/{b}")
def multiplication(a: int, b: int):
    return {"Solution": (a * b)}

@app.get("/divide/{a}/{b}")
def division(a: int, b: int):
    if b == 0:
        return {"Error": "Cannot divide by zero"}
    return {"Solution": (a / b)}