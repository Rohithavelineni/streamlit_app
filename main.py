import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

#information
st.set_page_config(layout="wide")
st.title('Coffe Chain Analytics')
with st.expander('About this app'):
  st.write('')
  #st.image('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', width=400)

coffe_data=pd.read_csv(r"C:\Users\Tk447\Desktop\Fall\Visual_Analytics_5122\streamlit\ro\data\CoffeeChainmid.csv")

st.write(coffe_data)

st.sidebar.header("Pick two variables for your scatterplot")
x_val=st.sidebar.selectbox("Pick your x-axis",coffe_data.select_dtypes(include=np.number).columns.tolist())
y_val=st.sidebar.selectbox("Pick your y-axis",coffe_data.select_dtypes(include=np.number).columns.tolist())

scatter =alt.Chart(coffe_data,title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip=[x_val,y_val]
)

st.altair_chart(scatter,use_container_width=True)

corr=round(coffe_data[x_val].corr(coffe_data[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")

st.header("Heading")

barchart=alt.Chart(coffe_data).mark_bar().encode(
    x='Margin',
    y='sum(Inventory)',
    color='Market',
    tooltip=[x_val,y_val]
)
st.altair_chart(barchart,use_container_width=True)







