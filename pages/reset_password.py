import streamlit as st
import csv


def is_temp_pass_correct(temp_password, email):
    generated_password = st.session_state["reset_password"]
    # generated_password = st.session_state["reset_password"]
    session_email = st.session_state["email"]

    if generated_password == temp_password and session_email == email:
        return True
    return False


def updated_file_content():
    modified_list = []
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            # st.write(row)
            row = list(row)

            if row[2] == email:
                row[3] = new_password1
                is_found = True
            modified_list.append(row)
    if is_found:
        return modified_list
    else:
        return None


def write_content(list):
    with open("users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list)
    st.success("Password reset successfully!")


def reset_password(email, new_password1, new_password2, temp_password):
    if is_temp_pass_correct(temp_password, email):
        if new_password1 == new_password2:
            if updated_file_content() is not None:
                modified_list = updated_file_content()
                write_content(modified_list)
            else:
                st.error("User Not Registered! ")
        else:
            st.error("Please write the same new password!")
    else:
        st.error("Please correct the temporart password!")


with st.container():

    email = st.text_input(label="Email", placeholder="Enter your email")

    temp_password = st.text_input(
        label="Temporary Password",
        placeholder="Enter your password received in email",
    )

    new_password1 = st.text_input(
        label="New Password",
        type="password",
        placeholder="Enter New strong password",
    )

    new_password2 = st.text_input(
        label="Re-enter New Password",
        type="password",
        placeholder="Re-enter New Password",
    )
    st.button(
        "Reset Password",
        on_click=reset_password,
        args=([email, new_password1, new_password2, temp_password]),
    )
