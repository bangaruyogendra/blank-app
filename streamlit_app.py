import streamlit as st
import pandas as pd
st.title("Student Ranking System")
rank_table = pd.DataFrame(
                         columns = ("Name","English","Hindi","Telugu","Maths","Science","Total Marks","Percentage","Rank")
                         )
st.write(
    rank_table
)
