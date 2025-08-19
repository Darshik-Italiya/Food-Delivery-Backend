from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from ..schemas.user import UserCreate, UserLogin
from ..models.user import User
from ..database.db import get_session
from ..auth.hash_jwt import hashed_password, verify_password, create_access_token


# Register:-------------------
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    check_email = select(User).where(User.email == user.email)
    existing_user = session.exec(check_email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hash_pass = await hashed_password(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_pass,
        phone_number=user.phone_number,
        address=user.address,
        role=user.role,
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


# Login:-------------------
async def login_user(user: UserLogin, session: Session = Depends(get_session)):
    check_email = select(User).where(User.email == user.email)
    existing_user = session.exec(check_email).first()

    if not existing_user or not verify_password(
        user.password, existing_user.password_hash
    ):
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    # Create token
    token = create_access_token({"sub": existing_user.name})
    return {"access_token": token, "token_type": "Bearer"}
