import streamlit as st
import pandas as pd

st.title("Portfolio Scenario Tool")

portfolio_value = st.number_input("Portfolio value", value=1000000)
growth_rate = st.slider("Annual growth rate", -20.0, 20.0, 5.0)
years = st.slider("Years", 1, 10, 5)

values = []

current_value = portfolio_value

for year in range(1, years + 1):
    current_value = current_value * (1 + growth_rate / 100)
    values.append({"Year": year, "Projected Value": current_value})

df = pd.DataFrame(values)

st.dataframe(df)
st.line_chart(df.set_index("Year"))
