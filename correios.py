pacotes = ("ABC123", "XYZ789", "DEF456", "JKL321", "MNO654", "PQR987","STU741") 

rastreio = ( "Enviado",  "Recebido", "Em Trânsito" ,"Enviado" ,"Recebido", "Em Trânsito","Enviado")

# 1) conte quantos pacotes estão em cada status: enoviado, recebido e em trânsito
status_enviado = print(" quantos pacotes foram enviados:", rastreio.count("Enviado"), "Pacotes: ABC123, JKL321, STU741")
status_recebido = print(" quantos pacotes foram recebidos:", rastreio.count("Recebido"), "Pacotes: XYZ789, MNO654")
status_em_transito = print(" quantos pacotes estão em trânsito:", rastreio.count("Em Trânsito"), "Pacotes: DEF456, PQR987")


#2) crie uma lista com os códigos dos pacotes que estão em trânsito
pacotes_em_transito = [pacotes[i] for i in range(len(rastreio)) if rastreio[i] == "Em Trânsito"]
print("Códigos dos pacotes em trânsito:", pacotes_em_transito)

#3) use uma função que recebe um codigo de rastreamento e retorna o status do pacote ou uma mensagem informando que o código não esta cadstrado
codigo = input("Digite o código de rastreamento do pacote: ")
if codigo in pacotes:
    index = pacotes.index(codigo)
    print(f"O status do pacote {codigo} é: {rastreio[index]}") 
else:
    print("Código não cadastrado.")
    
#4) ordene os pacotes por ratreamento e exiba a lista ordenada    
ordenados = sorted(rastreio)
