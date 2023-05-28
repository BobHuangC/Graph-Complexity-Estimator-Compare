from scipy.stats import entropy
import networkx as nx
import matplotlib.pyplot as plt
import math
import random
from KolmogorovComplexity import *


def adjMatrix2string(adj_matrix):
    
    n = len(adj_matrix)
    result = ""
    for i in range(n):
        for j in range(i+1, n):
            result += str(adj_matrix[i][j])
    return result


def GraphKolmogorovComplexity(adj_matrix):
    _tmp = adjMatrix2string(adj_matrix)
    return kolmogorov(_tmp)








# 输入邻接矩阵, 返回一个顶点的出度数组
def get_outdegrees(adj_matrix):
    n = len(adj_matrix)
    outdegrees = []
    for i in range(n):
        outdegree = sum(adj_matrix[i])
        outdegrees.append(outdegree)
    return outdegrees

from collections import Counter





# 输入出度数组, 返回
def calcOutdegreesEntropy(adj_matrix):
    outdegrees = get_outdegrees(adj_matrix)
    freq = Counter(outdegrees) # 使用Counter函数统计每个元素出现的次数
    freq_arr = [freq.get(i, 0) for i in range(max(outdegrees) + 1)] # 生成频率数组
    return entropy(freq_arr)

    # outdegrees: 顶点的出度数组
    # 返回值: 熵





# 输入一个二进制的字符串, 返回一个邻接矩阵
def binaryString2LinkMatrix(binary_str):
    n = int(math.sqrt(len(binary_str))) + 1
    link_matrix = [[0 for i in range(n)] for j in range(n)]
    _tmp = 0
    for i in range(n):
        for j in range(i):
            _tmp+=1
            link_matrix[i][j] = int(binary_str[_tmp])
            
    for i in range(n):
        for j in range(i, n):
            link_matrix[i][j] = link_matrix[j][i]
    return link_matrix





# 创建一个随机图
# 图的节点的数目是n, 每条边存在的概率是p
def generate_random_graph(n, p):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                G.add_edge(i, j)
    return G






def adj_matrix2nxGraph(adj_matrix):
    N = len(adj_matrix)
    G = nx.Graph()
    for i in range(N):
        for j in range(i+1, N):
            if adj_matrix[i][j] == 1:
                G.add_edge(i, j)
    return G





def calAdj_matrixEntropy(adj_matrix):
    _count1 = 0
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[0])):
            if (adj_matrix[i][j] == 1):
                _count1 += 1
    _count0 = len(adj_matrix) * len(adj_matrix[0]) - _count1
    return entropy([_count0, _count1])