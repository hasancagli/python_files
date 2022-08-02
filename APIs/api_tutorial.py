# To run the code: uvicorn <file_name_without_.py>:app --reload
from fastapi import FastAPI
from pydantic import BaseModel  # to create easier to read class


class Item(BaseModel):
    name: str
    price: float
    brand: str = None


class UpdateItem(BaseModel):
    name: str = None
    price: float = None
    brand: str = None


app = FastAPI()

# END POINT: Point of entry in a communication channel when two systems are interacting. (API and Server Interaction)
# endpoint examples: /hello, /home etc.

"""
METHODS
GET -> Getting, gathering information
POST -> Pushing new information
PUT -> Updating
DELETE -> Delete information
"""


@app.get('/')
def home():
    return {"Data": "Test"}


@app.get('/about')
def about():
    return {"Data": "About"}


inventory = {}


@app.get('/get-item/{item_id}')
def get_item(item_id: int):
    return inventory[item_id]

# Query Parameters: facebook.com?user=None etc.


@app.get('/get-by-name')
def get_item(name: str = None):  # name is an optional query parameter
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]

    return {"Data", "Not Found!"}


# POST METHOD
@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    if (item_id in inventory):
        return {"Error": "Item ID already exists."}
    inventory[item_id] = item
    return inventory[item_id]


# PUT METHOD
@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):
    if (item_id not in inventory):
        return {"Error": "Item ID does not exists."}

    if item.name != None:
        inventory[item_id].name = item.name

    if item.brand != None:
        inventory[item_id].brand = item.brand

    if item.price != None:
        inventory[item_id].price = item.price

    return inventory[item_id]

# DELETE METHOD


@app.delete("/delete-item")
def delete_item(item_id: int):
    if item_id not in inventory:
        return {"Error": "ID does not exists"}
    del inventory[item_id]
    return {"Success": "Deleted!"}
