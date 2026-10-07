from fastapi import FastAPI, Request

from mockData import products

app = FastAPI()


@app.get("/")
def Home():
    return "Welcome to FastApi"


@app.get("/products")
def get_products():
    return products

# path params
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
# if product available with the product id ,return product else return error message
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct
    return {
        "error": "Product not found for this product id"
    }
# Query params

@app.get("/greet")
def greet_user(name:str,age:int):
    return {
        "greet":f"Hello!,{name} Your age is {age}"
    }
# Request
@app.get("/greeta")
def greet_usera(request:Request):
    query_params = (dict(request.query_params))
    print(query_params)
    return {
        "greet":f"Hello!{query_params.get("name")}, Your age is {query_params.get("age")}"
    }