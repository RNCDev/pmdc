"""
Base class for CRUD operations for SQLAlchemy models.
Provides common methods like get, get_multi, create, update, delete.
"""

# from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from sqlalchemy.sql import Select
# from sqlalchemy import select

# from app.db.models.base import Base # Assuming your Base class is here

# ModelType = TypeVar("ModelType", bound=Base)
# CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
# UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

# class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
#     def __init__(self, model: Type[ModelType]):
#         """
#         CRUD object with default methods to Create, Read, Update, Delete (CRUD).

#         **Parameters**

#         * `model`: A SQLAlchemy model class
#         * `schema`: A Pydantic model (schema) class
#         """
#         self.model = model

#     def get(self, db: Session, id: Any) -> Optional[ModelType]:
#         statement = select(self.model).where(self.model.id == id)
#         return db.scalars(statement).first()

#     def get_multi(
#         self, db: Session, *, skip: int = 0, limit: int = 100
#     ) -> List[ModelType]:
#         statement = select(self.model).offset(skip).limit(limit)
#         return list(db.scalars(statement).all())

#     def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
#         obj_in_data = jsonable_encoder(obj_in)
#         db_obj = self.model(**obj_in_data)
#         db.add(db_obj)
#         db.commit()
#         db.refresh(db_obj)
#         return db_obj

#     def update(
#         self, 
#         db: Session, 
#         *, 
#         db_obj: ModelType, 
#         obj_in: Union[UpdateSchemaType, Dict[str, Any]]
#     ) -> ModelType:
#         obj_data = jsonable_encoder(db_obj)
#         if isinstance(obj_in, dict):
#             update_data = obj_in
#         else:
#             update_data = obj_in.model_dump(exclude_unset=True) # Pydantic v2
#         for field in obj_data:
#             if field in update_data:
#                 setattr(db_obj, field, update_data[field])
#         db.add(db_obj)
#         db.commit()
#         db.refresh(db_obj)
#         return db_obj

#     def remove(self, db: Session, *, id: int) -> ModelType:
#         statement = select(self.model).where(self.model.id == id)
#         obj = db.scalars(statement).one()
#         db.delete(obj)
#         db.commit()
#         return obj 