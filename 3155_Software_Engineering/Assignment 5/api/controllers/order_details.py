from sqlalchemy.orm import Session
from api.models import models
from api.models import schemas

def create(db: Session, order_detail_in: "schemas.OrderDetailCreate"):
    obj = models.OrderDetail(
        **(order_detail_in.model_dump() if hasattr(order_detail_in, "model_dump") else order_detail_in.dict())
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update(db: Session, order_detail_id: int, order_detail_in: "schemas.OrderDetailUpdate"):
    obj = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if not obj:
        return None
    data = (
        order_detail_in.model_dump(exclude_unset=True)
        if hasattr(order_detail_in, "model_dump")
        else order_detail_in.dict(exclude_unset=True)
    )
    for k, v in data.items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, order_detail_id: int):
    obj = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True

