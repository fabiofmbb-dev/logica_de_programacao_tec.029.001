# entarda de dados
nome = input("Informe seu nome: "). strip().title()
idade = int(input('Informe sua idade: '))

# estrutura de decisao
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")