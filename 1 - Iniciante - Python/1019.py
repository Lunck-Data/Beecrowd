# 1019 - Conversão de Tempo

#from datetime import datetime, timedelta
#segundos = int(input())
#hora = datetime(2005,12,15)
#hora = hora + timedelta(seconds=segundos)
#print(hora.strftime("%H:%M:%S"))

segundos = int(input())

hora = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(f"{hora}:{minutos}:{segundos}")