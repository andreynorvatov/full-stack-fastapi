from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependency import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.core.models import Services as ServicesModel
from app.core.schemas import Services as SRV
from typing import List

router = APIRouter()


@router.get("/",
            description="Описание эндпоинта",
            summary="Получить все сервисы",
            # response_model=List[SRV]
            )
def get_all_services(db: Session = Depends(get_db)):
    """
    Получение всех сервисов
    """
    query = select(ServicesModel)
    print(query)
    r = db.execute(query).all()
    # print([i.__dict__.items() for i in r])
    return r
