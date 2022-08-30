from calcular import *

horas_trab = input('Horas trabalhadas: ')
valor_hora= input(' Valor hora: ')
total_salario = calcular_pag(horas_trab, valor_hora)
print(f'O valor do seu salario é R$ {total_salario}')


