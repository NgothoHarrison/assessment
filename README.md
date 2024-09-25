# Savannah API

Welcome to the Savannah API! This RESTful API is designed to manage customer and order data, providing authentication, user profiles, and SMS notifications. 

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Database Setup](#database-setup)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Customers](#customers)
  - [Orders](#orders)
- [Sending SMS Notifications](#sending-sms-notifications)
- [Testing](#testing)
- [Continuous Integration and Deployment](#continuous-integration-and-deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication using OpenID Connect and Django Allauth.
- Customers can create and update their profiles.
- Orders can be created, viewed, updated, and deleted by customers.
- Admin users can manage all customers and orders.
- SMS notifications sent upon order creation.

## Technologies Used

- Django
- Django REST Framework
- Django Allauth
- PostgreSQL (or any other database of your choice)
- Africa’s Talking API for SMS
- Python
- Docker (optional for containerization)

## Getting Started

### Prerequisites

- Python 3.x
- pip
- PostgreSQL or any preferred database
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/savannah-api.git
   cd savannah-api
