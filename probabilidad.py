

import random
import sys
def main(fichero_entrada, fichero_salida, porcentaje):
    with open(fichero_entrada) as entrada:
        with open(fichero_salida, 'w') as salida:
            for linea in entrada:
                if random.random()<=porcentaje:
                    salida.write(linea)


if __name__=="__main__":
    if len(sys.argv)<4:
        print(f"Usage: {sys.argv[0]} <infilename> <outfilename> <ratio>")
        exit(1)
        
    fichero_entrada = sys.argv[1]
    fichero_salida = sys.argv[2]
    porcentaje = float(sys.argv[3])
    main(fichero_entrada, fichero_salida, porcentaje)
