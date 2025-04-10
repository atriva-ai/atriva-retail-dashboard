# components/checkout.py
import panel as pn

def checkout_efficiency_panel():
    staff_absent_time = 3.5  # hours
    avg_queue_length = 4.2
    avg_wait_time = 2.1  # minutes

def checkout_efficiency_panel():
    staff_absent_time = 3.5  # hours
    avg_queue_length = 4.2
    avg_wait_time = 2.1  # minutes

    return pn.Card(
        pn.Column(
            pn.pane.Markdown("## Checkout Efficiency"),
            pn.Row(
                pn.indicators.Number(name='Staff Absent Time (hrs)', value=staff_absent_time, format='{value:.1f}'),
                pn.indicators.Number(name='Avg Queue Length', value=avg_queue_length, format='{value:.1f}'),
                pn.indicators.Number(name='Avg Wait Time (min)', value=avg_wait_time, format='{value:.1f}')
            )
        ),
        title="Checkout Insights",
        margin=10,
        width=850,
        styles={'border-radius': '12px', "box-shadow": "0 2px 8px rgba(0,0,0,0.1)", 'padding': '16px'}
    )
