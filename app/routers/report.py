from fastapi import APIRouter

router = APIRouter()

@router.get("/trigger_report")
async def trigger_report():
    return {"Message": "Trigger Report"}

@router.get("/get_report")
async def get_report():
    return {"Message": "Get Report"}