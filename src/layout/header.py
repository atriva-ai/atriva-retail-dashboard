# layout/header.py
import panel as pn

# Logo image (use a path or URL)
logo = pn.pane.Image(
    'src/static/AtrivaTextLogo.png',  # Replace with your actual logo
    width=210,
    height=54,
    sizing_mode='fixed',
    # margin=(10, 20, 10, 20)  # Top, right, bottom, left
)

title_block = pn.pane.Markdown(
    "## Smart Retail Dashboard\nSmarter store insights through real-time video analytics.",
    styles={
        'fontSize': '20px',
        'padding': '10px 0',
        'color': '#333',
        'lineHeight': '1.2',
        'margin': '0',
    },
    sizing_mode='stretch_width'
)

# Wrap logo in a Row with alignment
logo_col = pn.Column(
    pn.Spacer(height=5),  # spacer to nudge vertical alignment slightly
    logo,
    sizing_mode='fixed',
    width=240,
    align='center'
)

# Combine logo and text in a row
header_pane = pn.Row(
    logo_col,
    title_block,
    styles={'background': '#F0F2F5'},
    sizing_mode='stretch_width',
    margin=(0, 0, 10, 0),
    align='center'
)