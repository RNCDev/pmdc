"""
SQLAlchemy model representing the link between a Publisher and a Subscriber,
controlling data access permissions.
"""

# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint
# from sqlalchemy.orm import relationship
# from .base import TimestampedBase # Or just Base

# class Subscription(TimestampedBase): # Or just Base
#     __tablename__ = "subscriptions"
    
#     # Enforce that a subscriber can only subscribe to a publisher once
#     __table_args__ = (UniqueConstraint("publisher_id", "subscriber_id", name="uq_publisher_subscriber"),)

#     # id (from Base)
#     # created_at (from Base)
#     # updated_at (from Base)

#     publisher_id = Column(Integer, ForeignKey("publishers.id"), nullable=False)
#     subscriber_id = Column(Integer, ForeignKey("subscribers.id"), nullable=False)

#     is_active = Column(Boolean(), default=True, nullable=False)
#     # Could add status field (e.g., pending, active, suspended)
#     # status = Column(String, nullable=False, default="active") 

#     # --- Relationships --- #

#     # Relationship back to Publisher (Many-to-One: Many Subscriptions -> One Publisher)
#     # publisher = relationship("Publisher", back_populates="subscriptions")

#     # Relationship back to Subscriber (Many-to-One: Many Subscriptions -> One Subscriber)
#     # subscriber = relationship("Subscriber", back_populates="subscriptions")

#     def __repr__(self):
#         return f"<Subscription(publisher_id={self.publisher_id}, subscriber_id={self.subscriber_id}, active={self.is_active})>" 