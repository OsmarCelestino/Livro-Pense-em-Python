import time
data_atual = time.ctime()
hora = data_atual.split()
separar_hora = hora[3]
repartir = separar_hora.split(':')
hora = repartir[0]
minutos = repartir[1]
segundos = repartir[2]
epoca = time.time()
print('Horas = {}'.format(hora))
print('Minutos = {}'.format(minutos))
print('Segundos = {}'.format(segundos))
print('Época = {}'.format(epoca))