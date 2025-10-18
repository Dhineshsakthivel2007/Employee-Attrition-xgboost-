# app.py
import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load trained XGBoost model
# -----------------------------
with open("XGboost_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Employee Attrition Prediction using XGBoost")
st.write("""
This app predicts **employee attrition** based on employee data.
You can either **upload a CSV** with numeric columns or **enter numeric values manually**.
""")

# -----------------------------
# Numeric columns used in training
# -----------------------------
numeric_cols = [
    'Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction',
    'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobSatisfaction', 'MonthlyIncome',
    'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike', 'PerformanceRating',
    'RelationshipSatisfaction', 'StockOptionLevel', 'TotalWorkingYears', 
    'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 
    'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

# -----------------------------
# Option selection
# -----------------------------
option = st.radio("Choose input method:", ("Upload CSV", "Manual Entry"))

# -----------------------------
# Option 1: CSV Upload
# -----------------------------
if option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df)

        if st.button("Predict Attrition for CSV"):
            try:
                # Select only numeric columns
                df_numeric = df[numeric_cols]
                predictions = model.predict(df_numeric)
                df["Attrition_Prediction"] = predictions
                st.write("Predictions:")
                st.dataframe(df)
            except Exception as e:
                st.error(f"Error in prediction: {e}")

# -----------------------------
# Option 2: Manual Entry
# -----------------------------
if option == "Manual Entry":
    st.header("Enter Numeric Employee Details Manually")
    with st.form(key="manual_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            Age = st.number_input("Age", 18, 65, 30)
            DailyRate = st.number_input("DailyRate", 100, 1500, 500)
            DistanceFromHome = st.number_input("DistanceFromHome", 0, 50, 5)
            Education = st.selectbox("Education", [1, 2, 3, 4, 5])
            EnvironmentSatisfaction = st.selectbox("EnvironmentSatisfaction", [1, 2, 3, 4])
            HourlyRate = st.number_input("HourlyRate", 20, 150, 60)
            JobInvolvement = st.selectbox("JobInvolvement", [1, 2, 3, 4])
            JobLevel = st.selectbox("JobLevel", [1, 2, 3, 4, 5])
            JobSatisfaction = st.selectbox("JobSatisfaction", [1, 2, 3, 4])

        with col2:
            MonthlyIncome = st.number_input("MonthlyIncome", 1000, 50000, 5000)
            MonthlyRate = st.number_input("MonthlyRate", 1000, 50000, 10000)
            NumCompaniesWorked = st.number_input("NumCompaniesWorked", 0, 20, 1)
            PercentSalaryHike = st.number_input("PercentSalaryHike", 10, 25, 15)
            PerformanceRating = st.selectbox("PerformanceRating", [1, 2, 3, 4])
            RelationshipSatisfaction = st.selectbox("RelationshipSatisfaction", [1, 2, 3, 4])
            StockOptionLevel = st.selectbox("StockOptionLevel", [0, 1, 2, 3])
            TotalWorkingYears = st.number_input("TotalWorkingYears", 0, 40, 5)

        with col3:
            TrainingTimesLastYear = st.number_input("TrainingTimesLastYear", 0, 20, 2)
            WorkLifeBalance = st.selectbox("WorkLifeBalance", [1, 2, 3, 4])
            YearsAtCompany = st.number_input("YearsAtCompany", 0, 40, 3)
            YearsInCurrentRole = st.number_input("YearsInCurrentRole", 0, 20, 2)
            YearsSinceLastPromotion = st.number_input("YearsSinceLastPromotion", 0, 15, 1)
            YearsWithCurrManager = st.number_input("YearsWithCurrManager", 0, 20, 2)

        submit_button = st.form_submit_button(label="Predict Attrition")

        if submit_button:
            input_data = pd.DataFrame({
                "Age":[Age],
                "DailyRate":[DailyRate],
                "DistanceFromHome":[DistanceFromHome],
                "Education":[Education],
                "EnvironmentSatisfaction":[EnvironmentSatisfaction],
                "HourlyRate":[HourlyRate],
                "JobInvolvement":[JobInvolvement],
                "JobLevel":[JobLevel],
                "JobSatisfaction":[JobSatisfaction],
                "MonthlyIncome":[MonthlyIncome],
                "MonthlyRate":[MonthlyRate],
                "NumCompaniesWorked":[NumCompaniesWorked],
                "PercentSalaryHike":[PercentSalaryHike],
                "PerformanceRating":[PerformanceRating],
                "RelationshipSatisfaction":[RelationshipSatisfaction],
                "StockOptionLevel":[StockOptionLevel],
                "TotalWorkingYears":[TotalWorkingYears],
                "TrainingTimesLastYear":[TrainingTimesLastYear],
                "WorkLifeBalance":[WorkLifeBalance],
                "YearsAtCompany":[YearsAtCompany],
                "YearsInCurrentRole":[YearsInCurrentRole],
                "YearsSinceLastPromotion":[YearsSinceLastPromotion],
                "YearsWithCurrManager":[YearsWithCurrManager]
            })
            try:
                prediction = model.predict(input_data)
                result = "Stay" if prediction[0] == 0 else "Leave"
                st.success(f"Predicted Attrition: {result}")
            except Exception as e:
                st.error(f"Error in prediction: {e}")

