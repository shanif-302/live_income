import pandas as pd
import numpy as np
import streamlit as st
import time
import plotly.express as px

st.set_page_config(
    page_title = "Income Live Dashboard",
    page_icon="💸",
    layout = "wide"
)

st.title("💸 Live Income Data Monitoring App")

# Load Data
df = pd.read_csv("income_data.csv")


# Filter
job_filter = st.selectbox("Choose a job",df["occupation"].unique())
df = df[df["occupation"] == job_filter]

place_holder = st.empty()

for duration in range(300):
    # Generate Random Data
    df["new_age"] = df["age"]*np.random.randint(1,5,size = len(df))
    df["whpw_new"]  = df["hours-per-week"]*np.random.randint(1,5,size = len(df))

    # KPI Calculations
    avg_age = np.mean(df["new_age"])

    count_married = int(

        df[df["marital-status"] == "Married-civ-spouse"]["marital-status"].count()
        + np.random.randint(1,30)

    )

hpw = np.mean(df["whpw_new"])

with place_holder.container():
    # KPI's
    kpi1, kpi2, kpi3 = st.columns(3)

    kpi1.metric("Average Age",round(avg_age),round(avg_age) - 10)
    kpi2.metric("Count of Married", count_married, 10 + count_married)
    kpi3.metric("Working Hours/Week",round(hpw),round(count_married / (hpw+1)) / 8)

    # Charts

    figCol1,figCol2 = st .columns(2)

    with figCol1:
        st.markdown("### Age vs Martial Status")

        fig = px.density_heatmap(
            data_frame = df,
             x = "marital-status",
             y = "new_age"
        )

        fig.update_layout(
            xaxis_title = "Martial Status",
            yaxis_title = "Age"
        )

        st.plotly_chart(fig, use_container_width=True)

    with figCol2:
        st.markdown("### Age Distribution")

        fig2 = px.histogram(df,x = "new_age")
        fig2.update_layout(xaxis_title = "Age")

        st.plotly_chart(fig2, use_container_width = True)

    # Data Table
    st.markdown("### Data View As Per Selection")
    st.dataframe(df)

time.sleep(1)






