class BayesNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def __repr__(self):
        for node in self.nodes:
            print(str(node))


class Node:
    def __init__(self, name, parents, prob_table):
        self.name = name
        self.parents = parents
        self.prob_table = prob_table

    def __repr__(self):
        # return self.name, self.parents, self.prob_table
        return "<%s has as parents: %s and as probability table %s >" % (self.name, self.parents, self.prob_table)
