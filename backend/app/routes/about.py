from fastapi import APIRouter

router = APIRouter()

@router.get("/about")
def about():
    return {"message": "This is a simple tarot card app."}
