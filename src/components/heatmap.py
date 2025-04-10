# components/heatmap.py
import panel as pn
import plotly.express as px
import pandas as pd
import numpy as np

def heatmap_placeholder():
    hours = [f"{h}:00" for h in range(9, 21)]
    zones = ["Aisle 1", "Aisle 2", "Promo Area", "Front Display"]

    data = pd.DataFrame(np.random.randint(0, 50, size=(len(zones), len(hours))), index=zones, columns=hours)
    df_melted = data.reset_index().melt(id_vars='index')
    df_melted.columns = ['Zone', 'Hour', 'Count']

    fig = px.density_heatmap(df_melted, x='Hour', y='Zone', z='Count', color_continuous_scale='Viridis')

    return pn.Card(
        pn.Column(
            pn.pane.Markdown("## Occupancy Heat Map"),
            pn.pane.Plotly(fig)
        ),
        title="Heatmap",
        margin=10,
        width=850,
        styles={'border-radius': '12px', "box-shadow": "0 2px 8px rgba(0,0,0,0.1)", 'padding': '16px'}
    )
