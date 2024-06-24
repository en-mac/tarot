from fastapi import APIRouter, Depends
from ..schemas.user import UserCreate, UserResponse
from ..services.auth_service import AuthService

router = APIRouter()

@router.post("/login", response_model=UserResponse)
def login(user: UserCreate):
    return AuthService.login(user)
