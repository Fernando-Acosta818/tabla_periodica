from django.shortcuts import render
import csv

# Create your views here.

def elemento(request, elem):
    
    dicElementos = {}

    keys = ['num_atom', 'elemento', 'nombre', 'masa', 'periodo', 'grupo', 'estructura', 'conf_elec', 'descubrimiento', 'densidad']
    values = []

    with open('elemento/elementos.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[2].lower() == elem or row[0] == elem:
                for i in range(len(keys)):
                    values = row
                    dicElementos[keys[i]] = values[i]

    return render(request, 'elemento/elemento.html', context = dicElementos)