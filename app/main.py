from fastapi import FastAPI
from neomodel import config, db
from ariadne.asgi import GraphQL

import os
from dotenv import load_dotenv
load_dotenv()

from routers import tree_graph, parent_child
from ariadne_resolvers import schema

app = FastAPI()

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
config.DATABASE_URL = f'bolt://{USERNAME}:{PASSWORD}@localhost:7687'

app.include_router(tree_graph.router)
app.include_router(parent_child.router)

app.mount("/graphql/", GraphQL(schema, debug=True))

@app.get("/")
def read_root():
    return {"Hello": "World"}




