# This file makes the directory a Python package

# Optionally, you could import specific schemas here for easier access,
# but it's often cleaner to import directly from the specific module.

# Example (if you had publisher_a.py and publisher_b.py):
# from .publisher_a import PublisherASchema
# from .publisher_b import PublisherBSchema

# Or define a function/registry to get schemas dynamically
# def get_publisher_schema(identifier: str):
#     if identifier == "publisher_a_v1":
#         from .publisher_a import PublisherASchema
#         return PublisherASchema
#     # ... other schemas
#     else:
#         raise KeyError(f"Unknown publisher schema identifier: {identifier}") 