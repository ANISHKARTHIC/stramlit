import streamlit as st

st.markdown("""
    <style>
        .main-title {color: #4CAF50; font-size: 50px; text-align: center; font-weight: bold;}
        .section-header {color: #0056b3; font-size: 26px; font-weight: bold; margin-top: 20px;}
        .subsection-header {color: #444; font-size: 20px; font-weight: bold;}
        .info {font-size: 16px; line-height: 1.6;}
        .contact-links a {text-decoration: none; color: #4CAF50; font-weight: bold;}
        .container {background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);}
        .social-icons {text-align: center; margin-top: 20px;}
        .social-icons a {margin: 0 10px; text-decoration: none; font-size: 30px; color: #333;}
        .social-icons a:hover {color: #4CAF50;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Anish Karthic's Portfolio</div>", unsafe_allow_html=True)

st.write("Hi, I am Anish Karthic from the Department of Artificial Intelligence and Data Science.")
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.image("I.png", width=200)

st.write("""
    I am a BTech student specializing in Artificial Intelligence and Data Science, currently in my first year. 
    I am fascinated by technology's potential to solve real-world problems and am particularly interested in 
    developing innovative solutions that enhance efficiency and improve user experiences. In addition to my studies, 
    I’m expanding my knowledge through practical projects and collaborations within the tech community.
""")


tab1, tab2, tab3 = st.tabs(["Education", "Certificates", "Contact"])

with tab1:
    st.markdown("<div class='section-header'>Education Qualification</div>", unsafe_allow_html=True)
    st.write("**B.Tech in Artificial Intelligence and Data Science** - 1st Year")
    st.write('''
        - **College**: [KGISL Institute of Technology](https://www.kgkite.ac.in/)
        - **Location**: Saravanampatti, Coimbatore
    ''')
    
    st.markdown("<div class='section-header'>Skills</div>", unsafe_allow_html=True)
    st.write('''
        - **Programming Languages**: Python, C++, HTML, CSS
        - **Frameworks & Libraries**: Django, Streamlit, Pandas (Currently Learning)
        - **Database**: SQLite
        - **Tools & Technologies**: Git, Visual Studio Code
        - **Soft Skills**: Teamwork, Problem Solving, Communication
    ''')

with tab2:
    st.markdown("<div class='section-header'>Certificates</div>", unsafe_allow_html=True)
    st.write("- [Data Analysis Using Python - by IBM](https://www.credly.com/badges/eaa605c9-2c93-42ae-8237-033bf5a394a0/linked_in_profile)")
    st.write("- [Excel for Beginners - by Great Learning](https://www.mygreatlearning.com/certificate/WEACJTQA)")

with tab3:
    st.markdown("<div class='section-header'>Contact Me</div>", unsafe_allow_html=True)
    st.write("Feel free to reach out!")
    st.markdown("""
            <div class='social-icons'>
                <a href="https://github.com/ANISHKARTHIC" target="_blank"><i class="fab fa-github"></i><span class='social-name'>GitHub</span></a>
                <a href="mailto:anishkarthicvs@gmail.com" target="_blank"><i class="fas fa-envelope"></i><span class='social-name'>Email</span></a>
                <a href="https://www.linkedin.com/in/anish-karthic-7583b7329" target="_blank"><i class="fab fa-linkedin"></i><span class='social-name'>LinkedIn</span></a>
                  <a href="https://www.instagram.com/i_am_ak_anish/profilecard/?igsh=MWozMWRwOHJuZmQ2cA==" target="_blank"><i class="fab fa-instagram"></i><span class='social-name'>Instagram</span></a> <!-- Instagram link -->
            </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)
