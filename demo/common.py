from pydantic import BaseModel
from typing import Dict, List, Optional, Any

# --- In-Memory Data Stores (Simulating Databases) ---

publishers: Dict[str, Dict[str, Any]] = {
    "pub1": {"name": "Publisher One", "token": "pub_token_123"},
    "pub2": {"name": "Publisher Two", "token": "pub_token_456"}
}

subscribers: Dict[str, Dict[str, Any]] = {
    "sub1": {"name": "Subscriber One", "token": "sub_token_abc"},
    "sub2": {"name": "Subscriber Two", "token": "sub_token_def"}
}

# Defines which subscribers are authorized by which publisher
subscriptions: Dict[str, List[str]] = {
    "pub1": ["sub1", "sub2"], # Publisher 1 authorizes Subscriber 1 and 2
    "pub2": ["sub1"]          # Publisher 2 authorizes only Subscriber 1
}

# Store transactions in canonical format
transactions: Dict[str, Dict[str, Any]] = {}
transaction_counter = 1

# --- Admin Configuration (Example) ---
ADMIN_TOKEN = "admin_secret_token" # Simple shared secret for demo admin access

# --- Pydantic Models ---

# Example: Publisher's format might be flat
class PublisherCapitalCall(BaseModel):
    transaction_id: str # ID from the publisher's system
    total_amount: float
    investment_amount: float
    investment_target: str
    fee_amount: float
    fee_description: str = "Management Fee"

# Example: Canonical format might be more structured
class CanonicalCapitalCall(BaseModel):
    pmdc_transaction_id: str
    publisher_id: str
    total_amount: float
    components: List[Dict[str, Any]] # e.g., [{'type': 'investment', 'target': 'ABC', 'amount': 1.8M}, {'type': 'fee', 'description': 'Mgmt Fee', 'amount': 0.2M}]

# Example: Subscriber might want specific fields
class SubscriberCapitalCallView(BaseModel):
    source_publisher: str
    call_id: str # Could be the pmdc_transaction_id
    total: float
    details: str # e.g., "Investment in ABC ($1.8M), Fees ($0.2M)"


# --- Helper Functions ---

def get_publisher_id_from_token(token: str) -> Optional[str]:
    for pub_id, data in publishers.items():
        if data.get("token") == token:
            return pub_id
    return None

def verify_subscriber_token(subscriber_id: str, token: str) -> bool:
    return subscriber_id in subscribers and subscribers[subscriber_id].get("token") == token

def is_subscriber_authorized(publisher_id: str, subscriber_id: str) -> bool:
    return publisher_id in subscriptions and subscriber_id in subscriptions.get(publisher_id, [])

def verify_admin_token(token: str) -> bool:
    return token == ADMIN_TOKEN

# --- Translation Logic ---
# These remain basic simulations for the demo

def translate_publisher_to_canonical(publisher_data: PublisherCapitalCall, pmdc_tx_id: str, publisher_id: str) -> CanonicalCapitalCall:
    components = []
    if publisher_data.investment_amount > 0:
        components.append({
            "type": "investment",
            "target": publisher_data.investment_target,
            "amount": publisher_data.investment_amount
        })
    if publisher_data.fee_amount > 0:
        components.append({
            "type": "fee",
            "description": publisher_data.fee_description,
            "amount": publisher_data.fee_amount
        })
    return CanonicalCapitalCall(
        pmdc_transaction_id=pmdc_tx_id,
        publisher_id=publisher_id,
        total_amount=publisher_data.total_amount,
        components=components
    )

def translate_canonical_to_subscriber(canonical_data: CanonicalCapitalCall) -> SubscriberCapitalCallView:
    detail_parts = []
    publisher_name = publishers.get(canonical_data.publisher_id, {}).get("name", "Unknown Publisher")
    for comp in canonical_data.components:
        amount_m = comp.get('amount', 0) / 1_000_000
        if comp.get("type") == "investment":
            detail_parts.append(f"Investment in {comp.get('target', 'N/A')} (${amount_m:.1f}M)")
        elif comp.get("type") == "fee":
             detail_parts.append(f"{comp.get('description', 'Fee')} (${amount_m:.1f}M)")
    details_str = ", ".join(detail_parts)

    return SubscriberCapitalCallView(
        source_publisher=publisher_name,
        call_id=canonical_data.pmdc_transaction_id,
        total=canonical_data.total_amount,
        details=details_str
    ) 