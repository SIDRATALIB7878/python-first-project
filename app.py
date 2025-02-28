import streamlit as st
import datetime

def get_growth_tips():
    tips = [
        "Embrace challenges as opportunities to grow.",
        "Learn from feedback and use it constructively.",
        "Celebrate effort, not just success.",
        "Replace 'I can't' with 'I can't yet'.",
        "Stay curious and keep exploring new ideas."
    ]
    return tips

# Navigation Menu
menu = ["Home", "Journal", "Progress", "Resources", "Settings"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.title("Growth Mindset Journal")
    st.subheader("Reflect, Learn, and Improve Daily")
    
    # Daily Tip
    st.write("### 🌱 Growth Tip of the Day")
    st.success(get_growth_tips()[datetime.datetime.now().day % len(get_growth_tips())])

elif choice == "Journal":
    # Journal Entry
    st.write("### 📖 Your Daily Reflection")
    date = st.date_input("Select Date", datetime.date.today())
    reflection = st.text_area("Write about a challenge you faced and how you handled it:")
    if st.button("Save Entry"):
        st.success("Your journal entry has been saved! Keep learning and growing.")

elif choice == "Progress":
    st.write("### 📊 Track Your Progress")
    progress = st.slider("Rate your growth mindset today", 0, 100, 50)
    st.write(f"Your current mindset level: {progress}%")

elif choice == "Resources":
    st.write("### 📚 Learning Resources")
    st.markdown("- [Carol Dweck's Growth Mindset TED Talk](https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve)")
    st.markdown("- [Book: Mindset - The New Psychology of Success](https://www.amazon.com/Mindset-Psychology-Carol-S-Dweck/dp/0345472322)")
    st.markdown("- [Online Course: Growth Mindset for Students](https://www.coursera.org/specializations/growth-mindset)")

elif choice == "Settings":
    st.write("### ⚙️ Settings")
    st.write("Here you can customize your experience.")

# Affirmation
st.write("### 💪 Positive Affirmation")
st.info("I am constantly learning and improving every day!")

# Footer
st.write("---")
st.write("🚀 Growth is a journey, not a destination. Keep pushing forward!")
