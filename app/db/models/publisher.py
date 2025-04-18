"""
SQLAlchemy model for Publishers (GPs or GP Agents).
"""

# from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.orm import relationship
# from .base import TimestampedBase # Or just Base

# class Publisher(TimestampedBase): # Or just Base
#     __tablename__ = "publishers"

#     # id (from Base)
#     # created_at (from Base)
#     # updated_at (from Base)

#     external_id = Column(String, unique=True, index=True, nullable=False)
#     name = Column(String, index=True, nullable=False)
#     is_active = Column(Boolean(), default=True)

#     # --- Foreign Key References / Relationships --- # 
    
#     # Define the expected input schema identifier for this publisher
#     # This is crucial for the intake service
#     schema_identifier = Column(String, nullable=True) # e.g., "publisher_a_v1", "juniper_square_v3"

#     # Relationship to Data Records (One-to-Many: One Publisher -> Many Data Records)
#     # data_records = relationship("DataRecord", back_populates="publisher")

#     # Relationship to Subscriptions (Many-to-Many through Subscription table)
#     # This defines which subscribers can see this publisher's data.
#     # subscriptions = relationship("Subscription", back_populates="publisher")

#     # Relationship to Auth Users (if users are stored separately)
#     # If using an external IdP, this might link to a user representation here,
#     # or permissions might be handled purely via the IdP roles/groups.
#     # e.g., users = relationship("User", secondary=publisher_user_association, back_populates="publishers")

#     def __repr__(self):
#         return f"<Publisher(id={self.id}, external_id=	\'{self.external_id}	\")>" 