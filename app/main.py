from fastapi import FastAPI
from .routers.userRouter import userRouter

app = FastAPI(title="Food Delivery System")

app.include_router(userRouter)
