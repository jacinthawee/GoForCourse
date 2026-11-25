import streamlit as st

st.set_page_config(page_title="Courses", page_icon="🧑‍🏫")
st.markdown("# Courses")
if "avatar" not in st.session_state:
    st.session_state.avatar = False

personalised, all_courses = st.tabs(["For You", "All Courses"])

with personalised:
    if st.session_state.avatar:
        c1 = st.container()
        c2 = st.container()
        c3 = st.container()
        match st.session_state.avatar:
            case "expert":
                c1.write("""GMS201: Making Expert Clinical Thinking visible  \n06:30""")
                c2.write("""GMS202: From Clinical Expert to Effective Educator  \n04:35""")
            case "formal_authority":
                c1.write("""GMS301: Balancing Guidance and Learner Independence  \n05:44""")
                c2.write("""GMS302: Setting Standards and Providing Constructive Feedback  \n06:15""")
            case "personal_model":
                c1.write("""GMS401: Designing Effective Demonstration-Based Learning  \n06:32""")
                c2.write("""GMS402: Assessing Clinical Skills Through Direct Observation  \n04:50""")
            case "facilitator":
                c1.write("""GMS501: Designing Learner-Centred Clinical Learning Experiences  \n07:19""")
                c2.write("""GMS502: The Art of Asking Powerful Questions  \n05:54""")
            case "delegator":
                c1.write("""GMS601: Matching Autonomy to Learner Readiness — Use graduated responsibility and entrustment principles.  \n06:20""")
                c2.write("""GMS602: Supervision Without Micromanagement — Balance learner independence with appropriate clinical oversight.  \n04:57""")
                c3.write("""GMS603: Closing the Feedback Loop — Use brief check-ins, direct observation and timely feedback.  \n05:24""")
    else:
        c = st.container()
        c.write("Find out your teaching style before getting curated courses!")
        st.page_link("pages/1_Questionnaire.py", label="Go To Questionnaire", icon="🖋️")


with all_courses:
    st.image("photos/course_matrix.jpg")
    # c1 = st.container()
    # c2 = st.container()
    # c3 = st.container()
    # c1.write("""#### PLAN  \nGMS202 From Clinical Expert to Effective Educator  \n04:35  \nGMS404: Planning Clinical Skills Demonstrations  \n05:06""")
    # c2.write("""#### TEACH  \nGMS303 Delivering Structured and Engaging Teaching Sessions  \n06:40  \nGMS502: The Art of Asking Powerful Questions  \n05:54""")
    # c3.write("""#### ASSESS  \nGMS402: Assessing Clinical Skills Through Direct Observation  \n04:50  \nGMS305: Designing Effective OSCE Stations  \n07:14""")
    # # c1.write("""For the Expert  \nGMS267: Making Expert Clinical Thinking visible \n06:30  \nGMS274: From Clinical Expert to Effective Educator \n04:35""")
    # # c2.write("""For the Formal Authority  \nGMS302: Balancing Guidance and Learner Independence  \n05:44  \nGMS311: Setting Standards and Providing Constructive Feedback  \n06:15""")
    # # c3.write("""For the Personal Model  \nGMS409: Designing Effective Demonstration-Based Learning  \n06:32  \nGMS423: Assessing Clinical Skills Through Direct Observation  \n04:50""")
    # # c4.write("""For the Facilitator  \nGMS500: Designing Learner-Centred Clinical Learning Experiences  \n07:19  \nGMS511: The Art of Asking Powerful Questions  \n05:54""")
    # # c5.write("""For the Delegator  \nGMS627: Designing Self-Directed Clinical Learning Experiences  \n06:20  \nGMS636: Empowering Learners Through Guided Independence  \n04:57""")
        