import streamlit as st
import csv


def is_authorized(username, password):
    is_found = False
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            # st.write(row)
            if username == row[1] and password == row[3]:
                is_found = True
        if is_found:
            return True
        else:
            return False


# login method to login the user and redirect to the home page
def login(username, password):
    if is_authorized(username, password):
        st.success("** Login Successfully ** ")
    else:
        st.warning("** Invalid Credentials **")


st.set_page_config(
    page_title="Login",
    page_icon="👋",
)
with st.container():

    username = st.text_input(label="Username", placeholder="Enter your username")
    password = st.text_input(
        label="Password",
        type="password",
        placeholder="Enter your password",
    )

    st.button("Login", on_click=login, args=([username, password]))
