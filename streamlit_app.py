import time
import streamlit as st
import pandas as pd
st.title("Student Ranking System")
rank_table = pd.DataFrame(
                         columns = ("Name","English","Hindi","Telugu","Maths","Science","Total Marks","Percentage","Rank")
                         )
def ranked(percent):
  if(percent>=90):
    st.success("You got A+ Grade")
    return "A+"
  elif(80 <= percent <= 89.99):
    st.success("You got A Grade")
    return "A"
  elif(70 <= percent <= 79.99):
    st.success("You got B Grade")
    return "B"
  elif(60 <= percent <= 69.99):
    st.success("You got C Grade")
    return "C"
  elif(50 <= percent <= 59.99):
    st.success("You got D Grade")
    return "D"
  else:
    st.info("Try to get Marks above 50")
    return "Fail"

with st.form("Marks"):
 Name = st.text_input("Name:","Enter your name")
 English_Marks = st.number_input("English:", min_value=0, max_value=100, step=1)
 Hindi_Marks = st.number_input("Hindi:", min_value=0, max_value=100, step=1)
 Telugu_Marks = st.number_input("Telugu:", min_value=0, max_value=100, step=1)
 Maths_Marks = st.number_input("Maths:", min_value=0, max_value=100, step=1)
 Science_Marks = st.number_input("Science:", min_value=0, max_value=100, step=1)
 submitted = st.form_submit_button("Submit")
 
if submitted:
  if not Name:
    st.warning("⚠️ Please enter Name")
  elif not English_Marks:
    st.warning("⚠️ Please enter English mark")
  elif not Hindi_Marks:
    st.warning("⚠️ Please enter Hindi mark")
  elif not Telugu_Marks:
    st.warning("⚠️ Please enter Telugu mark")
  elif not Maths_Marks:
    st.warning("⚠️ Please enter Maths mark")
  elif not Science_Marks:
    st.warning("⚠️ Please enter Science mark")
  else:
    with st.spinner("Wait for Getting results...", show_time=True):
      time.sleep(3)
    total = English_Marks+Hindi_Marks+Telugu_Marks+Maths_Marks+Science_Marks
    percent = total/500 * 100
    rank  = ranked(percent)
    new_row = {
            "Name": Name,
            "English": English_Marks,
            "Hindi": Hindi_Marks,
            "Telugu": Telugu_Marks,
            "Maths": Maths_Marks,
            "Science": Science_Marks,
            "Total Marks": total,
            "Percentage": percent,
            "Rank": rank
        }
    if "data" not in st.session_state:
      st.session_state.data = pd.DataFrame(columns=rank_table.columns)
    st.session_state.data = pd.concat([st.session_state.data,pd.DataFrame([new_row])],ignore_index=True)
    st.success(f"Thank you, {Name}")
    st.dataframe(st.session_state.data)
    














