
# E-commerce Admin API

This is a REST API made with FastAPI and MySQL to manage e-commerce stuff. You can do CRUD operations on products, manage categories, and track inventory. It’s built to be scalable and pretty fast.

## Features

* Manage products (create, read, update, delete)
* Manage categories
* Keep track of inventory
* Optimized database indexes for better speed
* RESTful API design
* Swagger/OpenAPI docs included
* Uses MySQL as the database

## Tech Stack

* FastAPI (Python web framework)
* MySQL database
* Python 3.8 or newer

## Prerequisites

* Python 3.8+
* MySQL Server installed
* pip package manager

## Installation

1. Clone the repo:

```bash
git clone <repository-url>
cd ecommerce-admin-api
```

2. Setup a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Setup your database:

   * Create a MySQL database for this project
   * Update the config file at `app/db/connection.py` with your DB credentials

5. Initialize the database tables:

```bash
# You can start the server and open /init-db in your browser,
# or call the GET/POST /init-db endpoint via any API client
```

## Running the app

1. Run the FastAPI server with:

```bash
uvicorn app.main:app --reload
```

2. Visit the docs to see the API in action:

   * Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   * ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Docs

Full API details are in the `API_DOCUMENTATION.md` file.

## Security

* Endpoints will have auth protection (still need to implement)
* Uses parameterized queries to avoid SQL injection
* Input validated through Pydantic models

## Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature/feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to your branch (`git push origin feature/feature`)
5. Open a pull request



## Thanks To

* FastAPI docs
* MySQL docs
* Python community
