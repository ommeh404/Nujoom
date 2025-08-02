# Nujoom Business Intelligence Dashboard

This repository contains a data-driven business intelligence project for **Nujoom**, a fast-growing food delivery platform. The project evaluates partner restaurant performance, CRM engagement, campaign uplift, and churn risk through integrated data modeling and visualization.

## 📊 Project Overview

The objective was to build an end-to-end analytics solution for internal business stakeholders to:
- Track restaurant KPIs (revenue, orders, ratings, delivery times)
- Analyze the impact of marketing campaigns
- Correlate CRM activity with churn likelihood
- Identify high-potential accounts and at-risk partners
- Enable data-driven decision-making through interactive Power BI dashboards

## 🧠 Key Insights
- CRM consistency strongly correlates with retention — frequent manager contact reduces churn.
- Campaign effectiveness varies: **Combo Offers** lead, while **Free Delivery** showed negative lift in some cases.
- Order volume is the biggest driver of revenue — not delivery time or ratings.
- Several high-lift restaurants are still at risk of churn — deeper interventions are needed.

## 📁 Contents

| File | Description |
|------|-------------|
| `dashboard.pbix` | Power BI dashboard file |
| `campaign_uplift_analysis.csv` | Campaign performance metrics |
| `restaurant_performance_summary.csv` | Aggregated restaurant KPIs |
| `crm_interactions.csv` | CRM interaction logs |
| `orders.csv` | Raw order data |
| `account_managers.csv` | Manager details |
| `campaigns.csv` | Campaign metadata |
| `restaurants.csv` | Restaurant master data |
| `*.py` scripts | Python preprocessing and churn model |
| `sql tables.sql` | SQL schema for relational setup |

## 🛠️ Tech Stack

- **Power BI** – Visual analytics and dashboard creation
- **Python (pandas, matplotlib)** – Data cleaning, transformation, modeling
- **SQL** – Data extraction, transformation, schema design
- **DAX** – Custom measures and calculated columns in Power BI

## 🚀 Setup Instructions

1. Clone the repository
2. Load data into Power BI using `dashboard.pbix`
3. Run preprocessing via Python scripts (optional for analysis)
4. Use `sql tables.sql` to recreate relational model (optional)

## 📈 Outcomes

The BI system enabled the Nujoom team to:
- Align CRM resource allocation with retention outcomes
- Quantify campaign ROI by restaurant and campaign type
- Proactively identify churn-prone accounts
- Uncover performance gaps and replication opportunities across managers

---

**Author**: [Om]  
**Role**: Business Analyst  
**Organization**: Nujoom

---

