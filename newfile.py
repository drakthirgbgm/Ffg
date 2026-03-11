nome = (input("digite seu nome: "))
resposta = input(f"olá, {nome} tudo bem?(sim/nao)")
if "sim":
    print("foda-se :)")
elif "nao":
    print("foda-se")
else:
    print("ta com graça aqui caralho, vai te fuder eleitor do lula arrombado")
idade = int(input("digite sua idade: "))

if idade < 16:
    print("voce nao pode votar, mais se for no lula ta liberado")
elif idade < 18:
    print("voce pode votar, mais é opcional, lula ou no nove dedos")
else: 
    print("seu voto é obrigatorio no lula, nao gostou? faz o l bem gostoso bebe)")
