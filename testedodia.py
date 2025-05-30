from datetime import datetime

def pede_info():
    nome = input("Olá, qual é o seu nome ?")
    idade = int(input(f"{nome}, Quantos anos você tem ?"))

    ano_atual = datetime.now().year
    ano_nascimento = ano_atual - idade
    print(f"{nome} você nasceu no ano de {ano_nascimento}")
   
    
    
    


pede_info()

