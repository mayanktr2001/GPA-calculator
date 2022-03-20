import streamlit as st

st.set_page_config( page_title = "GPA Calculator IPU", page_icon = ":memo:") 
def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0
    
    return grade
def calculator(sem):
    theory_sub = {}
    practical = {}
    GPA = 0
    flag = 0  
    credits = 0
    col1, col2 = st.columns(2)  

    if sem == 1 :
        theory_sub = { 'Applied. Mathematics-I' : 4, 'Applied Physics-I' : 3, 'Manufacturing Processes' : 3, 'Electrical Technology' : 3, 'Human Values and professional ethics (HVPE)' : 1, 'Fundamentals of Computing' : 2, 'Applied Chemistry' : 3 }
        practical = { 'Applied Physics Lab-I' : 1, 'Elecrical Technology Lab' : 1, 'Workshop Lab' : 2, 'Engineering Graphics Lab' : 2, 'FOC Lab' : 1, 'Applied Chemistry Lab' : 1 }
        credits = 27

    elif sem == 2:
        theory_sub = { 'Applied Mathematics-II' : 4, 'Applied Physics-II' : 3, 'Electronic Devices' : 3, 'Introduction To Programming' : 3, 'Engineering Mechanics' : 3, 'Communication Skills' : 3, 'Environmental Studies' : 3 }
        practical = { 'Applied Physics Lab-II' : 1, 'ITP Lab' : 1, 'Electronics Lab' : 1, 'Engineering Mechanics Lab' : 1, 'EVS Lab' : 1 }
        credits = 27

    elif sem == 3:
        theory_sub = { 'Applied Mathematics-III' : 4, 'Analog Electronics-I' : 4, 'Switching Theory & Logic Design' : 4, 'Electronic Instruments andMeasurements' : 4, 'Data Structures' : 4, 'Signals and Systems' : 4 }
        practical = { 'AE Lab' : 1, 'STLD lab' : 1, 'EIM Lab' : 1, 'DS Lab' : 1, 'SnS Lab' : 1 }
        credits = 29

    elif sem == 4:
        theory_sub = { 'Applied Mathematics-IV' : 4, 'Analog Electronics-II' : 4, 'Network Analysis and Synthesis' : 4, 'Communication Systems' : 4, 'Electromagnetic Field Theory' : 3, 'Computer Organization and Architecture' : 3 }
        practical = { 'Applied Mathematics Lab' : 1, 'NAS Lab' : 1, 'CS Lab' : 1, 'AE-II Lab' : 1, 'COA lab' : 1 }
        credits = 27

    elif sem == 5:
        theory_sub = { 'Communication Skills for Professionals' : 1, 'Digital Communication' : 4, 'Microprocessors and Microcontrollers' : 4, 'Control Systems' : 4, 'Digital System Design' : 4, 'Industrial Management' : 3 }
        practical = { 'CSP Lab' : 1, 'DSD lab' : 1, 'CS Lab' : 1, 'M and M LAb' : 1, 'DC Lab' : 1, 'Industrial training workshop' : 1 }
        credits = 26

    elif sem == 6:
        theory_sub = { 'Microwave Engineering' : 4, 'Information Theory and Coding' : 4, 'Digital Signal Processing' : 4, 'VLSI Design' : 3, 'Data Communication and Networks' : 4, 'Antenna and Wave Propagation' : 4 }
        practical = { 'ME Lab' : 1, 'VLSI design Lab' : 1, 'DSP Lab' : 1, 'DCN Lab' : 1, 'Industrial house training' : 1 }
        credits = 29

    elif sem == 7:
        theory_sub = { 'Embedded Systems' : 4, 'Optoelectronics and Optical Communication' : 4, 'Wireless Communication' : 4, 'Advanced DSP' : 3, 'Radar and Navigation' : 3 }
        practical = { 'OnWC Lab' : 1, 'ES Lab' : 1, 'Advanced DSP Lab' : 1, 'Seminar' : 1, 'Minor project' : 3, 'Industrial Training' : 1 }
        credits = 26

    elif sem == 8:
        theory_sub = { 'HVPE-II' : 1, 'Satellite Communication' : 4, 'AD HOC and sensors netowrk' : 3, 'Consumer Electronics' : 3, 'Robotics' : 3 }
        practical = { 'SnA Lab' : 1, 'Robotics Lab' : 1, 'Major project' : 8 }
        credits = 24
    

    with col1:
        with st.expander("Theory subject"):
            for subject in theory_sub:
                marks = st.number_input("{}:".format( subject ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * theory_sub[subject]

    with col2:
        with st.expander("Practical subject"):
            for lab in practical:
                marks = st.number_input("{}:".format( lab ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * practical[lab]

    if flag:
        st.warning("Please enter  the marks of all theory_sub!")

    GPA = GPA / credits
    return GPA

    

title1='<h1 style="font-family:Georgia;color:Red; text-align: center;">GPA Calculator IPU</h1>'
title2='<h3 style="font-family:Times;color:rgb(252,3,248); text-align: center;">Semester GPA Calculator of B.Tech(ECE) IPU</h3>'
st.markdown(title1, unsafe_allow_html=True)
st.markdown(title2, unsafe_allow_html=True)

with st.container():
    name = st.text_input("ENTER STUDENT NAME")
    ENROLL = st.text_input("ENTER YOUR ENROLLMENT NUMBER")

    if name:
        st.write("HOW YOU DOINN {}!".format(name))
        sem = st.radio("What's your semester",
     (1, 2, 3, 4, 5, 6, 7, 8))

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h2 style='text-align: center; '>Please Enter Student's Marks!</h2>", unsafe_allow_html=True)

            GPA = calculator(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9) 
            with cl5:
                ans = st.button("Submit")
                
            
            
    
            if ans:
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h2 style='text-align: center; '>{msg}</h2>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.balloons()
                    st.snow()
                    
