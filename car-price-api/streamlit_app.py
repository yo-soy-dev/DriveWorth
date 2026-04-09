# import streamlit as st
# import requests

# st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered")

# # API_URL = (
# #     "https://driveworth.onrender.com/predict"
# #     or "http://127.0.0.1:8000/predict"
# # )  # change if your endpoint differs

# API_URL = "http://127.0.0.1:8000/predict"

# st.title("🚗 Car Price Prediction")
# st.caption(
#     "This UI sends data to your FastAPI backend and shows predicted selling price."
# )

# # --- Inputs (match your dataset columns exactly) ---
# car_name = st.text_input("Car_Name (e.g. swift, ritz, sx4)", value="swift")

# year = st.number_input("Year", min_value=1990, max_value=2026, value=2014, step=1)

# present_price = st.number_input(
#     "Present_Price (in lakhs)", min_value=0.0, value=5.59, step=0.1
# )

# kms_driven = st.number_input("Kms_Driven", min_value=0, value=40000, step=1000)

# fuel_type = st.selectbox("Fuel_Type", ["Petrol", "Diesel", "CNG"])

# seller_type = st.selectbox("Seller_Type", ["Dealer", "Individual"])

# transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# # Owner is numeric in your dataset (0,1,3). Map UI labels to int.
# owner_label = st.selectbox(
#     "Owner", ["0 (First Owner)", "1 (Second Owner)", "3 (Third Owner)"]
# )
# owner = int(owner_label.split()[0])

# payload = {
#     "Car_Name": str(car_name),
#     "Year": int(year),
#     "Present_Price": float(present_price),
#     "Kms_Driven": int(kms_driven),
#     "Fuel_Type": str(fuel_type),
#     "Seller_Type": str(seller_type),
#     "Transmission": str(transmission),
#     "Owner": int(owner),
# }

# st.write("### Payload being sent:")
# st.json(payload)

# if st.button("Predict Price 💰"):
#     try:
#         res = requests.post(API_URL, json=payload, timeout=20)
#         if res.status_code == 200:
#             data = res.json()

#             # adjust keys based on your API response
#             # common patterns: {"prediction": 3.45} or {"predicted_price": 3.45}
#             # pred = data.get("prediction", data.get("predicted_price", None))
#             pred = data.get("prediction", data.get("predicted_price", data.get("prediction_price", None)))

#             if pred is None:
#                 st.warning(
#                     "API responded but prediction key not found. Full response below:"
#                 )
#                 st.json(data)
#             else:
#                 st.success(f"✅ Predicted Selling Price: **₹ {pred:.2f} lakhs**")
#         else:
#             st.error(f"❌ API Error {res.status_code}")
#             st.code(res.text)
#     except requests.exceptions.RequestException as e:
#         st.error("❌ Could not connect to API. Is FastAPI running?")
#         st.code(str(e))






import streamlit as st
import requests

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered")

API_URL = "https://driveworth.onrender.com/predict"

# ------------------------------
# Custom CSS
# ------------------------------
st.markdown("""
<style>
    body { background-color: #0e1117; }

    .hero {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }
    .hero h1 {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(90deg, #f97316, #facc15);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero p {
        color: #9ca3af;
        font-size: 1rem;
        margin-top: -0.5rem;
    }
    .card {
        background: #1f2937;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 1rem 0;
        border: 1px solid #374151;
    }
    .card-title {
        color: #f97316;
        font-size: 1rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
    }
    .result-card {
        background: linear-gradient(135deg, #1c1917, #292524);
        border: 2px solid #f97316;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin: 1.5rem 0;
    }
    .result-card .label {
        color: #d1d5db;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .result-card .price {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(90deg, #f97316, #facc15);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
    }
    .result-card .sublabel {
        color: #6b7280;
        font-size: 0.85rem;
    }
    .stButton > button {
        background: linear-gradient(90deg, #f97316, #facc15);
        color: #000;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 800;
        width: 100%;
        transition: opacity 0.2s;
    }
    .stButton > button:hover {
        opacity: 0.85;
        color: #000;
    }
    .badge {
        display: inline-block;
        background: #374151;
        color: #d1d5db;
        border-radius: 20px;
        padding: 0.2rem 0.8rem;
        font-size: 0.8rem;
        margin: 0.2rem;
    }
    div[data-testid="stSelectbox"] label,
    div[data-testid="stNumberInput"] label,
    div[data-testid="stTextInput"] label {
        color: #d1d5db !important;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Hero Header
# ------------------------------
st.markdown("""
<div class="hero">
    <h1>🚗 Car Price Predictor</h1>
    <p>Enter your car details below and get an instant AI-powered price estimate</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------
# Form Section
# ------------------------------
st.markdown('<div class="card"><div class="card-title">🚘 Car Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    car_name = st.text_input("Car Name", value="swift", placeholder="e.g. swift, ritz, sx4")
    year = st.number_input("Year of Purchase", min_value=1990, max_value=2026, value=2014, step=1)
    present_price = st.number_input("Current Ex-Showroom Price (₹ Lakhs)", min_value=0.0, value=5.59, step=0.1)
    kms_driven = st.number_input("Kilometres Driven", min_value=0, value=40000, step=1000)

with col2:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    owner_label = st.selectbox("Ownership", ["0 (First Owner)", "1 (Second Owner)", "3 (Third Owner)"])
    owner = int(owner_label.split()[0])

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# Summary Badges
# ------------------------------
age = 2024 - year
st.markdown(f"""
<div style="margin: 0.5rem 0 1rem 0;">
    <span class="badge">📅 {age} years old</span>
    <span class="badge">⛽ {fuel_type}</span>
    <span class="badge">⚙️ {transmission}</span>
    <span class="badge">🧑 {owner_label}</span>
    <span class="badge">🏢 {seller_type}</span>
    <span class="badge">📍 {kms_driven:,} km</span>
</div>
""", unsafe_allow_html=True)

# ------------------------------
# Predict Button
# ------------------------------
predict_btn = st.button("🔮 Predict Selling Price")

# ------------------------------
# Prediction Result
# ------------------------------
if predict_btn:
    payload = {
        "Car_Name": str(car_name),
        "Year": int(year),
        "Present_Price": float(present_price),
        "Kms_Driven": int(kms_driven),
        "Fuel_Type": str(fuel_type),
        "Seller_Type": str(seller_type),
        "Transmission": str(transmission),
        "Owner": int(owner),
    }

    try:
        with st.spinner("Calculating best price..."):
            res = requests.post(API_URL, json=payload, timeout=20)

        if res.status_code == 200:
            data = res.json()
            pred = data.get("prediction", data.get("predicted_price", data.get("prediction_price", None)))

            if pred is None:
                st.warning("API responded but prediction key not found.")
                st.json(data)
            else:
                depreciation = present_price - pred
                depreciation_pct = (depreciation / present_price) * 100 if present_price > 0 else 0

                st.markdown(f"""
                <div class="result-card">
                    <div class="label">Estimated Selling Price</div>
                    <div class="price">₹ {pred:.2f} Lakhs</div>
                    <div class="sublabel">Original Price: ₹ {present_price:.2f} L &nbsp;|&nbsp; Depreciation: ₹ {depreciation:.2f} L ({depreciation_pct:.1f}%)</div>
                </div>
                """, unsafe_allow_html=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("🏷️ Predicted Price", f"₹{pred:.2f}L")
                col2.metric("📉 Depreciation", f"₹{depreciation:.2f}L", delta=f"-{depreciation_pct:.1f}%", delta_color="inverse")
                col3.metric("📆 Car Age", f"{age} yrs")

        else:
            st.error(f"❌ API Error {res.status_code}")
            st.code(res.text)

    except requests.exceptions.RequestException as e:
        st.error("❌ Could not connect to FastAPI. Make sure it's running!")
        st.code(str(e))

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("🚗 Car Price Predictor — Built with ❤️ by soy_yo-dev")
