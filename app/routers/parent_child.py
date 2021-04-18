from fastapi import APIRouter

router = APIRouter(
    prefix='/parent-child',
    tags=['Parent & Child'],
)

@router.get('/')
def nodes_links():
    return {"Hello": "World"}