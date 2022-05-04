import csv

def obtener_elemento(nombre):

    dicElementos = {}

    keys = ['num_atom', 'elemento', 'nombre', 'masa', 'periodo', 'grupo', 'estructura', 'conf_elec', 'descubrimiento', 'densidad']
    values = []

    with open('elementos.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[2].lower() == nombre:
                for i in range(len(keys)):
                    values = row
                    dicElementos[keys[i]] = values[i]

    return dicElementos

print(obtener_elemento('oxigeno'))   