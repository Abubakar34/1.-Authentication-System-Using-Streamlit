import streamlit as st
import csv


def is_username_already_taken(username, email):
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for user in reader:
            if user[1] == username or user[2] == email:
                return True

    return False


def is_file_empty():
    with open("users.csv", "r") as file:
        if next(file, None) is None:
            return True

    return False


def clear():
    name = username = email = password = ""


def register_user(name, username, email, password):
    is_first_user = False
    is_username_taken = False

    with open("users.csv", "a") as file:
        # reader = csv.reader(file)

        if is_file_empty():
            file.write(f"{name},{username},{email},{password}\n")
            st.success("Account Created Successfully")
            is_first_user = True

        else:
            # Checking if user already exists
            if is_username_already_taken(username, email) == True:
                st.error("Username or Email already taken")
                return
            # If user does not exist already
            else:
                file.write(f"{name},{username},{email},{password}\n")
                st.success("Account Created Successfully")
    clear()


with st.container():

    name = st.text_input(label="Name", placeholder="Enter your name")
    username = st.text_input(label="Username", placeholder="Enter a unique username")
    email = st.text_input(label="Email", placeholder="Enter your email")
    password = st.text_input(
        label="Password",
        type="password",
        placeholder="Create a strong password",
    )
    st.button(
        "Register", on_click=register_user, args=(name, username, email, password)
    )
