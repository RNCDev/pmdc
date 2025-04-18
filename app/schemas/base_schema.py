"""
Base Pydantic models and common configuration.
"""

# from pydantic import BaseModel
# from pydantic_settings import BaseSettings

# class CustomBaseModel(BaseModel):
#     """Base model with shared configuration."""
#     model_config = {
#         "from_attributes": True, # Allow creating schemas from ORM models
#         "populate_by_name": True, # Allow using field aliases
#     }

# # Example for settings management (though usually in core/config.py)
# # class Settings(BaseSettings):
# #     API_V1_STR: str = "/api/v1"
# #     # ... other settings

# # Note: Often, simple schemas don't need a custom base model initially.
# # We can just use `from pydantic import BaseModel` directly in other schema files. 