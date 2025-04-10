# components/camera_status.py
import panel as pn

def camera_status_panel():
    camera_status = {
        'connected': 8,
        'disconnected': 0,
        'zones': {
            'entrance_exit': 2,
            'product_zone': 4,
            'checkout_zone': 2
        }
    }
    return pn.Card(
        pn.Row(
            pn.Column(
                pn.pane.Markdown("## Camera Status"),
                pn.Row(
                    pn.indicators.Number(
                        name='Connected', value=camera_status['connected']
                    ),
                    pn.indicators.Number(
                        name='Disconnected', value=camera_status['disconnected']
                    )
                ),
            ),
            pn.Column(
                pn.pane.Markdown("## Cameras by Zone"),
                pn.Row(
                    pn.indicators.Number(
                        name='Entrance/Exit', value=camera_status['zones']['entrance_exit']
                    ),
                    pn.indicators.Number(
                        name='Product Zone', value=camera_status['zones']['product_zone']
                    ),
                    pn.indicators.Number(
                        name='Checkout Zone', value=camera_status['zones']['checkout_zone'],
                    )
                )
            )
        ),
        title="Camera Summary",
        margin=10,
        width=850,
        styles={'border-radius': '12px', "box-shadow": "0 2px 8px rgba(0,0,0,0.1)", 'padding': '16px'}
    )
