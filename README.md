# 🚗 DriveWorth — Car Price Predictor (Full Stack ML Project)

## 📌 Project Overview

DriveWorth is a full-stack machine learning web application that predicts the selling price of a used car based on key features like car age, fuel type, kilometers driven, transmission, and more.

The system uses a trained Machine Learning model served via a FastAPI backend and an interactive Streamlit frontend for real-time predictions.

---

## 🧠 Machine Learning Model

* **Algorithm Used:** Random Forest Regressor
* **Evaluation Metrics:**

  * R² Score
  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)

### 🔑 Important Features:

* Car Age
* Present Price
* Kms Driven
* Fuel Type
* Seller Type
* Transmission
* Owner

---

## 🏗️ System Architecture

```
User → Streamlit UI → FastAPI Backend → ML Model → Prediction → UI Display
```

### 🔄 Workflow:

1. User inputs car details in Streamlit UI
2. Data is sent to FastAPI via POST request
3. Backend processes and sends data to ML model
4. Model predicts car price
5. API returns prediction as JSON
6. UI displays result with insights

---

## 🚀 Features

* ✅ Full Stack ML Application
* ⚡ FastAPI Backend (high performance API)
* 🎨 Streamlit UI (interactive dashboard)
* 📊 Real-time price prediction
* 📉 Depreciation calculation
* 📦 Clean API integration

---

## 📂 Project Structure

```
DriveWorth/
│
├── car-price-api/
│   ├── cardekho_data.csv
│   ├── feature_columns.pkl
│   ├── main.py
│   ├── model.py
│   ├── random_forest_model.pkl
│   ├── requirements.txt
│   ├── runtime.txt
│   ├── schema.py
│   ├── streamlit_app.py
│   ├── train.py
│
├── .gitignore
├── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/DriveWorth.git
cd DriveWorth/car-price-api
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run FastAPI Backend

```bash
uvicorn main:app --reload
```

### 4️⃣ Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

## 📊 Input Parameters

| Feature       | Description               |
| ------------- | ------------------------- |
| Car_Name      | Name of the car           |
| Year          | Year of purchase          |
| Present_Price | Current ex-showroom price |
| Kms_Driven    | Total kilometers driven   |
| Fuel_Type     | Petrol/Diesel/CNG         |
| Seller_Type   | Dealer/Individual         |
| Transmission  | Manual/Automatic          |
| Owner         | Number of previous owners |

---

## 📈 Output

* 💰 Predicted Selling Price (in Lakhs)
* 📉 Depreciation Value
* 📊 Depreciation Percentage
* 📅 Car Age

---

## 🔮 Future Improvements

* Deploy FastAPI on Render / AWS
* Deploy Streamlit on Streamlit Cloud
* Add multiple ML model comparison
* Add accuracy visualization charts
* Add price trend analysis

---

## 👨‍💻 Author

**Devansh Kumar Tiwari**

---

## 📚 Technologies Used

* Python
* Streamlit
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Plotly

---

## ⚠️ Disclaimer

This project is for educational purposes only and predictions may not reflect actual market prices.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
