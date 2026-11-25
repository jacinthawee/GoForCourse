import streamlit as st

st.set_page_config(page_title="Contact", page_icon="💬")
st.markdown("# Contact your Education Facilitator")

c = st.container()
c.write("Education facilitator: Dr Jason Lee  \nHP: +65 xxxxxxxx  \nEmail: jasonlee@nukedus.edu.sg")
st.image("photos/drjason.png", caption="Dr Jason Lee :)")

# prompt = st.chat_input("Say hi to your education facilitator!")
# if prompt:
#     with st.chat_message("user"):
#         st.write(prompt)
#     with st.chat_message("assistant"):
#         st.write("I'm your education facilitator :)")
