from fastapi import FastAPI, HTTPException
from .db.connection import get_connection
from .routes import category_routes, product_routes, inventory_routes
from .db.dml.indexes import CREATE_INDEXES
import os

# TODO: Add proper logging
app = FastAPI(
    title="E-commerce Admin API",
    description="API for managing e-commerce admin operations",
    version="1.0.0"
)

# Include all routers
app.include_router(category_routes.router, prefix="/api/v1", tags=["Categories"])
app.include_router(product_routes.router, prefix="/api/v1", tags=["Products"])
app.include_router(inventory_routes.router, prefix="/api/v1", tags=["Inventory"])

def initialize_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Create tables
        schema_path = os.path.join(os.path.dirname(__file__), 'db', 'ddl', 'creation.sql')
        with open(schema_path, 'r') as file:
            sql_commands = file.read()
            
        commands = sql_commands.split(';')
        
        for command in commands:
            if command.strip():
                cursor.execute(command)
                cursor.fetchall()  # Clear any results
        
        # Create indexes one by one
        index_commands = CREATE_INDEXES.split(';')
        for command in index_commands:
            if command.strip():
                try:
                    if command.strip().startswith('DROP INDEX'):
                        try:
                            cursor.execute(command)
                            cursor.fetchall()
                        except Exception:
                            # Ignore errors when dropping non-existent indexes
                            pass
                    else:
                        # For CREATE INDEX, check if it exists first
                        index_name = command.split('ON')[0].split('idx_')[1].strip()
                        table_name = command.split('ON')[1].split('(')[0].strip()
                        check_index = f"SHOW INDEX FROM {table_name} WHERE Key_name = 'idx_{index_name}'"
                        cursor.execute(check_index)
                        if not cursor.fetchall():
                            cursor.execute(command)
                            cursor.fetchall()
                except Exception as e:
                    print(f"Warning: Could not create index: {str(e)}")
                    continue
        
        conn.commit()
        return True, "Database initialized successfully with optimized indexes"
        
    except Exception as e:
        if conn:
            conn.rollback()
        return False, f"Error initializing database: {str(e)}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# FIXME: Add proper error handling
@app.get("/init-db")
@app.post("/init-db")
async def init_db():
    """
    Initialize the database by creating all necessary tables.
    This endpoint should only be called once during initial setup.
    """
    success, message = initialize_database()
    
    if success:
        return {"status": "success", "message": message}
    else:
        raise HTTPException(status_code=500, detail=message)

@app.get("/")
async def root():
    # TODO: Add health check
    return {
        "message": "Welcome to E-commerce Admin API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }
