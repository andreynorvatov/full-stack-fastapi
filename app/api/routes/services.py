from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()


@router.get("/", )
def get_all_services():
    """
    Получение всех сервисов
    """
    return {"test": "ok"}