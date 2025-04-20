from fastapi import FastAPI, HTTPException, Header, status, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from typing import List, Optional, Dict, Any
from pydantic import BaseModel

# Import shared components
# import common # No longer needed directly
from .common import (
    publishers, subscribers, subscriptions, transactions,
    ADMIN_TOKEN, verify_admin_token # Import admin token and verification
)

app = FastAPI(title="PMDC Admin Demo")

templates = Jinja2Templates(directory="demo/templates")

# --- Dependency for Admin Authentication ---
async def verify_admin_access(x_admin_token: Optional[str] = Header(None)):
    if not x_admin_token or not verify_admin_token(x_admin_token):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin token is missing or invalid")
    return True # Indicate success

# --- Admin Endpoints ---

@app.get("/", response_class=HTMLResponse)
async def admin_root(request: Request):
    """Serves the admin demo HTML page."""
    # Pass necessary data to the template
    # Note: In a real app, avoid passing raw tokens to the frontend if possible
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "publishers": publishers,
        "subscribers": subscribers,
        "subscriptions": subscriptions,
        "transactions": transactions,
        "admin_token_for_ui": ADMIN_TOKEN # Provide token for UI testing convenience
    })

# --- Read Operations (View Data) ---

@app.get("/admin/publishers", dependencies=[Depends(verify_admin_access)])
async def get_publishers():
    """Admin endpoint to view all publishers."""
    return publishers

@app.get("/admin/subscribers", dependencies=[Depends(verify_admin_access)])
async def get_subscribers():
    """Admin endpoint to view all subscribers."""
    return subscribers

@app.get("/admin/subscriptions", dependencies=[Depends(verify_admin_access)])
async def get_subscriptions():
    """Admin endpoint to view all subscription authorizations."""
    return subscriptions

@app.get("/admin/transactions", dependencies=[Depends(verify_admin_access)])
async def get_transactions():
    """Admin endpoint to view all stored canonical transactions."""
    return transactions

# --- Management Operations (Modify Data - Simplified for Demo) ---

# Model for updating subscriptions
class SubscriptionUpdate(BaseModel):
    subscriber_ids: List[str]

@app.put("/admin/subscriptions/{publisher_id}", dependencies=[Depends(verify_admin_access)])
async def update_publisher_subscriptions(
    publisher_id: str,
    update_data: SubscriptionUpdate
):
    """Admin endpoint to set the list of authorized subscribers for a publisher."""
    if publisher_id not in publishers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Publisher '{publisher_id}' not found")

    # Validate that all provided subscriber IDs exist
    valid_subscribers = set(subscribers.keys())
    for sub_id in update_data.subscriber_ids:
        if sub_id not in valid_subscribers:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Subscriber '{sub_id}' not found")

    # Update the subscriptions (overwrite existing list for this publisher)
    subscriptions[publisher_id] = update_data.subscriber_ids
    return {"message": f"Subscriptions for publisher '{publisher_id}' updated successfully", "new_subscriptions": subscriptions[publisher_id]}

# TODO: Add endpoints for adding/removing publishers/subscribers if needed for the demo
# TODO: Add endpoints related to schema translation management if needed

# --- Run Instructions (for local development) ---
# In your terminal in the 'demo' directory:
# 1. Ensure virtual environment is active and requirements installed (pip install -r requirements.txt)
# 2. Run this server: uvicorn admin_demo:app --reload --port 8003
# 3. Access the Admin Demo UI at http://localhost:8003/
# 4. Access the API docs (Swagger UI) at http://localhost:8003/docs
# 5. Remember to include the header 'X-Admin-Token: admin_secret_token' for protected endpoints. 