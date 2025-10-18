🧠 Employee Attrition Prediction App
🔗 Live App

👉 Employee Attrition Predictor

📋 Overview

This web application predicts whether an employee is likely to Stay or Leave a company based on various HR-related features.
It uses Machine Learning models (like XGBoost and Random Forest) trained on employee data to make accurate predictions.

The app provides two options for input:

CSV Upload – Upload a CSV file containing multiple employee records.

Manual Entry – Enter employee details manually for a single prediction.

⚙️ Features

✅ Predict employee attrition using trained ML models
✅ Supports both manual and batch CSV predictions
✅ Clean, interactive Streamlit interface
✅ Displays model-wise predictions (XGBoost & Random Forest)
✅ Error handling for incorrect inputs

🧩 Technologies Used

Python 3.x

Streamlit – for the web interface

Scikit-learn – for model building

XGBoost / Random Forest – for machine learning

Pandas, NumPy – for data handling

Pickle – for saving and loading trained models

🚀 How to Run Locally

Clone this repository:

git clone https://github.com/<your-username>/employee-attrition-app.git
cd employee-attrition-app


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py


Open in your browser:

http://localhost:8501

🧾 Example Output

Predicted Attrition: Stay ✅

Predicted Attrition: Leave 🚪

If both models are used, you’ll see:

XGBoost Prediction: Stay  
Random Forest Prediction: Leave  

📂 File Structure
employee-attrition-app/
│
├── app.py                     # Streamlit web app
├── model.pkl                  # Trained XGBoost model
├── model2.pkl                 # Trained Random Forest model
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
└── sample_input.csv           # Example input file


🏁 Conclusion

This Employee Attrition Prediction App demonstrates how machine learning can be effectively applied to human resource analytics.
By identifying employees who are likely to leave, organizations can take proactive steps to improve retention, optimize workforce management, and enhance workplace satisfaction.

This project highlights the power of data-driven decision-making and serves as a valuable foundation for further development in predictive HR systems.