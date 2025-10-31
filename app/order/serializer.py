from .schemas import OrderOut


def serialize_order(order):
    serialized_order = {
        "id": str(order.id),
        "customer_id": str(order.customer_id),
        "date": order.date.isoformat(),
        "status": order.status,
        "order_items": [
            {
                "id": str(item.id),
                "order_id": str(item.order_id),
                "product_name": item.product_name,
                "quantity": item.quantity,
                "price": float(item.price),
            }
            for item in order.order_items
        ],
    }
    return OrderOut(**serialized_order)
