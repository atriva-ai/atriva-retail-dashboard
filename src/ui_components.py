import holoviews as hv
# from .video_stream import video_pane
# from .video_detection import process_frame

import panel as pn
import pandas as pd
import numpy as np
import datetime as dt
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool

pn.extension('plotly', 'tabulator')
# hv.extension('bokeh')

# Simulated data for demo
now = dt.datetime.now()
dates = pd.date_range(end=now, periods=60)

# Demo time series data for people counts
people_data = pd.DataFrame({
    'date': dates,
    'count': np.random.poisson(lam=100, size=len(dates))
})

# Simulated camera status
camera_status = {
    'connected': 12,
    'disconnected': 3,
    'zones': {
        'entrance_exit': 5,
        'product_zone': 6,
        'checkout_zone': 4
    }
}

# Widgets
# camera_selector = pn.widgets.Select(name="Select Camera", options=["Webcam", "CCTV Feed"])
# toggle_button = pn.widgets.Toggle(name="Start Stream", button_type="primary")
# object_count = pn.indicators.Number(name="Objects Detected", value=0, format="{value}")

# Layout
# dashboard = pn.Column( 
#     "# Retail AI Video Analytics Dashboard",
#     pn.Row(camera_selector, toggle_button),
#     object_count,
#    video_pane
#)

# Layout functions

def camera_status_panel():
    return pn.Column(
        "## Camera Status",
        pn.Row(
            pn.indicators.Number(name='Connected', value=camera_status['connected'], format='{value}'),
            pn.indicators.Number(name='Disconnected', value=camera_status['disconnected'], format='{value}')
        ),
        pn.pane.Markdown("### Cameras by Zone"),
        pn.Row(
            pn.indicators.Number(name='Entrance/Exit', value=camera_status['zones']['entrance_exit']),
            pn.indicators.Number(name='Product Zone', value=camera_status['zones']['product_zone']),
            pn.indicators.Number(name='Checkout Zone', value=camera_status['zones']['checkout_zone'])
        )
    )

def people_comparison_panel():
    current = people_data.tail(30)
    previous = people_data.iloc[-60:-30]

    def compare_period(current, previous):
        delta = current.sum() - previous.sum()
        pct = (delta / previous.sum()) * 100 if previous.sum() > 0 else 0
        return delta, pct

    delta_30, pct_30 = compare_period(current['count'][-30:], previous['count'])
    delta_7, pct_7 = compare_period(current['count'][-7:], previous['count'][-7:])
    delta_1, pct_1 = compare_period(current['count'][-1:], previous['count'][-1:])

    return pn.Column(
        "## People Flow Comparison",
        pn.Row(
            pn.indicators.Number(name='Last 1 Day Δ', value=pct_1, format='±{value:.2f}%'),
            pn.indicators.Number(name='Last 7 Days Δ', value=pct_7, format='±{value:.2f}%'),
            pn.indicators.Number(name='Last 30 Days Δ', value=pct_30, format='±{value:.2f}%')
        )
    )

def heatmap_placeholder():
    return pn.pane.Markdown("## Occupancy Heat Map (Placeholder)")

def checkout_efficiency_panel():
    # Dummy data
    staff_absent_time = 3.5  # hours
    avg_queue_length = 4.2
    avg_wait_time = 2.1  # minutes

    return pn.Column(
        "## Checkout Efficiency",
        pn.Row(
            pn.indicators.Number(name='Staff Absent Time (hrs)', value=staff_absent_time, format='{value:.1f}'),
            pn.indicators.Number(name='Avg Queue Length', value=avg_queue_length, format='{value:.1f}'),
            pn.indicators.Number(name='Avg Wait Time (min)', value=avg_wait_time, format='{value:.1f}')
        )
    )

# Page components
def home_dashboard():
    return pn.Column(
        "# Retail AI Dashboard",
        camera_status_panel(),
        people_comparison_panel(),
        heatmap_placeholder(),
        checkout_efficiency_panel()
    )

def camera_setup_page():
    return pn.Column("# Camera Setup", pn.pane.Markdown("Detailed camera configuration goes here."))

def zone_details_page():
    return pn.Column("# Zone Details", pn.pane.Markdown("Information about each retail zone."))

# Tabs Layout
tabs = pn.Tabs(
    ('Home', home_dashboard()),
    ('Camera Setup', camera_setup_page()),
    ('Zone Details', zone_details_page())
)

# Serve the dashboard
tabs.servable()

