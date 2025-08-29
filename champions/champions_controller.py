from fastapi import APIRouter, HTTPException

from champions.champions_services import ChampionsService


router = APIRouter()

route = "/champions"

@router.get(route)
def get_all_champions():
    try:
        return ChampionsService().get_all_champions()
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("{route}/{name}")
def get_champion_by_name(name: str):
    try:
        return ChampionsService().get_champion_by_name(name)
    except HTTPException as e:
            raise HTTPException(status_code=500, detail=str(e))