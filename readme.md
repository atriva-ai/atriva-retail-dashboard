
```markdown
# 🛍️ Retail AI Dashboard

Smarter store insights through real-time video analytics.

This dashboard visualizes people flow, visitor demographics, and camera analytics powered by edge AI. Built with [Panel](https://panel.holoviz.org/) and [Plotly](https://plotly.com/), it is designed for use with Jetson, Rockchip, and other edge devices.

## 🚀 Features

- 📈 **People Flow Analytics**: Hourly, daily, and weekly comparison of foot traffic
- 🎯 **Demographics Insight**: Gender and age group distribution via pie charts
- 📹 **Camera Monitoring**: Real-time connected/disconnected status
- 🔍 **Zone Details**: Insights into specific store zones
- 📊 **Visitor Summary Cards**: Compare today's, this week's, and this month's visitors with historical data
- ⚡ Designed for edge inference devices and integrates with FastAPI

## 🖥️ UI Overview

- **Header**: Logo, dashboard title, and subtitle
- **Tabs**: Dashboard, Camera Setup, Zone Details
- **Cards**: Organized metrics and charts in a responsive layout

## 🧱 Tech Stack

- Python 3.12+
- Panel
- Plotly
- Pandas
- Numpy
- FastAPI (backend integration)
- Docker (optional)

## 📂 Project Structure

retail-ai-dashboard/
├── app.py                  # Main Panel application
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── src/
    ├── components/
    │   ├── people_flow.py         # People flow logic and charts
    │   ├── visitor_summary.py     # Visitor summary stats and deltas
    │   └── demographics.py        # Gender and age pie charts
    └── layout/
        ├── header.py              # Dashboard header with title and logo
        ├── home.py                # Main dashboard view
        ├── camera_setup.py        # Camera configuration view
        └── zone_details.py        # Zone monitoring view

## 🐳 Run with Docker

```bash
docker build -t retail-ai-dashboard .
docker run -p 5006:5006 retail-ai-dashboard
```

## ⚙️ Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/retail-ai-dashboard.git
   cd retail-ai-dashboard
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   panel serve app.py --autoreload --show
   ```

## 📈 Screenshots

> (Add dashboard screenshots or gifs here to showcase features)

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

**Made with ❤️ by Atriva**
```