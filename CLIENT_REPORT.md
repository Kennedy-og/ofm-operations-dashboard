# Client Report: OFM Operations Dashboard

## Table of Contents

* [Project Summary](#project-summary)
* [Purpose of the Dashboard](#purpose-of-the-dashboard)
* [How the System Works](#how-the-system-works)
* [Daily Tracker Data](#daily-tracker-data)
* [Dashboard Features](#dashboard-features)
* [Interactive Filters](#interactive-filters)
* [Mathematical and Statistical Insights](#mathematical-and-statistical-insights)
* [Benefits to the Agency](#benefits-to-the-agency)
* [Current System Limitation](#current-system-limitation)
* [Recommended Workflow](#recommended-workflow)
* [Deployment Plan](#deployment-plan)
* [Future Improvements](#future-improvements)
* [Final Note](#final-note)

## Project Summary

The OFM Operations Dashboard is an internal dashboard created to help the agency track daily chatter work activities in a more organized and professional way.

Instead of manually checking rows in a spreadsheet, the dashboard turns the daily tracker data into clear performance metrics, charts, summaries, and tables.

The system allows the agency to see what is happening across chatters, including who worked, who is currently working, who completed their session, how much input was recorded, how much commission was generated, and whether there were any issues.

The dashboard is designed to make daily operations easier to monitor, review, and manage.

## Purpose of the Dashboard

The purpose of the dashboard is to help the agency monitor chatter performance and daily work records without spending too much time reading through raw spreadsheet data.

It helps the agency answer important questions such as:

* Who worked today?
* Who is currently working?
* Who completed their shift?
* How much input was recorded?
* How much commission was generated?
* How many hours were worked?
* Which chatter performed best?
* Were there any issues or notes to review?

The dashboard gives the admin a simple way to understand daily performance at a glance.

## How the System Works

The system follows a simple process:

```text
Chatters or admin update the Google Sheet
        ↓
The dashboard reads the sheet
        ↓
The dashboard updates the metrics and charts
        ↓
Admin views performance from one dashboard page
```

The Google Sheet is used as the data entry point.

The Streamlit dashboard is used as the reporting and performance review interface.

This means the agency can continue using Google Sheets for daily updates while still having a more professional dashboard for reviewing the data.

## Daily Tracker Data

The dashboard is based on the `Daily Tracker` sheet.

The tracker records the following information:

* Chatter name
* Work status
* Date
* Start time
* End time
* Duration
* Input amount
* Commission amount
* Commission percentage
* Notes

Each row represents one work record or session from a chatter.

This gives the agency a simple but complete record of daily chatter work.

## Dashboard Features

The dashboard includes the following features:

* Total input
* Total commission
* Total hours worked
* Number of sessions
* Number of working chatters
* Number of completed sessions
* Number of issue records
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
* Searchable performance table
* Notes and issues section

These features allow the admin to quickly review both general performance and individual chatter performance.

## Interactive Filters

The dashboard includes filters that allow the admin to review data in different ways.

The admin can filter by:

* Date range
* Chatter name
* Status

This makes it easy to view:

* One day
* One week
* One month
* One chatter
* All chatters
* Only working sessions
* Only completed sessions
* Only issue records

Once a filter is selected, the dashboard automatically updates the metrics, charts, table, and notes section based on the selected data.

## Mathematical and Statistical Insights

The dashboard does more than display raw data. It also calculates important operational statistics.

The dashboard calculates:

* Total input
* Total commission
* Total hours
* Session count
* Average input
* Median input
* Standard deviation
* Maximum input

These statistics help the agency understand both performance and consistency.

For example:

* Average input shows the normal performance level.
* Median input gives a balanced view of performance.
* Standard deviation shows how much performance varies.
* Maximum input shows the highest recorded performance.
* Total commission shows the total payout amount based on recorded input.
* Total hours shows the amount of work time recorded.

These calculations help the agency make better decisions from the data instead of only looking at raw numbers.

## Benefits to the Agency

The dashboard gives the agency several benefits:

* Faster performance review
* Better daily tracking
* Clearer chatter comparison
* Easier issue monitoring
* Better commission visibility
* More professional reporting
* Less manual calculation
* Better decision-making for admin
* Easier review of notes and issues
* Cleaner presentation of daily work data

The dashboard saves time because the admin no longer has to manually calculate totals, compare chatters one by one, or search through the sheet to understand what happened.

## Current System Limitation

The current version reads data from the Google Sheet and displays it in the dashboard.

However, edits made inside the dashboard do not save back to the Google Sheet yet.

This means:

* Google Sheet remains the main place for entering data.
* The dashboard is mainly for viewing, filtering, analyzing, and reporting.
* Any permanent correction should still be done inside the Google Sheet.

This was done to keep the first version simple, fast, and easy to deploy.

A future version can allow edits from the dashboard to save directly back to Google Sheets.

## Recommended Workflow

Recommended daily workflow:

1. Chatter or admin updates the `Daily Tracker` in Google Sheets.
2. Admin opens the dashboard link.
3. Dashboard loads the latest available data.
4. Admin uses filters to review performance.
5. Admin checks total input, commission, hours, and session count.
6. Admin reviews top performers.
7. Admin checks notes and issues.
8. Admin uses the information for daily or weekly review.

This workflow keeps data entry simple while making performance review more professional.

## Deployment Plan

The project will be stored on GitHub for proper record keeping and version control.

The dashboard can then be deployed online using Streamlit Cloud.

Once deployed, the client will receive a dashboard link that can be opened in a browser.

The client does not need to install Python, VS Code, or any development tool to view the deployed dashboard.

The recommended deployment flow is:

```text
Project code
        ↓
GitHub repository
        ↓
Streamlit Cloud deployment
        ↓
Client dashboard link
```

## Future Improvements

Future improvements can include:

* Saving dashboard edits back to Google Sheets
* Login access for admin
* Separate views for admin and chatters
* Weekly downloadable reports
* Monthly downloadable reports
* Agent/account-level tracking
* More advanced charts
* Automated alerts for issue records
* More secure Google Sheets API connection
* Admin-only editing mode
* Chatter-specific performance pages
* Export button for filtered reports
* Better custom dashboard styling

These improvements can turn the current dashboard into a stronger internal operations system as the agency grows.

## Final Note

This dashboard is a practical first version of an internal OFM operations system.

It keeps data entry simple through Google Sheets while giving the agency a more professional and interactive dashboard for reviewing performance.

The current version is suitable for tracking daily chatter work data, reviewing performance, checking commissions, identifying top performers, and monitoring notes or issues.

* [Table of Contents](#table-of-contents)
