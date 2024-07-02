# React + FastAPI Application Requirements

## Goal: Motoki Coffee Customer Data Analysis Product v2
The requirements for a React + FastAPI application to meet the above goal are described below.

The requirements are defined following the principles of object-oriented design.

## 1. Purpose
The overall purpose of the system is to provide a data analysis platform for Motoki Coffee's customer data.

## 2. File and Folder Structure
```
├── diagrams/
│   ├── app_architecture.png
│   ├── sequence.png
├── frontend/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── package.json
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── store/
│   │   └── utils/
│   └── tsconfig.json
├── backend/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   └── routers/
│       ├── customers.py
│       └── orders.py
└── docker-compose.yml
```

![Sequence Diagram](diagrams/sequence.png)

## 3. Architecture Diagram
![Architecture Diagram](diagrams/app_architecture.png)

## 4. API Endpoints
The following API endpoints will be implemented using FastAPI:

- `GET /customers`: Retrieve a list of customers
- `GET /customers/{customer_id}`: Retrieve a specific customer
- `POST /customers`: Create a new customer
- `PUT /customers/{customer_id}`: Update a customer
- `DELETE /customers/{customer_id}`: Delete a customer
- `GET /orders`: Retrieve a list of orders
- `GET /orders/{order_id}`: Retrieve a specific order
- `POST /orders`: Create a new order
- `PUT /orders/{order_id}`: Update an order
- `DELETE /orders/{order_id}`: Delete an order

## 5. Data Models
The following data models will be defined using SQLAlchemy:

**Customer**
- `id`: int, primary key
- `name`: str
- `email`: str
- `phone`: str
- `created_at`: datetime
- `updated_at`: datetime

**Order**
- `id`: int, primary key
- `customer_id`: int, foreign key to Customer
- `product`: str
- `quantity`: int
- `total_amount`: float
- `created_at`: datetime
- `updated_at`: datetime

## 6. React Components
The main React components of the application are:

- `App`: The root component that manages the overall application state and routing
- `CustomerList`: Displays a list of customers
- `CustomerDetails`: Displays detailed information about a specific customer
- `OrderList`: Displays a list of orders
- `OrderDetails`: Displays detailed information about a specific order
- `CustomerForm`: Allows creating and updating customer information
- `OrderForm`: Allows creating and updating order information

## 7. User Interface
The application will have the following screen transitions:

1. Customer List
2. Customer Details
3. Create/Update Customer
4. Order List
5. Order Details
6. Create/Update Order

The wireframes or mockups for each screen are provided in the `ui/` directory.