from fastapi import APIRouter, HTTPException
from .models import Customer
from .schemas import CustomerIn, CustomerOut
from typing import List

# Initialize the Customer router
router = APIRouter()

# Create a new customer
@router.post("/", response_model=CustomerOut)
async def create_customer(customer: CustomerIn):
    customer_obj = await Customer.create(**customer.dict())
    return await CustomerOut.from_tortoise_orm(customer_obj)

# List all customers   
@router.get("/", response_model=List[CustomerOut])
async def list_customers():
    return await CustomerOut.from_queryset(Customer.all())

# Get customer by ID
@router.get("/{customer_id}", response_model=CustomerOut)
async def get_customer(customer_id: str):
    customer = await Customer.get_or_none(id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return await CustomerOut.from_tortoise_orm(customer)