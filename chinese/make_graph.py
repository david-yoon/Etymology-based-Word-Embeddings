# coding: utf-8

import codecs
import networkx as nx
import numpy as np


words = None

with codecs.open('../data/chinese_words.csv', 'rb', encoding='utf-8') as f:
    words = [line.strip() for line in f]
    print 'number of words : ', len(words)

# count unique character
chars = set()
for w in words:
    chars = chars.union(set( w ))    
print 'number of chars : ', len(chars)    


# build the graph
G = nx.Graph()


# add chars to the graph as nodes
for ch in chars:
    G.add_node(ch,{'chinese':ch})
print 'number of chars nodes : ', G.number_of_nodes()
    

# add words to the graph as nodes
# add edges among words and its chars
for i,w in enumerate(words):
    G.add_node(str(i),{'chinese': w })
    for ch in w:
        G.add_edge(str(i),ch)
print 'number of nodes (chars + words): ', G.number_of_nodes()

g_file_name = 'chinese_graph.graphml'
print 'export graph file: ', g_file_name
nx.write_graphml(G, g_file_name, encoding='utf-8')
