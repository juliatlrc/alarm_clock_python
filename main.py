from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(segundos):

    tempo_decorrido = 0

    print(CLEAR)
    while tempo_decorrido < segundos:
        time.sleep(1)
        tempo_decorrido += 1

        tempo_restante = segundos - tempo_decorrido
        minutos_restante = tempo_restante // 60
        segundos_restantes = tempo_restante % 60

        print(f"{CLEAR_AND_RETURN}O alarme irá tocar em:{minutos_restante:02d}:{segundos_restantes:02d}")


    playsound("Clock-sound-effect.mp3")


minutos = int(input("Quantos minutos você quer colocar?"))
segundos = int(input("Quantos segundos você quer esperar?"))
total_segundos = minutos * 60 + segundos

alarm(total_segundos)