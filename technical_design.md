Project Title: FTracker – Personal Budget & Financial Goals Tracker

Stack: FastAPI + Jinja2 (Server-Side Templates) + PostgreSQL
Author: Vrushabh
Date: 2025-07-25
Version: 1.0
1. Overview / Purpose

FTracker is a personal finance tracker web application built with FastAPI and Jinja2 to help users manage their budgets, track financial goals, and analyze spending patterns. It enables reporting, analysis, and future prediction of financial data.
2. Scope
✅ In-Scope

    Web-based application with server-rendered templates

    Transaction and category management

    Budget alerts and goal tracking

    Reports with visualizations

    Data import/export via CSV

    Sample data seeding

🚫 Out-of-Scope (v1)

    OAuth banking integration

    Mobile app

    Investment tracking

3. App Goals

    Report on finances clearly

    Analyze spending categories and trends

    Predict future expenses using simple visual projections

    Help improve and guide financial decisions

4. Features

    User-friendly web interface (Jinja2 templates)

    Real-time (on request) transaction display

    Custom categories and types

    Goal setting and progress tracking

    Budget alerts and reminders

    Import/export data via CSV

    Charts for weekly/monthly/yearly spending

    Sample data population script

5. System Architecture

[Browser]
   ↓
[Jinja2 Templates]
   ↓
[FastAPI Backend (MVC Pattern)]
   ↓
[PostgreSQL Database]

Technologies
Layer	Tech Stack
Backend	FastAPI (Python 3.11+)
Frontend	Jinja2 + Bootstrap
Database	PostgreSQL
ORM	SQLAlchemy / Tortoise
Charts	Chart.js
Auth	Session or JWT
File Import	Python csv, pandas
Deployment	Gunicorn + Nginx
6. Pages (Routes & Templates)
Page	Route	Template	Notes
Home	/	home.html	Show all transactions in bubbles with income/expense bar
Add Transaction	/transaction/add	transaction_form.html	Add form
Edit Transaction	/transaction/edit/{id}	transaction_form.html	Edit form
Delete Transaction (soft)	/transaction/delete/{id}	-	Set is_active=False
Inactive Transactions	/transactions/inactive	inactive_list.html	Manage deleted
Reports	/reports	reports.html	Weekly/monthly/yearly
Data Import/Export	/data	data.html	CSV import/export
Manage Categories	/categories	categories.html	Add/edit/delete
Manage Types	/types	types.html	Add/edit/delete
7. Database Schema (PostgreSQL)
transactions

id UUID PK
amount NUMERIC
type_id UUID FK
category_id UUID FK
date DATE
note TEXT
is_active BOOLEAN DEFAULT TRUE
created_at TIMESTAMP
updated_at TIMESTAMP

categories

id UUID PK
name TEXT
type TEXT CHECK (type IN ('Income', 'Expense', 'Savings', 'Investment', 'Other', 'Unknown', 'Timebound'))

transaction_types

id UUID PK
name TEXT

goals

id UUID PK
category_id UUID FK
target_amount NUMERIC
current_amount NUMERIC
due_date DATE
created_at TIMESTAMP

8. API Endpoints
Endpoint	Method	Description
/api/transactions	GET	List transactions
/api/transactions	POST	Create transaction
/api/transactions/{id}	PUT	Update transaction
/api/transactions/{id}	DELETE	Soft delete
/api/goals	GET/POST	Manage goals
/api/data/import	POST	Upload CSV
/api/data/export	GET	Download CSV
/api/reports/summary	GET	Summary by week/month/year
9. File Structure (Suggestion)

ftracker/
├── main.py
├── templates/
│   ├── home.html
│   ├── transaction_form.html
│   ├── reports.html
│   └── base.html
├── static/
│   ├── css/
│   └── js/
├── models/
│   └── models.py
├── routes/
│   ├── transactions.py
│   ├── reports.py
│   └── data.py
├── services/
│   └── goals.py
├── utils/
│   ├── importer.py
│   └── charts.py
├── tests/
└── alembic/ (if using migrations)

10. Sample Visual Features
💰 Home Page

    Bubble chart grouped by category

    Bar chart comparing income vs expenses

📊 Reports

    Pie charts for category breakdown

    Line charts for weekly/monthly/yearly trends

    Bar for profit/loss (future)

📥 Import/Export

    Drag & drop CSV upload

    Template download link

    Validation before import

11. Security

    Input validation using pydantic

    CSRF tokens in forms

    HTTPS in production

    User sessions or JWT for future multi-user support

12. Deployment Strategy

    Use Gunicorn + Nginx for serving FastAPI

    Dockerize with PostgreSQL and a volume for CSVs

    Static files served by Nginx

    Auto-backup PostgreSQL

13. Future Enhancements

    Add asset classes: stocks, gold, property, vehicles

    AI/ML module for predictive spending

    Monthly budget setting

    OAuth2 integration with banking APIs

    Mobile-friendly progressive web app

14. Development Plan (Milestones)
Phase	Features
Phase 1	Core CRUD, home page, import/export
Phase 2	Goals, alerts, report charts
Phase 3	Predictive features, sample data seeding
Phase 4	Asset management, multi-user, banking integration
