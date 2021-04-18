from fastapi import APIRouter
from neomodel import db
import networkx as nx
from networkx.readwrite import json_graph

router = APIRouter(
    prefix='/parent-child',
    tags=['Parent & Child'],
)

@router.get('/')
def nodes_links():
    
    rels = db.cypher_query(f'''
        MATCH (n) -[r]-> (m) 
        WHERE 
        NOT m:Arrondissement AND 
        NOT n:Arrondissement AND 
        NOT m:Epci AND 
        NOT n:Epci AND 
        NOT m:Subset AND 
        NOT n:Subset AND 
        NOT m:Collectivite AND 
        NOT n:Collectivite AND 
        NOT m:Group AND 
        NOT n:Group 
        RETURN n.id_1, m.id_1
    ''')

    rel = [(f'{s_id}', f'{r_id}') for s_id, r_id in rels[0]]

    G = nx.DiGraph(rel)
    data = json_graph.node_link_data(G)
    
    return {
        'nodes': data['nodes'], 
        'links': data['links']
        }