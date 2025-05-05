def calculadora_imc(pessoa):
    imc = pessoa ["peso"]/ pessoa ["altura"] * pessoa["altura"]
    resultado = f" o IMC {pessoa} é {imc:.2f}"
    #comando ternário:
    saudavel = 18.5 < imc < 25

    return{
        "nome": pessoa["nome"],
        "imc":imc,
        "resultado":resultado,
        "saudavel":saudavel
    }

pessoa1={
    "nome": "josé",
    "peso": 110,
    "altura": 1.75
}

print(calculadora_imc(pessoa1))

pessoa2={
    "nome":"Letícia",
    "peso": 51,
    "altura": 1.60

}

print (calculadora_imc(pessoa2))
