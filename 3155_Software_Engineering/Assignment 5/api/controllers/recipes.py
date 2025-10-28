from sqlalchemy.orm import Session
from api.models import models
from api.models import schemas

def create(db: Session, recipe_in: "schemas.RecipeCreate"):
    obj = models.Recipe(
        **(recipe_in.model_dump() if hasattr(recipe_in, "model_dump") else recipe_in.dict())
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe_id: int, recipe_in: "schemas.RecipeUpdate"):
    obj = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not obj:
        return None
    data = (
        recipe_in.model_dump(exclude_unset=True)
        if hasattr(recipe_in, "model_dump")
        else recipe_in.dict(exclude_unset=True)
    )
    for k, v in data.items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, recipe_id: int):
    obj = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True