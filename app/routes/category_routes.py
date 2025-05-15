from fastapi import APIRouter, HTTPException
from ..controller.category_controller import CategoryController

router = APIRouter()

@router.post("/categories")
async def create_category(name: str):
    success, result = CategoryController.create_category(name)
    if success:
        return {"message": result}
    raise HTTPException(status_code=400, detail=result)

@router.get("/categories")
async def get_all_categories():
    success, result = CategoryController.get_all_categories()
    if success:
        return result
    raise HTTPException(status_code=500, detail=result)

@router.get("/categories/{category_id}")
async def get_category(category_id: int):
    success, result = CategoryController.get_category_by_id(category_id)
    if success:
        if result:
            return result
        raise HTTPException(status_code=404, detail="Category not found")
    raise HTTPException(status_code=500, detail=result)

@router.put("/categories/{category_id}")
async def update_category(category_id: int, name: str):
    success, result = CategoryController.update_category(category_id, name)
    if success:
        return {"message": result}
    raise HTTPException(status_code=400, detail=result)

@router.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    success, result = CategoryController.delete_category(category_id)
    if success:
        return {"message": result}
    raise HTTPException(status_code=400, detail=result) 