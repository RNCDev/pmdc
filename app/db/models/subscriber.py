"""
SQLAlchemy model for Subscribers (LPs or LP Agents).
"""

# from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.orm import relationship
# from .base import TimestampedBase # Or just Base

# class Subscriber(TimestampedBase): # Or just Base
#     __tablename__ = "subscribers"

#     # id (from Base)
#     # created_at (from Base)
#     # updated_at (from Base)

#     external_id = Column(String, unique=True, index=True, nullable=False) # Could be org ID
#     name = Column(String, index=True, nullable=False)
#     is_active = Column(Boolean(), default=True)

#     # --- Preferences --- #

#     # Preferred output format identifier (e.g., "default_json", "subscriber_xyz_v1")
#     # Used by the delivery service/translator
#     preferred_output_format = Column(String, nullable=False, default="default_json")

#     # Delivery mechanism preferences (e.g., API pull, SFTP push - Future?)
#     # delivery_method = Column(String, nullable=False, default="API_PULL")
#     # delivery_config = Column(JSON, nullable=True) # Store SFTP creds, API endpoints etc.

#     # --- Relationships --- #

#     # Relationship to Subscriptions (Many-to-Many through Subscription table)
#     # This defines which publishers this subscriber can see data from.
#     # subscriptions = relationship("Subscription", back_populates="subscriber")

#     # Relationship to Auth Users (if users are stored separately)
#     # users = relationship("User", secondary=subscriber_user_association, back_populates="subscribers")

#     def __repr__(self):
#         return f"<Subscriber(id={self.id}, external_id=	\'{self.external_id}	\')>" 