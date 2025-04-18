# Pseudocode for app/db/crud/__init__.py

"""
Make CRUD operations easily importable.

Example usage in services or API endpoints:
from app.db import crud

# ... later in code ...
db_publisher = crud.publisher.get_by_external_id(db, external_id=pub_ext_id)
"""

# from .crud_publisher import publisher
# from .crud_subscriber import subscriber
# from .crud_subscription import subscription
# from .crud_data_record import data_record
# # Import other CRUD objects as needed (e.g., audit log) 