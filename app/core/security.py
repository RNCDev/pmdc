"""
Security-related utilities, including password hashing (if storing users locally),
JWT token handling, and authorization checks.
"""

# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, SecurityScopes
# from jose import JWTError, jwt
# from pydantic import ValidationError
# from sqlalchemy.orm import Session

# from app.core.config import settings
# from app import crud, models, schemas
# from app.api import deps
# from typing import Optional

# # --- Constants --- #
# ALGORITHM = settings.AUTH_ALGORITHMS[0] if settings.AUTH_ALGORITHMS else "RS256"
# # This depends on how the IdP structures the token URL
# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl=f"{settings.API_V1_STR}/login/token" # Needs an actual login endpoint if using password flow
#     # If using Implicit/Authorization Code flow from IdP, this might not be used directly
#     # but FastAPI still needs it for dependency injection.
#     # Alternatively, use OpenIdConnect dependency for OIDC flows.
#     # schemes=["bearer"],
#     # scopes={settings.SCOPE_PUBLISHER_WRITE: "Write data as publisher",
#     #         settings.SCOPE_SUBSCRIBER_READ: "Read data as subscriber",
#     #         settings.SCOPE_ADMIN: "Manage system settings"}
# )

# # --- JWT Handling (Example using PyJWT / python-jose) --- #

# # In a real OAuth2/OIDC setup with an external IdP, you often don't *create* tokens here.
# # You primarily *validate* tokens received from the IdP.

# def validate_token(token: str = Depends(oauth2_scheme)) -> schemas.TokenPayload:
#     """Validate the JWT token received from the client via the IdP."""
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     unauthorized_exception = HTTPException(
#         status_code=status.HTTP_403_FORBIDDEN, 
#         detail="Operation not permitted"
#     )
    
#     try:
#         # Fetch JWKS from IdP (cache this in production!)
#         # jwks = fetch_jwks(settings.AUTH_JWKS_URL)
#         # header = jwt.get_unverified_header(token)
#         # rsa_key = find_rsa_key(jwks, header["kid"])
        
#         # payload = jwt.decode(
#         #     token,
#         #     rsa_key,
#         #     algorithms=settings.AUTH_ALGORITHMS,
#         #     audience=settings.AUTH_AUDIENCE,
#         #     issuer=settings.AUTH_ISSUER
#         # )
#         # Simulate a decoded payload for pseudocode
#         payload = {
#             "sub": "auth0|user123", # Subject (user ID from IdP)
#             "iss": str(settings.AUTH_ISSUER),
#             "aud": settings.AUTH_AUDIENCE,
#             "scope": "read:data write:data", # Example scopes
#             "exp": 9999999999, # Expiry timestamp
#             "iat": 1600000000, # Issued at timestamp
#             # Custom claims might identify the publisher/subscriber ID
#             "ext_publisher_id": "pub_a_123", 
#             "ext_subscriber_id": None,
#             "azp": "clientid123" # Authorized party (client ID)
#         }
        
#         token_data = schemas.TokenPayload(**payload)
        
#     except (JWTError, ValidationError, KeyError) as e:
#         print(f"Token Validation Error: {e}") # Log the error
#         raise credentials_exception

#     # --- Optional: Map IdP user to local user/entity --- #
#     # You might need to look up the user/publisher/subscriber in your DB based on `token_data.sub`
#     # or custom claims like `ext_publisher_id`.
#     # user = crud.user.get_by_external_id(db, external_id=token_data.sub)
#     # if not user or not user.is_active:
#     #    raise credentials_exception 

#     return token_data

# # --- Authorization Dependencies --- #

# def get_current_active_user(
#     security_scopes: SecurityScopes,
#     token_payload: schemas.TokenPayload = Depends(validate_token),
#     db: Session = Depends(deps.get_db) # Assuming DB dependency exists
# ) -> models.User: # Or just return the token_payload if not mapping to DB users
#     """Dependency to get the current user and check scopes."""
    
#     # Check scopes from the token against required scopes for the endpoint
#     token_scopes = set(token_payload.scope.split())
#     for scope in security_scopes.scopes:
#         if scope not in token_scopes:
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail="Not enough permissions",
#                 headers={"WWW-Authenticate": security_scopes.scope_str},
#             )
            
#     # --- Map token subject/claims to internal DB entity (Publisher/Subscriber) --- #
#     # This logic is crucial and depends on your IdP setup and custom claims.
#     user_identifier = token_payload.sub # Or a custom claim
    
#     # Example: Try to find a publisher linked to this token
#     publisher = crud.publisher.get_by_external_id(db, external_id=user_identifier) # Or use ext_publisher_id claim
#     if publisher and publisher.is_active:
#         # Here you might attach the publisher object to the request state or return it
#         # For simplicity, we might just return a representation or confirm the role.
#         print(f"Authenticated as Publisher: {publisher.external_id}")
#         # return publisher # If your endpoint expects a Publisher model
#         pass # Placeholder
        
#     # Example: Try to find a subscriber linked to this token
#     subscriber = crud.subscriber.get_by_external_id(db, external_id=user_identifier) # Or use ext_subscriber_id claim
#     if subscriber and subscriber.is_active:
#         print(f"Authenticated as Subscriber: {subscriber.external_id}")
#         # return subscriber # If your endpoint expects a Subscriber model
#         pass # Placeholder

#     # If no specific role found, or if just a generic user concept exists:
#     # user = crud.user.get(db, id=token_data.user_id) # If mapping sub to internal user ID
#     # if not user or not user.is_active:
#     #     raise HTTPException(status_code=400, detail="Inactive user")
#     # return user

#     # For pseudocode, let's assume we return the validated payload
#     # The endpoint logic will use claims from this payload.
#     return token_payload # Modify return type based on actual needs

# # --- Simple Permission Checks (Example) --- #
# # These could be used within API endpoints after getting the current user/payload

# def can_publisher_write(token_payload: schemas.TokenPayload, target_publisher_id: str) -> bool:
#     """Check if the token allows writing for the target publisher."""
#     # Logic: Check if token has write scope AND if the token's associated publisher ID
#     # (e.g., from a custom claim `ext_publisher_id`) matches `target_publisher_id`.
#     has_scope = settings.SCOPE_PUBLISHER_WRITE in token_payload.scope.split()
#     matches_publisher = token_payload.ext_publisher_id == target_publisher_id # Assuming custom claim
#     return has_scope and matches_publisher

# def can_subscriber_read(token_payload: schemas.TokenPayload, db: Session, target_publisher_id: Optional[str] = None) -> bool:
#     """Check if the token allows reading data, optionally for a specific publisher."""
#     has_scope = settings.SCOPE_SUBSCRIBER_READ in token_payload.scope.split()
#     if not has_scope:
#         return False

#     # Find the subscriber associated with the token
#     subscriber = crud.subscriber.get_by_external_id(db, external_id=token_payload.sub) # Or ext_subscriber_id
#     if not subscriber or not subscriber.is_active:
#         return False # No valid subscriber found for this token

#     if target_publisher_id:
#         # Check if this subscriber has an active subscription to the target publisher
#         target_publisher = crud.publisher.get_by_external_id(db, external_id=target_publisher_id)
#         if not target_publisher:
#             return False # Target publisher doesn't exist
#         subscription = crud.subscription.get_by_publisher_subscriber(
#             db, publisher_id=target_publisher.id, subscriber_id=subscriber.id
#         )
#         return subscription is not None and subscription.is_active
#     else:
#         # If no specific publisher is requested, just check if they have the read scope
#         # (and are a valid subscriber, checked above)
#         return True 