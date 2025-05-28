# main.py

import streamlit as st
from script_generator import get_topic_ideas, generate_script

st.set_page_config(page_title="🎙️ Data Science Reel Script Generator", page_icon="📈")
st.title("🎙️ Data Science Voiceover Script Generator")

# Step 1: Subject selection
subject = st.selectbox(
    "Choose a broad topic area:",
    ["Statistics", "SQL", "Python", "Machine Learning", "AI / ML Latest News", "GenAI / LLMs"]
)

# Step 2: Fetch topic ideas
if st.button("Get Topic Ideas"):
    with st.spinner("Thinking of fresh content ideas..."):
        ideas = get_topic_ideas(subject)
        st.session_state["ideas_raw"] = ideas

# Step 3: Display suggested topics
if "ideas_raw" in st.session_state:
    st.subheader("🧠 Suggested Topics")

    # Split basic and advanced
    ideas = st.session_state["ideas_raw"].split("ADVANCED_TOPICS:")
    basic = ideas[0].replace("BASIC_TOPICS:", "").strip().split("- ")
    advanced = ideas[1].strip().split("- ")

    basic_topics = [t.strip() for t in basic if t.strip()]
    advanced_topics = [t.strip() for t in advanced if t.strip()]

    st.markdown("### 📘 Basic Concepts")
    selected_basic = st.radio("Choose a basic topic (optional):", basic_topics, key="basic")

    st.markdown("### 📗 Nuanced / Industry-Relevant")
    selected_advanced = st.radio("Choose a nuanced topic (optional):", advanced_topics, key="advanced")

    # Final topic selection
    topic = st.selectbox("🎯 Final Topic to Use:", [selected_basic, selected_advanced])

    # Step 4: Hook style
    st.subheader("🎯 Hook Style for the Reel")
    hook_style = st.radio("Choose a hook style:", [
        "Interview-style question",
        "Funny or personal story",
        "Direct technical hook about the concept itself",
        "I'll write my own"
    ])

    custom_hook = ""
    if hook_style == "I'll write my own":
        custom_hook = st.text_input("Write your custom hook style here:")

    final_hook = custom_hook if custom_hook.strip() else hook_style

    # Step 5: Generate script
    if st.button("🎬 Generate Reel Script"):
        with st.spinner("Creating your voiceover script..."):
            script = generate_script(topic, final_hook)
            st.success("Your script is ready!")
            st.text_area("🎤 Voiceover Script", script, height=400)
