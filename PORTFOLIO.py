import streamlit as st

st.title("Anish karthic's Portfolio")
st.write("Hi, I am Anish Karthic department of ARTFICIAL INTELLIGENCE AND DATA SCIENCE ")
c1,c2,c3=st.columns([1,2,1])
with c2:
    st.image("I.png",width=200,)
st.write(''' I am Anish Karthic, a passionate BTech student specializing in Artificial Intelligence and Data Science.
          Currently in my first year, I am fascinated by technology and its potential to solve real-world problems. 
         I am particularly interested in developing innovative solutions that enhance efficiency and improve user experiences.
          In addition to my studies, I’m eager to expand my knowledge through practical projects and collaborations within the tech community.''')
if "section" not in st.session_state:
    st.session_state.section = "Home"

# Button-based navigation
col1, col2, col3 = st.columns(3)
if col1.button("EDUCATION"):
    st.session_state.section = "EDUCATION"
if col2.button("CERTIFICATE"):
    st.session_state.section = "CERTIFICATE"
if col3.button("CONTACT"):
    st.session_state.section = "Contact"

# Display content based on the current section
if st.session_state.section == "EDUCATION":
    st.title("EDUCATION QUALIFICATION ")
    st.header('''B.Tech Artificial intelligence and Data Science  ''')
    st.header("I year")
    st.write('''
            - **COLLAGE**:  [KGISL INSTUTION OF TECHNOLOGY](https://www.kgkite.ac.in/)
            - **LOCATION**:  SARAVANAPATTI,COIMBATORE ''')
    st.title("SKILLS")
    st.write('''
            - **PROGRAMMING LANGUAGES KNOWN** : PYTHON , C++ , HTML , CSS. 
            - **FRAMEWORKS AND LIBRARIES** :DJANGO , STREAMLIT ,PANDAS (Currently Learning)
            - **DATABASE** : SQLITE
            - **TOOLS AND TECHNOLOGIES** : GIT , VISUAL STUDIO CODE 
            - **SOFT SKILLS**: TEAMWORK ,PROBLEM SOLVING ,COMMUNICATION 
                ''')
    
    
elif st.session_state.section == "CERTIFICATE":
    st.title("CERTIFICATES")
    st.header("Here are some of my Certificates:")
    st.write("- [Data Analysis Using Python - by  ibm](https://www.credly.com/badges/eaa605c9-2c93-42ae-8237-033bf5a394a0/linked_in_profile)")
    st.write("- [Excel for Beginners - by Great Learning](https://www.mygreatlearning.com/certificate/WEACJTQA)")
elif st.session_state.section == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out!")
    st.write("- GIT HUB :[ANISHKARTHIC](https://github.com/ANISHKARTHIC)")
    st.write("- Email: anishkarthicvs@gmail.com")
    st.write("- LinkedIn: [ANISH KARTHIC LinkedIn Profile](https://www.linkedin.com/in/anish-karthic-7583b7329)")
