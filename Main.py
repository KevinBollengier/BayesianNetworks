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

nodes = lines[0].strip().split(', ')
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
    temp_list = []
    for probability in probabilities:
        split = probability[0].split("|")
        node_nameslist = [x.strip("+").strip("-").strip(" ") for x in split]
        temp_list.append(node_nameslist)
    for prob_node in temp_list:
        if prob_node not in node_names_unique:
            node_names_unique.append(prob_node)
    # print(node_names_unique)
    for sublist in node_names_unique:
        if len(sublist) > 1:
            node_el = search_node(sublist[0])
            parent_index = 1
            while parent_index < len(sublist):
                node_el.parents.append(sublist[parent_index])
                parent_index += 1

    # first_sub = [x[0].strip() for x in list_return]
    # print(first_sub)
    # voor elk element in de lijst 'list_return' neem ik de eerste value van het element,
    #  en strip ik de whitespaces/newlines.
    # Resulaten in nieuwe lijst
    # print([node for node in bay_net.nodes if node.name in first_sub])
    # voor elk element in de lijst 'bay_net.nodes' kijk ik als de 'name' van het element in de lijst 'first_sub' zit.
    # Alle resultaten steek ik in een nieuwe lijst
    # = list comprehension


def set_prob_tables():
    for probability in probabilities:
        keys = probability[0].strip(" ").split("|")
        value = float(probability[1])
        node = search_node(keys[0][1:])
        if node.name == keys[0][1:]:
            node.prob_table.append((keys, value))
        #    count = 1
        #     while count < len(keys):
        #         if keys[0][:1] == '+':
        #             temp_key = '-' + keys[0][1:]
        #             temp_key.append(keys[count])
        #         else:
        #             temp_key = '+' + keys[0][1:]
        #             temp_key.append(keys[count])
        #         count += 1
        # node.prob_table.append((temp_key, 1-value))
    print(bay_net)

    # for sublist in node_names_unique:
    #     node_el = search_node(sublist[0])
    #     for probability in probabilities:
    #         trim = probability.strip(" ").strip("+").strip("-")
    #         print(trim)


def search_node(name)->Node:
    for node_el in bay_net.nodes:
        if node_el.name == name:
            return node_el


def enumeration(queries , probabilities):
    pass


def parse_queries():
    pass


set_parents()
set_prob_tables()
# print(bay_net)
