from fastapi import APIRouter, HTTPException
from ..controller.product_controller import ProductController

router = APIRouter()

@router.post("/products")
async def create_product(name: str, category_id: int, price: float):
    # TODO: Add input validation
    success, result = ProductController.create_product(name, category_id, price)
    if success:
        return {"message": result}
    raise HTTPException(status_code=400, detail=result)

@router.get("/products")
async def get_all_products():
    # FIXME: Add pagination
    success, result = ProductController.get_all_products()
    if success:
        return result
    raise HTTPException(status_code=500, detail=result)

@router.get("/products/{product_id}")
async def get_product(product_id: int):
    success, result = ProductController.get_product_by_id(product_id)
    if success:
        if result:
            return result
        raise HTTPException(status_code=404, detail="Product not found")
    raise HTTPException(status_code=500, detail=result)

# TODO: Add sorting options
@router.get("/products/category/{category_id}")
async def get_products_by_category(category_id: int):
    success, result = ProductController.get_products_by_category(category_id)
    if success:
        return result
    raise HTTPException(status_code=500, detail=result)

@router.get("/products/price-range")
async def get_products_by_price_range(min_price: float, max_price: float):
    # FIXME: Validate price range
    success, result = ProductController.get_products_by_price_range(min_price, max_price)
    if success:
        return result
    raise HTTPException(status_code=500, detail=result)

@router.get("/products/category/{category_id}/price")
async def get_products_by_category_and_price(category_id: int, max_price: float):
    success, result = ProductController.get_products_by_category_and_price(category_id, max_price)
    if success:
        return result
    raise HTTPException(status_code=500, detail=result)

# TODO: Add partial update support
@router.put("/products/{product_id}")
async def update_product(product_id: int, name: str, category_id: int, price: float):
    success, result = ProductController.update_product(product_id, name, category_id, price)
    if success:
        return {"message": result}
    raise HTTPException(status_code=400, detail=result)

@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    # FIXME: Add soft delete
    success, result = ProductController.delete_product(product_id)
    if success:
        return {"message": result}
    raise HTTPException(status_code=400, detail=result) 