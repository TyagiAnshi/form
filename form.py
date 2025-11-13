import streamlit as st 

st.title("Form Demo")
form_values = {
    "name" : None,
    "age" : None,
    "dob" : None,
    "gen" : None,
    "location" : None
}
with st.form(key = "Text Form"):
 st.subheader("Text Inputs")
 name = st.text_input("Enter your Name")
 location = st.text_input("Enter your Location")
 age = st.number_input("Enter your age: ")
 feedback = st.text_area("Provide feedback")
 
 st.markdown("## Date and Time Inputs")
 dob = st.date_input("Select your Birth Date")
 time = st.time_input("Select your Preferred Working Hours")

 st.markdown("## Selectors Inputs")
 preferred_loc = st.radio("Select your prefered location: ",["Delhi","Banglore","Gurgaoon","Kerela"])
 gen = st.selectbox("Select your Gender: ",["Male","Female","Other","Don't want to reveal"])
 salary = st.slider("Your Expected Salary: ",50000 , 100000)

 st.markdown("## Toggles & Checkboxes")
 check1 =st.checkbox("Your can work 9-5")
 check2 = st.checkbox("Your can work on weekends")
 check3 = st.checkbox("Your can work part-time")
 submit=st.form_submit_button(label="Submit")
 if submit:
   if not name or not location or not age or not dob or not gen:
       st.warning("Please fill in all of the Fields")
   else:
       st.success("Submitted")
       st.balloons()
       for(key,values) in form_values.items():
           st.write(f"{key}:{values}")

st.button("Click me") 
st.markdown("[Link](https://github.com/TyagiAnshi)")

