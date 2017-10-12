class BayesNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)


class Node:
    def __init__(self, name, parents, prob_table):
        self.name = name
        self.parents = parents
        self.prob_table = prob_table

