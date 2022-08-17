import os


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
            os.system("cls")  
            print(f"Sorry there is not enough {ingred}.")
            return False
        return True


def conferir_moedas(bebida, valor_inserido):
        troco = valor_inserido - bebida["cost"]
        return troco


def produzir_bebida(receita):
    for item in receita:
        resources[item] -= receita[item]
        

def processar_moedas():
    
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))* 0.10
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return round(total,2)

caixa = 0
maquina_on = True

while maquina_on:
    escolha = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if escolha == "off":
        maquina_on = False
    elif escolha == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${caixa:.2f}")
    else:
          bebida = MENU[escolha]
          #print(bebida) TEMP
          #print(bebida.get("ingredients")) TEMP

          recursos_ok = recursos_suf(receita=bebida["ingredients"])

          #print(recursos_ok) TEMP
          if recursos_ok == True:             
            valor_inserido = processar_moedas()
            troco = round(conferir_moedas(bebida, valor_inserido),2)
            if troco >= 0:
                caixa += bebida["cost"]
                produzir_bebida(receita=bebida["ingredients"])
                os.system("cls") 
                print(f"Here is ${troco} in change.\nHere is your latte ☕️. Enjoy!")
                
            else:
                os.system("cls")   
                print("Sorry that's not enough money.\nMoney refunded.")
                
          
           
                  





  






