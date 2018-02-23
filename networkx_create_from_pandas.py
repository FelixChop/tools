# tools for creating a graph from a pandas dataframe
import networkx as nx

# Create graph edges first
col_node_1 = 'Person_ID'
col_node_2 = 'Company_ID'
col_attr = ['start_date', 'end_date']
G = nx.from_pandas_edgelist(df = df, 
                             source=col_node_1, 
                             target=col_node_2, 
                             edge_attr=col_attr)
# OR
G = nx.from_pandas_edgelist(df = df.assign(has_worked=1), 
                             source=col_node_1, 
                             target=col_node_2, 
                             edge_attr=col_attr+['has_worked'])

# Add node labels
list_person_1 = [] # list of person with special type
G.add_nodes_from(df.loc[(df[col_node_1].isin(list_person_1)), 
	col_node_1].unique().tolist(), label='person_type_1')
G.add_nodes_from(df.loc[~(df[col_node_1].isin(list_person_1)), 
	col_node_1].unique().tolist(), label='person_type_2')

G.add_nodes_from(df[col_node_2].unique().tolist(), label='Company')

# Create links for people with same email and same telephone

# There is only one variable for email
col_edge = 'email'
emails = df[[col_node_1, col_edge]].dropna(subset=[col_edge]).drop_duplicates()
emails = emails.merge(emails[[col_node_1, col_edge]].rename(columns={col_node_1:col_node_1+"_2"}),
    on=col_edge)
d = emails[~(emails[col_node_1]==emails[col_node_1+"_2"])].dropna()[[col_node_1, col_node_1+"_2"]]
links = d.apply(lambda row: tuple(row), axis=1).tolist() # or tqdm_pandas() progress_apply
G.add_edges_from(links, same_email=1)

# There are two variables for phone numbers
col_edge_1 = 'tel_number_1'
col_edge_2 = 'tel_number_2'
tels = df[[col_node_1, col_edge_1]].dropna(subset=[col_edge_1]).rename(columns={col_edge_1:'tel_number'}) \
 .append(df[[col_node_1, col_edge_2]].dropna(subset=[col_edge_2]).rename(columns={col_edge_2:'tel_number'})) \
 .drop_duplicates()

tels = tels.merge(tels[[col_node_1, 'tel_number']].rename(columns={col_node_1:col_node_1+"_2"}),
    on='tel_number')

d = tels[~(tels[col_node_1]==tels[col_node_1+"_2"])].dropna()[[col_node_1, col_node_1+"_2"]]
links = d.apply(lambda row: tuple(row), axis=1).tolist() # or tqdm_pandas() progress_apply
G.add_edges_from(links, same_phone=1)
