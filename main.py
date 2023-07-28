import os

def preguntarNotas():
    os.system('cls')
    notasExamen = 11
    totalNota = []
    print(f"""      Boletin
          
 ¡Hola! A continuacion te pedimos que completes el boletin
          """)
    name = input(' Dinos tu nombre: ')
    print("""
 Le pedimos que ingrese la puntuacion que a sacado en cada examen.
          """)
    for nota in range(1, notasExamen):
        notaExa = int(input(f'- Examen N°{nota}: '))
        totalNota.append(notaExa)
        
        if int(notaExa) > 10:
            print('Una nota mayor a 10 no es válida')
            totalNota.remove(int(notaExa))
            continue
    
    promedio = sum(totalNota) / len(totalNota)
    
    if promedio >= 6:
        print(f'Felicidades {name}! Has aprobado con {int(promedio)}')    
    else:
        print(f'Lo sentimos {name}, no has aprobado, has sacado: {int(promedio)}')    
    
preguntarNotas()