"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import pylab

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    print "Loaded graph with", len(graph_lines), "nodes"
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))
    return answer_graph

"""
#1 Description
"""
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 
             1: set([2, 6]), 
             2: set([3]), 
             3: set([0]), 
             4: set([1]), 
             5: set([2]), 
             6: set([])} 
EX_GRAPH2 = {0: set([1, 4, 5]), 
             1: set([2, 6]), 
             2: set([3, 7]), 
             3: set([7]), 
             4: set([1]), 
             5: set([2]), 
             6: set([]), 
             7: set([3]), 
             8: set([1, 2]), 
             9: set([0, 3, 4, 5, 6, 7])}

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
    
#print make_complete_graph(-1)
#print make_complete_graph(4)

def compute_in_degrees(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) 
    and computes the in-degrees for the nodes in the graph. 
    return a dictionary with the same set of keys (nodes) as 
    digraph whose corresponding values are the number of edges 
    whose head matches a particular node.
    '''
    in_degrees = {}
    for source in digraph:
        for dest in digraph[source]:
            if source not in in_degrees:
                in_degrees[source] = 0
            if dest in in_degrees:
                in_degrees[dest] += 1
            else:
                in_degrees[dest] = 1
    return in_degrees

#print compute_in_degrees(EX_GRAPH0)
#print compute_in_degrees(EX_GRAPH1)
#print compute_in_degrees(EX_GRAPH2)

def in_degree_distribution(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) 
    and computes the unnormalized distribution of the in-degrees of 
    the graph. 
    The function should return a dictionary whose keys correspond 
    to in-degrees of nodes in the graph. 
    '''
    in_degrees = compute_in_degrees(digraph)
    distribution = {}
    for node in in_degrees:
        if in_degrees[node] not in distribution:
            distribution[in_degrees[node]] = 1
        else:
            distribution[in_degrees[node]] += 1
    return distribution

#print in_degree_distribution(EX_GRAPH0)
#print in_degree_distribution(EX_GRAPH1)
#print in_degree_distribution(EX_GRAPH2)


citation_graph = load_graph(CITATION_URL)
citation_out_degree_distribution = {}
sum = 0.0
for key in citation_graph:
    citation_out_degree_distribution[key] = len(citation_graph[key])
for i in citation_out_degree_distribution:
    sum += citation_out_degree_distribution[i]
average_citation_out_degree = sum / len(citation_graph)
print average_citation_out_degree 


citation_in_degree_distribution = in_degree_distribution(citation_graph )

# normalize citation_in_degree_distribution 
sum = 0.0
for i in citation_in_degree_distribution:
    sum += citation_in_degree_distribution[i]
for i in citation_in_degree_distribution:
    citation_in_degree_distribution[i] /= sum

# cal x/y
temp = list(citation_in_degree_distribution.items())
temp = sorted(temp, key = lambda x: x[0])
x = []
y = []
for pair in temp:
    x.append(pair[0])
    y.append(pair[1])

# draw plot
pylab.figure('High energy physics theory papers cited log/log plot ')
pylab.plot(x, y, 'ro')
pylab.title('High energy physics theory papers cited log/log plot ')
#pylab.xscale('log')
#pylab.yscale('log')
pylab.xlabel('Cited Times')
pylab.ylabel('Frequency ')
pylab.show()

def plot(title):
    pylab.figure(title, x, y, xlabel, ylabel)
    pylab.plot(x, y, 'ro')
    pylab.title(title)
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.show()






