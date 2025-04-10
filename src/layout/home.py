# layout/home.py
import panel as pn
from src.components.camera_status import camera_status_panel
from src.components.people_flow import people_comparison_panel
from src.components.heatmap import heatmap_placeholder
from src.components.checkout import checkout_efficiency_panel
from src.components.people_flow import visitor_demography_card
from src.components.people_flow import visitor_summary_card

def home_dashboard():
    return pn.Column(
        pn.pane.Markdown("""
        # Retail AI Dashboard - Smart insights for better operations
        """),
        pn.Spacer(height=10),
        camera_status_panel(),
        pn.Spacer(height=10),
        visitor_summary_card(),
        pn.Spacer(height=10),
        visitor_demography_card(),
        pn.Spacer(height=10),
        people_comparison_panel(),
        pn.Spacer(height=10),
        heatmap_placeholder(),
        pn.Spacer(height=10),
        checkout_efficiency_panel(),
    )
