#primeira questao#
f = float(input("Temperatura em Fahrenheit: "))
c = (f - 32) * 5 / 9
print(f"{f}°F = {c:.2f}°C")

congelando = c <= 0
print(congelando)
if congelando:
    print("esta congelando!")

esquentando = c >= 30
print(esquentando)
if esquentando:
    print("esta esquentando!")

#segunda questao#

idade = 18
saldo_ingresso = 50.00
horario_chegada = 22

idade >= 18
saldo_ingresso >= 50.00
horario_chegada <= 22


#marcos
nome = "marcos"
print(nome)
idade = 20
saldo_ingresso = 60.00
horario_chegada = 20

print(idade >= 18 and saldo_ingresso >= 50.00 and horario_chegada <= 22)
if idade >= 18 and saldo_ingresso >= 50.00 and horario_chegada <= 22:
    print(f"{nome} está liberado!")

else :
    print(f"{nome} não está liberado!")
#julia
nome = "julia"
print(nome)
idade = 17
saldo_ingresso = 150.00
horario_chegada = 21

print(idade >= 18 and saldo_ingresso >= 50.00 and horario_chegada <= 22)
if idade >= 18 and saldo_ingresso >= 50.00 and horario_chegada <= 22:
    print(f"{nome} está liberada!")

else :
    print(f"{nome} não está liberada!")

#roberto
nome = "roberto"
print(nome)
idade = 25
saldo_ingresso = 45.00
horario_chegada = 23

print(idade >= 18 and saldo_ingresso >= 50.00 and horario_chegada <= 22)
if idade >= 18 and saldo_ingresso >= 50.00 and horario_chegada <= 22:
    print(f"{nome} está liberado!")

else :
    print(f"{nome} não está liberado!")

#ana 
nome = "ana"
print(nome)
idade = 18
saldo_ingresso = 50.00
horario_chegada = 22

print(idade >= 18 and saldo_ingresso >= 50.00 and horario_chegada <= 22)
if idade >= 18 and saldo_ingresso >= 50.00 and horario_chegada <= 22:
    print(f"{nome} está liberada!")

else :
    print(f"{nome} não está liberada!")

#terceira questao#

peso_carga = 1850
eixo = 4
saldo_motorista = 30.00
tarifa_base = 15.50
limite_peso = 2000

(peso_carga + 200) > limite_peso
eixo == 4
saldo_motorista >= 2 * tarifa_base
limite_peso != 2500
(saldo_motorista - tarifa_base) <= 10.00

print((peso_carga + 200) > limite_peso)
print(eixo == 4)
print(saldo_motorista >= 2 * tarifa_base)
print(limite_peso != 2500)
print((saldo_motorista - tarifa_base) <= 10.00)

#quarta questao#

n1 = float(input("digite sua nota:"))
n2 = float(input("digite sua nota:"))
n3 = float(input("digite sua nota:"))

media = (n1 + n2 + n3) / 3
resultado = media >= 7

if media >= 7:
    print("aprovado")
else:
    print("reprovado")

print(media)
print(resultado)





