import fileinput
from BayesNetwork import *

lines = []
probabilities = []
node_names_unique = []
temp = []
queries = []
bay_net = BayesNetwork()

for line in fileinput.input():
    lines.append(line)

nodes = lines[0].strip().split(',')
amount_probabilities = int(lines[1].strip())

prob_index = 2
last_prob = prob_index + amount_probabilities

query_index = last_prob + 1

while lines[prob_index] != lines[last_prob]:
    temp.append(lines[prob_index].strip())
    prob_index += 1

for prob in temp:
    probabilities.append(prob.split("="))

while query_index < len(lines):
    queries.append(lines[query_index].strip())
    query_index += 1

for node in nodes:
    # make node with all the names in nodes list, but init with empty parents list, empty dict
    bay_node = Node(node, [], [])
    bay_net.add_node(bay_node)


def set_parents():
    for probability in probabilities:
        hey = probability[0].replace('|', ',')
        hey = hey.replace('+', ' ')
        hey = hey.replace('-', ' ')
        hey = hey.strip(" ")
        hey = hey.split(", ")
        node_el = search_node(hey[0])
        count = 1
        while count < len(hey):
            if hey[count] not in node_el.parents:
                node_el.parents.append(hey[count])
            count += 1


def set_prob_tables():
    for probability in probabilities:
        keys = probability[0].strip(" ").split("|")
        value = float(probability[1])
        node = search_node(keys[0][1:])
        if node.name == keys[0][1:]:
            node.prob_table.append((keys, value))


def search_node(name)->Node:
    for node_el in bay_net.nodes:
        if node_el.name == name:
            return node_el


def parse_queries(queries_list):
    for query in queries_list:
        check_existing_probabilities(query)
    pass


def check_existing_probabilities(query):
    print(query)
    pass


def enumeration_algorithm():
    pass


def find_complement():
    pass


set_parents()
set_prob_tables()
parse_queries(queries)
# print(bay_net)
