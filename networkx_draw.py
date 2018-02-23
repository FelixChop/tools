# tools for graph

############################
# Example of use:
# g = nx.ego_graph(G, n=node, radius=4)
# draw(g)

import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)

###################
# With one type of edge
NODE_SIZE = {'type_1': 100, 'type_2':20}
NODE_COLOR = {'type_1': 'orange', 'type_2': 'red'}

def node_sizes(s, specific_node_size=None): 
    if not specific_node_size:
        return [NODE_SIZE[s.nodes[node]['label']] for node in s.nodes()]
    else:
        return [NODE_SIZE[s.nodes[node]['label']] if node not in specific_node_size.keys() 
                else specific_node_size[node] for node in s.nodes()]

def node_colors(s): return [NODE_COLOR[s.nodes[node]['label']] for node in s.nodes()]

def draw(s, specific_node_size=None):
    nx.draw(s, node_size=node_sizes(s, specific_node_size=specific_node_size), 
        node_color=node_colors(s), 
        alpha=0.8, arrows = False,
        labels=dict((n,n) for n,d in s.nodes(data=True) if s.node[n]['label']=='email'), 
        font_color='black', font_size=8, font_weight='bold')

####################
# With different edges
NODE_SIZE = {'node_type_1': 100, 'node_type_2':20}
NODE_COLOR = {'node_type_1': 'orange', 'node_type_2': 'red'}

EDGE_SIZE = {'edge_type_1': 2, 'edge_type_2': 1, 'edge_type_3': 5}
EDGE_COLOR = {'edge_type_1': 'purple', 'edge_type_2': 'yellow', 'edge_type_3': 'red'}

def node_sizes(s, specific_node_size=None): 
    if not specific_node_size:
        return [NODE_SIZE[s.nodes[node]['label']] for node in s.nodes()]
    else:
        return [NODE_SIZE[s.nodes[node]['label']] 
                if node not in specific_node_size.keys() 
                else specific_node_size[node]
                for node in s.nodes()]
    
def node_colors(s): return [NODE_COLOR[s.nodes[node]['label']] for node in s.nodes()]

def clean_edge(edge):
    s.edge[edge[0], edge[1]].values()

def c_(list_edges): return [a for a in list_edges if a in list(EDGE_COLOR.keys())]
    
# For nx.Graph()
def edge_sizes(s): return [EDGE_SIZE[c_(list(s.edges[edge[0], edge[1]].keys()))[-1]] for edge in s.edges()] # /!\ multiple links => one size
def edge_colors(s): return [EDGE_COLOR[c_(list(s.edges[edge[0], edge[1]].keys()))[-1]] for edge in s.edges()] # /!\ multiple links => one color

# For nx.MultiDiGraph()
# def edge_sizes(s): return [EDGE_SIZE[s.edge[edge[0]][edge[1]][0]['label']] for edge in s.edges()] # /!\ multiple links => one size
# def edge_colors(s): return [EDGE_COLOR[s.edge[edge[0]][edge[1]][0]['label']] for edge in s.edges()] # /!\ multiple links => one color

def draw(s, specific_node_size=None):
    nx.draw(s, node_size=node_sizes(s, specific_node_size=specific_node_size), 
        node_color=node_colors(s), 
        width=edge_sizes(s), edge_color=edge_colors(s), alpha=0.8, arrows = False)