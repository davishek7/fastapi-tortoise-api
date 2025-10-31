from fastapi import APIRouter, HTTPException
from .models import Order, OrderItem
from ..customer.models import Customer
from .schemas import OrderIn, OrderOut
from .enum import OrderStatus
from .serializer import serialize_order

# Initialize the Order router
router = APIRouter()

VALID_TRANSITIONS = {
    OrderStatus.DRAFT: [OrderStatus.CONFIRMED],
    OrderStatus.CONFIRMED: [OrderStatus.SHIPPED],
    OrderStatus.SHIPPED: [],
}

@router.post("/", response_model=OrderOut)
async def create_order(order_data: OrderIn):
    order = await Order.create(customer_id=order_data.customer_id, status=order_data.status)
    for item in order_data.order_items:
        await OrderItem.create(order_id=order.id, **item.model_dump())
    await order.fetch_related("order_items")
    return serialize_order(order)

@router.get("/{order_id}", response_model=OrderOut)
async def get_order(order_id: str):
    order = await Order.get_or_none(id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    await order.fetch_related("order_items")
    return serialize_order(order)

@router.get("/customer/{customer_id}/total_spend")
async def get_total_spend(customer_id: str):
    customer = await Customer.get_or_none(id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    orders = await Order.filter(customer_id=customer_id, status__in=[OrderStatus.CONFIRMED, OrderStatus.SHIPPED]).prefetch_related("order_items")
    total_spend = 0
    for order in orders:
        for item in order.order_items:
            total_spend += item.quantity * item.price
    return {"customer_id": customer_id, "total_spend": total_spend}

@router.put("/{order_id}/status", response_model=OrderOut)
async def update_order_status(order_id: str, new_status: OrderStatus):
    order = await Order.get_or_none(id=order_id)
    await order.fetch_related("order_items")
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if new_status not in VALID_TRANSITIONS[order.status]:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status transition from {order.status} to {new_status}",
        )

    order.status = new_status
    await order.save()
    return serialize_order(order)