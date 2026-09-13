  import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ECO-SMART Tracker v4.0", 
    page_icon="🌱", 
    layout="wide"
)

# --- 2. TOP BANNER & HEADER (অ্যাপের একদম শুরু) ---
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🌿 ECO-SMART Tracker v4.0 🌿</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>পরিবেশবান্ধব অভ্যাস গড়ার স্মার্ট ডিজিটাল প্ল্যাটফর্ম ও অফিশিয়াল সিস্টেম ড্যাশবোর্ড</p>", unsafe_allow_html=True)

# মূল ব্যানার ছবি (শুরুর ব্যানার)
st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=1200&auto=format&fit=crop", use_container_width=True, caption="Green Earth & Sustainability Initiative")
st.markdown("---")

# --- 3. GLOBAL SIDEBAR: OFFICIAL COPYRIGHT & INFO (1st Image/Logo) ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/environmental-care.png", width=80, caption="Eco System")
    st.markdown("### ECO-SMART Tracker v4.0")
    st.markdown("**Official System Dashboard**")
    st.markdown("---")
    st.markdown("🔒 **Official Copyright Notice**")
    st.markdown("© **2025–2026 Team JKL**")
    st.markdown("Vasha Shaheed Abdul Jabbar Ansar VDP School and College.")
    st.markdown("All rights reserved. Unauthorized reproduction, distribution, or commercial use of this system is strictly prohibited.")
    st.markdown("---")
    st.markdown("📌 *Department: Science (9B)*")

# --- 4. NAVIGATION TABS (MULTI-TAB ARCHITECTURE) ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Project Overview", 
    "2. Live Statistics", 
    "3. Data History & Scores", 
    "4. Resource Hub & Feedback",
    "5. Eco Assessment Quiz 📝"
])

# --- TAB 1: PROJECT OVERVIEW & INSTITUTIONAL DETAILS ---
with tab1:
    st.markdown("## OFFICIAL PROJECT REPORT")
    st.markdown("# ECO-SMART Tracker v4.0")
    
    # ২ নম্বর ছবি: গ্লোব বা আর্থ লোগো
    st.image("https://img.icons8.com/color/480/earth-planet.png", width=150, caption="Global Sustainability")
    
    st.markdown("### An Advanced Interactive Web Application & Digital Front-End Environmental Tracking System")
    st.markdown("**Architecture:** Streamlit Cloud & GitHub Architecture")
    
    st.markdown("---")
    st.markdown("### 1. Project Overview & Platform Identity")
    
    st.info("**Core Identity**\n\n"
            "- **Project Name:** ECO-SMART Tracker v4.0\n"
            "- **Type:** Interactive Web Application & Digital Interface\n"
            "- **Hosting Platform:** Streamlit Cloud & GitHub Repository")
    
    st.success("**Main Objective**\n\n"
               "To establish a modern, live, and user-friendly digital system for environmental tracking and data collection, "
               "accessible instantly via cross-device QR code scanning without manual friction.")
    
    st.markdown("---")
    st.markdown("### Institutional & Team Details")
    st.markdown("- **Institution:** Vasha Shaheed Abdul Jabbar Ansar VDP School and College")
    st.markdown("- **Project Type:** School project")
    st.markdown("- **Department:** Science (9B)")
    st.markdown("- **Academic Session:** 2025–2026")
    st.markdown("- **Team Members (Team JKL):**")
    st.markdown("  * Ekhtear Uddin Mohammad Jiyad (Main Developer)")
    st.markdown("  * Mahmudul Hasan")
    st.markdown("  * Al Razi")
    st.markdown("  * Jakaria Islam")
    st.markdown("  * Ahmed Santo")
    st.markdown("  * Junayed Ahmed")
    st.markdown("  * Morsalin")
    st.markdown("  * Mehrab Mostofa Noor")
    st.markdown("  * Ahmed Saim")

# --- TAB 2: LIVE STATISTICS & ANALYTICS ---
with tab2:
    st.header("Live Statistics & Environmental Metrics")
    
    # ৩ নম্বর ছবি: প্ল্যান্ট বা অ্যানালিটিক্স আইকন
    st.image("https://img.icons8.com/color/480/plant-under-sun.png", width=130, caption="Eco Metrics Dashboard")
    
    st.write("Real-time data visualization and monitoring dashboard.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Active QR Scans", "1,245", "+12%")
    col2.metric("Data Sync Rate", "99.8%", "Optimal")
    col3.metric("System Status", "Live", "Cloud Active")

# --- TAB 3: DATA HISTORY LOG & SCORE TRACKING ---
with tab3:
    st.header("System Data History Log & Score Tracking")
    st.write("Submit new scores or records and view the complete history log.")
    
    # Score Submission Form
    with st.form("score_entry_form", clear_on_submit=True):
        st.subheader("➕ Add New Score / Record")
        st.caption("ℹ️ আপনি চাইলে একাধিকবার স্কোর সাবমিট করতে পারবেন। প্রথমবার সাবমিট করার পর এটি সাথে সাথে সেভ হয়ে যাবে।")
        
        participant_name = st.text_input("Name / Team ID")
        score_value = st.number_input("Score / Value", min_value=0, step=1)
        category = st.selectbox("Category / Zone", ["Zone-A", "Zone-B", "Zone-C", "General"])
        score_submitted = st.form_submit_button("Save Score")
        
        if score_submitted:
            if participant_name:
                score_file = "scores_data.csv"
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_score_df = pd.DataFrame([[current_time, participant_name, score_value, category]], 
                                            columns=["Timestamp", "Participant Name", "Score", "Category"])
                
                if os.path.exists(score_file):
                    new_score_df.to_csv(score_file, mode='a', header=False, index=False)
                else:
                    new_score_df.to_csv(score_file, mode='w', header=True, index=False)
                
                st.success("✅ আপনার স্কোর সফলভাবে সেভ হয়েছে!")
            else:
                st.warning("Please enter a name or ID.")
    
    st.markdown("---")
    st.subheader("📊 All Recorded Scores & History")
    score_file = "scores_data.csv"
    if os.path.exists(score_file):
        df_scores = pd.read_csv(score_file)
        if not df_scores.empty:
            st.dataframe(df_scores, use_container_width=True)
        else:
            st.info("No score entries found yet.")
    else:
        st.info("No score file created yet. Add a score above to start tracking.")

# --- TAB 4: RESOURCE HUB & FEEDBACK ---
with tab4:
    st.header("Educational Resources & Feedback Hub")
    
    # ৪ নম্বর ছবি: রিসাইকেল বা রিসোর্স আইকন
    st.image("https://img.icons8.com/color/480/recycle.png", width=120, caption="Resource Hub")
    
    with st.expander("📘 Read Guidelines & Documentation"):
        st.write("This section contains official documentation, sustainability guides, and paperless workflow protocols supporting the Smart Bangladesh initiative.")
        
    st.markdown("---")
    
    # Feedback Form
    with st.form("feedback_form", clear_on_submit=True):
        st.subheader("Submit System Feedback")
        st.caption("ℹ️ আপনি চাইলে একাধিকবার ফিডব্যাক সাবমিট করতে পারবেন।")
        
        user_name = st.text_input("Your Name / ID", key="fb_name")
        feedback_text = st.text_area("Feedback or Observation", key="fb_text")
        submitted = st.form_submit_button("Submit Feedback")
        
        if submitted:
            if user_name and feedback_text:
                feedback_file = "feedback_data.csv"
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_data = pd.DataFrame([[current_time, user_name, feedback_text]], 
                                        columns=["Timestamp", "User Name", "Feedback"])
                
                if os.path.exists(feedback_file):
                    new_data.to_csv(feedback_file, mode='a', header=False, index=False)
                else:
                    new_data.to_csv(feedback_file, mode='w', header=True, index=False)
                
                st.success("✅ আপনার ফিডব্যাক সফলভাবে জমা হয়েছে!")
            else:
                st.warning("Please fill in both fields before submitting.")

    st.markdown("---")
    st.subheader("📥 View All Submitted Feedbacks")
    
    feedback_file = "feedback_data.csv"
    if os.path.exists(feedback_file):
        df_feedbacks = pd.read_csv(feedback_file)
        if not df_feedbacks.empty:
            st.dataframe(df_feedbacks, use_container_width=True)
        else:
            st.info("No feedback entries found yet.")
    else:
        st.info("No feedback file created yet. Submit a feedback above to create one.")

# --- TAB 5: ECO ASSESSMENT QUIZ MODULE ---
with tab5:
    st.header("❓ পরিবেশগত অভ্যাসের মূল্যায়ন মডিউল")
    st.write("আপনার দৈনন্দিন অভ্যাস যাচাই করুন এবং ইকো-স্কোর জেনে নিন।")
    
    # ইউজারের তথ্য ইনপুট নেওয়ার সেকশন
    st.subheader("📝 আপনার তথ্য প্রদান করুন:")
    col1, col2 = st.columns(2)
    with col1:
        user_name = st.text_input("পূর্ণ নাম (Name)", placeholder="আপনার নাম লিখুন", key="quiz_name")
        user_class = st.text_input("শ্রেণি (Class)", placeholder="যেমন: 9", key="quiz_class")
        user_section = st.text_input("সেকশন (Section)", placeholder="যেমন: B", key="quiz_sec")
    with col2:
        user_roll = st.text_input("রোল (Roll)", placeholder="রোল নম্বর", key="quiz_roll")
        user_sid = st.text_input("আইডি (SID)", placeholder="স্টুডেন্ট আইডি", key="quiz_sid")

    st.markdown("---")
    st.subheader("প্রশ্নমালা:")

    # প্রশ্ন ও অপশনগুলো
    q1 = st.radio("১. স্কুলে যাতায়াত মাধ্যম কেমন?", ("হেঁটে বা বাইসাইকেল (+20 pts)", "রিকশা বা পাবলিক বাস (+10 pts)", "কার বা মোটরসাইকেল (0 pts)"))
    q2 = st.radio("২. প্লাস্টিক বা পলিথিন ব্যবহার?", ("একদম বর্জন করি (+20 pts)", "মাঝে মাঝে ব্যবহার (+10 pts)", "নিয়মিত ব্যবহার (0 pts)"))
    q3 = st.radio("৩. রুম ছেড়ে যাওয়ার সময় ফ্যান-লাইট?", ("নিয়ম মেনে বন্ধ করি (+20 pts)", "মাঝে মাঝে ভুলে যাই (+10 pts)", "খেয়ালই করি না (0 pts)"))
    q4 = st.radio("৪. ব্রাশ বা ওযুর সময় পানির ব্যবহার?", ("প্রয়োজন ছাড়া কল বন্ধ (+20 pts)", "মাঝে মাঝে খোলা থাকে (+10 pts)", "কল সম্পূর্ণ খোলা রাখি (0 pts)"))
    q5 = st.radio("৫. কাগজ ও গাছপালা নিয়ে অভ্যাস?", ("কাগজ বাঁচাই ও গাছ লাগাই (+20 pts)", "মাঝে মাঝে কাজে লাগাই (+10 pts)", "কাগজ নষ্ট করি (0 pts)"))
    q6 = st.radio("৬. প্লেটে খাবার নেওয়ার সময়?", ("পরিমাণমতো নিয়ে খাই (+20 pts)", "মাঝে মাঝে বেঁচে যায় (+10 pts)", "অতিরিক্ত ফেলে দিই (0 pts)"))

    # সাবমিট বাটন
    if st.button("🚀 ফাইনাল রিপোর্ট সাবমিট করুন", key="quiz_submit"):
        if not user_name:
            st.warning("⚠️ দয়া করে আপনার নাম ইনপুট করুন!")
        else:
            # স্কোর ক্যালকুলেশন
            score = 0
            for q in [q1, q2, q3, q4, q5, q6]:
                if "+20" in q:
                    score += 20
                elif "+10" in q:
                    score += 10
                else:
                    score += 0

            st.success(f"ধন্যবাদ, {user_name}! আপনার অ্যাসেসমেন্ট সফল হয়েছে।")
            
            # রেজাল্ট কার্ড
            st.markdown(f"### 🎯 আপনার মোট ইকো স্কোর: **{score} / 120**")
            
            if score >= 100:
                st.markdown("🌟 **স্ট্যাটাস: ECO-HERO (পৃথিবীর রক্ষক) 🌿**")
                st.info("💡 ডিন রাস্কের বাণী: \"গাছ লাগানো মানে আগামী প্রজন্মের জন্য আশা রোপণ করা।\"")
            elif score >= 60:
                st.markdown("🌤️ **স্ট্যাটাস: ECO-CONSCIOUS (সচেতন নাগরিক) 💡**")
                st.info("💡 ডব্লিউ এডওয়ার্ডসের বাণী: \"আমরা পৃথিবী আমাদের পূর্বপুরুষদের কাছ থেকে উত্তরাধিকার সূত্রে পাইনি, বরং সন্তানদের কাছ থেকে ধার নিয়েছি।\"")
            else:
                st.markdown("⚡ **স্ট্যাটাস: HIGH EMISSION WARNING! 🚨**")
                st.warning("💡 মার্গারেট মিডিের বাণী: \"কয়েকজন সচেতন নাগরিক বিশ্বকে বদলে দিতে পারে—প্রকৃতপক্ষে সবসময় তাইই ঘটে এসেছে।\"")

            # এসডিজি ১৩ বার্তা
            st.markdown("---")
            st.markdown("🌐 **[SDG 13 - Climate Action লক্ষ্য]:** *\"জলবায়ু পরিবর্তন ও এর প্রভাব মোকাবিলায় জরুরি পদক্ষেপ গ্রহণ করা\"—এই মূল মন্ত্রে উজ্জীবিত হয়ে আমাদের পরিবেশবান্ধব অভ্যাস গড়ে তুলতে হবে।*")

            # ফাইলে ডেটা সেভ করা
            submit_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            table_data = f"Name: {user_name} | Class: {user_class} | Section: {user_section} | Roll: {user_roll} | SID: {user_sid} | Eco-Score: {score}/120 | Date: {submit_date}\n"

            try:
                with open("eco_log.txt", "a", encoding="utf-8") as file:
                    file.write(table_data)
                st.toast("💾 ডেটা সফলভাবে সার্ভার ফাইলে সেভ হয়েছে!", icon="✅")
            except Exception as e:
                st.error("⚠️ ডেটা সেভ করতে সমস্যা হয়েছে।")

# --- GLOBAL APP FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 14px;'>"
    "© 2025–2026 <b>Team JKL</b> (Science 9B) • Vasha Shaheed Abdul Jabbar Ansar VDP School and College. All Rights Reserved."
    "</p>", 
    unsafe_allow_html=True
)
               
    
