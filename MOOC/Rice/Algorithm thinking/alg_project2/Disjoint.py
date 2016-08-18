'''
About graph resilience
'''

import alg_module2_graphs 
from alg_application2_provided import *
from alg_upa_trial import *
import simpleplot
import codeskulptor
codeskulptor.set_timeout(180)

class Disjoint:
    '''
    Disjoint
    '''
    def __init__(self):
        '''
        __init__
        '''
        self._sets = []

    def create_set(self, repr0):
        '''
        createSet
        '''
        self._sets.append([repr0])

    def merge_sets(self, repr1, repr2):
        '''
        mergeSets
        '''
        set1 = self.find_set(repr1);
        set2 = self.find_set(repr2);
        if set1 != set2:
            set1.extend(set2);
            self._sets.remove(set2);

    def find_set(self, repr1):
        '''
        findSet
        '''
        for one_set in self._sets:
            if repr1 in one_set:
                return one_set


    def get_sets(self):
        '''
        getSets
        '''
        return self._sets;

def bfs_visited(ugraph, start_node):
    '''
    search a tree
    '''
    quene = [start_node]
    visited = set([start_node])
    while quene != []:
        live = quene.pop(0)
        for neighbor in ugraph[live]:
            if neighbor not in visited:
                visited.add(neighbor)
                quene.append(neighbor)
    return visited

def cc_visited(ugraph):
    '''
    search a undirected graph
    '''
    remain = set(ugraph.keys())
    connected_component = []
    while remain != set([]):
        current = bfs_visited(ugraph,remain.pop())
        connected_component.append(current)
        remain = remain.difference(current)
    return connected_component

def largest_cc_size(ugraph):
    '''
    find the largest connected component size
    '''
    #CC = cc_visited(ugraph)
    #largest = 0
    #for group in CC:
    #    if len(group) > max:
    #        largest = len(group)
    return max(map(len, cc_visited(ugraph)))

def compute_resilience(ugraph, attack_order):
    '''
    it's hard to say
    '''
    node_set = set(ugraph.keys())
    rest_node = node_set.difference(attack_order)
    disjoint = Disjoint()
    for node in rest_node:
        disjoint.create_set(node)
    for node1 in rest_node:
        for node2 in ugraph[node1]:
            if node2 in rest_node:
                disjoint.merge_sets(node1, node2)

    resilience = []
    resilience.append(max(map(len, disjoint.get_sets()) + [0]))

    for attacked_node in attack_order[::-1]:
        rest_node.add(attacked_node)
        disjoint.create_set(attacked_node)
        for node2 in ugraph[attacked_node]:
            if node2 in rest_node:
                disjoint.merge_sets(attacked_node, node2)
        resilience.append(max(map(len, disjoint.get_sets())))
    resilience.reverse()
    return resilience

def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes 
    returns a dictionary corresponding to a complete 
    directed graph with the specified number of nodes. 
    num_nodes is not positive returns a dictionary corresponding to the empty graph.
    '''
    complete_graph = {}
    if num_nodes > 0:
        for source in range(num_nodes):
            complete_graph[source] = set([])
            for dest in range(num_nodes):
                if dest != source:
                    complete_graph[source].add(dest)
    return complete_graph

def make_er_graph(num_nodes, prop):
    '''
    Takes the number of nodes num_nodes 
    returns a dictionary corresponding to a complete 
    undirected graph with the specified number of nodes. 
    num_nodes is not positive returns a dictionary corresponding to the empty graph.
    '''
    er_graph = {}
    if num_nodes > 0:
        for node1 in range(num_nodes):
            er_graph[node1] = set([])
            for node2 in range(node1):
                if random.random() < prop:
                    er_graph[node1].add(node2)
                    er_graph[node2].add(node1)
    return er_graph

def make_upa_graph(total, num_nodes):
    '''
    a complete graph on num_nodes nodes
    '''
    upa_graph = make_complete_graph(num_nodes)
    upa_trial = UPATrial(num_nodes)
    for new_node in range(num_nodes, total):
        new_node_neighbors = upa_trial.run_trial(num_nodes)
        upa_graph[new_node] = new_node_neighbors
        for neighbor in new_node_neighbors:
            upa_graph[neighbor].add(new_node)
    return upa_graph
        
def random_order(ugraph):
    attack_order = list(ugraph.keys())
    random.shuffle(attack_order)
    return attack_order
    
def random_attack(ugraph):
    attack_order = random_order(ugraph)
    return compute_resilience(ugraph, attack_order)

def random_attack_legend():
    """
    Plot three curves with legends
    """
    network_ugraph = load_graph(NETWORK_URL)
    num_network_nodes = len(network_ugraph)
    num_network_edges = sum(map(len, network_ugraph.values())) / 2
    max_network_edges = num_network_nodes * (num_network_nodes - 1) / 2
    prop = num_network_edges * 1.0 / max_network_edges

    er_graph = make_er_graph(num_network_nodes, prop)
    upa_graph = make_upa_graph(num_network_nodes, 2)

    yvals1 = random_attack(network_ugraph)
    yvals2 = random_attack(er_graph)
    yvals3 = random_attack(upa_graph)
    xvals = range(max(len(yvals1), len(yvals2), len(yvals3)))
    curve1 = [[xvals[idx], yvals1[idx]] for idx in range(len(yvals1))]
    curve2 = [[xvals[idx], yvals2[idx]] for idx in range(len(yvals2))]
    curve3 = [[xvals[idx], yvals3[idx]] for idx in range(len(yvals3))]
    
    simpleplot.plot_lines("Resilience of graphs under ramdom attack", 
                          800, 600, "the number of nodes removed",
                          "the size of the largest connect component",
                          [curve1, curve2, curve3], False, 
                          ["network_ugraph", 
                           "er_graph (p = " + str(prop) + ")",
                           "upa_graph (m = 2)"])
    
#random_attack_legend()

def fast_target_order(ugraph):
    new_graph = copy_graph(ugraph)
    num_nodes = len(new_graph)
    degree_sets = {}
    for degree in range(num_nodes):
        degree_sets[degree] = set()

    for node in new_graph.keys():
        degree_sets[len(new_graph.get(node, []))].add(node)
    answer_list = []
    for degree in range(num_nodes - 1, -1, -1):
        while degree_sets[degree] != set():
            top_node = degree_sets[degree].pop()
            neighbors = new_graph[top_node]
            for neighbor in neighbors:
                neighbor_degree = len(new_graph[neighbor])
                degree_sets[neighbor_degree].remove(neighbor)
                degree_sets[neighbor_degree - 1].add(neighbor)
            answer_list.append(top_node)
            new_graph.pop(top_node)
            for neighbor in neighbors:
                new_graph[neighbor].remove(top_node)
    return answer_list

def analyze_running_time():
    fast_target_order_list = []
    targeted_order_list = []
    xvals = []
    m = 5
    for n in range(10, 1000, 10):
        upa_graph = make_upa_graph(n, m)
        xvals.append(n)
        
        time1 = time.time()
        fast_target_order(upa_graph)
        time2 = time.time()
        fast_target_order_list.append(time2 - time1)
        
        time1 = time.time()
        targeted_order(upa_graph)
        time2 = time.time()
        targeted_order_list.append(time2 - time1)
    
    curve1 = [[xvals[idx], fast_target_order_list[idx]] for idx in range(len(xvals))]
    curve2 = [[xvals[idx], targeted_order_list[idx]] for idx in range(len(xvals))]
    simpleplot.plot_lines("CodeSkulptor running times ", 
                          800, 600, "the number of nodes",
                          "running time",
                          [curve1, curve2], False, 
                          ["fast_target_order", 
                           "targeted_order"])

def target_attack(ugraph):
    attack_order = fast_target_order(ugraph)
    return compute_resilience(ugraph, attack_order)

def target_attack_legend():
    """
    Plot three curves with legends
    """
    network_ugraph = load_graph(NETWORK_URL)
    num_network_nodes = len(network_ugraph)
    num_network_edges = sum(map(len, network_ugraph.values())) / 2
    max_network_edges = num_network_nodes * (num_network_nodes - 1) / 2
    prop = num_network_edges * 1.0 / max_network_edges

    er_graph = make_er_graph(num_network_nodes, prop)
    upa_graph = make_upa_graph(num_network_nodes, 2)

    yvals1 = target_attack(network_ugraph)
    yvals2 = target_attack(er_graph)
    yvals3 = target_attack(upa_graph)
    xvals = range(max(len(yvals1), len(yvals2), len(yvals3)))
    curve1 = [[xvals[idx], yvals1[idx]] for idx in range(len(yvals1))]
    curve2 = [[xvals[idx], yvals2[idx]] for idx in range(len(yvals2))]
    curve3 = [[xvals[idx], yvals3[idx]] for idx in range(len(yvals3))]
    
    simpleplot.plot_lines("Resilience of graphs under targeted attack", 
                          800, 600, "the number of nodes removed",
                          "the size of the largest connect component",
                          [curve1, curve2, curve3], False, 
                          ["network_ugraph", 
                           "er_graph (p = " + str(prop) + ")",
                           "upa_graph (m = 2)"])


#target_attack_legend()









'''
num_network_nodes = len(network_ugraph)
num_network_edges = sum(map(len, network_ugraph.values())) / 2
max_network_edges = num_network_nodes * (num_network_nodes - 1) / 2
prop = num_network_edges * 1.0 / max_network_edges

er_graph = make_er_graph(num_network_nodes, prop)
#num_er_graph_edges = sum(map(len, er_graph.values())) / 2

upa_graph = make_upa_graph(num_network_nodes, 2)
#num_upa_graph_edges = sum(map(len, upa_graph.values())) / 2

legend_trial(random_attack(network_ugraph),
            random_attack(er_graph),
            random_attack(upa_graph))
#print compute_resilience(ugraph, targeted_order(ugraph)[:10]) 
'''
