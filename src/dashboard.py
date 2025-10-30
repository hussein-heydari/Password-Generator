import streamlit as st
from main import RandomPasswordGenerator, MemorablePasswordGenerator, PinNumberGenerator

st.title("WELCOME TO MY PASSWORD GENERATOR!", width="content")

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Random Password")
        pass_len = st.slider("Password length", 10, 20)
        st.write("Include in password:")
        prefrences = [st.checkbox('Numbers'), st.checkbox('Special Characters')]
        random_password = RandomPasswordGenerator(pass_len, prefrences[0], prefrences[1])
        if st.button("Generate Random Password"):
            st.write(random_password.generate())

    with col2:
        st.markdown("### Memorable Password")
        word_count = st.slider("Number of words", 3, 8)
        separator = st.text_input("Separator", "-")
        capitalize = st.checkbox("Capitalize Words")
        memorable_password = MemorablePasswordGenerator(word_count, separator, capitalize)
        if st.button("Generate Memorable Password"):
            st.write(memorable_password.generate())

    with col3:
        st.markdown("### PIN Number")
        pin_length = st.slider("PIN length", 3, 8)
        pin_number = PinNumberGenerator(pin_length)
        if st.button("Generate PIN Number"):
            st.write(pin_number.generate())