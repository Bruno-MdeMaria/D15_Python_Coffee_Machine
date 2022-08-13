MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

escolha = input("What would you like? (espresso/latte/cappuccino): ").lower()

bebida = MENU[escolha]
print(bebida)
print(bebida.get("ingredients"))

def produzir_bebida(bebida,resources):
    for item in bebida.get("ingredients"):
        resources["item"] -= bebida["item"]


produzir_bebida(bebida,resources)

print(resources)


#def verificar(tipo):


