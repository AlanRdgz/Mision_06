# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: Lee r, R y l y genera un espirografo.

import pygame   # Librería de pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

def generarColorAzar():
    rojo = random.randint(0,255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    colorX = (rojo,verde,azul)
    return colorX


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        k=r/R
        color=generarColorAzar()
        for angulo in range(0, 360 * r // math.gcd(r,R)):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R*(((1-k)*math.cos(a)+1*k+math.cos(((1-k)/k)*a))))
            y = int(R*(((1-k)*math.sin(a)+1*k+math.sin(((1-k)/k)*a))))
            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1)


        for angulo in range(0, 360 * r // math.gcd(r,R)):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R*(((2-k)*math.cos(a)+1*k+math.cos(((1-k)/k)*a))))
            y = int(R*(((2-k)*math.sin(a)+1*k+math.sin(((1-k)/k)*a))))
            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1)


        for angulo in range(0, 360 * r // math.gcd(r,R)):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R*(((3-k)*math.cos(a)+1*k+math.cos(((1-k)/k)*a))))
            y = int(R*(((3-k)*math.sin(a)+1*k+math.sin(((1-k)/k)*a))))
            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1)


        for angulo in range(0, 360 * r // math.gcd(r,R)):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R*(((4-k)*math.cos(a)+1*k+math.cos(((1-k)/k)*a))))
            y = int(R*(((4-k)*math.sin(a)+1*k+math.sin(((1-k)/k)*a))))
            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1)


        for angulo in range(0, 360 * r // math.gcd(r,R)):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R*(((5-k)*math.cos(a)+1*k+math.cos(((1-k)/k)*a))))
            y = int(R*(((5-k)*math.sin(a)+1*k+math.sin(((1-k)/k)*a))))
            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r=int(input("r: "))
    R=int(input("R: "))
    l=float(input("l: "))
    dibujar(r,R,l)   # Por ahora, solo dibuja


# Llamas a la función principal
main()