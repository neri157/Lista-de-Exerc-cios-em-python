#primeira questão

fahrenheit = float(input('digite a temperatura'))
celsius = (fahrenheit - 32) * 5 / 9
print ('temperatura em celsius', celsius)

#segunda questão

total_pares = int(input('digite a quantidade de pares'))

caixas = total_pares // 12
sobra = total_pares % 12

print(f"caixas completas", caixas)
print(f"pares que sobraram", sobra)

#terceira questão
x = float(input ('digite o valor de x'))
y = float(input ('digite o valor de y'))
z = float(input ('digite o valor de z'))

resultado = ((x + y) ** 2) // (x - z)

print("resultado =", resultado)