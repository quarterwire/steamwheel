from fastapi import APIRouter
from app.services.game_service import get_random_game, get_game_by_id

router = APIRouter()


@router.get("/random_game")
async def random_game_controller():
    game = await get_random_game()
    return game


@router.get("/game/{game_id}")
async def get_game_controller(game_id: int):
    game = get_game_by_id(game_id)
    return {"item_id": game}
