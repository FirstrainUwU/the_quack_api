import requests
from dataclasses import dataclass

@dataclass(frozen=True)
class DuckData:
    message: str
    quackcount: str 
    fav_food: str
    fav_color: str
    is_happy: bool

def filter(response) -> DuckData:
    message = response['message']
    quackcount = str(response['quackcount'])

    fav_dic = response['favorites']
    fav_food = fav_dic['food']
    fav_color = fav_dic['color']

    is_happy = response['is_duck_happy']

    return DuckData(
        message=message,
        quackcount=quackcount,
        fav_color=fav_color,
        fav_food=fav_food,
        is_happy=is_happy
    )

def printings(duck):    
    print("Duck says", duck.message)
    print("Duck has quacked",duck.quackcount,"times!")
    print("Duck loves to eat",duck.fav_food,"and she loves the color",duck.fav_color,"!")
    
    if duck.is_happy:
        print('Duck is happy!')
    else:
        print('Duck is sad :(')

def main():
    url = 'https://the-quack-api.fly.dev/duck'
    response = requests.get(url).json()

    data = filter(response)
    printings(data)

if __name__ == '__main__':
    main()