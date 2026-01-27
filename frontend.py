# Step1: Setup UI with streamlit
import streamlit as st

# ================== 🔥 ADD THE THEME HERE 🔥 ==================
st.markdown("""
<style>

/* =====================================================
   GLOBAL BACKGROUND + DEPTH
   ===================================================== */
html, body, [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at center, #16001f, #05010d 70%) !important;
    color: #e5e7eb !important;
    font-family: 'Orbitron', monospace;
}

/* =====================================================
   SCANLINE EFFECT (SUBTLE)
   ===================================================== */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(
        to bottom,
        rgba(255,255,255,0.03) 0px,
        rgba(255,255,255,0.03) 1px,
        transparent 2px,
        transparent 4px
    );
    pointer-events: none;
    mix-blend-mode: overlay;
    opacity: 0.15;
    z-index: 0;
}

/* =====================================================
   MAIN CONTENT (DARK TERMINAL PANEL)
   ===================================================== */
[data-testid="stMain"] {
    background: linear-gradient(
        180deg,
        rgba(10, 2, 25, 0.97),
        rgba(5, 1, 13, 0.97)
    ) !important;
    padding: 2rem;
    position: relative;
    z-index: 1;
}

/* =====================================================
   SIDEBAR
   ===================================================== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b0714, #16001f) !important;
    border-right: 1px solid rgba(34,211,238,0.3);
}

/* =====================================================
   TITLES (NEON PULSE)
   ===================================================== */
@keyframes neonPulse {
    0% { text-shadow: 0 0 8px #f472b6; }
    50% { text-shadow: 0 0 18px #f472b6, 0 0 30px #22d3ee; }
    100% { text-shadow: 0 0 8px #f472b6; }
}

h1 {
    color: #f472b6 !important;
    animation: neonPulse 3s infinite;
}

h2, h3 {
    color: #22d3ee !important;
    text-shadow: 0 0 12px rgba(34,211,238,0.9);
}

/* =====================================================
   INPUTS (TERMINAL FEEL)
   ===================================================== */
input, textarea, select {
    background: linear-gradient(
        180deg,
        rgba(5, 10, 30, 0.9),
        rgba(2, 6, 23, 0.9)
    ) !important;
    border: 1px solid rgba(236,72,153,0.6) !important;
    color: #e5e7eb !important;
    border-radius: 14px !important;
}

input:focus, textarea:focus {
    box-shadow:
        0 0 10px rgba(236,72,153,0.9),
        0 0 25px rgba(236,72,153,0.7) !important;
}

/* =====================================================
   BLINKING CURSOR EFFECT (VISUAL)
   ===================================================== */
input::after {
    content: "▮";
    animation: blink 1.2s infinite;
}

@keyframes blink {
    0%, 50% { opacity: 1; }
    51%, 100% { opacity: 0; }
}

/* =====================================================
   BUTTON (ENERGY CORE)
   ===================================================== */
@keyframes glow {
    0% { box-shadow: 0 0 15px #ec4899; }
    50% { box-shadow: 0 0 35px #22d3ee; }
    100% { box-shadow: 0 0 15px #ec4899; }
}

button {
    background: linear-gradient(90deg, #ec4899, #22d3ee) !important;
    color: black !important;
    font-weight: 900 !important;
    border-radius: 16px !important;
    animation: glow 2.5s infinite;
}

button:hover {
    transform: translateY(-2px) scale(1.05);
}

/* =====================================================
   CHAT / CONTENT BLOCKS
   ===================================================== */
[data-testid="stMarkdownContainer"] > div {
    background: linear-gradient(
        180deg,
        rgba(2, 6, 23, 0.9),
        rgba(4, 3, 30, 0.9)
    );
    border-radius: 16px;
    padding: 12px;
    box-shadow: inset 0 0 15px rgba(34,211,238,0.08);
}

/* =====================================================
   METRICS
   ===================================================== */
[data-testid="stMetric"] {
    background: rgba(2, 6, 23, 0.95);
    border: 1px solid rgba(34,211,238,0.4);
    border-radius: 14px;
    box-shadow: 0 0 14px rgba(34,211,238,0.6);
}

/* =====================================================
   SCROLLBAR
   ===================================================== */
::-webkit-scrollbar {
    width: 6px;
}
::-webkit-scrollbar-thumb {
    background: linear-gradient(#ec4899, #22d3ee);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================== 🔥 THEME ENDS HERE 🔥 ==================


st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")


system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile",]
MODEL_NAMES_GEMINI = ["gemini-2.5-flash-lite",]

provider=st.radio("Select Provider:", ("Groq", "gemini"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "gemini":
    selected_model = st.selectbox("Select Gemini Model:", MODEL_NAMES_GEMINI)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        # response="hi this is a demo response"
        # st.subheader("Agent Response")
        # st.markdown(f"**Final Response:** {response}")

        #Step2: Connect with backend via URL
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                #st.markdown(f"**Final Response:** {response}")
                st.markdown(f"**Final Response:** {response_data}")


    

