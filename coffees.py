# movies.py

from datetime import datetime
from flask import abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# name:
#   type: "string"
# roaster:
#   type: "string"
# origin:
#   type: "array"
# variety:
#   type: "array"
# process:
#   type: "array"
# altitude:
#   type: "string"

COFFEES = {
  "Don Cayito": {
    "name": "Don Cayito",
    "roaster": "Detour",
    "origin": ["Costa Rica"],
    "variety": ["Catuai"],
    "process": ["White Honey"],
    "altitude": "1750 to 2000 MASL",
    "tasting": ["cachew", "yellow plum", "sugar cane"]
  },
  "El Molino Natural": {
    "name": "El Molino Natural",
    "roaster": "Detour",
    "origin": ["El Salvador"],
    "variety": ["Bourbon", "Pacas"],
    "process": ["Natural"],
    "altitude": "1500 MASL",
    "tasting": ["dried apple", "toasted almond", "chocolate"]
  },
  "Old School Espresso": {
    "name": "Old School Espresso",
    "roaster": "Detour",
    "origin": ["Honduras"],
    "variety": ["Caturra", "Catuai"],
    "process": ["Washed"],
    "altitude": "1800 MASL",
    "tasting": ["caramel", "dark chocolate", "nuts"]
  }
  
}

def read_all():
  return list(COFFEES.values())

def create(coffee):
  name = coffee.get("name")
  roaster = coffee.get("roaster")
  origin = coffee.get("origin")
  variety = coffee.get("variety")
  process = coffee.get("process")
  altitude = coffee.get("altitude")
  tasting = coffee.get("tasting")

  if name not in COFFEES:
    COFFEES[name] = {
      "name": name,
      "roaster": roaster,
      "origin": origin,
      "variety": variety,
      "process": process,
      "altitude": altitude,
      "tasting": tasting,
      "timestamp": get_timestamp(),
    }
    return COFFEES[name], 201
  else:
    abort(
      406,
      f"There is a coffee with {name} already exists"
    )

def read_one(name):
  if name in COFFEES:
    return COFFEES[name]
  else:
    abort(
        404, f"A coffee with the name {name} not found"
    )
    