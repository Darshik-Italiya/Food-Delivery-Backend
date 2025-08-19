from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..schemas.user import UserOut, UserCreate, UserLogin
from ..models.user import User
from ..database.db import get_session
from ..services.userService import create_user, login_user

userRouter = APIRouter(prefix="/users", tags=["Users"])


@userRouter.post("/register", response_model=UserOut)
async def register(user: UserCreate, session: Session = Depends(get_session)):
    return await create_user(user, session)


@userRouter.post("/login")
async def login(user: UserLogin, session: Session = Depends(get_session)):
    return await login_user(user, session)
