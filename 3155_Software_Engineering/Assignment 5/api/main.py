from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders
from .dependencies.database import engine, get_db
from api.models import schemas
from api.dependencies.database import get_db
from api.controllers import sandwiches as sandwiches_controller
from api.controllers import resources as resources_controller
from api.controllers import orders as recipes_controller
from api.controllers import order_details as order_details_controller


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# sandwiches endpoints
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich_in: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches_controller.create(db=db, sandwich_in=sandwich_in)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches_controller.read_all(db)

@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich | None, tags=["Sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return sandwiches_controller.read_one(db, sandwich_id)

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich | None, tags=["Sandwiches"])
def update_sandwich(sandwich_id: int, sandwich_in: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    return sandwiches_controller.update(db, sandwich_id, sandwich_in)

@app.delete("/sandwiches/{sandwich_id}", response_model=bool | None, tags=["Sandwiches"])
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return sandwiches_controller.delete(db, sandwich_id)
                                                              
# resources endpoints
# (Similar endpoints for resources would go here)

@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource_in: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources_controller.create(db=db, resource_in=resource_in)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources_controller.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource | None, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources_controller.read_one(db, resource_id)

@app.put("/resources/{resource_id}", response_model=schemas.Resource | None, tags=["Resources"])
def update_resource(resource_id: int, resource_in: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    return resources_controller.update(db, resource_id, resource_in)

@app.delete("/resources/{resource_id}", response_model=bool | None, tags=["Resources"])
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources_controller.delete(db, resource_id)

# recipe endpoints

@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe_in: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes_controller.create(db=db, recipe_in=recipe_in)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes_controller.read_all(db)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe | None, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipes_controller.read_one(db, recipe_id)

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe | None, tags=["Recipes"])
def update_recipe(recipe_id: int, recipe_in: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    return recipes_controller.update(db, recipe_id, recipe_in)

@app.delete("/recipes/{recipe_id}", response_model=bool | None, tags=["Recipes"])
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipes_controller.delete(db, recipe_id)


#order details endpoints

@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def create_order_detail(order_detail_in: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details_controller.create(db=db, order_detail_in=order_detail_in)

@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["OrderDetails"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details_controller.read_all(db)

@app.get("/order_details/{order_detail_id}", response_model=schemas.OrderDetail | None, tags=["OrderDetails"])
def read_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    return order_details_controller.read_one(db, order_detail_id)

@app.put("/order_details/{order_detail_id}", response_model=schemas.OrderDetail | None, tags=["OrderDetails"])
def update_order_detail(order_detail_id: int, order_detail_in: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    return order_details_controller.update(db, order_detail_id, order_detail_in)

@app.delete("/order_details/{order_detail_id}", response_model=bool | None, tags=["OrderDetails"])
def delete_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    return order_details_controller.delete(db, order_detail_id)








# orders endpoints

@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)