# OFM Operations Dashboard

## Table of Contents

- [Project Overview](#project-overview)
- [Project Objective](#project-objective)
- [Technology Stack](#technology-stack)
- [Data Architecture](#data-architecture)
- [Expected Google Sheet Columns](#expected-google-sheet-columns)
- [Data Loading Process](#data-loading-process)
- [Data Cleaning Process](#data-cleaning-process)
- [Dashboard Features](#dashboard-features)
- [Mathematical and Statistical Operations](#mathematical-and-statistical-operations)
- [Filtering System](#filtering-system)
- [Visualization System](#visualization-system)
- [Interactive Table](#interactive-table)
- [Current Limitation](#current-limitation)
- [Future Improvements](#future-improvements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Run the App Locally](#run-the-app-locally)
- [Deployment Plan](#deployment-plan)
- [Security Notes](#security-notes)
- [Project Status](#project-status)
- [Author](#author)

## Project Overview

The OFM Operations Dashboard is a Python-based internal analytics dashboard built for tracking daily chatter operations. It helps agency admins monitor chatter performance, work status, input amount, commission, working hours, and operational notes from one centralized dashboard.

The system uses Google Sheets as the data source and Streamlit as the dashboard interface.

The basic workflow is:

```text
Google Sheet Daily Tracker
        ↓
Streamlit reads the data
        ↓
Dashboard displays KPIs, charts, statistics, and tables
```

## Project Objective

The objective of this project is to create an interactive and updatable dashboard that helps an OFM agency track daily chatter work data in a professional and easy-to-read format.

The dashboard helps solve these problems:

* Manual checking of daily chatter performance
* Difficulty tracking total input and commission
* Poor visibility of who is working, done, or having issues
* Lack of quick performance comparison between chatters
* No simple way to view daily or date-range-based performance
* No centralized visual dashboard for admin review

## Technology Stack

The project uses:

* Python
* Streamlit
* pandas
* Plotly Express
* Google Sheets
* GitHub
* Streamlit Cloud

## Data Architecture

The data flow is:

```text
Google Sheet Daily Tracker
        ↓
Google Sheets CSV/gviz link
        ↓
Python data loader
        ↓
pandas dataframe
        ↓
Data cleaning and validation
        ↓
Dashboard calculations
        ↓
Streamlit visual interface
```

Google Sheets acts as the live data source. Each row represents a chatter’s work record.

## Expected Google Sheet Columns

The dashboard expects the Google Sheet tab to contain these columns:

```text
Name
Status
Date
Start Time
End Time
Duration
Input Amount
Commission Amount
Commission
Note
```

These column names are important because the dashboard depends on them for calculations and visualizations.

## Data Loading Process

The app reads from a Google Sheet using a CSV-style Google Visualization link.

Because the sheet may contain title rows or extra formatting above the real table, the app scans the sheet to find the real header row. It searches for important headers such as:

* Name
* Status
* Date
* Start Time
* End Time
* Duration

Once the real header row is found, the data is loaded into a pandas dataframe.

## Data Cleaning Process

After loading the data, the app cleans it by:

* Removing extra spaces from column names
* Converting Date into datetime format
* Converting Duration into numeric format
* Converting Input Amount into numeric format
* Converting Commission Amount into numeric format
* Cleaning text fields such as Name, Status, and Note
* Removing rows that are fully empty or not useful for analysis

## Dashboard Features

The dashboard includes:

* Date range filter
* Chatter filter
* Status filter
* Total input KPI
* Total commission KPI
* Total hours KPI
* Session count KPI
* Working count
* Done count
* Issue count
* Average input
* Median input
* Standard deviation
* Maximum input
* Input by chatter chart
* Hours by chatter chart
* Commission by chatter chart
* Status breakdown chart
* Top chatter by input
* Top chatter by hours
* Searchable interactive table
* Notes and issues section

## Mathematical and Statistical Operations

The dashboard performs these operational calculations:

* Total Input = sum of Input Amount
* Total Commission = sum of Commission Amount
* Total Hours = sum of Duration
* Sessions = count of filtered records
* Working Count = count of records with status Working
* Done Count = count of records with status Done
* Issue Count = count of records with status Issue

It also performs these statistical calculations:

* Average Input
* Median Input
* Standard Deviation
* Maximum Input

These calculations help the agency understand both productivity and consistency.

## Filtering System

The dashboard includes filters for:

* Date range
* Chatter name
* Status

All KPIs, charts, summaries, and tables update based on the selected filters.

## Visualization System

The dashboard uses Plotly Express for charts.

Current charts include:

* Input by Chatter
* Hours by Chatter
* Commission by Chatter
* Status Breakdown

## Interactive Table

The dashboard includes an interactive table using Streamlit’s data editor.

The table supports:

* Searching by text
* Viewing filtered records
* Status dropdown interaction
* Formatted number columns
* Clean data display

Current table edits are temporary and do not save back to Google Sheets because the current version uses a CSV read-only connection.

## Current Limitation

The current version reads data from Google Sheets but does not write changes back to the sheet.

This means:

* Google Sheet is the main data entry point
* Streamlit is the dashboard/reporting interface
* Edits made inside Streamlit do not permanently update the Google Sheet

## Future Improvements

Recommended future upgrades:

* Save edits from Streamlit back to Google Sheets
* Add login/authentication
* Add weekly and monthly trend charts
* Add downloadable filtered reports
* Add individual chatter profile pages
* Add admin-only editing mode
* Add better UI styling
* Add agent/account-level filtering
* Replace CSV link with Google Sheets API
* Use Streamlit secrets for secure credentials

## Project Structure

```text
ofm-operations-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── CLIENT_REPORT.md
└── .gitignore
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the App Locally

Run:

```bash
python -m streamlit run app.py
```

## Deployment Plan

Recommended deployment:

1. Push project to GitHub
2. Connect GitHub repo to Streamlit Cloud
3. Deploy the Streamlit app
4. Share the dashboard link with the client

## Security Notes

The current version uses a Google Sheet link as the data source.

Do not store sensitive information in the connected sheet, such as:

* Passwords
* Private client usernames
* Payment details
* Personal IDs
* Sensitive account information

For production-level security, the project should be upgraded to use the Google Sheets API with a service account and Streamlit secrets.

## Project Status

Current version:

* Google Sheets data connection completed
* Dashboard metrics completed
* Charts completed
* Mathematical and statistical operations completed
* Searchable interactive table completed
* Notes and issues section completed
* GitHub setup in progress

## Author

Built as an internal operations dashboard project for OFM chatter performance tracking.

* [Table of Contents](#table-of-contents)