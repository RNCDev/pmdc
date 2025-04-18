"""
SQLAlchemy model for the canonical data records (Capital Calls / Distributions).
"""

# from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey, JSON
# from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import JSONB # Use JSONB for better indexing in Postgres
# from .base import TimestampedBase # Or just Base

# class DataRecord(TimestampedBase): # Or just Base
#     __tablename__ = "data_records"

#     # id (from Base)
#     # created_at (from Base) - Represents when the record was created in *our* system
#     # updated_at (from Base)

#     # --- Core Canonical Fields --- #
#     # Based on common elements for Capital Calls/Distributions.
#     # This needs careful definition based on ILPA standards or target commonality.

#     transaction_type = Column(String, index=True, nullable=False) # e.g., "CAPITAL_CALL", "DISTRIBUTION"
#     transaction_date = Column(DateTime(timezone=True), index=True, nullable=False) # Effective date from source
#     amount = Column(Numeric(precision=18, scale=4), nullable=False) # High precision for currency
#     currency = Column(String(3), nullable=False, default="USD") # ISO 4217 currency code

#     # Optional common fields?
#     fund_identifier = Column(String, index=True, nullable=True) # Identifier for the fund
#     investor_identifier = Column(String, index=True, nullable=True) # Identifier for the LP receiving/paying
#     notice_identifier = Column(String, index=True, nullable=True) # Unique ID from the source notice PDF/data

#     # --- Foreign Key References --- #

#     publisher_id = Column(Integer, ForeignKey("publishers.id"), nullable=False, index=True)
#     # Relationship back to Publisher (Many-to-One: Many Data Records -> One Publisher)
#     # publisher = relationship("Publisher", back_populates="data_records")

#     # --- Audit / Provenance --- #

#     # Identifier of the original source schema used during intake
#     source_schema_identifier = Column(String, nullable=True) 

#     # Store the original payload received from the publisher (optional, for audit)
#     # Consider storage implications. JSONB is efficient in Postgres.
#     # original_publisher_payload = Column(JSONB, nullable=True)

#     # Store the data received from the SaaS provider (optional, for audit)
#     # original_saas_payload = Column(JSONB, nullable=True)

#     # --- Processing Status --- #
#     # status = Column(String, index=True, nullable=False, default="PROCESSED") # e.g., RECEIVED, PROCESSING, FAILED, PROCESSED
#     # processing_error = Column(String, nullable=True) # Store error message if status is FAILED

#     # Relationship to Audit Log (One-to-Many)
#     # audit_logs = relationship("AuditLog", back_populates="data_record")

#     def __repr__(self):
#         return f"<DataRecord(id={self.id}, type=	\'{self.transaction_type}	\")>" 