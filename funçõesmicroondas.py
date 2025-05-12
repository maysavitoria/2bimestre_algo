import time

# variaveis globais  
ligado = False
tempo = 0
potencia = 0

# Função para ligar o microondas
def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = nova_potencia
        print(f"Microondas ligado por {tempo} segundos na potência {potencia}.")
        iniciar_cronometro(tempo)
        desligar() #desligr automaticamente
    else:
        print("Microondas já está ligado.")
        
def desligar():
    global ligado
    if ligado:
        ligado = False
        print("Microondas desligado.")
    else:
        print("Microondas já está desligado.")
        
def status():
    if ligado:
        print(f"{tempo}: segundos \n potência {potencia}.")
    else:
        print("Microondas desligado.")
        
def iniciar_cronometro(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print("\n Tempo esgotado!")
    
#pré definições do microondas

def pipoca():
    ligar(30, 100)
    
#rodar função
pipoca()
