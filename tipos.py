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


def conferir_moedas(bebida, valor_inserido):
        troco = valor_inserido - bebida["cost"]
        return troco


def produzir_bebida(receita):
    for item in receita:
        resources[item] -= receita[item]
        

def processar_moedas():
    print("Por favor insira as moedas:")
    total = int(input("Quantos quarters?: "))*0.25
    total += int(input("Quantos dimes?: "))* 0.10
    total += int(input("Quantos nickles?: "))*0.05
    total += int(input("Quantos pennies?: "))*0.01
    return total



escolha = input("What would you like? (espresso/latte/cappuccino): ").lower()

bebida = MENU[escolha]
print(bebida)
print(bebida.get("ingredients"))

recursos_ok = recursos_suf(receita=bebida["ingredients"])

print(recursos_ok)
if recursos_ok == True:
        valor_inserido = processar_moedas()
        troco = round(conferir_moedas(bebida, valor_inserido),2)
if troco >= 0:
    produzir_bebida(receita=bebida["ingredients"])
    print(f"Here is ${troco} in change.\nHere is your latte ☕️. Enjoy!")
else: print("Desculpe, não há dinheiro suficiente.\nDinheiro reembolsado")       

print(valor_inserido)
print(resources)







