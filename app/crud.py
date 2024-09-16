from sqlalchemy.orm import Session
from .models import Cliente, Mesa
from .schemas import ClienteCreate, ClienteUpdate, MesaCreate, MesaUpdate, PedidoCreate, Pedido, PedidoUpdate
from . import models

def create_cliente(db: Session, cliente_data: ClienteCreate):
    db_cliente = Cliente(**cliente_data.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def get_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def get_all_clientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cliente).offset(skip).limit(limit).all()

def update_cliente(db: Session, cliente_id: int, cliente_data: ClienteUpdate):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if db_cliente:
        for key, value in cliente_data.items():
            setattr(db_cliente, key, value)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente
    return None

def delete_cliente(db: Session, cliente_id: int):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
        return {"message": "Cliente eliminado"}
    return {"message": "Cliente no encontrado"}

def create_mesa(db: Session, mesa_data: MesaCreate):
    db_mesa = Mesa(**mesa_data.dict())
    db.add(db_mesa)
    db.commit()
    db.refresh(db_mesa)
    return db_mesa

def get_mesa(db: Session, mesa_id: int):
    return db.query(Mesa).filter(Mesa.id == mesa_id).first()

def get_all_mesas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Mesa).offset(skip).limit(limit).all()

def update_mesa(db: Session, mesa_id: int, mesa_data: dict):
    mesa = db.query(models.Mesa).filter(models.Mesa.id == mesa_id).first()
    if not mesa:
        return None
    for key, value in mesa_data.items():
        setattr(mesa, key, value)
    db.commit()
    db.refresh(mesa)
    return mesa

def delete_mesa(db: Session, mesa_id: int):
    db_mesa = db.query(Mesa).filter(Mesa.id == mesa_id).first()
    if db_mesa:
        db.delete(db_mesa)
        db.commit()
        
        
def create_pedido(db: Session, pedido_data: PedidoCreate):
    db_pedido = Pedido(**pedido_data.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

def get_pedido(db: Session, pedido_id: int):
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()

def get_all_pedidos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Pedido).offset(skip).limit(limit).all()

def update_pedido(db: Session, pedido_id: int, pedido_data: PedidoUpdate):
    db_pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if db_pedido:
        for key, value in pedido_data.dict().items():
            setattr(db_pedido, key, value)
        db.commit()
        db.refresh(db_pedido)
        return db_pedido
    return None

def delete_pedido(db: Session, pedido_id: int):
    db_pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if db_pedido:
        db.delete(db_pedido)
        db.commit()
        return {"message": "Pedido eliminado"}
    return {"message": "Pedido no encontrado"}