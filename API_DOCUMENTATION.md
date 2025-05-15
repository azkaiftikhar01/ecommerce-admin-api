

# E-commerce Admin API Documentation

This doc explains the API endpoints you can use, what requests look like, responses, and some examples.

## Base URL

All API endpoints start with `/api/v1`

## Authentication

*Heads up: authentication isn’t done yet. Soon all endpoints will require you to be logged in.*

## API Endpoints

### Categories

#### Get All Categories

```
GET /api/v1/categories
```

**Response example**

```json
{
  "categories": [
    {
      "id": 1,
      "name": "Electronics",
      "description": "Electronic devices and accessories",
      "created_at": "2024-03-20T10:00:00Z",
      "updated_at": "2024-03-20T10:00:00Z"
    }
  ]
}
```

#### Get Category by ID

```
GET /api/v1/categories/{category_id}
```

**Response example**

```json
{
  "id": 1,
  "name": "Electronics",
  "description": "Electronic devices and accessories",
  "created_at": "2024-03-20T10:00:00Z",
  "updated_at": "2024-03-20T10:00:00Z"
}
```

#### Create Category

```
POST /api/v1/categories
```

**Request body**

```json
{
  "name": "Electronics",
  "description": "Electronic devices and accessories"
}
```

#### Update Category

```
PUT /api/v1/categories/{category_id}
```

**Request body**

```json
{
  "name": "Updated Electronics",
  "description": "Updated description"
}
```

#### Delete Category

```
DELETE /api/v1/categories/{category_id}
```

---

### Products

#### Get All Products

```
GET /api/v1/products
```

**Query params**

* `page` (optional): which page to get
* `limit` (optional): how many items per page
* `category_id` (optional): filter by category
* `search` (optional): search by name or description

**Response example**

```json
{
  "products": [
    {
      "id": 1,
      "name": "Smartphone",
      "description": "Latest model smartphone",
      "price": 999.99,
      "category_id": 1,
      "created_at": "2024-03-20T10:00:00Z",
      "updated_at": "2024-03-20T10:00:00Z"
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 10
}
```

#### Get Product by ID

```
GET /api/v1/products/{product_id}
```

#### Create Product

```
POST /api/v1/products
```

**Request body**

```json
{
  "name": "Smartphone",
  "description": "Latest model smartphone",
  "price": 999.99,
  "category_id": 1
}
```

#### Update Product

```
PUT /api/v1/products/{product_id}
```

**Request body**

```json
{
  "name": "Updated Smartphone",
  "description": "Updated description",
  "price": 899.99,
  "category_id": 1
}
```

#### Delete Product

```
DELETE /api/v1/products/{product_id}
```

---

### Inventory

#### Get Inventory Status

```
GET /api/v1/inventory
```

**Query params**

* `product_id` (optional): filter by product
* `low_stock` (optional): show only low stock items

**Response example**

```json
{
  "inventory": [
    {
      "product_id": 1,
      "quantity": 100,
      "last_updated": "2024-03-20T10:00:00Z"
    }
  ]
}
```

#### Update Inventory

```
PUT /api/v1/inventory/{product_id}
```

**Request body**

```json
{
  "quantity": 150
}
```

---

## Error responses

You might get these errors sometimes:

### 400 Bad Request

```json
{
  "detail": "Invalid request parameters"
}
```

### 404 Not Found

```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error

```json
{
  "detail": "Internal server error"
}
```

---

## Rate limiting

*Note: rate limiting isn’t ready yet. Will add it soon.*
