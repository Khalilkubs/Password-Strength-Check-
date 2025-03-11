import streamlit as st
import re

def check_password_strength(password):
    strength = "Weak"
    suggestions = []
    
    if len(password) < 8:
        suggestions.append("Increase the length to at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Add at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        suggestions.append("Include at least one number.")
    if not re.search(r"[@$!%*?&]", password):
        suggestions.append("Use at least one special character (@, $, !, %, *, ?, &).")
    
    entropy_score = len(password) * (len(set(password)) / len(password))
    
    if len(password) >= 12 and entropy_score > 6 and len(suggestions) == 0:
        strength = "Very Strong"
    elif len(password) >= 8 and len(suggestions) == 0:
        strength = "Strong"
    elif len(password) >= 6 and len(suggestions) <= 2:
        strength = "Moderate"
    
    return strength, suggestions, entropy_score

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")
st.title("🔒 Khalil Password Strength Checker🚀")
st.markdown("""
    *Check the strength of your password and get suggestions to improve it!*
    
    - A strong password should have at least *12 characters*.
    - Include *uppercase, lowercase, numbers, and special characters*.
    - Avoid using common words or patterns.
""")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, suggestions, entropy_score = check_password_strength(password)
    
    st.progress(min(len(password) / 12, 1.0))
    st.subheader(f"Password Strength: {strength}")
    st.write(f"*Entropy Score:* {entropy_score:.2f} (Higher is better)")
    
    if suggestions:
        st.warning("🔍 Improve your password with these tips:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
    else:
        st.success("✅ Your password is very strong!")