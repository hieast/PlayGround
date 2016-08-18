"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random
import pylab

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    

DPA = DPATrial(13)
for i in range(13,27770):
    DPA.run_trial(13)
    
print DPA._num_nodes
DPA_graph = {}

for node in DPA._node_numbers:
    if node in DPA_graph:
        DPA_graph[node] += 1
    else:
        DPA_graph[node] = 0

citation_in_degree_distribution = {}
for node in DPA_graph:
    if DPA_graph[node] in citation_in_degree_distribution:
        citation_in_degree_distribution[DPA_graph[node]] += 1
    else:
        citation_in_degree_distribution[DPA_graph[node]] = 1

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
pylab.figure('DPA Graph with n = 27770/ m = 13 log/log plot ')
pylab.plot(x, y, 'ro')
pylab.title('DPA Graph with n = 27770/ m = 13 log/log plot ')
pylab.xscale('log')
pylab.yscale('log')
pylab.xlabel('In-degree')
pylab.ylabel('Frequency ')
pylab.show()


