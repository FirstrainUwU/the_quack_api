# Imports
from random import choice

from fastapi import FastAPI

# Main app object
app = FastAPI(
    title="TheQuackAPI", description="A really simple API which quacks at you!"
)

# storage for counting quacks
global quackcount
quackcount = 0

favorite_duck_foods = ["pasta", "leaves", "juice"]
favorite_duck_color = ["blue", "green", "yellow"]
is_duck_happy = [True, False]
message = ["Quack quack!", "Pack pack!", "I'm a happy duck"]


# root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to TheQuackAPI!"}


# duck endpoint
@app.get("/duck")
def duck():
    global quackcount
    quackcount += 1

    return {
        "message": choice(message),
        "quackcount": quackcount,
        "favorites": {
            "food": choice(favorite_duck_foods),
            "color": choice(favorite_duck_color),
        },
        "is_duck_happy": choice(is_duck_happy),
    }
