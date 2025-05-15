from fastapi import APIRouter, HTTPException
from ..controller.inventory_controller import InventoryController

router = APIRouter()

@router.put("/inventory/{product_id}")
async def update_inventory(product_id: int, quantity: int):
    success, result = InventoryController.update_inventory(product_id, quantity)
    if success:
        return {"message": result}
    raise HTTPException(status_code=400, detail=result)

@router.get("/inventory/{product_id}")
async def get_inventory(product_id: int):
    success, result = InventoryController.get_inventory(product_id)
    if success:
        if result:
            return result
        raise HTTPException(status_code=404, detail="Inventory not found")
    raise HTTPException(status_code=500, detail=result)

@router.get("/inventory")
async def get_all_inventory():
    success, result = InventoryController.get_all_inventory()
    if success:
        return result
    raise HTTPException(status_code=500, detail=result)

@router.get("/inventory/low-stock")
async def get_low_stock_products(threshold: int = 10):
    success, result = InventoryController.get_low_stock_products(threshold)
    if success:
        return result
    raise HTTPException(status_code=500, detail=result)

@router.get("/inventory/recent-updates")
async def get_recently_updated_inventory(days: int = 7):
    success, result = InventoryController.get_recently_updated_inventory(days)
    if success:
        return result
    raise HTTPException(status_code=500, detail=result) 