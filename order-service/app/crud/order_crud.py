from typing import List
from sqlmodel import Session, select
from fastapi import HTTPException
from app.model.order_model import Order, OrderItem

def create_order_item(db: Session, order: Order) -> Order:
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_order_from_db(db: Session, order_id: int) -> Order:
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

def update_order_in_db(db: Session, order_id: int, order_update: Order) -> Order:
    db_order = db.get(Order, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    for key, value in order_update.dict(exclude_unset=True).items():
        setattr(db_order, key, value)
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order_from_db(db: Session, order_id: int) -> Order:
    db_order = db.get(Order, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return db_order

def add_order_item_to_db(db: Session, order_id: int, item: OrderItem) -> OrderItem:
    db_order = db.get(Order, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found!")
    item.order_id = order_id
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_order_item_from_db(db: Session, order_id: int) -> List[OrderItem]:
    items = db.exec(select(OrderItem).where(OrderItem.order_id == order_id)).all()
    return items