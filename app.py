import streamlit as st
import random
import time

from vector_store import transform
from utils import utilities
from retreiver import db_retreiver
from models import base_model

st.sidebar.image(r"/home/ec2-user/environment/talk_to_code/resources/demo1.jpg", use_column_width=True)
st.title("J.A.C.O.S")
st.markdown("Just AI code optimization system.")
utilities.set_model()
pyspark_results , all_guideline_docs  = db_retreiver.get_db_data()
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Accept user input
if prompt := st.chat_input("How can i help you !!! "):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Streamed response emulator
def response_generator():

  print(prompt)
  if prompt:
    final_logs = db_retreiver.get_logs_data(prompt)
    out = base_model.execute(pyspark_results , all_guideline_docs , final_logs,prompt)
    print("*******************")
    print(out)
    for word in out:
        yield word + " \n"
        time.sleep(0.05)

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})