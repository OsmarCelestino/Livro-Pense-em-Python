class time:
    "recebe os parametros, horas, minutos, segundos"
def time_to_int(tempo):
    minutes = tempo.hour * 60 + tempo.minute
    seconds = minutes * 60 + tempo.second
    return seconds
def int_to_time(tempo, seconds):
    time = tempo()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
def multime(tempo, distancia):
    segundos = time_to_int(tempo)
    distancia_media = segundos / distancia
    obj_tempo = int_to_time(tempo, segundos)
    return obj_tempo

