nome = input('Informe seu nome: ').title().strip() 
massa = float(input("Informe a sua massa: ").replace(",",'.'))
altura = float(input("Informe a sua altura: ").replace(",",'.'))
imc = massa/(altura * altura)

print("Seu IMC é:", imc)

if imc < 18.5:
    print(f"{nome} está abaixo do peso")
elif imc <25:
    print(f"{nome} está no peso ideal")
elif imc <30:
    print(f"{nome} está acima do peso")
elif imc <35:
    print(f"{nome} está obeso")
elif imc <40:
    print(f"{nome} está com obesidade nivel 2")
else:
    print(f"{nome} está com obsesidade mórbida") 


  