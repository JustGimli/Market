from fastapi import APIRouter

router = APIRouter(
    tags=['home']
)


@router.get('/')
async def home_page():
    return 'd'
