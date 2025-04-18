"""
Pydantic schema representing the default JSON output format for subscribers.

This is used to structure data retrieved from the canonical database
before sending it back in the /delivery API response.
"""

# from pydantic import BaseModel, Field
# from datetime import datetime
# from decimal import Decimal
# from typing import Optional

# class DefaultJsonTransaction(BaseModel):
#     """Defines the structure of a single transaction record in the default JSON output."""
#     # Fields derived from the Canonical Schema, but potentially renamed or formatted.
#     record_id: int = Field(..., description="Internal PMDC ID for the data record")
#     publisher_identifier: str = Field(..., description="External ID of the originating publisher")
#     transaction_kind: str = Field(..., alias="type", description="Type of transaction (e.g., CAPITAL_CALL)")
#     effective_date: str = Field(..., alias="date", description="Effective date of the transaction (YYYY-MM-DD)")
#     transaction_amount: Decimal = Field(..., alias="value", description="Amount of the transaction")
#     currency: str = Field(..., description="ISO 4217 currency code")
    
#     # Optional fields might be included based on availability in canonical record
#     fund_ref: Optional[str] = Field(None, description="Fund identifier, if available")
#     investor_ref: Optional[str] = Field(None, description="Investor identifier, if available")
#     notice_ref: Optional[str] = Field(None, description="Source notice identifier, if available")

#     # Timestamp of when PMDC processed the record
#     processed_at: datetime = Field(..., description="Timestamp when the record was processed by PMDC")

# # The API endpoint (`/delivery`) will likely return a List[DefaultJsonTransaction] 