# layout/camera_setup.py
import panel as pn

def camera_setup_page():
    return pn.Column(
        "# Camera Setup",
        pn.pane.Markdown("### Detailed camera configuration goes here.")
    )