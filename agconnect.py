import streamlit as st
from datetime import datetime

# ---- App Config ----
st.set_page_config(page_title="Agknow", layout="wide", page_icon="🌱")

# ---- Custom CSS for Styling ----
st.markdown("""
    <style>
        body {
            background-color: #f4f9f4;
        }
        .main {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 1.5rem;
        }
        h1, h2, h3, h4, h5 {
            color: #2f7336;
        }
        .stButton > button {
            background-color: #56ab2f;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }
        .stButton > button:hover {
            background-color: #3b7721;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Sidebar ----
st.sidebar.markdown("""<h1 style='color:#56ab2f;'>🌾 Agknow</h1>""", unsafe_allow_html=True)
st.sidebar.markdown("Empowering the Agricultural Ecosystem 🌱")
user_type = st.sidebar.selectbox("Who are you?", ["Farmer", "Buyer", "Agri-Industry", "Student", "Consumer", "Researcher"])
crop_interest = st.sidebar.text_input("Your Primary Crop Interest (e.g., Tomato)")
st.sidebar.markdown("___")

# ---- Header Section ----
st.markdown("""
<div style="background: linear-gradient(to right, #56ab2f, #a8e063); border-radius: 15px; padding: 30px;">
    <h1 style="color: white; text-align: center;">Agknow: Smart Agri Network</h1>
    <p style="color: #f5f5f5; text-align: center;">Connecting Growers, Buyers, Experts, and Innovators for Sustainable Agriculture</p>
</div>
""", unsafe_allow_html=True)

# ---- Section: Crop Feed ----
st.markdown("### 📢 Crop-Specific Feed")
st.markdown(f"#### For: **{crop_interest.title() if crop_interest else 'Your Crop'}**")

col1, col2 = st.columns([2, 1])

with col1:
    with st.container():
        st.info("🔍 **New Tomato Pesticide Launched** - Try 'BioBlast X' for pest resistance")
        st.success("🤝 **Nearby Tomato Farmer Meetup** - June 15, Madurai")
        st.warning("📉 **Tomato Market Prices Dropping** - Consider Storage Options")
        st.info("🏭 **Ketchup Industry in Chennai** looking for 5T/day Tomato Supply")
        st.success("📚 **Free Webinar**: 'New Tech in Tomato Cultivation' on May 20")

with col2:
    with st.container():
        st.metric("📈 Today’s Market Price", "₹14/kg", "+₹2")
        st.metric("🏆 Top Buyer Nearby", "FreshKart Ltd.")
        st.button("🌟 View All Opportunities")

# ---- Section: Connect ----
st.markdown("### 🌐 Connect with Agri Stakeholders")
connect_type = st.selectbox("Choose Group to Connect", ["Farmers", "Buyers", "Industries", "Experts", "Students"])

with st.container():
    if connect_type == "Farmers":
        st.success("👩‍🌾 **Ramesh Kumar** – Organic Tomato Grower, Salem")
        st.success("👩‍🌾 **Lakshmi Devi** – Greenhouse Tomato Farmer, Erode")
    elif connect_type == "Buyers":
        st.warning("🏪 **AgriBazaar Pvt. Ltd.** – Tomato Buyer (Bulk), Coimbatore")
        st.warning("🏪 **TomatoKing Exports** – Export Quality Tomatoes")
    elif connect_type == "Industries":
        st.info("🏭 **RedGold Ketchup** – Requires 5T/day Supply")
    elif connect_type == "Experts":
        st.info("🎓 **Dr. Anjali** – Tomato Disease Specialist, TNAU")
        st.info("🎓 **Mr. Senthil** – Smart Irrigation Consultant")
    else:
        st.info("👨‍🎓 **Arun R** – Final Year Agri Student, Project on Tomato Tech")

# ---- Section: Share Your Post ----
st.markdown("### 📣 Share Your Update")
with st.form("post_form"):
    post_text = st.text_area("What's happening in your field, market, or lab?", height=150)
    file = st.file_uploader("Upload Image or Report", type=["jpg", "png", "pdf"])
    submitted = st.form_submit_button("🚀 Post Now")
    if submitted:
        st.balloons()
        st.success("✅ Your update has been posted successfully!")

# ---- Section: Events & Trainings ----
st.markdown("### 🎓 Upcoming Events & Webinars")
event_col1, event_col2 = st.columns(2)
with event_col1:
    st.info("🗓️ **Soil Health Workshop** – June 20, Trichy")
    st.info("🗓️ **Certified Organic Farming Course** – Starting June 10")
with event_col2:
    st.info("🗓️ **AI in Agriculture Hackathon** – July 2, Online")

# ---- Section: Jobs & Internships ----
st.markdown("### 💼 Jobs & Internships")
job_col1, job_col2 = st.columns(2)
with job_col1:
    st.warning("🔎 **Field Officer (Tomato Contracts)** – TomatoKing Exports")
    st.success("🎓 **Internship: Smart Agri Devices** – Final Year Project, Coimbatore")
with job_col2:
    st.info("💼 **Agri-Marketing Manager** – FreshKart Ltd.")
    st.info("🧪 **Research Intern** – AgriTech Labs, Chennai")

# ---- Footer ----
st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #888;'>
        © 2025 <strong>Agknow</strong> | Made with ❤️ for India's Agricultural Future
    </div>
""", unsafe_allow_html=True)
