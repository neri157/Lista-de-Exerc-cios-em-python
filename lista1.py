#primeira questao#
f = float(input("temperatura em fahrenheit: "))
c = (f - 32) * 5 / 9 #* multiplicacao / divisao
print(f"{f}°F = {c:.2f}°C") 


#segunda questao#
total_pares = 58
caixa = total_pares // 12  #divisao inteira
sobra = total_pares % 12  #resto da divisao
print(f"total de pares: {total_pares}") 
print(f"caixas cheias: {caixa}")
print(f"pares restantes: {sobra}")

#tercerira questao#

x = float(input("digite um numero:")) #float responsavel por numeros decimais 
y = float(input("digite um numero:")) #input para o usuario digitar algo 
z = float(input("digite um numero:")) 

conta = (x + y) ** 2 / (x - z) #** pra fazer a elevaçao/ dividir/ () para fazer a prioridade da conta

print(f"resultado: {conta:.2f}") #f para formatar a saida do resultado/ .2f para limitar a 2 casas decimais
