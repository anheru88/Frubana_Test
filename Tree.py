import numpy as np


class Tree:

    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes
        self.nodes = np.zeros((number_of_nodes, number_of_nodes))

    def add_color(self, node1, node2, color):
        self.nodes[node1, node2] = color

    def getnodes(self):
        return self.nodes

    def sum(self, node1):
        for x in range(self.number_of_nodes):
            self.distance(node1 - 1, x)

    def distance(self, node1, node2):
        values = []
        for x in range(self.number_of_nodes):


        print(node1, node2)