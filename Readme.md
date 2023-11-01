# Restaurant Monitoring System

The Restaurant Monitoring System is a backend application that helps restaurant owners track the online/offline status of their stores during business hours. This system generates reports containing information about uptime and downtime for specified time intervals.

## Table of Contents
- [System Overview](#system-overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## System Overview

The Restaurant Monitoring System is designed to monitor and report on the operational status of multiple restaurants. It consists of the following components:

- A PostgreSQL database to store historical store status data and generated reports.
- A Flask-based web application that provides APIs for report generation and retrieval.
- A report generation module to compute uptime and downtime based on historical data.
- Automatic report generation at hourly intervals for all stores.

## Features

- Dynamic report generation based on the latest data.
- Automatic report generation and database updates every hour.
- RESTful API for triggering report generation and retrieving reports.
- Customizable time intervals for report generation.

## Setup

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/ChetanP07/store_monitoring

pip install flask psycopg2

python app.py
