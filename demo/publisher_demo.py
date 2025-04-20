from fastapi import FastAPI, HTTPException, Header, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

# Import shared components
from common import (
    publishers, subscriptions, transactions, transaction_counter,
    PublisherCapitalCall, CanonicalCapitalCall,
    get_publisher_id_from_token, translate_publisher_to_canonical
)

app = FastAPI(title="PMDC Publisher Demo")

templates = Jinja2Templates(directory="templates")

# --- Publisher Endpoints ---

@app.get("/", response_class=HTMLResponse)
async def publisher_root(request: Request):
    """Serves the publisher demo HTML page."""
    # In a real UI, you might pass publisher-specific data
    return templates.TemplateResponse("publisher.html", {"request": request, "publishers": publishers})

@app.post("/publish", status_code=status.HTTP_201_CREATED)
async def publish_transaction(
    payload: PublisherCapitalCall,
    x_publisher_token: Optional[str] = Header(None)
):
    """Receives a transaction from a publisher, translates it, and stores it."""
    global transaction_counter # Use the global counter from common

    if not x_publisher_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Publisher token missing")

    publisher_id = get_publisher_id_from_token(x_publisher_token)
    if not publisher_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid publisher token")

    # Simulate processing
    pmdc_tx_id = f"pmdc_tx_{transaction_counter:04d}"
    canonical_data = translate_publisher_to_canonical(payload, pmdc_tx_id, publisher_id)

    # Store the transaction (in-memory, shared via common)
    transactions[pmdc_tx_id] = canonical_data.model_dump() # Store as dict
    common.transaction_counter += 1 # Ensure we increment the counter in common

    return {
        "message": "Transaction received and processed by Publisher Demo",
        "pmdc_transaction_id": pmdc_tx_id,
        "canonical_data": canonical_data
    }


@app.get("/publisher/{publisher_id}/authorized_subscribers")
async def get_authorized_subscribers(
    publisher_id: str,
    x_publisher_token: Optional[str] = Header(None)
):
    """Allows a publisher to see which subscribers are authorized for them."""
    if not x_publisher_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Publisher token missing")

    requesting_publisher_id = get_publisher_id_from_token(x_publisher_token)
    if not requesting_publisher_id or requesting_publisher_id != publisher_id:
        # Ensure the requesting publisher matches the ID in the path and token is valid
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or mismatched publisher token")

    return {"publisher_id": publisher_id, "authorized_subscribers": subscriptions.get(publisher_id, [])}

# --- Run Instructions (for local development) ---
# In your terminal in the 'demo' directory:
# 1. Ensure virtual environment is active and requirements installed (pip install -r requirements.txt)
# 2. Run this server: uvicorn publisher_demo:app --reload --port 8001
# 3. Access the Publisher Demo UI at http://localhost:8001/
# 4. Access the API docs (Swagger UI) at http://localhost:8001/docs 