import streamlit as st
import string
from main import RandomPasswordGenerator, MemorablePasswordGenerator, PinNumberGenerator

st.set_page_config(
    page_title="Password Generator",
    page_icon=":lock:",
    layout="wide",
)

'''
# Password Generator Dashboard
Generate secure and memorable passwords or PIN numbers using the options below.'''

col1, col2, col3 = st.columns(3)

with col1:
    left_cell = col1.container(border=True,)
    with left_cell:
        st.markdown("### Random Password")
        pass_len = st.slider("Password length", 8, 16, 12)
        st.write("Include in password:")
        prefrences = [st.checkbox('Numbers'), st.checkbox('Special Characters')]
        random_password = RandomPasswordGenerator(pass_len, prefrences[0], prefrences[1])
        if st.button("Generate Random Password"):
            st.write(random_password.generate())

with col2:
    middle_cell = col2.container(border=True,)
    with middle_cell:
        st.markdown("### Memorable Password")
        word_count = st.slider("Number of words", 4, 8, 5)
        separator = st.text_input("Separator", "-", max_chars=1)
        capitalize = st.checkbox("Capitalize Words")
        memorable_password = MemorablePasswordGenerator(word_count, separator, capitalize)
        if st.button("Generate Memorable Password"):
            if not separator in string.punctuation:
                st.error("You should use a special characther as seperator!")
            else:
                st.write(memorable_password.generate())

with col3:
    right_cell = col3.container(border=True,)
    with right_cell:
        st.markdown("### PIN Number")
        pin_length = st.slider("PIN length", 7, 14, 10)
        pin_number = PinNumberGenerator(pin_length)
        if st.button("Generate PIN Number"):
            st.write(pin_number.generate())
