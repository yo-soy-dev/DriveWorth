# 🚗 DriveWorth - Car Price Predictor — Full Stack ML Project

## 📌 Project Overview

Car Price Predictor is a full stack machine learning web application that predicts the selling price of a used car based on various features such as car age, fuel type, kilometers driven, transmission type, and more. The system uses a Machine Learning model served through a FastAPI backend and a Streamlit frontend for user interaction.

This project demonstrates the integration of Machine Learning with Web Development using API architecture.

---

## 🧠 Machine Learning Model

* Algorithm Used: Linear Regression / Random Forest (update based on your model)
* Evaluation Metrics:

  * R2 Score
  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)
* Important Features:

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
User → Streamlit Frontend → FastAPI Backend → ML Model → Prediction → Streamlit UI
```

### Detailed Flow:

1. User enters car details in Streamlit UI
2. Streamlit sends data to FastAPI via HTTP POST request
3. FastAPI processes the data and sends it to the ML model
4. ML model predicts the car selling price
5. FastAPI returns the prediction as JSON response
6. Streamlit displays the predicted price and analytics

---

## 🚀 Features

* Full Stack Machine Learning Application
* FastAPI Backend for ML Model Serving
* Streamlit Frontend UI
* Real-time Price Prediction
* Depreciation Calculation
* Interactive UI with Cards and Metrics
* API Integration

---

## 📂 Project Structure

```
Car-Price-Predictor/
│
├── frontend/
│   └── app.py                # Streamlit UI
│
├── backend/
│   └── main.py               # FastAPI server
│
├── model/
│   ├── car_price_model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
├── notebook/
│   └── model_training.ipynb
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
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
streamlit run app.py
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

* Predicted Selling Price (in Lakhs)
* Depreciation Value
* Depreciation Percentage
* Car Age

---

## 🔮 Future Improvements

* Deploy FastAPI on cloud (Render / AWS)
* Deploy Streamlit on Streamlit Cloud
* Add more ML models for comparison
* Add model accuracy visualization
* Add price trend visualization

---

## 👨‍💻 Author

Devansh Tiwari

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

This project is for educational purposes only and the predicted price may not reflect actual market prices.

---

## ⭐ If you like this project, give it a star on GitHub!
