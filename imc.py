altura = float(input("Digite sua altura em Metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2
 
print("Seu IMC é: %.4f" % imc)
 
if imc < 16:
	print("Magreza muito abaixo")
elif imc < 17:
	print("Magreza abaixo")
elif imc < 18.5:
	print("Magreza leve")
elif imc < 25:
	print("Parabéns!! Saudável")
elif imc < 30:
	print("Sobrepeso")
elif imc < 35:
	print("Obesidade Grau I")
elif imc < 40:
	print("Obesidade Grau II (severa)")
else:
	print("Obesidade Grau III (mórbida)")