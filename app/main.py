from fastapi import FastAPI
from . import auth_routes
from . import order_routes

app = FastAPI()

app.include_router(auth_routes.auth_router)
app.include_router(order_routes.order_router)

@app.get("/")
def default():
    return {"message:":"Default main method..."}