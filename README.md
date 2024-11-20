# ServiceDesk Project

## Overview
This project implements a ServiceDesk system for managing user requests. Users can send messages, and support operators can manage these requests through an API.

## Features
- User workflow with email notifications for new requests, responses, and closures.
- API for request management:
  - List requests with filtering and sorting options.
  - Assign requests to operators.
  - Exchange messages via the API.
  - Close requests.
- Uses Django, DRF, and PostgreSQL.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Documentation**: Swagger (via drf-yasg)
- **Testing**: Django Test Framework

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL installed and running

### Steps
1. Clone the repository.
   ```bash
   git clone <repository-url>
   cd ServiceDeskProject
