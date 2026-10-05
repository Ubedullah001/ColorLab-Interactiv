import streamlit as st

st.set_page_config(
    page_title="Color Learning Studio",
    page_icon="🎨",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #555;
        margin-bottom: 30px;
    }
    .color-card {
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        color: white;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    }
    .info-box {
        padding: 20px;
        border-radius: 15px;
        background: #f5f7fa;
        margin: 10px 0;
    }
    .result-box {
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        color: white;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }
    .footer {
        text-align: center;
        color: #777;
        padding: 30px;
        font-size: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="main-title">🎨 Color Learning Studio</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Learn colors, mix colors, and discover beautiful new colors!</div>', unsafe_allow_html=True)
st.divider()

# ---------- Primary Colors ----------
st.header("🎯 Primary Colors")
st.write("Primary colors are the basic colors. They cannot be created by mixing other colors.")

primary = {
    "Red": "#FF0000",
    "Yellow": "#FFD700",
    "Blue": "#0000FF"
}

cols = st.columns(3)
for col, (name, code) in zip(cols, primary.items()):
    with col:
        st.markdown(f"""
            <div class="color-card" style="background:{code};">
                {name}<br><small>{code}</small>
            </div>
            """, unsafe_allow_html=True)

# ---------- Secondary Colors ----------
st.header("🌈 Secondary Colors")
st.write("Secondary colors are created by mixing two primary colors.")

secondary = {
    "Orange": ("Red + Yellow", "#FF8C00"),
    "Green": ("Yellow + Blue", "#00A651"),
    "Purple": ("Blue + Red", "#800080")
}

cols = st.columns(3)
for col, (name, data) in zip(cols, secondary.items()):
    mixture, code = data
    with col:
        st.markdown(f"""
            <div class="color-card" style="background:{code};">
                {name}<br><small>{mixture}</small>
            </div>
            """, unsafe_allow_html=True)

st.divider()

# ---------- Color Mixer ----------
st.header("🧪 Interactive Color Mixer")
st.write("Select two primary colors and discover the resulting color.")

colors = {
    "Red": "#FF0000",
    "Yellow": "#FFD700",
    "Blue": "#0000FF"
}

col1, col2 = st.columns(2)
with col1:
    first_color = st.selectbox("Choose the first color", list(colors.keys()))
with col2:
    second_color = st.selectbox("Choose the second color", list(colors.keys()), index=1)

# Color mixing logic
pair = {first_color, second_color}

if pair == {"Red", "Yellow"}:
    result_name = "Orange"
    result_code = "#FF8C00"
    explanation = "Red + Yellow creates Orange."
elif pair == {"Yellow", "Blue"}:
    result_name = "Green"
    result_code = "#00A651"
    explanation = "Yellow + Blue creates Green."
elif pair == {"Blue", "Red"}:
    result_name = "Purple"
    result_code = "#800080"
    explanation = "Blue + Red creates Purple."
elif first_color == second_color:
    result_name = first_color
    result_code = colors[first_color]
    explanation = "You selected the same color twice, so the result remains the same."
else:
    result_name = "Mixed Color"
    result_code = "#808080"
    explanation = "This combination produces a mixed color."

st.subheader("✨ Mixing Result")
st.markdown(f"""<div class="result-box" style="background:{result_code};">{result_name}</div>""", unsafe_allow_html=True)
st.success(explanation)

# ---------- Color Wheel Concept ----------
st.header("🔵 Understanding the Color Wheel")
st.markdown("""
<div class="info-box">
<b>Primary Colors</b><br>🔴 Red &nbsp;&nbsp; 🟡 Yellow &nbsp;&nbsp; 🔵 Blue
<br><br><b>Secondary Colors</b><br>🟠 Orange &nbsp;&nbsp; 🟢 Green &nbsp;&nbsp; 🟣 Purple
<br><br><b>Simple Rule:</b><br>Primary + Primary → Secondary Color
</div>
""", unsafe_allow_html=True)

# ---------- Quick Learning ----------
st.header("📚 Quick Learning Guide")
learning = {
    "🔴 Red + 🟡 Yellow": "🟠 Orange",
    "🟡 Yellow + 🔵 Blue": "🟢 Green",
    "🔵 Blue + 🔴 Red": "🟣 Purple"
}
for mixture, result in learning.items():
    st.write(f"**{mixture} → {result}**")

# ---------- Footer ----------
st.divider()
st.markdown("""<div class="footer">🎨 Color Learning Studio<br>Learn • Mix • Discover</div>""", unsafe_allow_html=True)
