__author__ = "Angel Jimenez Escobar"

import sys
import networkx as nx

MaxNodes = pow(10, 5)
MaxColors = pow(10, 5)
colors = []
numbers_nodes = 0
G = nx.Graph()


def read_file(filename):
    """ This is the method to read the file, and contain all the core of this program
        I use a library call networkx

        Parameters:
        filename (string): this is the path of the name to read

        Returns:
            void
    """

    """ First Check if the path of the file exist or not"""
    try:
        f = open(filename)
    except OSError as e:
        print("El archivo no puede ser accedido o no existe")
        sys.exit()

    iterator: int = 0
    i = 0

    ''' Read each line of the file'''
    for line in f:

        ''' in the first line check if is a number or not'''
        if iterator == 0:
            try:
                numbers_nodes = int(line)
                val = int(line)
                if MaxNodes < val:
                    print("Excede la cantidad maxima de nodos")
                    sys.exit(0)
            except ValueError:
                print("La primera linea debe ser un numero entero")
                sys.exit(0)

        ''' in this iteraction check the numbr of color, need the same number of color to number of colors'''
        if iterator == 1:
            colors = list(map(int, line.strip().split(' ')))

            if MaxColors < len(colors):
                print("Excede la cantidad maxima de colores")
                sys.exit(0)

            if numbers_nodes != len(colors):
                print("La cantidad de nodos y de colores debe ser la misma")
                sys.exit(0)

            ''' when finish to check if the program can run, create all nodes in the graph, and add the color value'''
            for x in range(numbers_nodes):
                G.add_node(x + 1, color = colors[x])

        if iterator > 1:
            ''' check each line after the list of colors, and conect each node with others '''
            G.add_edge(int(line[0]), int(line[2]))

        iterator += 1


    ''' This section is for calculate each value to print '''
    for x in range(numbers_nodes):
        sum = 0
        for y in range(numbers_nodes):
            values = []
            nodes = nx.shortest_path(G, source= x + 1, target= y + 1)
            for z in nodes:
                data = G.nodes[z]['color']
                if data not in values:
                    values.append(data)
            sum += len(values)

        print(sum)

def display_usage():
    """ this method only print one message"""
    print('Por favor pase como parametro el archivo a evaluar')


if __name__ == '__main__':
    """ Check if the program is running with the name of the file to read 
        if the file doesn't pass, the program show message and finish
    """
    if len(sys.argv) < 2:
        display_usage()
        sys.exit(0)

    ''' Get the name of the file to read'''
    file_name = sys.argv[1]

    ''' excecute program '''
    read_file(file_name)