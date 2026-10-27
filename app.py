import pickle
import pandas as pd

with open("love_life_model.pkl", "rb") as file:
    model = pickle.load(file)
import base64
import streamlit as st



import base64
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Jagroop's Love Life 💜",
    page_icon="🌙",
    layout="wide"
)

# ---------------- MIDNIGHT ROMANCE BACKGROUND ----------------
with open("love.png", "rb") as image_file:
    encoded_image = base64.b64encode(
        image_file.read()
    ).decode("utf-8")

st.markdown(f"""
<style>
/* Full-page background */
.stApp {{
    background:
        linear-gradient(
            rgba(10, 8, 35, 0.30),
            rgba(20, 10, 45, 0.45)
        ),
        url("data:image/png;base64,{encoded_image}");

    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    min-height: 100vh;
}}

/* Transparent content area */
[data-testid="stAppViewContainer"] {{
    background: transparent;
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

[data-testid="stMain"] {{
    background: transparent;
}}

/* Romantic glass-style content panel */
.block-container {{
    background: rgba(15, 12, 40, 0.48);
    border: 1px solid rgba(220, 190, 255, 0.35);
    border-radius: 24px;
    padding: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
}}

/* Headings */
h1, h2, h3 {{
    color: #f4d7ff !important;
}}

/* Paragraphs and labels */
p, label, [data-testid="stMarkdownContainer"] {{
    color: #ffffff;
}}

/* Romantic buttons */
.stButton > button {{
    background: linear-gradient(90deg, #a855f7, #ec4899);
    color: white;
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 30px;
    padding: 0.65rem 1.3rem;
    font-weight: bold;
    transition: 0.3s;
}}

.stButton > button:hover {{
    transform: translateY(-3px);
    box-shadow: 0 5px 20px rgba(236, 72, 153, 0.45);
}}
</style>
""", unsafe_allow_html=True)

# ---------------- ROMANTIC HEADER ----------------
st.markdown("""
<div style="text-align:center; padding:15px;">
    <h1>🌙 Jagroop's love life 💜</h1>
    <p style="font-size:19px; font-style:italic;">
        Two Hearts · One Beautiful Story
    </p>
    <p style="font-size:24px;">✨ 💕 🌌 💕 ✨</p>
</div>
""", unsafe_allow_html=True)



# ---------------- OPENING ----------------


st.markdown("""
<div class="love-card">

<h2>💌 Welcome to Their Little Love Story</h2>

<p class="story">
Some people enter our lives unexpectedly...
<br>
and slowly become a beautiful part of our everyday world. 🥹❤️
<br><br>

Some conversations become memories.
<br>
Some smiles become reasons to smile.
<br>
And sometimes, two names become one beautiful story. 🌹
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- LOVE QUOTE ----------------

st.markdown("""
<div class="quote">

"Maybe love isn't about finding someone perfect...
<br>
Maybe it's about finding someone whose presence
<br>
makes ordinary moments feel special." ❤️

</div>
""", unsafe_allow_html=True)


st.divider()


# ---------------- THEIR STORY ----------------

st.header("🌸 A Story Written by Two Hearts")

st.markdown("""
<div class="love-card">

<p class="story">
Every beautiful relationship has little moments that nobody else understands. 💕
<br><br>
The first conversation...<br>
The first smile...<br>
The silly arguments...<br>
The endless conversations...<br>
The moments of missing each other...<br>
And the memories that quietly become precious. 🌙
<br><br>
Love is not always about perfect days.
<br><br>
It is about having someone who stays,<br>
someone who understands,<br>
someone who cares,<br>
and someone you can choose again and again. 🫶❤️
</p>

<hr>

<h2 style="text-align:center;">💞 ਦੋ ਦਿਲਾਂ ਦੀ ਸ਼ਾਇਰੀ 💞</h2>

<p class="story" style="font-size:21px; line-height:2;">
ਤੇਰੀ ਮੁਸਕਾਨ ਮੇਰੀ ਖੁਸ਼ੀ ਬਣ ਜਾਵੇ,<br>
ਤੇਰੀ ਹਰ ਗੱਲ ਮੇਰੀ ਯਾਦ ਬਣ ਜਾਵੇ।<br>
ਰੱਬ ਕਰੇ ਸਾਡਾ ਸਾਥ ਇੰਝ ਹੀ ਬਣਿਆ ਰਹੇ,<br>
ਸਾਡੀ ਮੁਹੱਬਤ ਹਰ ਦਿਨ ਹੋਰ ਵੀ ਗਹਿਰੀ ਬਣ ਜਾਵੇ। ❤️
</p>


<p style="text-align:center; color:#e9d5ff;">
✨ ਇੱਕ ਕਹਾਣੀ, ਦੋ ਦਿਲ, ਤੇ ਪਿਆਰ ਬੇਸ਼ੁਮਾਰ ✨
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- SPECIAL MESSAGE ----------------

st.header("💖 A Little Message")

st.markdown("""
<div class="love-card">

<p class="quote">

"Two people may have different dreams,
different personalities and different ways of seeing the world...

<br><br>

But when they genuinely care for each other,
they create a little world of their own." 🌹

</p>

</div>
""", unsafe_allow_html=True)


# ---------------- NAMES ----------------

st.header("💌 The Two Hearts")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        '<div class="love-card"><h3>🌷 Jagroop Singh</h3></div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="love-card"><h3>🌷 Jagroop Kaur</h3></div>',
        unsafe_allow_html=True
    )


st.divider()


# ---------------- ENDING ----------------

st.markdown("""
<div class="love-card">

<h2>🌙 And Their Story Continues...</h2>

<p class="story">

Maybe the most beautiful part of a love story
is not knowing exactly what happens next.

<br><br>

It is simply enjoying every moment,
every laugh,
every memory,
and every little reason to say...

<br><br>

<strong>
❤️ "I'm glad I found you." ❤️
</strong>

</p>

</div>
""", unsafe_allow_html=True)


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">

🌹 Jagroop Singh ❤️ Jagroop Kaur 🌹
<br>
<i>A little project made with a lot of feelings.</i> 🥹💕

</div>
""", unsafe_allow_html=True)




# ---------------- PHASE 2: INTERACTIVE LOVE QUESTIONS ----------------

st.divider()

st.header("💞 A Little Test of Two Hearts")

st.markdown("""
<div class="love-card">
<p class="story">
Every relationship has its own beautiful little moments. ❤️

<br><br>

Trust, care, understanding and memories
make every story unique.

<br><br>

Let's explore the beautiful bond between
Jagroop Singh and Jagroop Kaur. 🥹🌹
</p>
</div>
""", unsafe_allow_html=True)

st.subheader("💗 Tell Us About Their Bond")
trust = st.slider(
    "🤝 How much do they trust each other?",
    min_value=0,
    max_value=10,
    value=8,
    key="love_trust"
)

understanding = st.slider(
    "🫶 How well do they understand each other?",
    0, 10, 8,
    key="love_understanding"
)

communication = st.slider(
    "💬 How good is their communication?",
    0, 10, 8,
    key="love_communication"
)

care = st.slider(
    "🌷 How much do they care for each other?",
    0, 10, 9,
    key="love_care"
)

support = st.slider(
    "💖 How much do they support each other?",
    0, 10, 8,
    key="love_support"
)

memories = st.slider(
    "🌙 How special are the memories they share?",
    0, 10, 8,
    key="love_memories"
)

st.caption(
    "💕 Rate each aspect from 0 (not at all) "
    "to 10 (very much)."
)


st.divider()

st.header("💖 Our Love Score")

# Calculate the average of all six sliders
love_score = (
    trust + understanding + communication
    + care + support + memories
) / 6

# Convert the average from a 10-point scale to 100
love_score = round(love_score * 10)

st.subheader(f"💕 Our Love Score: {love_score}/100")

st.progress(love_score / 100)

if love_score >= 90:
    st.success("💖 Two hearts, one beautiful bond!")
elif love_score >= 75:
    st.info("🥰 A lovely bond filled with care and understanding!")
elif love_score >= 50:
    st.warning("🌷 Every beautiful relationship keeps growing!")
else:
    st.write("💌 Every little moment is a chance to grow closer.")


st.divider()

st.header("💌 Our Beautiful Love Story")
st.write(
    "Every little moment becomes a beautiful memory "
    "when two hearts share a special bond. ❤️"
)

import pandas as pd

# Our Love Story Dataset
love_data = {
    "Memory": [
        "First Meeting",
        "First Conversation",
        "Special Moment",
        "Trust",
        "Care",
        "Together Forever"
    ],
    "Love_Level": [80, 85, 95, 90, 98, 100],
    "Happiness": [85, 90, 98, 92, 99, 100]
}

df = pd.DataFrame(love_data)

st.subheader("🌷 Our Memory Table")
st.dataframe(df, use_container_width=True)


st.subheader("💞 Love & Happiness Graph")

chart_data = df.set_index("Memory")[["Love_Level", "Happiness"]]

st.bar_chart(chart_data)

st.caption(
    "❤️ Every memory adds its own colour to our story."
)


st.divider()

st.header("💝 Add a Special Memory")

with st.form("memory_form"):
    memory_name = st.text_input(
        "✨ Memory Title",
        placeholder="e.g. Our favourite moment"
    )

    category = st.selectbox(
        "💌 Memory Category",
        ["First Meeting", "Special Moment", "Trust",
         "Care", "Celebration", "Future Dreams"]
    )

    happiness = st.slider(
        "🥰 How happy does this memory make you?",
        min_value=1,
        max_value=10,
        value=8
    )

    submitted = st.form_submit_button("💖 Save Memory")

    if submitted:
        if memory_name.strip():
            st.session_state.setdefault("special_memories", [])

            st.session_state.special_memories.append({
                "Memory": memory_name.strip(),
                "Category": category,
                "Happiness": happiness
            })

            st.success("Your special memory has been added! ❤️")
        else:
            st.warning("Please enter a memory title first.")


if st.session_state.get("special_memories"):
    st.subheader("📖 Our Memory Collection")

    memories_df = pd.DataFrame(
        st.session_state.special_memories
    )

    st.dataframe(memories_df, use_container_width=True)

    st.subheader("🌸 Happiness in Our Memories")
    st.bar_chart(
        memories_df.set_index("Memory")["Happiness"]
    )

    
# ---------------- LOVE SCORE RESULT ----------------

st.divider()

if st.button("❤️ Reveal Their Love Story ❤️"):

    love_score = model.predict(pd.DataFrame([{
    "trust": trust,
    "understanding": understanding,
    "communication": communication,
    "care": care,
    "support": support,
    "memories": memories
}]))[0]

love_score = max(0, min(100, love_score))

st.subheader("💕 Their Love Story Result")
st.progress(int(love_score))
st.write(f"❤️ Love Story Score: {love_score:.1f}%")
if love_score >= 85:
        st.success("🥹❤️ A beautiful and deeply connected bond!")

        st.markdown("""
        <div class="love-card">
        <p class="quote">
        "Some connections are difficult to explain.

        <br><br>

        They live in the little moments,
        the silent understanding,
        the caring words and the memories
        that make two hearts feel close. 🌹

        <br><br>

        May their story always be filled
        with kindness, trust and beautiful moments. ❤️"
        </p>
        </div>
        """, unsafe_allow_html=True)

elif love_score >= 60:
        st.info("💕 Their bond has room to grow beautifully.")

        st.write("""
        Every relationship grows through patience,
        honest conversations and understanding. 🫶

        The little efforts we make for each other
        can become the most precious memories. 🌷
        """)

else:
        st.info("🌸 Every story deserves patience and understanding.")

        st.write("""
        Relationships aren't defined by a number.
        Listening, respect, honesty and kindness
        matter much more than a score. ❤️
        """)


st.subheader("💗 A Little Look Inside Their Story")

factors = {
    "Trust": trust,
    "Understanding": understanding,
    "Communication": communication,
    "Care": care,
    "Support": support,
    "Memories": memories
}

st.bar_chart(factors)




