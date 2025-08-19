from fastapi import Depends, status, HTTPException
from jose import jwt, JWTError
from .hash_jwt import verify_password, create_access_token


def require_role(*allowed_roles):
    def role_checker(current_user=Depends(create_access_token)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )
        return current_user

    return role_checker
