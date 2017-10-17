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
        parents = probability[0].replace('|', ',')
        parents = parents.replace('+', ' ')
        parents = parents.replace('-', ' ')
        parents = parents.strip(" ")
        parents = parents.split(", ")
        node_el = search_node(parents[0])
        count = 1
        while count < len(parents):
            if parents[count] not in node_el.parents:
                node_el.parents.append(parents[count])
            count += 1


def set_prob_tables():
    for probability in probabilities:
        key = probability[0].strip()
        search_index = probability[0].strip(" ").split("|")
        value = float(probability[1])
        node = search_node(search_index[0][1:])
        if node.name == search_index[0][1:]:
            node.prob_table.append((key, value))


def search_node(name)->Node:
    for node_el in bay_net.nodes:
        if node_el.name == name:
            return node_el


def parse_queries(queries_list):
    for query in queries_list:
        result = check_existing_probabilities(query)
        if result == -1:
            result = find_complement(query)
        if result == -1:
            print("Enumeraton not ready")
            # result = enumeration_algorithm(query)
        print(result)
    pass


def check_existing_probabilities(query):
    result = -1.0
    temp1 = query.replace('+', '')
    temp1 = temp1.replace('-', '')
    temp1 = temp1.split('|')
    node1 = search_node(temp1[0])
    count = 0
    while count < len(node1.prob_table):
        if query == node1.prob_table[count][0]:
            result = node1.prob_table[count][1]
        count += 1
    return result


def enumeration_algorithm(query):
    result = -1
    temp = query.split
    return result


def find_complement(query):
    result = -1.0
    temp1 = query.replace('+', '')
    temp1 = temp1.replace('-', '')
    temp1 = temp1.split('|')
    node1 = search_node(temp1[0])
    count = 0
    temptemp = list(query)
    if temptemp[0] == '-':
        temptemp[0] = '+'
    else:
        temptemp[0] = '-'
    temptemp = "".join(temptemp)
    while count < len(node1.prob_table):
        if temptemp == node1.prob_table[count][0]:
            result = 1 - node1.prob_table[count][1]
        count += 1
    return result


set_parents()
set_prob_tables()

parse_queries(queries)

# print(bay_net)
# parse_queries(queries)
# print(bay_net)
