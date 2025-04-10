# Project Structure Overview
# ├── app.py                  # Entry point to serve the dashboard
# ├── layout/
# │   ├── home.py             # Layout for Home Dashboard
# │   ├── camera_setup.py     # Layout for Camera Setup Page
# │   └── zone_details.py     # Layout for Zone Details Page
# └── components/
#     ├── camera_status.py    # UI for camera status
#     ├── people_flow.py      # UI for people flow comparison
#     ├── heatmap.py          # UI for occupancy heat map
#     └── checkout.py         # UI for checkout efficiency

# import panel as pn
# from src.ui_components import dashboard
# pn.extension()
# dashboard.show()

# Target pages
# Dashboard
# - Store Name
# - Current Week
# - Customer Flow Tracker
#     - People count chart by Hourly, Daily, Weekly
#     - Up to date count today / compariing to yesterday (+/- X%)
# - Customer Demographics
#     - Male/female in pie chart
#     - Age in bar chart
#     - With children/family (X%)
# - Popular Area
#     - Top 3 area name and zone occupancy
# - Sales efficiency
#     - Average customers waiting by time period
#     - Missing staff time in cashier by time period
# Anaytics
# Products
# - Heatmap
# Customers
# Settings
# - Site Name edit
# - Camera settings: location name, zone settings, analytics settings

# app.py
import panel as pn

custom_css =  """
.bk-header .bk-tab {
    # background-color: #FF0000;
    # color: #FFFFFF;
    /* Style unselected tabs */
    background-color: #f0f0f0;
    color: #333;
    padding: 8px 16px;
    font-size: 16px;
    border-radius: 6px 6px 0 0;
    margin-right: 4px;
    border: 1px solid #ccc;
    border-bottom: none;
}
.bk-header .bk-tab.bk-active {
    # background-color: #FFFF00 !important;
    # color: #000000 !important;
    # font-weight: bold;
    background-color: #ffffff !important;
    color: #007BFF !important;
    font-weight: bold;
    border: 1px solid #ccc;
    border-bottom: none;
}
/* Match tab content background with selected tab */
.bk-header .bk-tabs-content {
    background-color: #ffffff;
    padding: 20px;
    border: 1px solid #ccc;
}
.connected-indicator .bk {
    font-size: 10px;
    color: #333;
}
.disconnected-indicator .bk {
    font-size: 10px;
    color: #007BFF;
}
"""

pn.extension(raw_css=[custom_css])

from src.layout.home import home_dashboard
from src.layout.camera_setup import camera_setup_page
from src.layout.zone_details import zone_details_page
from src.layout.header import header_pane

pn.extension('plotly', 'tabulator')

tabs = pn.Tabs(
    ('Dashboard', home_dashboard()),
    ('Camera Setup', camera_setup_page()),
    ('Zone Details', zone_details_page()),
    tabs_location='above',   # ensure tabs appear below header
    styles={
        'background': '#ffffff',
        'borderTop': '2px solid #ccc',
        'padding': '10px',
        'fontSize': '20px' # make tab labels bigger
    }
)

dashboard = pn.Column(
    header_pane,  # Big bold title + subtitle
    tabs,
    sizing_mode='stretch_width'
)

print(type(dashboard))
dashboard.servable()

