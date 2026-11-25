import streamlit_survey as ss
import streamlit as st
import pandas as pd
import plotly.express as px 

st.set_page_config(page_title="Questionnaire", page_icon="🖋️")
st.markdown("# Questionnaire")
st.markdown("### Think about how you usually teach juniors in clinical settings. Rate each statement from 1 to 5  \n##### 1 = Never true of me, 2 = Rarely, 3 = Sometimes, 4 = Often, 5 = Almost always")

survey = ss.StreamlitSurvey()

if "clicked" not in st.session_state:
    st.session_state.clicked = False
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "scores" not in st.session_state:
    st.session_state.scores = False
if "avatar" not in st.session_state:
    st.session_state.avatar = False

def calculate_score(scores):
    expert = scores["Q4"]["value"] + scores["Q13"]["value"] + (6 - scores["Q6"]["value"])
    formal_authority = scores["Q10"]["value"] + scores["Q15"]["value"] + (6 - scores["Q2"]["value"])
    personal_model = scores["Q5"]["value"] + scores["Q9"]["value"] + (6 - scores["Q11"]["value"])
    facilitator = scores["Q1"]["value"] + scores["Q7"]["value"] + (6 - scores["Q14"]["value"])
    delegator = scores["Q3"]["value"] + scores["Q12"]["value"] + (6 - scores["Q8"]["value"])

    st.session_state.scores = {
        "expert": expert,
        "formal_authority": formal_authority,
        "personal_model": personal_model,
        "facilitator": facilitator,
        "delegator": delegator
    }

    st.session_state.clicked = True

def display_radar_chart():
    df = pd.DataFrame(dict(
        r=list(st.session_state.scores.values()),
        theta=list(st.session_state.scores.keys())
    ))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.plotly_chart(fig, alt="Your teaching style")

def display_avatar():
    if st.session_state.scores != False:
        avatar = max(st.session_state.scores, key=st.session_state.scores.get)
        st.session_state.avatar = avatar
        match avatar:
            case "expert": 
                st.image("photos/expert.jpg", caption="You're an Expert - The Knowledge Specialist!  \nStrengths: Identifies essential clinical knowledge; plans comprehensive content; prioritizes accuracy  \nWeaknesses: Overloads sessions with information; may not tailor content to learner level; overlook learner participation")
            case "formal_authority": 
                st.image("photos/formal_authority.jpg", caption="You're a Formal Authority - The Structured Educator!  \nStrengths: Defines clear learning objectives; creates organized teaching plans; aligns with clinical standards  \nWeaknesses: May be rigid; insufficiently adapts plans to learners' needs; promotes passive compliance")
            case "personal_model": 
                st.image("photos/personal_model.jpg", caption="You're a Personal Model - The Role Model!  \nStrengths: Identifies practical skills for demonstration; provides real-world examples; identifies technique-related errors  \nWeaknesses: May not explicitly define objectives; relies on opportunistic observation; allow insufficient learner practice")
            case "facilitator": 
                st.image("photos/facilitator.jpg", caption="You're a Facilitator - The Learning Coach!  \nStrengths: Tailors teaching to learner needs; encourages learner-generated goals; accommodates different approaches  \nWeaknesses: May lack defined outcomes; sessions may become unfocused; learners may feel overwhelmed by questions")
            case "delegator": 
                st.image("photos/delegator.jpg", caption="You're a Delegator - The Independence Builder!  \nStrengths: Promotes learner independence; encourages self-directed learning; builds confidence and ownership  \nWeaknesses: Not suitable for all learner levels; risk of inconsistent learning outcomes; can create learner anxiety")



survey.radio("Q1: When a learner asks me a question, I often respond with a question to get them thinking it through.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q1")

survey.radio("Q2: I'm relaxed about learners doing tasks their own way, even when it differs from the standard approach.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q2")

survey.radio("Q3: I give learners real responsibility for patients or tasks and step in only when needed.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q3")

survey.radio("Q4: I make sure learners hear the correct answer along with the reasoning behind it.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q4")

survey.radio("Q5: I mainly teach by letting learners watch me work and explaining what I'm doing.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q5")

survey.radio("Q6: I tend to hold back my own clinical knowledge so learners can discover things themselves.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q6")

survey.radio("Q7: I guide learners to build their own clinical reasoning rather than telling them what to do.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q7")

survey.radio("Q8: I prefer to stay closely involved in what learners do rather than leaving them to work independently.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q8")

survey.radio("Q9: I try to be a role model whose approach to patients and practice learners can follow.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q9")

survey.radio("Q10: I set clear expectations for how learners should perform tasks and correct them when they deviate.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q10")

survey.radio("Q11: I rarely demonstrate tasks myself; I'd rather learners figure out how by doing them.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q11")

survey.radio("Q12: I encourage learners to find answers themselves or to teach each other.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q12")

survey.radio("Q13: Learners rely on my knowledge and experience to decide what they need to learn.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q13")

survey.radio("Q14: When learners are stuck, I usually tell them what to do rather than prompting their thinking.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q14")

survey.radio("Q15: There is a right way to present a case or do a task, and I expect learners to follow it.", 
            options=[1, 2, 3, 4, 5], 
            horizontal=True,
            id="Q15")

# scores = survey.data
# print(scores["Q1"])

if st.button("Calculate scores"):
    calculate_score(survey.data)
    display_avatar()
    display_radar_chart()

# st.button("Calculate scores", on_click=calculate_score(survey.data))
# if st.session_state.clicked:
#     sc = st.session_state.scores
#     # st.write(sc)
#     display_avatar()
#     display_radar_chart()
#     st.session_state.clicked = False