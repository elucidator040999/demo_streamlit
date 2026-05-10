import streamlit as st
import pandas as pd

st.title("Deploy Streamlit APP", text_alignment='center')
df = pd.DataFrame([{'Ten': 'Phat','Tuoi': 18, 'Nghe': 'Bi'}])
st.dataframe(df)
if st.button("button"):
    st.balloons()
