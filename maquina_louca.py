import time

ligado=False
tempo=0
temperatura=0

def ligar(novo_tempo, nova_temperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado=True
        tempo=novo_tempo
        temperatura=nova_temperatura
        print(f"maquina de lavar louça ligado por {tempo} segundos na temperatura {temperatura}.")
        iniciar_cronometro(tempo)
        desligar() #desligr automaticamente
    else:
        print("maquina de lavar louça já está ligado.")
        
def desligar():
    global ligado
    if ligado:
        ligado=False
        print("maquina de lavar louça desligado.")
    else:
        print("maquina de lavar louça já está desligado.")
        
def status():
    if ligado:
        print(f"{tempo}: segundos \n temperatura {temperatura}.")
    else:
        print("maquina de lavar louça desligado.")   
        
def iniciar_cronometro(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print("\n Tempo esgotado!")


def vidro():
    ligar(120, 100)

def plastico():
    ligar(60, 21)

def metal():
    ligar(120, 30)

escolha = input("Escolha o tipo de louça (vidro, plástico, metal): ")
if escolha == "vidro":
    vidro()
elif escolha == "plástico":
    plastico()
elif escolha == "metal":
    metal()
else:
    print("Tipo de louça inválido.")    