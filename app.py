import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="OFM Operations Dashboard",
    layout="wide"
)

# -----------------------------
# Google Sheet CSV connection
# -----------------------------
CSV_URL = "https://docs.google.com/spreadsheets/d/1BXG8nBevxGrVIeBZj8j69bkTN2u7PYG864qA6aA0yBA/gviz/tq?tqx=out:csv&sheet=Daily%20Tracker"


@st.cache_data(ttl=60)
def load_data():
    try:
        raw_df = pd.read_csv(CSV_URL, header=None)

        # Remove fully empty rows and columns
        raw_df = raw_df.dropna(how="all")
        raw_df = raw_df.dropna(axis=1, how="all")

        required_headers = [
            "Name",
            "Status",
            "Date",
            "Start Time",
            "End Time",
            "Duration",
            "Input Amount",
            "Commission Amount",
            "Commission",
            "Note"
        ]

        header_row_index = None

        for index, row in raw_df.iterrows():
            row_values = [
                str(value).strip().replace("\xa0", " ")
                for value in row.tolist()
            ]

            matches = sum(header in row_values for header in required_headers)

            if matches >= 5:
                header_row_index = index
                break

        if header_row_index is None:
            st.error("Could not find the real header row in your Google Sheet.")
            st.write("First rows Streamlit is reading from your sheet:")
            st.dataframe(raw_df.head(20), use_container_width=True)
            st.write("Make sure the tracker headers are written as:")
            st.write(required_headers)
            st.stop()

        df = pd.read_csv(CSV_URL, skiprows=header_row_index)
        df.columns = df.columns.str.strip().str.replace("\xa0", " ")

        return df

    except Exception as e:
        st.error("Could not load data from Google Sheet.")
        st.write("Make sure your Google Sheet is shared as: Anyone with the link -> Viewer")
        st.write("CSV link being used:")
        st.code(CSV_URL)
        st.write("Error details:")
        st.exception(e)
        st.stop()


# -----------------------------
# Load data
# -----------------------------
df = load_data()

# -----------------------------
# Clean column names
# -----------------------------
df.columns = df.columns.str.strip()

# -----------------------------
# Required columns check
# -----------------------------
required_columns = [
    "Name",
    "Status",
    "Date",
    "Start Time",
    "End Time",
    "Duration",
    "Input Amount",
    "Commission Amount",
    "Commission",
    "Note"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"Missing columns in Google Sheet: {missing_columns}")
    st.write("Columns found in your sheet:")
    st.write(list(df.columns))
    st.stop()

# -----------------------------
# Clean data
# -----------------------------
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Duration"] = pd.to_numeric(df["Duration"], errors="coerce").fillna(0)
df["Input Amount"] = pd.to_numeric(df["Input Amount"], errors="coerce").fillna(0)
df["Commission Amount"] = pd.to_numeric(df["Commission Amount"], errors="coerce").fillna(0)

df["Name"] = df["Name"].fillna("").astype(str).str.strip()
df["Status"] = df["Status"].fillna("").astype(str).str.strip()
df["Note"] = df["Note"].fillna("").astype(str).str.strip()

# Remove rows that are fully empty
df = df[
    (df["Name"] != "") |
    (df["Status"] != "") |
    (df["Input Amount"] > 0) |
    (df["Duration"] > 0)
]

# -----------------------------
# Header
# -----------------------------
st.title("OFM Operations Dashboard")
st.caption("Interactive dashboard for tracking chatter daily work data.")

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filters")

available_dates = df["Date"].dropna()

if available_dates.empty:
    st.error("No valid dates found in your Google Sheet.")
    st.stop()

min_date = available_dates.min().date()
max_date = available_dates.max().date()

selected_date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(selected_date_range, tuple):
    if len(selected_date_range) == 2:
        start_date, end_date = selected_date_range
    elif len(selected_date_range) == 1:
        start_date = selected_date_range[0]
        end_date = selected_date_range[0]
    else:
        start_date = min_date
        end_date = max_date
else:
    start_date = selected_date_range
    end_date = selected_date_range

selected_name = st.sidebar.selectbox(
    "Select Chatter",
    ["All"] + sorted(df["Name"].dropna().unique().tolist())
)

selected_status = st.sidebar.selectbox(
    "Select Status",
    ["All"] + sorted(df["Status"].dropna().unique().tolist())
)

# -----------------------------
# Apply filters
# -----------------------------
filtered_df = df[
    (df["Date"].dt.date >= start_date) &
    (df["Date"].dt.date <= end_date)
]

if selected_name != "All":
    filtered_df = filtered_df[filtered_df["Name"] == selected_name]

if selected_status != "All":
    filtered_df = filtered_df[filtered_df["Status"] == selected_status]

# -----------------------------
# KPI metrics
# -----------------------------
total_input = filtered_df["Input Amount"].sum()
total_commission = filtered_df["Commission Amount"].sum()
total_hours = filtered_df["Duration"].sum()
session_count = len(filtered_df)

working_count = filtered_df[filtered_df["Status"] == "Working"].shape[0]
done_count = filtered_df[filtered_df["Status"] == "Done"].shape[0]
issue_count = filtered_df[filtered_df["Status"] == "Issue"].shape[0]

avg_input = filtered_df["Input Amount"].mean() if not filtered_df.empty else 0
median_input = filtered_df["Input Amount"].median() if not filtered_df.empty else 0
std_input = filtered_df["Input Amount"].std() if len(filtered_df) > 1 else 0
max_input = filtered_df["Input Amount"].max() if not filtered_df.empty else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Input", f"${total_input:,.2f}")
col2.metric("Total Commission", f"${total_commission:,.2f}")
col3.metric("Total Hours", f"{total_hours:,.2f}")
col4.metric("Sessions", session_count)

col5, col6, col7 = st.columns(3)
col5.metric("Working", working_count)
col6.metric("Done", done_count)
col7.metric("Issues", issue_count)

st.divider()

# -----------------------------
# Mathematical and statistical overview
# -----------------------------
st.subheader("Mathematical and Statistical Overview")

stat1, stat2, stat3, stat4 = st.columns(4)
stat1.metric("Average Input", f"${avg_input:,.2f}")
stat2.metric("Median Input", f"${median_input:,.2f}")
stat3.metric("Standard Deviation", f"${std_input:,.2f}")
stat4.metric("Maximum Input", f"${max_input:,.2f}")

st.divider()

# -----------------------------
# Charts
# -----------------------------
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Input by Chatter")

    input_by_chatter = (
        filtered_df
        .groupby("Name", as_index=False)["Input Amount"]
        .sum()
        .sort_values(by="Input Amount", ascending=False)
    )

    if input_by_chatter.empty:
        st.info("No input data for this selected filter.")
    else:
        fig = px.bar(
            input_by_chatter,
            x="Name",
            y="Input Amount",
            text="Input Amount"
        )
        fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig.update_layout(
            height=350,
            xaxis_title="Chatter",
            yaxis_title="Input Amount"
        )
        st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    st.subheader("Hours by Chatter")

    hours_by_chatter = (
        filtered_df
        .groupby("Name", as_index=False)["Duration"]
        .sum()
        .sort_values(by="Duration", ascending=False)
    )

    if hours_by_chatter.empty:
        st.info("No hours data for this selected filter.")
    else:
        fig = px.bar(
            hours_by_chatter,
            x="Name",
            y="Duration",
            text="Duration"
        )
        fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig.update_layout(
            height=350,
            xaxis_title="Chatter",
            yaxis_title="Hours"
        )
        st.plotly_chart(fig, use_container_width=True)

chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.subheader("Commission by Chatter")

    commission_by_chatter = (
        filtered_df
        .groupby("Name", as_index=False)["Commission Amount"]
        .sum()
        .sort_values(by="Commission Amount", ascending=False)
    )

    if commission_by_chatter.empty:
        st.info("No commission data for this selected filter.")
    else:
        fig = px.bar(
            commission_by_chatter,
            x="Name",
            y="Commission Amount",
            text="Commission Amount"
        )
        fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig.update_layout(
            height=350,
            xaxis_title="Chatter",
            yaxis_title="Commission Amount"
        )
        st.plotly_chart(fig, use_container_width=True)

with chart_col4:
    st.subheader("Status Breakdown")

    status_count = filtered_df["Status"].value_counts().reset_index()
    status_count.columns = ["Status", "Count"]

    if status_count.empty:
        st.info("No status data for this selected filter.")
    else:
        fig = px.pie(
            status_count,
            names="Status",
            values="Count",
            hole=0.45
        )
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------------
# Top performers
# -----------------------------
st.subheader("Top Performers")

top_col1, top_col2 = st.columns(2)

with top_col1:
    if not input_by_chatter.empty:
        top_input = input_by_chatter.iloc[0]
        st.metric(
            "Top Chatter by Input",
            top_input["Name"],
            f"${top_input['Input Amount']:,.2f}"
        )
    else:
        st.info("No input performer data available.")

with top_col2:
    if not hours_by_chatter.empty:
        top_hours = hours_by_chatter.iloc[0]
        st.metric(
            "Top Chatter by Hours",
            top_hours["Name"],
            f"{top_hours['Duration']:,.2f} hours"
        )
    else:
        st.info("No hours performer data available.")

st.divider()

# -----------------------------
# Interactive performance table
# -----------------------------
st.subheader("Interactive Daily Performance Table")

table_columns = [
    "Name",
    "Status",
    "Date",
    "Start Time",
    "End Time",
    "Duration",
    "Input Amount",
    "Commission Amount",
    "Commission",
    "Note"
]

search_text = st.text_input(
    "Search table",
    placeholder="Search by name, status, note, date, or any value"
)

table_df = filtered_df[table_columns].copy()

if search_text:
    search_text = search_text.lower()
    table_df = table_df[
        table_df.astype(str)
        .apply(lambda row: row.str.lower().str.contains(search_text).any(), axis=1)
    ]

st.data_editor(
    table_df,
    use_container_width=True,
    hide_index=True,
    disabled=[
        "Date",
        "Start Time",
        "End Time",
        "Duration",
        "Input Amount",
        "Commission Amount",
        "Commission"
    ],
    column_config={
        "Status": st.column_config.SelectboxColumn(
            "Status",
            options=["Working", "Done", "Issue"]
        ),
        "Duration": st.column_config.NumberColumn(
            "Duration",
            format="%.2f hrs"
        ),
        "Input Amount": st.column_config.NumberColumn(
            "Input Amount",
            format="$%.2f"
        ),
        "Commission Amount": st.column_config.NumberColumn(
            "Commission Amount",
            format="$%.2f"
        )
    }
)

st.caption(
    "Note: This table is interactive inside Streamlit, but edits do not save back to Google Sheets because this version uses a CSV read-only connection."
)

# -----------------------------
# Notes / Issues
# -----------------------------dir
st.subheader("Notes / Issues")

notes_df = filtered_df[
    (filtered_df["Status"] == "Issue") |
    (filtered_df["Note"].str.strip() != "")
]

if notes_df.empty:
    st.success("No notes or issues for this selected filter.")
else:
    st.dataframe(
        notes_df[["Name", "Status", "Date", "Note"]],
        use_container_width=True,
        hide_index=True
    )