# components/people_flow.py
import panel as pn
import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px

pn.extension('plotly')

def generate_hourly_data():
    now = dt.datetime.now()
    today = now.date()
    yesterday = today - dt.timedelta(days=1)

    # Generate 12 hourly slots: 8AM to 8PM
    hours = [f"{hour:02d}:00" for hour in range(8, 21)]

    data = []
    for hour in hours:
        data.append({'hour': hour, 'count': np.random.randint(20, 150), 'day': 'Yesterday'})
        data.append({'hour': hour, 'count': np.random.randint(20, 150), 'day': 'Today'})

    return pd.DataFrame(data)

# Define the data generation function for daily data
def generate_daily_data():
    
    now = dt.datetime.now()
    today = now.date()
    start_this_week = today - dt.timedelta(days=today.weekday())
    start_last_week = start_this_week - dt.timedelta(days=7)

    dates = [start_this_week + dt.timedelta(days=i) for i in range(7)]
    dates_last_week = [start_last_week + dt.timedelta(days=i) for i in range(7)]

    data = []
    for d in dates_last_week:
        data.append({'date': d.strftime('%A'), 'count': np.random.randint(300, 1000), 'week': 'Last Week'})
    for d in dates:
        data.append({'date': d.strftime('%A'), 'count': np.random.randint(300, 1000), 'week': 'This Week'})

    return pd.DataFrame(data)

def generate_weekly_data():
    
    today = dt.date.today()
    # Define weekly ranges
    start_this_month = today - dt.timedelta(days=today.weekday()) - dt.timedelta(weeks=3)  # 4 weeks ago, aligned to Monday
    start_last_month = start_this_month - dt.timedelta(weeks=4)  # 8 weeks ago, aligned to Monday

    # Create week groups
    data = []

    # Last month data (Weeks 1–4)
    for i in range(4):
        week_start = start_last_month + dt.timedelta(weeks=i)
        data.append({
            'week': f'Week {i + 1}',
            'count': np.random.randint(1000, 3000),
            'month': 'Last Month'
        })

    # This month data (Weeks 1–4)
    for i in range(4):
        week_start = start_this_month + dt.timedelta(weeks=i)
        data.append({
            'week': f'Week {i + 1}',
            'count': np.random.randint(1000, 3000),
            'month': 'This Month'
        })
    return pd.DataFrame(data)

view_selector = pn.widgets.RadioButtonGroup(
    name='View Mode',
    options=['Hourly', 'Daily', 'Weekly'],
    button_type='primary'
)

plot_pane = pn.pane.Plotly(height=500)

def update_plot(event=None):
    mode = view_selector.value
    if mode == 'Hourly':
        df = generate_hourly_data()
        # Group past and current day side by side
        df['day'] = pd.Categorical(df['day'], categories=['Yesterday', 'Today'], ordered=True)

        fig = px.bar(df, x='hour', y='count', color='day', barmode='group', title='Hourly People Flow (8AM–8PM)')
    elif mode == 'Daily':
        df = generate_daily_data()  # Generate daily data
        fig = px.bar(df, x='date', y='count', color='week', barmode='group', title='Daily People Flow (Last Week vs This Week)')
    else:
        df = generate_weekly_data()
        # Group past and current week side by side
        fig = px.bar(df, x='week', y='count', color='month', barmode='group',
            text='count', labels={'week_group': 'Week of Month', 'count': 'People Count'},
            title='Weekly People Flow Comparison'
        )

        fig.update_layout(
            xaxis_title='Week of Month',
            yaxis_title='People Count',
            bargap=0.2,
            plot_bgcolor='white',
            legend_title='',
            font=dict(size=14),
        )
        fig.update_traces(textposition='outside')

    plot_pane.object = fig


view_selector.param.watch(update_plot, 'value')
update_plot()

people_flow_panel = pn.Column(
    pn.pane.Markdown("### 🧍 People Flow", styles={'margin-bottom': '10px'}),
    view_selector,
    plot_pane,
    sizing_mode='stretch_width'
)

def people_comparison_panel():

    return pn.Card(
        people_flow_panel,
        title="People Flow",
        margin=10,
        width=850,
        styles={"border-radius": "12px", "box-shadow": "0 2px 8px rgba(0,0,0,0.1)", "padding": "10px"}
    )

def visitor_demography_card():
    # Sample data
    gender_data = pd.DataFrame({
        'Gender': ['Male', 'Female'],
        'Count': [120, 95]
    })

    age_data = pd.DataFrame({
        'Age Group': ['Adult', 'Elder', 'Child'],
        'Count': [150, 30, 35]
    })

    # Pie Charts
    gender_pie = px.pie(
        gender_data, names='Gender', values='Count', title='Gender Distribution',
        color_discrete_sequence=px.colors.sequential.RdBu
    )

    age_pie = px.pie(
        age_data, names='Age Group', values='Count', title='Age Group Distribution',
        color_discrete_sequence=px.colors.sequential.Aggrnyl
    )

    return pn.Card(
        pn.Row(
            pn.pane.Plotly(gender_pie, config={'displayModeBar': False}, width=400, height=300),
            pn.pane.Plotly(age_pie, config={'displayModeBar': False}, width=400, height=300)
        ),
        title="Visitor Demographics",
        collapsible=True,
        width=850,
        margin=10
    )
    
def get_percentage_change(current, previous):
    if previous == 0:
        return "N/A"
    change = ((current - previous) / previous) * 100
    arrow = "▲" if change >= 0 else "▼"
    return f"{arrow} {abs(change):.1f}%"

def visitor_summary_card():
    # Simulated visitor counts
    today_visitors = 860
    yesterday_visitors = 790

    this_week_visitors = 5100
    last_week_same_days = 4700

    this_month_visitors = 15800
    last_month_same_days = 14500

    # Percentage change
    today_change = get_percentage_change(today_visitors, yesterday_visitors)
    week_change = get_percentage_change(this_week_visitors, last_week_same_days)
    month_change = get_percentage_change(this_month_visitors, last_month_same_days)

    # Metrics Display
    metrics = pn.Row(
        pn.Column(
            pn.pane.Markdown("### Today"),
            pn.indicators.Number(name="Visitors", value=today_visitors, format="{value}"),
            pn.pane.Markdown(f"**Change from Yesterday:** {today_change}")
        ),
        pn.Spacer(width=40),
        pn.Column(
            pn.pane.Markdown("### This Week"),
            pn.indicators.Number(name="Visitors", value=this_week_visitors, format="{value}"),
            pn.pane.Markdown(f"**Change from Last Week:** {week_change}")
        ),
        pn.Spacer(width=40),
        pn.Column(
            pn.pane.Markdown("### This Month"),
            pn.indicators.Number(name="Visitors", value=this_month_visitors, format="{value}"),
            pn.pane.Markdown(f"**Change from Last Month:** {month_change}")
        ),
    )

    return pn.Card(
        metrics,
        title="Visitor Summary",
        collapsible=True,
        width=850,
        margin=10
    )
