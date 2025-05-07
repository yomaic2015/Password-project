import streamlit as st
from main import gen_password, checker, entropy

st.set_page_config(page_title="Password Strength Checker", layout="centered")

st.title("🔐 Password Strength Checker")
st.write("Use this tool to check how secure your password is. You can also generate a strong one automatically.")

# Handling session state
if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""

# creating a Form Section
with st.form("password_form"):
    st.subheader("Password Options")

    use_generated = st.checkbox("Use generated password", value=False)

    regenerate_password = st.form_submit_button("🔁 Regenerate Password")
    if regenerate_password:
        st.session_state.generated_password = gen_password(16)
        st.success("New password generated!")

    if use_generated:
        user_password = st.text_input("Your Password:", value=st.session_state.generated_password, type="password")
    else:
        user_password = st.text_input("Enter Your Password:", type="password")

    submitted = st.form_submit_button("Check My Password")

if submitted and user_password:
    st.subheader("🔍 Password Check:")

    feedback_list = checker(user_password)
    for feedback in feedback_list:
        if "✅" in feedback:
            st.success(feedback)
        else:
            st.warning(feedback)

    st.subheader("🔐 Password Strength:")

    strength_info = entropy(user_password)

    # Extract just the label ("Very Weak", "Weak", etc.)
    strength_label = strength_info.split("—")[-1].strip()

    # Show strength with message and progress bar
    if strength_label == "Very Weak":
        st.error(f"⚠️ {strength_info}")
        st.progress(0.2)
    elif strength_label == "Weak":
        st.warning(f"⚠️ {strength_info}")
        st.progress(0.4)
    elif strength_label == "Moderate":
        st.info(f"🟠 {strength_info}")
        st.progress(0.7)
    else:
        st.success(f"✅ {strength_info}")
        st.progress(1.0)
