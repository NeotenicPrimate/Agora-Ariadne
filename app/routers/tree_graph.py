from fastapi import APIRouter

router = APIRouter(
    prefix='/tree-graph',
    tags=['Tree Graph'],
)

@router.get('/')
def tree_graph():
    return {"Hello": "World"}