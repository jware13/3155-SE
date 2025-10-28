from sqlalchemy.orm import Session
from api.dependencies.database import SessionLocal
from api.models import models
from api.models import schemas

def create(db: Session, sandwich_in: "schemas.SandwichCreate"):
    obj = models.Sandwich(**sandwich_in.model_dump()) if hasattr(sandwich_in, "model_dump") else sandwich_in.dict()
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich_id: int, sandwich_in: "schemas.SandwichUpdate"):
    obj = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if not obj:
        return None
    data = sandwich_in.model_dump(exclude_unset=True) if hasattr(sandwich_in, "model_dump") else sandwich_in.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, sandwich_id: int):
    obj = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return True