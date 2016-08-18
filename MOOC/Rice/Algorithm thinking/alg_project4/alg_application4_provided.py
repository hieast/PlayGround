"""
Provide code and solution for Application 4
"""

DESKTOP = True

import math
import random
import urllib.request as urllib2

if DESKTOP:
    import matplotlib.pyplot as plt
    import alg_project4_solution as student
else:
    import simpleplot
    import user41_eaGlMfAW3s_22 as student
    

proxy_support = urllib2.ProxyHandler({"http":"http://127.0.0.1:8787"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"


###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline().decode()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.decode().split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict




def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq.decode()


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)
    
    # read in files as string
    words = word_file.read().decode()
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print ("Loaded a dictionary with", len(word_list), "words")
    return word_list

#seq_x = 'MQNSHSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEKQQMGADGMYDKLRMLNGQTGSWGTRPGWYPGTSVPGQPTQDGCQQQEGGGENTNSISSNGEDSDEAQMRLQLKRKLQRNRTSFTQEQIEALEKEFERTHYPDVFARERLAAKIDLPEARIQVWFSNRRAKWRREEKLRNQRRQASNTPSHIPISSSFSTSVYQPIPQPTTPVSSFTSGSMLGRTDTALTNTYSALPPMPSFTMANNLPMQPPVPSQTSSYSCMLPTSPSVNGRSYDTYTPPHMQTHMNSQPMGTSGTTSTGLISPGVSVPVQVPGSEPDMSQYWPRLQ'
#seq_y = 'MRNLPCLGTAGGSGLGGIAGKPSPTMEAVEASTASHPHSTSSYFATTYYHLTDDECHSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQSTGSGSSSTSAGNSISAKVSVSIGGNVSNVASGSRGTLSSSTDLMQTATPLNSSESGGASNSGEGSEQEAIYEKLRLLNTQHAAGPGPLEPARAAPLVGQSPNHLGTRSSHPQLVHGNHQALQQHQQQSWPPRHYSGSWYPTSLSEIPISSAPNIASVTAYASGPSLAHSLSPPNDIESLASIGHQRNCPVATEDIHLKKELDGHQSDETGSGEGENSNGGASNIGNTEDDQARLILKRKLQRNRTSFTNDQIDSLEKEFERTHYPDVFARERLAGKIGLPEARIQVWFSNRRAKWRREEKLRNQRRTPNSTGASATSSSTSATASLTDSPNSLSACSSLLSGSAGGPSVSTINGLSSPSTLSTNVNAPTLGAGIDSSESPTPIPHIRPSCTSDNDNGRQSEDCRRVCSPCPLGVGGHQNTHHIQSNGHAQGHALVPAISPRLNFNSGSFGAMYSNMHHTALSMSDSYGAVTPIPSFNHSAVGPLAPPSPIPQQGDLTPSSLYPCHMTLRPPPMAPAHHHIVPGDGGRPAGVGLGSGQSANLGASCSGSGYEVLSAYALPPPPMASSSAADSSFSAASSASANVTPHHTIAQESCPSPCSSASHFGVAHSSGFSSDPISPAVSSYAHMSYNYASSANTMTPSSASGTSAHVAPGKQQFFASCFYSPWV'
#scoring_matrix = {'A': {'A': 5, 'R': -5, 'N': -2, 'D': -2, 'C': -5, 'Q': -3, 'E': -1, 'G': -1, 'H': -5, 'I': -3, 'L': -5, 'K': -5, 'M': -4, 'F': -7, 'P': 0, 'S': 0, 'T': 0, 'W': -11, 'Y': -6, 'V': -1, 'B': -2, 'Z': -2, 'X': -2, '-': -5}, 'R': {'A': -5, 'R': 8, 'N': -4, 'D': -7, 'C': -6, 'Q': 0, 'E': -7, 'G': -7, 'H': 0, 'I': -4, 'L': -7, 'K': 1, 'M': -3, 'F': -8, 'P': -3, 'S': -2, 'T': -5, 'W': -1, 'Y': -8, 'V': -6, 'B': -5, 'Z': -2, 'X': -4, '-': -5}, 'N': {'A': -2, 'R': -4, 'N': 7, 'D': 2, 'C': -8, 'Q': -2, 'E': -1, 'G': -2, 'H': 1, 'I': -4, 'L': -6, 'K': 0, 'M': -6, 'F': -7, 'P': -4, 'S': 1, 'T': -1, 'W': -7, 'Y': -3, 'V': -6, 'B': 5, 'Z': -1, 'X': -2, '-': -5}, 'D': {'A': -2, 'R': -7, 'N': 2, 'D': 7, 'C': -11, 'Q': -1, 'E': 3, 'G': -2, 'H': -2, 'I': -6, 'L': -10, 'K': -3, 'M': -8, 'F': -12, 'P': -6, 'S': -2, 'T': -3, 'W': -12, 'Y': -9, 'V': -6, 'B': 6, 'Z': 2, 'X': -4, '-': -5}, 'C': {'A': -5, 'R': -6, 'N': -8, 'D': -11, 'C': 9, 'Q': -11, 'E': -11, 'G': -7, 'H': -6, 'I': -5, 'L': -12, 'K': -11, 'M': -11, 'F': -10, 'P': -6, 'S': -2, 'T': -6, 'W': -13, 'Y': -3, 'V': -5, 'B': -9, 'Z': -11, 'X': -7, '-': -5}, 'Q': {'A': -3, 'R': 0, 'N': -2, 'D': -1, 'C': -11, 'Q': 8, 'E': 2, 'G': -5, 'H': 2, 'I': -6, 'L': -4, 'K': -2, 'M': -3, 'F': -10, 'P': -2, 'S': -4, 'T': -4, 'W': -10, 'Y': -9, 'V': -5, 'B': -2, 'Z': 6, 'X': -3, '-': -5}, 'E': {'A': -1, 'R': -7, 'N': -1, 'D': 3, 'C': -11, 'Q': 2, 'E': 7, 'G': -3, 'H': -3, 'I': -4, 'L': -7, 'K': -3, 'M': -5, 'F': -11, 'P': -4, 'S': -3, 'T': -4, 'W': -13, 'Y': -7, 'V': -5, 'B': 2, 'Z': 6, 'X': -3, '-': -5}, 'G': {'A': -1, 'R': -7, 'N': -2, 'D': -2, 'C': -7, 'Q': -5, 'E': -3, 'G': 6, 'H': -7, 'I': -8, 'L': -9, 'K': -6, 'M': -7, 'F': -8, 'P': -4, 'S': -1, 'T': -4, 'W': -12, 'Y': -11, 'V': -4, 'B': -2, 'Z': -4, 'X': -4, '-': -5}, 'H': {'A': -5, 'R': 0, 'N': 1, 'D': -2, 'C': -6, 'Q': 2, 'E': -3, 'G': -7, 'H': 9, 'I': -7, 'L': -5, 'K': -4, 'M': -8, 'F': -5, 'P': -3, 'S': -4, 'T': -5, 'W': -6, 'Y': -2, 'V': -5, 'B': 0, 'Z': 0, 'X': -4, '-': -5}, 'I': {'A': -3, 'R': -4, 'N': -4, 'D': -6, 'C': -5, 'Q': -6, 'E': -4, 'G': -8, 'H': -7, 'I': 8, 'L': 0, 'K': -5, 'M': 0, 'F': -1, 'P': -7, 'S': -5, 'T': -1, 'W': -11, 'Y': -5, 'V': 3, 'B': -5, 'Z': -5, 'X': -3, '-': -5}, 'L': {'A': -5, 'R': -7, 'N': -6, 'D': -10, 'C': -12, 'Q': -4, 'E': -7, 'G': -9, 'H': -5, 'I': 0, 'L': 6, 'K': -6, 'M': 2, 'F': -1, 'P': -6, 'S': -7, 'T': -5, 'W': -5, 'Y': -5, 'V': -1, 'B': -7, 'Z': -5, 'X': -5, '-': -5}, 'K': {'A': -5, 'R': 1, 'N': 0, 'D': -3, 'C': -11, 'Q': -2, 'E': -3, 'G': -6, 'H': -4, 'I': -5, 'L': -6, 'K': 6, 'M': -1, 'F': -11, 'P': -5, 'S': -3, 'T': -2, 'W': -9, 'Y': -8, 'V': -7, 'B': -1, 'Z': -2, 'X': -4, '-': -5}, 'M': {'A': -4, 'R': -3, 'N': -6, 'D': -8, 'C': -11, 'Q': -3, 'E': -5, 'G': -7, 'H': -8, 'I': 0, 'L': 2, 'K': -1, 'M': 10, 'F': -3, 'P': -6, 'S': -4, 'T': -3, 'W': -10, 'Y': -8, 'V': 0, 'B': -7, 'Z': -4, 'X': -4, '-': -5}, 'F': {'A': -7, 'R': -8, 'N': -7, 'D': -12, 'C': -10, 'Q': -10, 'E': -11, 'G': -8, 'H': -5, 'I': -1, 'L': -1, 'K': -11, 'M': -3, 'F': 9, 'P': -8, 'S': -5, 'T': -7, 'W': -3, 'Y': 3, 'V': -6, 'B': -9, 'Z': -11, 'X': -6, '-': -5}, 'P': {'A': 0, 'R': -3, 'N': -4, 'D': -6, 'C': -6, 'Q': -2, 'E': -4, 'G': -4, 'H': -3, 'I': -7, 'L': -6, 'K': -5, 'M': -6, 'F': -8, 'P': 8, 'S': -1, 'T': -3, 'W': -11, 'Y': -11, 'V': -4, 'B': -5, 'Z': -3, 'X': -4, '-': -5}, 'S': {'A': 0, 'R': -2, 'N': 1, 'D': -2, 'C': -2, 'Q': -4, 'E': -3, 'G': -1, 'H': -4, 'I': -5, 'L': -7, 'K': -3, 'M': -4, 'F': -5, 'P': -1, 'S': 6, 'T': 1, 'W': -4, 'Y': -5, 'V': -4, 'B': -1, 'Z': -3, 'X': -2, '-': -5}, 'T': {'A': 0, 'R': -5, 'N': -1, 'D': -3, 'C': -6, 'Q': -4, 'E': -4, 'G': -4, 'H': -5, 'I': -1, 'L': -5, 'K': -2, 'M': -3, 'F': -7, 'P': -3, 'S': 1, 'T': 6, 'W': -10, 'Y': -5, 'V': -2, 'B': -2, 'Z': -4, 'X': -2, '-': -5}, 'W': {'A': -11, 'R': -1, 'N': -7, 'D': -12, 'C': -13, 'Q': -10, 'E': -13, 'G': -12, 'H': -6, 'I': -11, 'L': -5, 'K': -9, 'M': -10, 'F': -3, 'P': -11, 'S': -4, 'T': -10, 'W': 13, 'Y': -4, 'V': -12, 'B': -8, 'Z': -11, 'X': -9, '-': -5}, 'Y': {'A': -6, 'R': -8, 'N': -3, 'D': -9, 'C': -3, 'Q': -9, 'E': -7, 'G': -11, 'H': -2, 'I': -5, 'L': -5, 'K': -8, 'M': -8, 'F': 3, 'P': -11, 'S': -5, 'T': -5, 'W': -4, 'Y': 9, 'V': -6, 'B': -5, 'Z': -8, 'X': -6, '-': -5}, 'V': {'A': -1, 'R': -6, 'N': -6, 'D': -6, 'C': -5, 'Q': -5, 'E': -5, 'G': -4, 'H': -5, 'I': 3, 'L': -1, 'K': -7, 'M': 0, 'F': -6, 'P': -4, 'S': -4, 'T': -2, 'W': -12, 'Y': -6, 'V': 7, 'B': -6, 'Z': -5, 'X': -3, '-': -5}, 'B': {'A': -2, 'R': -5, 'N': 5, 'D': 6, 'C': -9, 'Q': -2, 'E': 2, 'G': -2, 'H': 0, 'I': -5, 'L': -7, 'K': -1, 'M': -7, 'F': -9, 'P': -5, 'S': -1, 'T': -2, 'W': -8, 'Y': -5, 'V': -6, 'B': 5, 'Z': 1, 'X': -3, '-': -5}, 'Z': {'A': -2, 'R': -2, 'N': -1, 'D': 2, 'C': -11, 'Q': 6, 'E': 6, 'G': -4, 'H': 0, 'I': -5, 'L': -5, 'K': -2, 'M': -4, 'F': -11, 'P': -3, 'S': -3, 'T': -4, 'W': -11, 'Y': -8, 'V': -5, 'B': 1, 'Z': 6, 'X': -3, '-': -5}, 'X': {'A': -2, 'R': -4, 'N': -2, 'D': -4, 'C': -7, 'Q': -3, 'E': -3, 'G': -4, 'H': -4, 'I': -3, 'L': -5, 'K': -4, 'M': -4, 'F': -6, 'P': -4, 'S': -2, 'T': -2, 'W': -9, 'Y': -6, 'V': -3, 'B': -3, 'Z': -3, 'X': -4, '-': -5}, '-': {'A': -5, 'R': -5, 'N': -5, 'D': -5, 'C': -5, 'Q': -5, 'E': -5, 'G': -5, 'H': -5, 'I': -5, 'L': -5, 'K': -5, 'M': -5, 'F': -5, 'P': -5, 'S': -5, 'T': -5, 'W': -5, 'Y': -5, 'V': -5, 'B': -5, 'Z': -5, 'X': -5, '-': -100}}

def run_q1():
    seq_x = read_protein(HUMAN_EYELESS_URL)
    seq_y = read_protein(FRUITFLY_EYELESS_URL)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    alignment_matrix = student.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, False)
    return student.compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    
#print(run_q1())

def run_q2(origin_seq_x):
    seq_x = origin_seq_x.replace('-', '')
    seq_y = 'GHGGVNQLGGVFVNGRPLPDVVRQRIVELAHQGVRPCDISRQLRVSHGCVSKILGRYYETGSIKPGVIGGSKPKVATPKVVEKIAEYKRQNPTMFAWEIRDRLLAERVCDNDTVPSVSSINRIIR'
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    alignment_matrix = student.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, True)
    score, aglin_x, aglin_y = student.compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    assert len(aglin_x) == len(aglin_y)
    length = len(aglin_y)
    match = 0
    print (len(seq_x), len(seq_y), len(aglin_x) , len(aglin_y))
    for idx in range(length):
        if aglin_x[idx] == aglin_y[idx]:
            match += 1
    return match * 1.0 / length
    
#print (run_q2('HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ'))
#print (run_q2('HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ'))

def run_q3():
    def poisson(k):
        return lamb ** k / denominator / math.factorial(k)
    lamb = 133.0 /23
    denominator = math.e ** lamb
    res = [poisson(k+1) for k in range(133)]
    print (sum(res[:40]))
    print (res)
def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    scoring_distribution = {}
    rand_y = list(seq_y[:])
    for trial in range(num_trials):
        random.shuffle(rand_y)
        alignment_matrix = student.compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        score = student.compute_local_alignment(seq_x, rand_y, scoring_matrix, alignment_matrix)[0]
        if score in scoring_distribution:
            scoring_distribution[score] += 1
        else:
            scoring_distribution[score] = 1
    return scoring_distribution
def run_q3():
    seq_x = read_protein(HUMAN_EYELESS_URL)
    seq_y = read_protein(FRUITFLY_EYELESS_URL)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    print (generate_null_distribution(seq_x, seq_y, scoring_matrix, 1000))
    
#run_q3()

dic_q4 = {64: 12, 65: 12, 66: 9, 67: 8, 68: 1, 69: 5, 70: 4, 71: 2, 74: 3, 76: 1, 78: 2, 80: 3, 81: 1, 83: 1, 92: 1, 38: 1, 39: 1, 40: 7, 41: 11, 42: 18, 43: 27, 44: 36, 45: 52, 46: 50, 47: 53, 48: 91, 49: 71, 50: 55, 51: 68, 52: 56, 53: 49, 54: 51, 55: 52, 56: 39, 57: 38, 58: 19, 59: 25, 60: 17, 61: 14, 62: 17, 63: 17}

def normalize(dic):
    denominator = sum(dic.values())
    for key in dic:
        dic[key] /= denominator
    print ('has been normalized!!')

def barplot(dic):
    N = len(dic)
    plt.xlabel('Scores')
    plt.ylabel('probability')
    plt.title('random y-sequence score distribution')
    plt.bar(dic.keys(), dic.values())
    plt.show()
#barplot(dic_q4)

def getz(s):
    n = sum(dic_q4.values())
    mean = sum((i*j for (i, j) in dic_q4.items()))/ n
    std = math.sqrt(sum(( math.pow(i - mean, 2) * j) for (i, j) in dic_q4.items()) / n)
    return (s - mean)/std

#print (getz(875))

def check_spelling(checked_word, dist, word_list):
    scoring_matrix = student.build_scoring_matrix(set('abcdefghijklmnopqrstuvwxyz'), 2, 1, 0)
    def score(x, y):
        alignment_matrix = student.compute_alignment_matrix(x, y, scoring_matrix, True)
        return student.compute_global_alignment(x, y, scoring_matrix, alignment_matrix)[0]
    return list(word for word in word_list if len(checked_word) + len(word) - score(checked_word, word) == dist)
        
word_list = read_words(WORD_LIST_URL)
print (check_spelling("humble", 1, word_list))
print (check_spelling("firefly", 2, word_list))
