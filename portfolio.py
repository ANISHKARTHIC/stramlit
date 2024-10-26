import streamlit as st

st.title("Anish karthic's Portfolio")
st.write("Hi, Iam Anish Karthic department of ARTFICIAL INTELLIGENCE AND DATA SCIENCE ")

col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths
with col3:
    st.image("anish.jpg", width=100, caption="Anish Karthic") 
with col1:
    st.write(''':orange[LANGUAGES KNOWN ]
    \n:orange[NO OF PROJECTS]
    \n :orange[TOOLS]
    \n :red[INTERNSHIPS] 
    \n :red[CERTIFICATIONS AND TRAINING]
    \n :green[EXTRA CURICULAR  ]
    \n :green[HOBBIES ]''')
    
with col2:
    st.write(''' \n:    Python , C++ , Html, Css                 
     \n :      5
     \n : VS code
     \n :   with ibm
     \n : Data Analysis with python certified by ibm in great learning
     \n : dance 
     \n : chess and listning music ''')
st.write(":blue[I'm passionate about developing projects that solve real-world problems.]")
st.write("""
- **Email**: anishkarthicvs@gmail.com
- **LinkedIn**: [linkedin.com/in/anishkarthic](https://www.linkedin.com/in/anish-karthic-7583b7329)
""")
