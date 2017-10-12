import fileinput
from BayesNetwork import *

lines = []
probabilities = []
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
    bay_node = Node(node, [], {})
    bay_net.add_node(bay_node)

