"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import random
import alg_cluster
import time
import codeskulptor
codeskulptor.set_timeout(200)
import simpleplot




######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    number = len(cluster_list)
    assert number >= 2
    ansewer = (float("inf"), -1, -1)
    for idx1 in range(number):
        for idx2 in range(idx1 + 1, number):
            ansewer = min(ansewer, pair_distance(cluster_list, idx1, idx2))
    return ansewer

def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    idx_list = filter(lambda idx: abs(cluster_list[idx].horiz_center() - horiz_center) < half_width, 
                      range(len(cluster_list)))
    idx_list.sort(key = lambda idx: cluster_list[idx].vert_center())
    number = len(idx_list)
    ansewer = (float("inf"), -1, -1)
    for idxidx1 in range(number):
        for idxidx2 in range(idxidx1 + 1, 
                             min(idxidx1 + 4, number)):
            ansewer = min(ansewer, 
                          pair_distance(cluster_list, idx_list[idxidx1], idx_list[idxidx2]))
    return ansewer

#print closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)], 1.5, 1.0) 
#print closest_pair_strip([alg_cluster.Cluster(set([]), -4.0, 0.0, 1, 0), alg_cluster.Cluster(set([]), 0.0, -1.0, 1, 0), alg_cluster.Cluster(set([]), 0.0, 1.0, 1, 0), alg_cluster.Cluster(set([]), 4.0, 0.0, 1, 0)], 0.0, 4.1231059999999999) 


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    number = len(cluster_list)
    assert number >= 2
    if number <= 3:
        return slow_closest_pair(cluster_list)
    mid = number / 2
    answer_left = fast_closest_pair(cluster_list[:mid])
    answer_right = fast_closest_pair(cluster_list[mid:])
    answer = min(answer_left, 
                 (answer_right[0], 
                  answer_right[1] + mid,
                  answer_right[2] + mid))
    horiz_center = (cluster_list[mid - 1].horiz_center() + 
                    cluster_list[mid].horiz_center()) / 2.0
    answer = min(answer, 
                 closest_pair_strip(cluster_list, horiz_center, answer[0]))
    return answer

#print fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0)])


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    clusters = list(cluster_list)
    number = len(clusters)
    
    while number > num_clusters:
        clusters.sort(key = lambda cluster: cluster.horiz_center())
        idx1, idx2 = fast_closest_pair(clusters)[1:]
        clusters.append(clusters[idx1].merge_clusters(clusters[idx2]))
        clusters.remove(clusters[idx2])
        clusters.remove(clusters[idx1])
        number -= 1
    return clusters

######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
    point_list = [(cluster.total_population(), cluster.horiz_center(), cluster.vert_center()) for cluster in cluster_list]
    centers = []
    for dummy_i in range(num_clusters):
        temp_point = max(point_list)
        centers.append((temp_point[1], temp_point[2]))
        point_list.remove(temp_point)
    answer = []
    for dummy_i in range(num_iterations):
        answer = []
        for center in centers:
            answer.append(alg_cluster.Cluster(set([]), center[0], center[1], 0, 0))
        for cluster in cluster_list:
            temp_dist = (float("inf"), -1)
            for idx in range(num_clusters):
                temp_dist = min(temp_dist, (cluster.distance(alg_cluster.Cluster(set([]), centers[idx][0], centers[idx][1], 0, 0)), idx))
            answer[temp_dist[1]].merge_clusters(cluster)
        centers = [(mean.horiz_center(), mean.vert_center()) for mean in answer]
    return answer
                   
                   
#print kmeans_clustering([alg_cluster.Cluster(set([1]), 10, 10, 1, 0), alg_cluster.Cluster(set([2]), 20, 20, 1, 0)], 1, 5)
    
def gen_random_clusters(num_clusters):
    cluster_list = []
    for dummy_idx in range(num_clusters):
        cluster_list.append(alg_cluster.Cluster(set([]), random.random(), random.random(), 0, 0))
    return cluster_list

def q1_legend(low, high):
    xvals = []
    slow = []
    fast = []
    for num_clusters in range(low, high, 100):
        xvals.append(num_clusters)
        cluster_list = gen_random_clusters(num_clusters)
        
        time1 = time.time()
        slow_closest_pair(cluster_list)
        time2 = time.time()
        slow.append(time2 - time1)
        
        time1 = time.time()
        fast_closest_pair(cluster_list)
        time2 = time.time()
        fast.append(time2 - time1)
        
    yvals1 = slow
    yvals2 = fast
    curve1 = [[xvals[idx], yvals1[idx]] for idx in range(len(xvals))]
    curve2 = [[xvals[idx], yvals2[idx]] for idx in range(len(xvals))]
    print curve1
    print curve2
    simpleplot.plot_lines("The running times of closest-pair-find functions", 
                          800, 600, "the number of initial clusters",
                          "the running time of the function in seconds",
                          [curve1, curve2], True, 
                          ["slow_closest_pair", 
                           "fast_closest_pair"])
    
