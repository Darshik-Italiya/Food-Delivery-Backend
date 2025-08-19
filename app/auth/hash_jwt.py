from passlib.context import CryptContext
from ..schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def hashed_password(password: str):
    return pwd_context.hash(password)
