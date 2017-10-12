class BayesNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def __repr__(self):
        return '\n'.join([str(n) for n in self.nodes])


class Node:
    def __init__(self, name, parents, prob_table):
        self.name = name
        self.parents = parents
        self.prob_table = prob_table

    def __repr__(self):
        return "<%s has as parents: %s and as probability table %s" % (self.name, self.parents, self.prob_table)
