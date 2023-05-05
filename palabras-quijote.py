

from pyspark import SparkContext
import sys


def main(infilename, outfilename):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        data = sc.textFile(infilename)
        words_rdd = data.map(lambda y: len(y.split()))
        with open(outfilename, 'w') as outfile:
            outfile.write('RESULTS------------------')
            outfile.write('Número de palabras fichero de entrada: '+ str(words_rdd.sum()))
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 {0} <infilename> <outfilename>".format(sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])


