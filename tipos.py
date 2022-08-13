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

def produzir_bebida(ordem_ingredientes):
    for item in ordem_ingredientes:
        resources[item] -= ordem_ingredientes[item]


produzir_bebida(ordem_ingredientes=bebida["ingredients"])

print(resources)


#def verificar(tipo):


