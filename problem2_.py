__author__ = "Angel Jimenez Escobar"

import sys
from Tree import Tree

MaxNodes = pow(10, 5)
MaxColors = pow(10, 5)
colors = []
numbers_nodes = 0


def read_file(filename):
    """ This is the first method to read, and contain all the core

        Parameters:
        filename (string): this is the path of the name to read

        Returns:
            void
    """
    try:
        f = open(filename)
    except OSError as e:
        print("El archivo no puede ser accedido o no existe")
        sys.exit()

    iterator: int = 0
    i = 0

    for line in f:
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

        if iterator == 1:
            colors = list(map(int, line.strip().split(' ')))

            if MaxColors < len(colors):
                print("Excede la cantidad maxima de colores")
                sys.exit(0)

            if numbers_nodes != len(colors):
                print("La cantidad de nodos y de colores debe ser la misma")
                sys.exit(0)

            tree = Tree(numbers_nodes)

            for color in colors:
                tree.add_color(i, i, color)
                i += 1

            i = 0

        if iterator > 1:
            tree.add_color(int(line[0]) - 1, int(line[2]) - 1, -1)
            i += 1

        iterator += 1

    tree.sum(5)

    '''    if iterator > 1:
            if len(tree.all_nodes()) == 0:
                tree.create_node(line[0], line[0], data=colors[i])
                i += i
                tree.create_node(line[2], line[2], parent=line[0], data=colors[i])
            else:
                tree.create_node(line[2], line[2], parent=line[0], data=colors[i])
            i += i
        iterator += 1

    tree.show()
    print(tree.to_json(with_data=True))
    print(tree.get_node('2'))

    tre = graph(numbers_nodes)
    print(tre.getnodes())
    '''


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
