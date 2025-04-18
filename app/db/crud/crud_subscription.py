# Pseudocode for app/db/crud/crud_subscription.py

"""
CRUD operations for the Subscription model.
"""

# from typing import List, Optional, Set

# from sqlalchemy.orm import Session
# from sqlalchemy import select, and_
# from sqlalchemy.orm import joinedload

# from .base import CRUDBase
# from app.db.models.subscription import Subscription
# from app.schemas.subscription import SubscriptionCreate, SubscriptionUpdate # Assuming these schemas exist

# class CRUDSubscription(CRUDBase[Subscription, SubscriptionCreate, SubscriptionUpdate]):

#     def get_by_publisher_subscriber(
#         self, db: Session, *, publisher_id: int, subscriber_id: int
#     ) -> Optional[Subscription]:
#         """Get a specific subscription link."""
#         statement = select(self.model).where(
#             and_(self.model.publisher_id == publisher_id, self.model.subscriber_id == subscriber_id)
#         )
#         return db.scalars(statement).first()

#     def get_active_by_subscriber(
#         self, db: Session, *, subscriber_id: int
#     ) -> List[Subscription]:
#         """Get all active subscriptions for a given subscriber, potentially joining publisher info."""
#         statement = (
#             select(self.model)
#             .where(and_(self.model.subscriber_id == subscriber_id, self.model.is_active == True))
#             # Eager load the publisher details to avoid N+1 queries later
#             # .options(joinedload(self.model.publisher))
#         )
#         return list(db.scalars(statement).all())

#     def get_active_publishers_for_subscriber(
#         self, db: Session, *, subscriber_id: int
#     ) -> List[int]: # Return list of publisher IDs
#         """Get the IDs of all publishers a subscriber has an active subscription to."""
#         statement = (
#             select(self.model.publisher_id) # Select only the publisher_id
#             .where(and_(self.model.subscriber_id == subscriber_id, self.model.is_active == True))
#             .distinct()
#         )
#         return list(db.scalars(statement).all())

#     def create_subscription(self, db: Session, *, publisher_id: int, subscriber_id: int) -> Subscription:
#         """Create a new subscription link."""
#         # Check if it already exists?
#         existing = self.get_by_publisher_subscriber(db, publisher_id=publisher_id, subscriber_id=subscriber_id)
#         if existing:
#             if not existing.is_active:
#                 # Reactivate if exists but inactive
#                 existing.is_active = True
#                 db.add(existing)
#                 db.commit()
#                 db.refresh(existing)
#                 return existing
#             return existing # Already exists and active
        
#         # Create new if doesn't exist
#         db_obj = self.model(publisher_id=publisher_id, subscriber_id=subscriber_id, is_active=True)
#         db.add(db_obj)
#         db.commit()
#         db.refresh(db_obj)
#         return db_obj

#     def deactivate_subscription(self, db: Session, *, publisher_id: int, subscriber_id: int) -> Optional[Subscription]:
#         """Mark a subscription as inactive."""
#         db_obj = self.get_by_publisher_subscriber(db, publisher_id=publisher_id, subscriber_id=subscriber_id)
#         if db_obj and db_obj.is_active:
#             db_obj.is_active = False
#             db.add(db_obj)
#             db.commit()
#             db.refresh(db_obj)
#         return db_obj

# # Instantiate the CRUD object
# subscription = CRUDSubscription(Subscription) 