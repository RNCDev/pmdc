# Private Markets Data Cooperative (PMDC) - Data Exchange Platform
# v. 0.1.0

## 1. Executive Summary

*   **Cooperative:** Private Markets Data Cooperative (PMDC)
*   **Mission:** To fundamentally change and improve private markets fund administration by providing a seamless, secure, and efficient platform for managing capital calls, distributions, capital accounts and basic SOI data. We hope to eliminate eliminating the pain points working with PDFs as the fundamental unit of operations in the private equity market.

## 2. Core Principles

*   **Efficiency:** Streamlining fund administration processes.
*   **Accuracy:** Uncompromising commitment to data integrity and precision.
*   **Security:** Protecting sensitive financial data with robust security measures.
*   **Innovation:** Continuously improving the platform and adapting to evolving industry needs.

## 3. Market Analysis

*   **Market Size & Opportunity:** ~60 M transactions annually at capacity.
*   **Target Market Segmentation:**
    *   General Partners (GP): Manage vehicles that consume capital.
    *   GP Agents: Service providers to GPs that help manage fund accounting and operations.
    *   Limited Partners (LP): May manage vehicles or invest directly with GPs; providers of capital.
    *   LP Agents: Service providers to LPs that help manage portfolio accounting and operations.

## 4. Products and Services

*   **Key Features (MVP - Phase 1):**
    *   **GP Data Push API:** Secure API for GPs to upload capital call and distribution data in their original format.
    *   **Authentication and Authorization:** Robust security mechanisms (OAuth 2.0/OIDC) to control access.
    *   **Data Validation:** Checks to ensure data integrity before sending to the SaaS provider.
    *   **SaaS Integration:** Seamless integration with the chosen SaaS provider (Matterbeam/Lume/Nexla) for schema translation.
    *   **Error Handling:** Comprehensive error handling and reporting for API interactions and SaaS communication.
    *   **Retry Mechanisms:** Automated retries for temporary SaaS API failures.
    *   **Rate Limit Handling:** Compliance with SaaS provider's rate limits.
    *   **LP Data Pull API:** Secure API for LPs to retrieve standardized capital call and distribution data.
    *   **Authentication and Authorization:** Secure access control for LPs.
    *   **Data Retrieval:** Efficient retrieval of data from the canonical database.
    *   **Canonical Database:** Centralized PostgreSQL database storing data in a standardized format.
*   **User Interface (Future Phases):** A user-friendly dashboard for GPs and LPs to manage data, track status, and audit data flows.
*   **SaaS Provider Integration:**
    *   **Choice:** Prioritizing selection between Matterbeam, Lume, and Nexla within the first two weeks based on a detailed comparison matrix (technical capabilities, security, pricing, long-term viability).
    *   **Integration Details:** The platform will handle sending data to the SaaS provider, receiving the translated data, mapping it to the canonical schema, and storing it.
*   **Technology Stack:**
    *   **Programming Languages:** Python
    *   **Frameworks:** FastAPI
    *   **Database:** PostgreSQL (managed via SQLAlchemy and Alembic for migrations)
    *   **Authentication:** OAuth 2.0 / OIDC (likely via a managed Identity Provider like Auth0, Okta, Azure AD B2C)
    *   **Cloud Provider:** [To Be Determined - e.g., AWS, Azure, GCP]
    *   **API Gateway:** [To Be Determined - or leverage FastAPI/Cloud Provider features]
    *   **Monitoring Tools:** [To Be Determined - e.g., Prometheus, Grafana, DataDog, CloudWatch/Azure Monitor]

## 5. Operations Plan

*   **Development Process:**
    *   Agile Methodology: Scrum with two-week sprints.
    *   Version Control: Git (e.g., GitHub).
    *   CI/CD: Continuous Integration and Continuous Deployment pipeline (e.g., GitHub Actions, GitLab CI, Jenkins).
    *   Testing: Unit (pytest), Integration, End-to-End tests, Security, Performance tests.
*   **Customer Support:**
    *   Channels: Email, phone, online chat, knowledge base.
    *   SLAs: Defined response/resolution times.
    *   Onboarding: Comprehensive materials and training.
*   **Data Security and Compliance:**
    *   Data Encryption: In transit (TLS) and at rest.
    *   Access Control: Role-based access control (RBAC) tied to OAuth scopes and internal permissions.
    *   Compliance: Adherence to relevant regulations (e.g., GDPR, CCPA); SOC 2 considerations.
    *   Regular Security Audits & Penetration Testing.
    *   SaaS Provider Security Vetting.
    *   Data Backup and Recovery Plan.

## 6. Management Team (Illustrative Tech Roles)

*   **Technical Lead:** Responsible for overall technical architecture, development, team leadership.
*   **Backend Engineer:** Focus on SaaS integration, API development, data pipeline orchestration, data validation.
*   **Database Engineer:** Design, implementation, optimization of the canonical PostgreSQL database.
*   **DevOps Engineer:** Cloud infrastructure management (IaC - Terraform/Pulumi), CI/CD, monitoring, security operations.
*   **Security Lead (Part-time):** Oversees security aspects, including SaaS integration and compliance.

## 7. Financial Plan

*   **Funding Request:** $250,000
*   **Use of Funds:** Team Salaries, Cloud Infrastructure, Software Licenses & Tools, SaaS Subscription Fees (CRITICAL), Legal & Administrative.
*   **Financial Projections:** Aim for break-even sustainability supported by producers and consumers.

## 8. Build Plan: Phase 1 - Three-Month Plan (SaaS Schema Translation)

*   **Week 1: Project Kick-off & Initial Setup**
    *   Activities: Onboarding, requirements refinement, high-level architecture (SaaS focus), initial cloud setup, canonical DB schema draft (leverage ILPA Core?), initial SaaS provider research.
    *   Deliverables: Project plan, architecture doc, basic cloud infra, DB schema draft, SaaS comparison doc (initial).
*   **Week 2: SaaS Provider Deep Dive & Selection**
    *   Activities: Deep dive into Matterbeam/Lume/Nexla APIs/SDKs, POC integrations, security evaluations, final provider selection, integration layer design kickoff. (Requires sample data from GenII, Juniper Square, Aduro, Standish, Leverpoint, Franklin Park, Cendana, Mercer).
    *   Deliverables: Detailed SaaS comparison matrix, selected provider justification, integration architecture design.
*   **Week 3-6: GP Data Push API & SaaS Integration (Capital Calls & Distributions)**
    *   Activities: Develop GP Push API (spec, auth skeleton), implement DB schema, implement SaaS integration (send original, receive translated, map to canonical, store), handle SaaS API errors, security review (SaaS comms), setup dev deployment pipeline.
    *   Deliverables: Functional GP Push API (SaaS integrated), SaaS integration layer, data validation (post-translation), API deployed to dev.
*   **Week 7-8: LP Data Pull API (Both Data Types) & End-to-End Testing**
    *   Activities: Develop LP Pull API (retrieve from canonical DB), optimize DB queries, integrate Distributions end-to-end (Push -> SaaS -> CanonDB -> SaaS -> Pull), comprehensive E2E testing (including SaaS steps/errors), enhance CI/CD.
    *   Deliverables: Functional LP Pull API, demonstrated E2E flow, improved test suite, basic API monitoring (including SaaS interactions).
*   **Week 9-10: Integration Refinement & Robustness**
    *   Activities: Refine SaaS integration (error handling, retries, rate limits), optimize data flow, enhance validation (post-translation), improve logging (incl. SaaS logs), implement basic data quality checks, security code review (SaaS focus).
    *   Deliverables: Robust SaaS integration, enhanced validation/quality checks, improved logging, security review report.
*   **Week 11: Security Hardening & Pre-Production Environment**
    *   Activities: Setup pre-prod env, implement security configs (secure SaaS keys), security testing (focus on SaaS integration points), address findings, performance testing.
    *   Deliverables: Secured pre-prod env (SaaS integrated), security test report, hardening measures implemented, performance test results, finalized pre-prod deployment pipeline.
*   **Week 12: Final Testing, Documentation, MVP Release & Review**
    *   Activities: Final testing (functional, integration, security, performance) including SaaS scenarios, bug fixing, API documentation prep, MVP release notes, deploy MVP to production, setup prod monitoring (incl. SaaS), team retrospective, assess SaaS provider performance/costs.
    *   Deliverables: MVP Release (SaaS Integrated), API documentation, release notes, production env deployed/monitored.

## 9. Project Status (As of [Current Date])

*   **Scaffolding:**
    *   Backend folder structure created (`app/`, `tests/`, `scripts/`, `alembic/`).
    *   Pseudocode generated for core backend components:
        *   API Endpoints (`intake`, `delivery`)
        *   Services (`intake`, `delivery`, `translation`, `saas_integration`)
        *   Database Models (`base`, `publisher`, `subscriber`, `subscription`, `data_record`)
        *   Pydantic Schemas (`base`, `canonical`, `publisher_in`, `subscriber_out`)
        *   CRUD Operations (`base`, `data_record`, `subscription`, `publisher`, `subscriber`)
        *   Core Configuration (`config.py`)
        *   Security Helpers (`security.py`)
    *   `docker-compose.yml` created for local PostgreSQL and Redis.
    *   `.env.example` created for environment variable configuration.
*   **Next Steps:**
    *   Set up Alembic for database migrations.
    *   Generate initial `requirements.txt`.
    *   Begin implementing Python code based on pseudocode.
    *   Develop the fake data demo (see TODO below).

## 10. TODO: Fake Data Demo Requirements

Develop a small, clickable web interface demonstration using consistent, fake data to illustrate the core information flow. This demo should showcase:

*   **Onboarding:**
    *   Simulated onboarding process for a new Publisher.
    *   Simulated onboarding process for a new Subscriber.
    *   Admin Interface Mockup: Simple view for an admin to approve/manage publishers and subscribers.
*   **Connecting Publisher & Subscriber:**
    *   Admin Interface Mockup: View for an admin to establish an active subscription link between a specific publisher and subscriber.
*   **Data Flow:**
    *   Publisher View: Ability to simulate publishing a transaction (e.g., a capital call) via a simple form.
    *   System View (Conceptual): Visualization of the transaction being processed:
        *   Received at Intake API.
        *   (Simulated) Sent to SaaS for translation.
        *   (Simulated) Received back from SaaS.
        *   Stored in the Canonical Database.
        *   Schema/Translation Visualization: Show examples of the data format at each stage (Publisher -> Canonical -> Subscriber).
    *   Subscriber View: Ability to view data received from subscribed publishers.
*   **History/Audit:**
    *   Publisher DMZ View: A history list showing transactions published by the selected publisher.
    *   Subscriber DMZ View: A history list showing transactions received by the selected subscriber from their subscriptions.
    *   Audit Log View: Simplified view tracing a single transaction's key steps through the system.
*   **Error Simulation:**
    *   Demonstrate how the UI might indicate a processing error for a transaction (e.g., simulated SaaS failure).

# PMDC Demo Application

This directory contains a demonstration application showcasing a potential Private Market Data Controller (PMDC) concept using FastAPI.

## Overview

The demo simulates the interactions between different roles in a data exchange:

*   **Publishers:** Entities that submit data (e.g., capital call notices) in their own format.
*   **Subscribers:** Entities that retrieve data, translated into a format suitable for them.
*   **Admin:** A central role for managing the system, viewing data, and controlling access rights.

To provide a clear demonstration for each role, the demo is split into three separate FastAPI applications:

1.  `demo/publisher_demo.py`: Simulates the publisher's perspective, allowing them to submit transactions.
2.  `demo/subscriber_demo.py`: Simulates the subscriber's perspective, allowing them to fetch authorized and translated data.
3.  `demo/admin_demo.py`: Simulates the admin's perspective, allowing viewing of all data and management of subscriber authorizations.

Shared data models, in-memory data stores (simulating databases), and helper functions are located in `demo/common.py`.

Basic HTML frontends for interacting with each demo are provided in the `demo/templates/` directory.

## Prerequisites

*   Python 3.7+
*   pip (Python package installer)
*   Virtual environment tool (optional but recommended)

## Setup

1.  **Clone the repository (if you haven't already).**

2.  **Navigate to the workspace root directory.**

3.  **Create and activate a virtual environment (recommended):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install the required Python packages:**
    ```bash
    pip install -r demo/requirements.txt
    ```

## Running the Demos

Each demo application runs as a separate web server on a different port. You can run them simultaneously in separate terminals.

**Make sure your virtual environment is activated before running these commands.** Navigate to the workspace root directory if you aren't already there.

1.  **Run the Publisher Demo:**
    ```bash
    uvicorn demo.publisher_demo:app --reload --port 8001
    ```
    *   Access the UI: [http://localhost:8001/](http://localhost:8001/)
    *   Access the API Docs (Swagger): [http://localhost:8001/docs](http://localhost:8001/docs)

2.  **Run the Subscriber Demo:**
    ```bash
    uvicorn demo.subscriber_demo:app --reload --port 8002
    ```
    *   Access the UI: [http://localhost:8002/](http://localhost:8002/)
    *   Access the API Docs (Swagger): [http://localhost:8002/docs](http://localhost:8002/docs)

3.  **Run the Admin Demo:**
    ```bash
    uvicorn demo.admin_demo:app --reload --port 8003
    ```
    *   Access the UI: [http://localhost:8003/](http://localhost:8003/)
    *   Access the API Docs (Swagger): [http://localhost:8003/docs](http://localhost:8003/docs)
    *   **Note:** Admin API endpoints require an `X-Admin-Token` header with the value `admin_secret_token`. The admin UI provides an input field for this.

## How to Use the Demo

1.  Start all three servers.
2.  Open the **Publisher Demo** (`localhost:8001`). Select a publisher and submit a transaction.
3.  Open the **Admin Demo** (`localhost:8003`). Observe the submitted transaction in the "Stored Transactions" section. Use the admin interface (providing the token `admin_secret_token`) to manage which subscribers are authorized for each publisher.
4.  Open the **Subscriber Demo** (`localhost:8002`). Select a subscriber and enter their corresponding token (e.g., `sub_token_abc` for Subscriber One). Fetch data to see the translated transactions they are authorized to view based on the admin settings.