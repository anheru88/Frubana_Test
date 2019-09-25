__author__ = "Angel Jimenez Escobar"

import sys
import numpy as np

listN = []
MaxOperations = pow(10, 5)

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

    for line in f:
        if iterator == 0:
            try:
                val = int(line)
                if MaxOperations < val:
                    print("Excede la cantidad maxima de operaciones")
                    sys.exit(0)
            except ValueError:
                print("La primera linea debe ser un numero entero")
                sys.exit(0)
            iterator += 1
        else:
            for index in range(len(line)):
                number = ''.join([n for n in line if n.isdigit()])
                if index == 0:
                    if line[index] == "r":
                        remove(number)
                    else:
                        if line[index] == "a":
                            add(number)


def remove(number):
    """
        This method remove one integer for the list of numbers.
        First check if the number exist in the list, if doesn't exist return Wrong.
        If the number exist in the list, remove the number from the list, and check if the list if not empty
        When the list is not empty call median method.
    """
    if number in listN:
        listN.remove(number)

        if len(listN) > 0:
            median()
        else:
            print("Wrong")
    else:
        print("Wrong")


def add(number):
    """ This method is used to add number to the list"""
    listN.append(number)
    median()


def display_usage():
    """ this method only print one message"""
    print('Por favor pase como parametro el archivo a evaluar')


def format_number(number):
    """ Return the number formatted, if the number contain .0 return only the integer part """
    if number % 1 == 0:
        return int(number)
    else:
        return number


def median():
    """ this method return the median of the list values"""
    numberList = []
    for i in listN:
        numberList.append(int(i))

    print(format_number(np.median(numberList)))

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