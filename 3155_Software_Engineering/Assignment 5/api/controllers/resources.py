from sqlalchemy.orm import Session
from api.models import models
from api.models import schemas

# CREATE
def create(db: Session, resource_in: "schemas.ResourceCreate"):
    obj = models.Resource(
        **(resource_in.model_dump() if hasattr(resource_in, "model_dump") else resource_in.dict())
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# READ ALL
def read_all(db: Session):
    return db.query(models.Resource).all()

# READ ONE
def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

# UPDATE
def update(db: Session, resource_id: int, resource_in: "schemas.ResourceUpdate"):
    obj = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if not obj:
        return None
    data = (
        resource_in.model_dump(exclude_unset=True)
        if hasattr(resource_in, "model_dump")
        else resource_in.dict(exclude_unset=True)
    )
    for k, v in data.items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

# DELETE
def delete(db: Session, resource_id: int):
    obj = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
