#Caixa eletrônico
#Autor: Matheus Henrique
print("Bem vindo(A) ao caixa eletrônico.")
entrada = input("Quer entrar ou sair?")
if entrada == 'entrar':
    conta = float(input("Quanto de dinheiro tem na sua conta?"))
    print("Carregando...")
    conta2 = float(input("Quanto quer sacar?"))
    soma = conta - conta2
    print("Carregando...")
    print(f"Pronto, saque com sucesso! sobrou: {soma}")
    print("Volte sempre!")
elif entrada == 'sair':
    print("Até a proxima!")
else:
    print("Você não entrou e nem saiu!! reveja!") 


