import streamlit as st
from datetime import datetime

# ---- App Config ----
st.set_page_config(page_title="AgriConnect", layout="wide", page_icon="🌱")

# ---- Sidebar ----
# Removed logo image
st.sidebar.markdown("""
    <h2 style='color: green;'>🌿 AgriConnect</h2>
    <p style='color: #555;'>Empowering the Agri-Ecosystem</p>
""", unsafe_allow_html=True)
user_type = st.sidebar.selectbox("Who are you?", ["Farmer", "Buyer", "Agri-Industry", "Student", "Consumer", "Researcher"])
crop_interest = st.sidebar.text_input("Your Primary Crop Interest (e.g., Tomato)")
st.sidebar.markdown("---")

# ---- Header ----
st.markdown("""
    <div style='background: linear-gradient(to right, #a8e063, #56ab2f); padding: 25px; border-radius: 15px;'>
        <h1 style='text-align: center; color: white;'>🌾 AgriConnect</h1>
        <h4 style='text-align: center; color: #f1f1f1;'>Bringing Together Farmers, Buyers, Experts & More</h4>
    </div>
""", unsafe_allow_html=True)

# ---- Section: Crop Feed ----
st.markdown("<br>", unsafe_allow_html=True)
st.subheader(f"📢 Updates & Opportunities for {crop_interest.title() if crop_interest else 'Your Crop'}")
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
        st.metric("Today’s Market Price (Tomato)", "₹14/kg", "+₹2")
        st.metric("Top Buyer Near You", "FreshKart Ltd.")
        st.button("🌟 View All Opportunities")

# ---- Section: Connect ----
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🌐 Connect with Others")
connect_type = st.selectbox("Select Category to Connect", ["Farmers", "Buyers", "Industries", "Experts", "Students"])

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
        st.write("👨‍🎓 **Arun R** – Final Year Agri Student, Project on Tomato Tech")

# ---- Section: Post/Share ----
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("📣 Share Your Update")
with st.form("post_form"):
    post_text = st.text_area("What's happening in your field or lab?", height=150)
    file = st.file_uploader("Upload Image or Report", type=["jpg", "png", "pdf"])
    submitted = st.form_submit_button("🚀 Post Update")
    if submitted:
        st.balloons()
        st.success("✅ Your post has been shared successfully!")

# ---- New Section: Events & Trainings ----
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🎓 Events & Trainings")
with st.container():
    st.info("🗓️ **Soil Health Management Workshop** – June 20, Trichy")
    st.info("🗓️ **AI in Agriculture Hackathon** – July 2, Online")
    st.info("🗓️ **Certified Organic Farming Course** – Starting June 10")

# ---- New Section: Jobs & Internships ----
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("💼 Jobs & Internships")
with st.container():
    st.warning("🔎 **Field Officer (Tomato Contracts)** – TomatoKing Exports")
    st.success("🎓 **Internship: Smart Agri Devices** – Final Year Project, Coimbatore")
    st.info("💼 **Agri-Marketing Manager** – FreshKart Ltd.")

# ---- Footer ----
st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; color: #888;'>© 2025 AgriConnect | Made with ❤️ for Farmers</p>
""", unsafe_allow_html=True)
