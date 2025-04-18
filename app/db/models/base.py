"""
Base model for SQLAlchemy models, potentially including common fields like ID, timestamps.
"""

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, DateTime
# from sqlalchemy.sql import func

# Base = declarative_base()

# class TimestampedBase(Base):
#     """An abstract base model with primary key, created_at, and updated_at fields."""
#     __abstract__ = True # Makes sure SQLAlchemy doesn't create a table for this

#     id = Column(Integer, primary_key=True, index=True)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())

# # If no common fields are needed initially, just use:
# # Base = declarative_base() 