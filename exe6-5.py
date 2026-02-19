#  Usando elif (múltiplas condições)
# entrada de dados e variaveis
nota = float(input("digite sua primeira nota : "))
nota2 = float(input("digite sua outra nota : "))
nota3 = float(input("digite sua outra nota : "))
nota4 = float(input("digite sua outra nota : "))

media = (nota + nota2 + nota3 + nota4)/4

20


# condição 1
if media >= 90:
    print("Parabéns! Excelente nota.")
# condição 2    
elif media >= 65:
    print("Muito bom! Você foi aprovado.")
# condição 3    
else:
    print("Você precisa estudar mais.")
    