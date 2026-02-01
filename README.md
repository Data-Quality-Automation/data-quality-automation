# Data Quality Automation – Fund Valuation Pipelines

## Overview
This project implements an automated data quality testing framework for fund valuation data pipelines.  
The objective is to validate **financial calculation correctness**, **data completeness across pipeline layers**, and **core business rule compliance** using automated, data-driven tests with CI/CD execution.

The framework is intentionally lightweight, maintainable, and aligned with real-world data QA practices in banking and investment management systems.

---

## Pipeline Context

Data flows through multiple transformation layers before being consumed by reporting and downstream systems.  
This framework validates data integrity and correctness at each stage.

---

## Scope

### In Scope
- Validation of derived metrics (AUM) for:
  - Daily
  - Monthly (MTD)
  - Year-to-Date (YTD)
  - Yearly
- Data completeness checks across Landing, Mart, and Final layers
- Detection of missing funds between pipeline layers
- Deduplication rule validation
- ID transformation and normalization checks
- Core data quality rules (NULLs, ranges, invalid values)
- Data-driven testing using synthetic and production-like datasets
- Regression execution via CI/CD with automated reporting

### Out of Scope
- Real-time or streaming pipelines
- Performance and load testing
- UI or regulatory reporting logic

---

## Test Architecture

The framework is organized into layered tests:

- **Unit Tests**
  - Validate financial calculation logic (AUM) using Pandas
- **Integration Tests**
  - Validate data movement across pipeline layers
- **Reconciliation Tests**
  - Compare record counts and key metrics between layers using SQL
- **Data Quality Tests**
  - Enforce business rules and data constraints

---

## Technology Stack

- Test Framework: pytest  
- Data Processing: Python (Pandas)  
- Data Validation: SQL (RDBMS-based checks)  
- Storage: SQLite (used for exercise; easily replaceable with Snowflake/BigQuery)  
- CI/CD Orchestration: Jenkins  
- Reporting: pytest-html  

---

## Data-Driven Testing Approach
Expected results for AUM calculations are externalized into CSV files.  
Tests dynamically read input data and expected outcomes, enabling:

- Validation across multiple funds and periods
- Easy extension without code changes
- Clear traceability between test inputs and results

Configurable tolerances are applied to handle rounding differences.

---

## Business Rules Implemented
- **AUM Calculation**: Units × NAV × FX Rate
- FX rate must be greater than zero
- NAV must be positive and non-null
- Units cannot be negative
- Duplicate records (same fund and trade date) are removed in the mart layer
- Fund IDs are normalized during transformation (e.g., prefix stripping)

---

## Edge Cases Covered
- Leap year dates (e.g., Feb 29)
- Missing trading days (weekends/holidays)
- Division by zero scenarios
- Rounding differences between systems
- Duplicate records from upstream providers

Synthetic datasets are designed to intentionally include these cases.

---

## Reconciliation Strategy
Reconciliation tests validate:
- Record counts across Landing → Mart → Final layers
- Presence of all expected funds in downstream layers
- Controlled reduction of records due to deduplication or filtering

Late-arriving data within the same batch window is allowed and handled gracefully.

---

## CI/CD Execution
The test suite is designed to run:
- On every deployment to test/stage environments
- On a scheduled (nightly) basis

Jenkins executes the tests and generates an HTML report.  
Any critical data quality failure results in a failed build, providing early feedback to data engineering teams.

---

## Assumptions
- MTD, YTD, and Yearly aggregations are simplified to summation for this exercise
- Minor rounding differences are acceptable within a defined tolerance
- SQLite is used as a lightweight demonstration database
- ID mappings are deterministic and rule-based

All assumptions are documented to ensure transparency of scope.

---

## Extensibility
The framework can be extended by:
- Adding new test cases via CSV files
- Introducing additional financial metrics
- Replacing the database with an enterprise data warehouse
- Integrating dbt or Great Expectations for additional validation layers

---
