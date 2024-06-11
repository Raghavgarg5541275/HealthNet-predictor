import streamlit as st
import numpy as np
import pickle

heart_disease_model = pickle.load(open('C:/Users/Raghav/Desktop/HealthNet/Drive/saved models/HealthNet_Heart.sav', 'rb'))
diabetes_model = pickle.load(open('C:/Users/Raghav/Desktop/HealthNet/Drive/saved models/HealthNet_Diabetes.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/Raghav/Desktop/HealthNet/Drive/saved models/HealthNet_ parkinsons.sav', 'rb'))

st.set_page_config(page_title="HealthNet", page_icon=":heartbeat:")
st.title("HealthNet")
st.write("Welcome to HealthNet - Predicting Tomorrow, Protecting Today: Your Health, Our Tech")

with st.sidebar:
    st.markdown("**Choose a Prediction**")
    selected = st.selectbox("", ['Heart Disease Prediction', 'Diabetes Prediction', "Parkinson's Disease Prediction"])

heart_disease_ranges = {
    "Age": (20, 80),
    "Resting Blood Pressure": (90, 120),
    "Serum Cholestoral (mg/dl)": (125, 200),
    "Maximum Heart Rate Achieved": (60, 100),
    "ST Depression Induced by Exercise": (0, 1),
    "Number of Major Vessels Colored by Fluoroscopy": (0, 3)
}

diabetes_ranges = {
    "Glucose": (70, 140),
    "Blood Pressure": (60, 90),
    "Skin Thickness": (10, 35),
    "Insulin": (40, 150),
    "BMI": (18.5, 24.9),
    "Diabetes Pedigree Function": (0.1, 0.5)
}

parkinsons_ranges = {
    "MDVP:Fo(Hz)": (80, 350),
    "MDVP:Fhi(Hz)": (80, 600),
    "MDVP:Flo(Hz)": (40, 250),
    "MDVP:Jitter(%)": (0.0, 1.0),
    "MDVP:Jitter(Abs)": (0.0, 0.01),
    "MDVP:RAP": (0.0, 0.05),
    "MDVP:PPQ": (0.0, 0.05),
    "Jitter:DDP": (0.0, 0.15),
    "MDVP:Shimmer": (0.0, 0.1),
    "MDVP:Shimmer(dB)": (0.0, 1.0),
    "Shimmer:APQ3": (0.0, 0.05),
    "Shimmer:APQ5": (0.0, 0.1),
    "MDVP:APQ": (0.0, 0.1),
    "Shimmer:DDA": (0.0, 0.1),
    "NHR": (0.0, 0.2),
    "HNR": (10, 30),
    "RPDE": (0.3, 0.7),
    "DFA": (0.5, 1.0),
    "spread1": (-10, 10),
    "spread2": (0, 5),
    "D2": (1, 10),
    "PPE": (0.0, 0.5)
}

placeholder = st.empty()

if selected == "Heart Disease Prediction":
    st.header("Heart Disease Prediction")
    st.write("Please enter the following details to predict heart disease:")

    age = st.slider("Age", min_value=1, max_value=100, value=25)
    sex = st.radio("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Types", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    trestbps = st.slider("Resting Blood Pressure", min_value=80, max_value=200, value=120)
    chol = st.slider("Serum Cholestoral (mg/dl)", min_value=50, max_value=400, value=200)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
    restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    thalach = st.slider("Maximum Heart Rate Achieved", min_value=50, max_value=220, value=150)
    exang = st.radio("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.slider("ST Depression Induced by Exercise", min_value=0.0, max_value=6.2, value=3.0)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", ["0", "1", "2", "3"])
    thal = st.selectbox("Thal", ["Normal", "Fixed Defect", "Reversible Defect"])

    if st.button("Predict Heart Disease"):
        try:
            sex = 1 if sex == "Male" else 0
            cp_values = ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"]
            cp_encoded = cp_values.index(cp)
            fbs = 1 if fbs == "Yes" else 0
            restecg_values = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"]
            restecg_encoded = restecg_values.index(restecg)
            exang = 1 if exang == "Yes" else 0
            slope_values = ["Upsloping", "Flat", "Downsloping"]
            slope_encoded = slope_values.index(slope)
            thal_values = ["Normal", "Fixed Defect", "Reversible Defect"]
            thal_encoded = thal_values.index(thal)

            input_data = np.array([age, sex, cp_encoded, trestbps, chol, fbs, restecg_encoded, thalach, exang, oldpeak, slope_encoded, ca, thal_encoded], dtype=float).reshape(1, -1)

            heart_prediction = heart_disease_model.predict(input_data)

            if heart_prediction[0] == 1:
                st.error("The person is predicted to have heart disease.")
            else:
                st.success("The person is predicted to be healthy.")

            placeholder.write("**Healthy Person Ranges**")
            for param, (min_val, max_val) in heart_disease_ranges.items():
                placeholder.write(f"- {param}: {min_val}-{max_val}")

        except ValueError:
            st.error("Please enter valid input values.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if selected == "Diabetes Prediction":
    st.header("Diabetes Prediction")
    st.write("Please enter the following details to predict diabetes:")

    pregnancies = st.slider("Pregnancies", min_value=0, max_value=17, value=3)
    glucose = st.slider("Glucose", min_value=0, max_value=200, value=100)
    blood_pressure = st.slider("Blood Pressure", min_value=0, max_value=122, value=70)
    skin_thickness = st.slider("Skin Thickness", min_value=0, max_value=99, value=20)
    insulin = st.slider("Insulin", min_value=0, max_value=846, value=79)
    bmi = st.slider("BMI", min_value=0, max_value=67, value=25)
    diabetes_pedigree_function = st.slider("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
    age = st.slider("Age", min_value=21, max_value=100, value=30)

    if st.button("Predict Diabetes"):
        try:
            input_data = np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age], dtype=float).reshape(1, -1)

            diabetes_prediction = diabetes_model.predict(input_data)

            if diabetes_prediction[0] == 1:
                st.error("The person is predicted to have diabetes.")
            else:
                st.success("The person is predicted to be healthy.")

            placeholder.write("**Healthy Person Ranges**")
            for param, (min_val, max_val) in diabetes_ranges.items():
                placeholder.write(f"- {param}: {min_val}-{max_val}")

        except ValueError:
            st.error("Please enter valid input values.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
if selected == "Parkinson's Disease Prediction":
    st.header("Parkinson's Disease Prediction")
    st.write("Please enter the following details to predict Parkinson's disease:")

    mdvp_fo_hz = st.slider("MDVP:Fo(Hz)", min_value=80, max_value=350, value=200)
    mdvp_fhi_hz = st.slider("MDVP:Fhi(Hz)", min_value=80, max_value=600, value=300)
    mdvp_flo_hz = st.slider("MDVP:Flo(Hz)", min_value=40, max_value=250, value=150)
    mdvp_jitter = st.radio("MDVP:Jitter", ["Low", "Medium", "High"])
    mdvp_jitter_abs = st.slider("MDVP:Jitter(Abs)", min_value=0.0, max_value=0.01, value=0.005)
    mdvp_rap = st.slider("MDVP:RAP", min_value=0.0, max_value=0.05, value=0.025)
    mdvp_ppq = st.slider("MDVP:PPQ", min_value=0.0, max_value=0.05, value=0.025)
    jitter_ddp = st.slider("Jitter:DDP", min_value=0.0, max_value=0.15, value=0.075)
    mdvp_shimmer = st.radio("MDVP:Shimmer", ["Low", "Medium", "High"])
    mdvp_shimmer_db = st.slider("MDVP:Shimmer(dB)", min_value=0.0, max_value=1.0, value=0.5)
    shimmer_apq3 = st.slider("Shimmer:APQ3", min_value=0.0, max_value=0.05, value=0.025)
    shimmer_apq5 = st.slider("Shimmer:APQ5", min_value=0.0, max_value=0.1, value=0.05)
    mdvp_apq = st.slider("MDVP:APQ", min_value=0.0, max_value=0.1, value=0.05)
    shimmer_dda = st.slider("Shimmer:DDA", min_value=0.0, max_value=0.1, value=0.05)
    nhr = st.slider("NHR", min_value=0.0, max_value=0.2, value=0.1)
    hnr = st.slider("HNR", min_value=10, max_value=30, value=20)
    rpde = st.slider("RPDE", min_value=0.3, max_value=0.7, value=0.5)
    dfa = st.slider("DFA", min_value=0.5, max_value=1.0, value=0.75)
    spread1 = st.slider("spread1", min_value=-10, max_value=10, value=0)
    spread2 = st.slider("spread2", min_value=0, max_value=5, value=3)
    d2 = st.slider("D2", min_value=1, max_value=10, value=5)
    ppe = st.slider("PPE", min_value=0.0, max_value=0.5, value=0.25)

    if st.button("Predict Parkinson's Disease"):
        try:

            input_data = np.array([
                mdvp_fo_hz, mdvp_fhi_hz, mdvp_flo_hz,
                0 if mdvp_jitter == "Low" else 1 if mdvp_jitter == "Medium" else 2,
                mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp,
                0 if mdvp_shimmer == "Low" else 1 if mdvp_shimmer == "Medium" else 2,
                mdvp_shimmer_db, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda,
                nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe
            ]).reshape(1, -1)

            parkinsons_prediction = parkinsons_model.predict(input_data)

            if parkinsons_prediction[0] == 1:
                st.error("The person is predicted to have Parkinson's disease.")
            else:
                st.success("The person is predicted to be healthy.")

            placeholder.write("**Healthy Person Ranges**")
            for param, (min_val, max_val) in parkinsons_ranges.items():
                placeholder.write(f"- {param}: {min_val}-{max_val}")

        except ValueError:
            st.error("Please enter valid input values.")

        except Exception as e:
            st.error(f"An error occurred: {e}")