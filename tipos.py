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


def recursos_suf (receita):
    for ingred in receita:
        if receita[ingred] > resources[ingred]:
            print(f"Desculpe não há {ingred} suficiente.")
            return False
        return True

def produzir_bebida(receita):
    for item in receita:
        resources[item] -= receita[item]

def solicitar_valor():
    print("Por favor insira as moedas")
    total = input("Quantos quarters?: ")
    total += int(input("Quantos dimes?: "))* 0.10
    input("Quantos nickles?: ")
    input("Quantos pennies?: ")

escolha = input("What would you like? (espresso/latte/cappuccino): ").lower()

bebida = MENU[escolha]
print(bebida)
print(bebida.get("ingredients"))

recursos_ok = recursos_suf(receita=bebida["ingredients"])
print(recursos_ok)
if recursos_ok == True:
    input("Por favor insira as moedas")
    produzir_bebida(receita=bebida["ingredients"])



print(resources)




#def verificar(tipo):


