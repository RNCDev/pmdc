from fastapi import FastAPI, HTTPException, Header, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List, Optional

# Import shared components
from .common import (
    publishers, subscribers, subscriptions, transactions,
    CanonicalCapitalCall, SubscriberCapitalCallView,
    verify_subscriber_token, is_subscriber_authorized, translate_canonical_to_subscriber
)

app = FastAPI(title="PMDC Subscriber Demo")

templates = Jinja2Templates(directory="demo/templates")

# --- Subscriber Endpoints ---

@app.get("/", response_class=HTMLResponse)
async def subscriber_root(request: Request):
    """Serves the subscriber demo HTML page."""
    # Pass subscriber list for UI selection
    return templates.TemplateResponse("subscriber.html", {"request": request, "subscribers": subscribers})

@app.get("/subscribe/{subscriber_id}", response_model=List[SubscriberCapitalCallView])
async def get_subscriber_data(
    subscriber_id: str,
    x_subscriber_token: Optional[str] = Header(None)
):
    """Provides translated transaction data to an authorized subscriber."""
    if not x_subscriber_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Subscriber token missing")

    if not verify_subscriber_token(subscriber_id, x_subscriber_token):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid subscriber token or ID")

    authorized_data = []
    # Iterate through a copy of items to avoid issues if transactions change during iteration
    for tx_id, tx_data_dict in list(transactions.items()):
        try:
            # Re-create model from dict for processing
            canonical_tx = CanonicalCapitalCall(**tx_data_dict)
            publisher_id = canonical_tx.publisher_id

            # Check if this subscriber is authorized by the transaction's publisher
            if is_subscriber_authorized(publisher_id, subscriber_id):
                subscriber_view = translate_canonical_to_subscriber(canonical_tx)
                authorized_data.append(subscriber_view)
        except Exception as e:
            # Log error for debugging, but don't fail the whole request
            print(f"Error processing transaction {tx_id} for subscriber {subscriber_id}: {e}")
            # Depending on requirements, might want to surface this differently
            pass

    return authorized_data

# --- Run Instructions (for local development) ---
# In your terminal in the 'demo' directory:
# 1. Ensure virtual environment is active and requirements installed (pip install -r requirements.txt)
# 2. Run this server: uvicorn subscriber_demo:app --reload --port 8002
# 3. Access the Subscriber Demo UI at http://localhost:8002/
# 4. Access the API docs (Swagger UI) at http://localhost:8002/docs 