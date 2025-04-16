# Data Ingestion Tool (ClickHouse to Flat File and Flat File to ClickHouse)

## Overview
This web-based application allows bidirectional data ingestion between ClickHouse and flat files (CSV). It supports both ClickHouse to flat file and flat file to ClickHouse ingestion, with JWT token authentication for ClickHouse.

## Features
- **Bidirectional Data Flow**:
  - ClickHouse → Flat File (CSV)
  - Flat File (CSV) → ClickHouse
- **ClickHouse Authentication**: JWT token-based authentication
- **Column Selection**: Select specific columns for data ingestion
- **Error Handling**: Provides meaningful error messages for connection/authentication/file issues
- **Progress Reporting** (Optional): Displays progress during the data ingestion process
- **Testing**: Example test cases for ClickHouse and Flat File operations

## Requirements
- Python 3.x
- Django 3.x or above
- ClickHouse instance (local or cloud)
- ClickHouse Python client library (`clickhouse-driver`)

