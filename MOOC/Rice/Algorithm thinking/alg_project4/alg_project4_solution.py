"""
In Project 4, we will implement four functions. 
The first pair of functions will return matrices 
that we will use in computing the alignment of two 
sequences. The second pair of functions will return 
global and local alignments of two input sequences 
based on a provided alignment matrix. You will then 
use these functions in Application 4 to analyze two 
problems involving comparison of similar sequences.
"""
def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score): 
    """
    Takes as input a set of characters alphabet and three 
    scores diag_score, off_diag_score, and dash_score. 
    The function returns a dictionary of dictionaries 
    whose entries are indexed by pairs of characters in 
    alphabet plus '-'.
    """
    res = {}
    for chra1 in alphabet:
        res[chra1] = {}
        for chra2 in alphabet:
                res[chra1][chra2] = off_diag_score
    for key in res:
        res[key][key] = diag_score
    res['-'] = {}
    for key in res:
        res[key]['-'] = dash_score
        res['-'][key] = dash_score
    return res
    
#scoring_matrix = (build_scoring_matrix(set(['A', 'C', 'G', 'T']), 10, 4, -6))


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag): 
    """
    Takes as input two sequences seq_x and seq_y 
    whose elements share a common alphabet with the 
    scoring matrix scoring_matrix. The function computes 
    and returns the alignment matrix for seq_x and seq_y 
    as described in the Homework.
    """
    m_len = len(seq_x)
    n_len = len(seq_y)
    alignment_matrix = list([None for dummy_col in range(n_len + 1)] for dummy_row in range(m_len + 1))
    alignment_matrix[0][0] = 0
    for dummy_i in range(1,m_len + 1):
        alignment_matrix[dummy_i][0] = (alignment_matrix[dummy_i-1][0] + scoring_matrix[seq_x[dummy_i-1]]['-']) if global_flag else 0
    for dummy_j in range(1,n_len + 1):
        alignment_matrix[0][dummy_j] = (alignment_matrix[0][dummy_j-1] + scoring_matrix['-'][seq_y[dummy_j-1]]) if global_flag else 0
    for dummy_i in range(1,m_len + 1):
        for dummy_j in range(1,n_len + 1):
            #a = alignment_matrix[dummy_i - 1][dummy_j - 1] + scoring_matrix[seq_x[dummy_i-1]][seq_y[dummy_j-1]]
            #b = alignment_matrix[dummy_i - 1][dummy_j] + scoring_matrix[seq_x[dummy_i-1]]['-']
            #c = alignment_matrix[dummy_i][dummy_j - 1] + scoring_matrix['-'][seq_y[dummy_j-1]]
            #print(dummy_i, dummy_j, a, b, c)
            #I don't know where goes wrong, but it works well
            temp = max(
                alignment_matrix[dummy_i - 1][dummy_j - 1] + scoring_matrix[seq_x[dummy_i-1]][seq_y[dummy_j-1]],
                alignment_matrix[dummy_i - 1][dummy_j] + scoring_matrix[seq_x[dummy_i-1]]['-'],
                alignment_matrix[dummy_i][dummy_j - 1] + scoring_matrix['-'][seq_y[dummy_j-1]])
            if (not global_flag) and temp < 0:
                temp = 0
            alignment_matrix[dummy_i][dummy_j] = temp
    return alignment_matrix

#global_flag = False
#print (compute_alignment_matrix(['A','A','A','A'], ['A','A','A'], scoring_matrix, global_flag))
#print (compute_alignment_matrix('A', 'A', {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}, True))

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix): 
    """
    Takes as input two sequences seq_x and seq_y whose elements 
    share a common alphabet with the scoring matrix scoring_matrix.
    This function computes a global alignment of seq_x and seq_y 
    using the global alignment matrix alignment_matrix.The 
    function returns a tuple of the form (score, align_x, align_y)
    where score is the score of the global alignment align_x 
    and align_y. Note that align_x and align_y should have the 
    same length and may include the padding character '-'.
    """
    idx_x = len(seq_x)
    idx_y = len(seq_y)
    align_x = ''
    align_y = ''
    while idx_x and idx_y:
        if alignment_matrix[idx_x][idx_y] == (
            alignment_matrix[idx_x-1][idx_y-1] + scoring_matrix[seq_x[idx_x-1]][seq_y[idx_y-1]]):
            align_x = seq_x[idx_x-1] + align_x
            align_y = seq_y[idx_y-1] + align_y
            idx_x -= 1
            idx_y -= 1
        elif alignment_matrix[idx_x][idx_y] == (
            alignment_matrix[idx_x-1][idx_y] + scoring_matrix[seq_x[idx_x-1]]['-']):
            align_x = seq_x[idx_x-1] + align_x
            align_y = '-' + align_y
            idx_x -= 1
        else:
            align_x = '-' + align_x 
            align_y = seq_y[idx_y-1] + align_y
            idx_y -= 1
    while idx_x:
        align_x = seq_x[idx_x-1] + align_x
        align_y = '-' + align_y
        idx_x -= 1
    while idx_y:
        align_x = '-' + align_x 
        align_y = seq_y[idx_y-1] + align_y
        idx_y -= 1
    return (alignment_matrix[-1][-1], align_x, align_y)
            
#print compute_global_alignment('ACTACT', 'GGACTGCTTCTGG', {'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1}, 'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1}, '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0}, 'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1}, 'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}}, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [0, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [0, 1, 2, 3, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6], [0, 1, 2, 4, 4, 6, 7, 7, 7, 7, 7, 7, 7, 7], [0, 1, 2, 4, 6, 6, 7, 9, 9, 9, 9, 9, 9, 9], [0, 1, 2, 4, 6, 8, 8, 9, 11, 11, 11, 11, 11, 11]]) 

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a 
    common alphabet with the scoring matrix scoring_matrix. This function 
    computes a local alignment of seq_x and seq_y using the local alignment 
    matrix alignment_matrix.The function returns a tuple of the form 
    (score, align_x, align_y) where score is the score of the optimal 
    local alignment align_x and align_y. Note that align_x and align_y 
    should have the same length and may include the padding character '-'.
    """
    start = [0,0]
    best = 0
    for row in range(len(alignment_matrix)):
        temp = max(alignment_matrix[row])
        if temp > best:
            start[0] = row
            start[1] = alignment_matrix[row].index(temp)
            best = temp
    idx_x = start[0]
    idx_y = start[1]
    align_x = ''
    align_y = ''
    while alignment_matrix[idx_x][idx_y]:
        if alignment_matrix[idx_x][idx_y] == (
            alignment_matrix[idx_x-1][idx_y-1] + scoring_matrix[seq_x[idx_x-1]][seq_y[idx_y-1]]):
            align_x = seq_x[idx_x-1] + align_x
            align_y = seq_y[idx_y-1] + align_y
            idx_x -= 1
            idx_y -= 1
        elif alignment_matrix[idx_x][idx_y] == (
            alignment_matrix[idx_x-1][idx_y] + scoring_matrix[seq_x[idx_x-1]]['-']):
            align_x = seq_x[idx_x-1] + align_x
            align_y = '-' + align_y
            idx_x -= 1
        else:
            align_x = '-' + align_x 
            align_y = seq_y[idx_y-1] + align_y
            idx_y -= 1
    return (alignment_matrix[start[0]][start[1]], align_x, align_y)

#print compute_local_alignment('XYZ', 'EYX', {'-': {'-': -100, 'A': -5, 'C': -5, 'B': -5, 'E': -5, 'D': -5, 'G': -5, 'F': -5, 'I': -5, 'H': -5, 'K': -5, 'M': -5, 'L': -5, 'N': -5, 'Q': -5, 'P': -5, 'S': -5, 'R': -5, 'T': -5, 'W': -5, 'V': -5, 'Y': -5, 'X': -5, 'Z': -5}, 'A': {'-': -5, 'A': 5, 'C': -5, 'B': -2, 'E': -1, 'D': -2, 'G': -1, 'F': -7, 'I': -3, 'H': -5, 'K': -5, 'M': -4, 'L': -5, 'N': -2, 'Q': -3, 'P': 0, 'S': 0, 'R': -5, 'T': 0, 'W': -11, 'V': -1, 'Y': -6, 'X': -2, 'Z': -2}, 'C': {'-': -5, 'A': -5, 'C': 9, 'B': -9, 'E': -11, 'D': -11, 'G': -7, 'F': -10, 'I': -5, 'H': -6, 'K': -11, 'M': -11, 'L': -12, 'N': -8, 'Q': -11, 'P': -6, 'S': -2, 'R': -6, 'T': -6, 'W': -13, 'V': -5, 'Y': -3, 'X': -7, 'Z': -11}, 'B': {'-': -5, 'A': -2, 'C': -9, 'B': 5, 'E': 2, 'D': 6, 'G': -2, 'F': -9, 'I': -5, 'H': 0, 'K': -1, 'M': -7, 'L': -7, 'N': 5, 'Q': -2, 'P': -5, 'S': -1, 'R': -5, 'T': -2, 'W': -8, 'V': -6, 'Y': -5, 'X': -3, 'Z': 1}, 'E': {'-': -5, 'A': -1, 'C': -11, 'B': 2, 'E': 7, 'D': 3, 'G': -3, 'F': -11, 'I': -4, 'H': -3, 'K': -3, 'M': -5, 'L': -7, 'N': -1, 'Q': 2, 'P': -4, 'S': -3, 'R': -7, 'T': -4, 'W': -13, 'V': -5, 'Y': -7, 'X': -3, 'Z': 6}, 'D': {'-': -5, 'A': -2, 'C': -11, 'B': 6, 'E': 3, 'D': 7, 'G': -2, 'F': -12, 'I': -6, 'H': -2, 'K': -3, 'M': -8, 'L': -10, 'N': 2, 'Q': -1, 'P': -6, 'S': -2, 'R': -7, 'T': -3, 'W': -12, 'V': -6, 'Y': -9, 'X': -4, 'Z': 2}, 'G': {'-': -5, 'A': -1, 'C': -7, 'B': -2, 'E': -3, 'D': -2, 'G': 6, 'F': -8, 'I': -8, 'H': -7, 'K': -6, 'M': -7, 'L': -9, 'N': -2, 'Q': -5, 'P': -4, 'S': -1, 'R': -7, 'T': -4, 'W': -12, 'V': -4, 'Y': -11, 'X': -4, 'Z': -4}, 'F': {'-': -5, 'A': -7, 'C': -10, 'B': -9, 'E': -11, 'D': -12, 'G': -8, 'F': 9, 'I': -1, 'H': -5, 'K': -11, 'M': -3, 'L': -1, 'N': -7, 'Q': -10, 'P': -8, 'S': -5, 'R': -8, 'T': -7, 'W': -3, 'V': -6, 'Y': 3, 'X': -6, 'Z': -11}, 'I': {'-': -5, 'A': -3, 'C': -5, 'B': -5, 'E': -4, 'D': -6, 'G': -8, 'F': -1, 'I': 8, 'H': -7, 'K': -5, 'M': 0, 'L': 0, 'N': -4, 'Q': -6, 'P': -7, 'S': -5, 'R': -4, 'T': -1, 'W': -11, 'V': 3, 'Y': -5, 'X': -3, 'Z': -5}, 'H': {'-': -5, 'A': -5, 'C': -6, 'B': 0, 'E': -3, 'D': -2, 'G': -7, 'F': -5, 'I': -7, 'H': 9, 'K': -4, 'M': -8, 'L': -5, 'N': 1, 'Q': 2, 'P': -3, 'S': -4, 'R': 0, 'T': -5, 'W': -6, 'V': -5, 'Y': -2, 'X': -4, 'Z': 0}, 'K': {'-': -5, 'A': -5, 'C': -11, 'B': -1, 'E': -3, 'D': -3, 'G': -6, 'F': -11, 'I': -5, 'H': -4, 'K': 6, 'M': -1, 'L': -6, 'N': 0, 'Q': -2, 'P': -5, 'S': -3, 'R': 1, 'T': -2, 'W': -9, 'V': -7, 'Y': -8, 'X': -4, 'Z': -2}, 'M': {'-': -5, 'A': -4, 'C': -11, 'B': -7, 'E': -5, 'D': -8, 'G': -7, 'F': -3, 'I': 0, 'H': -8, 'K': -1, 'M': 10, 'L': 2, 'N': -6, 'Q': -3, 'P': -6, 'S': -4, 'R': -3, 'T': -3, 'W': -10, 'V': 0, 'Y': -8, 'X': -4, 'Z': -4}, 'L': {'-': -5, 'A': -5, 'C': -12, 'B': -7, 'E': -7, 'D': -10, 'G': -9, 'F': -1, 'I': 0, 'H': -5, 'K': -6, 'M': 2, 'L': 6, 'N': -6, 'Q': -4, 'P': -6, 'S': -7, 'R': -7, 'T': -5, 'W': -5, 'V': -1, 'Y': -5, 'X': -5, 'Z': -5}, 'N': {'-': -5, 'A': -2, 'C': -8, 'B': 5, 'E': -1, 'D': 2, 'G': -2, 'F': -7, 'I': -4, 'H': 1, 'K': 0, 'M': -6, 'L': -6, 'N': 7, 'Q': -2, 'P': -4, 'S': 1, 'R': -4, 'T': -1, 'W': -7, 'V': -6, 'Y': -3, 'X': -2, 'Z': -1}, 'Q': {'-': -5, 'A': -3, 'C': -11, 'B': -2, 'E': 2, 'D': -1, 'G': -5, 'F': -10, 'I': -6, 'H': 2, 'K': -2, 'M': -3, 'L': -4, 'N': -2, 'Q': 8, 'P': -2, 'S': -4, 'R': 0, 'T': -4, 'W': -10, 'V': -5, 'Y': -9, 'X': -3, 'Z': 6}, 'P': {'-': -5, 'A': 0, 'C': -6, 'B': -5, 'E': -4, 'D': -6, 'G': -4, 'F': -8, 'I': -7, 'H': -3, 'K': -5, 'M': -6, 'L': -6, 'N': -4, 'Q': -2, 'P': 8, 'S': -1, 'R': -3, 'T': -3, 'W': -11, 'V': -4, 'Y': -11, 'X': -4, 'Z': -3}, 'S': {'-': -5, 'A': 0, 'C': -2, 'B': -1, 'E': -3, 'D': -2, 'G': -1, 'F': -5, 'I': -5, 'H': -4, 'K': -3, 'M': -4, 'L': -7, 'N': 1, 'Q': -4, 'P': -1, 'S': 6, 'R': -2, 'T': 1, 'W': -4, 'V': -4, 'Y': -5, 'X': -2, 'Z': -3}, 'R': {'-': -5, 'A': -5, 'C': -6, 'B': -5, 'E': -7, 'D': -7, 'G': -7, 'F': -8, 'I': -4, 'H': 0, 'K': 1, 'M': -3, 'L': -7, 'N': -4, 'Q': 0, 'P': -3, 'S': -2, 'R': 8, 'T': -5, 'W': -1, 'V': -6, 'Y': -8, 'X': -4, 'Z': -2}, 'T': {'-': -5, 'A': 0, 'C': -6, 'B': -2, 'E': -4, 'D': -3, 'G': -4, 'F': -7, 'I': -1, 'H': -5, 'K': -2, 'M': -3, 'L': -5, 'N': -1, 'Q': -4, 'P': -3, 'S': 1, 'R': -5, 'T': 6, 'W': -10, 'V': -2, 'Y': -5, 'X': -2, 'Z': -4}, 'W': {'-': -5, 'A': -11, 'C': -13, 'B': -8, 'E': -13, 'D': -12, 'G': -12, 'F': -3, 'I': -11, 'H': -6, 'K': -9, 'M': -10, 'L': -5, 'N': -7, 'Q': -10, 'P': -11, 'S': -4, 'R': -1, 'T': -10, 'W': 13, 'V': -12, 'Y': -4, 'X': -9, 'Z': -11}, 'V': {'-': -5, 'A': -1, 'C': -5, 'B': -6, 'E': -5, 'D': -6, 'G': -4, 'F': -6, 'I': 3, 'H': -5, 'K': -7, 'M': 0, 'L': -1, 'N': -6, 'Q': -5, 'P': -4, 'S': -4, 'R': -6, 'T': -2, 'W': -12, 'V': 7, 'Y': -6, 'X': -3, 'Z': -5}, 'Y': {'-': -5, 'A': -6, 'C': -3, 'B': -5, 'E': -7, 'D': -9, 'G': -11, 'F': 3, 'I': -5, 'H': -2, 'K': -8, 'M': -8, 'L': -5, 'N': -3, 'Q': -9, 'P': -11, 'S': -5, 'R': -8, 'T': -5, 'W': -4, 'V': -6, 'Y': 9, 'X': -6, 'Z': -8}, 'X': {'-': -5, 'A': -2, 'C': -7, 'B': -3, 'E': -3, 'D': -4, 'G': -4, 'F': -6, 'I': -3, 'H': -4, 'K': -4, 'M': -4, 'L': -5, 'N': -2, 'Q': -3, 'P': -4, 'S': -2, 'R': -4, 'T': -2, 'W': -9, 'V': -3, 'Y': -6, 'X': -4, 'Z': -3}, 'Z': {'-': -5, 'A': -2, 'C': -11, 'B': 1, 'E': 6, 'D': 2, 'G': -4, 'F': -11, 'I': -5, 'H': 0, 'K': -2, 'M': -4, 'L': -5, 'N': -1, 'Q': 6, 'P': -3, 'S': -3, 'R': -2, 'T': -4, 'W': -11, 'V': -5, 'Y': -8, 'X': -3, 'Z': 6}}, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 9, 4], [0, 6, 4, 6]]) 
