# student-performance-end-to-end

#### Project Overview
- This is a personal academic project developed to predict student academic success (Pass/Fail) based on a variety of demographic, social, and academic factors. The system leverages a full-stack approach, integrating custom   Python data structures, Exploratory Data Analysis (EDA), Machine Learning, and Deep Learning, culminating in a web-based deployment using Flask.

---
#### Dataset Information
The project utilizes the student dataset (**student_data_3.csv**), which tracks 30+ features across the following domains:
*   **Demographics:** School, gender, age, address type, family size, and parental cohabitation status[cite: 4].
*   **Social Factors:** Parental education/jobs, reason for school choice, and home environment quality (family relations, free time, going out, and alcohol consumption)[cite: 4].
*   **Academic Factors:** Weekly study time, number of past class failures, school/family educational support, extracurricular activities, and desire for higher education[cite: 4].
*   **Performance Metrics:** Grades for three specific subjects (G1, G2, G3) and number of school absences[cite: 4].

---
#### Repositry Structure
```text 
├── data/
│   ├── student_data_3.csv             # Processed dataset used for ML/DL training
│   └── students_export.json       # Raw data exported via custom file-handling
├── notebooks/
│   └── Student_Performance_End_to_End_.ipynb  # Comprehensive Module 1-7 technical workflow
├── templates/
│   └── index.html                     # Pure HTML frontend for the Flask web application
├── .gitignore                         # Prevents venv/ and __pycache__/ from being uploaded
├── README.md                          # Project documentation, insights, and setup instructions
├── main.py                            # Flask backend entry point for real-time prediction
├── requirements.txt                   # Dependency list (Flask, pandas, scikit-learn==1.6.1, etc.)
└── student_classifier.pkl             # Serialized Logistic Regression pipeline (Scaler + Model)
```
---
#### Insights & Observations
Key technical and academic patterns identified during the research phase include:
*  **Top Performance Predictors:** Grade 1 (G1) and Grade 2 (G2) scores have the strongest positive correlation ($0.80+$) with the final outcome, making them the most reliable early warning signs.
*  **Primary Academic Risk:** The number of past class failures is the most significant negative predictor; as failures increase, the likelihood of a "Pass" drop significantly.
*  **The "Ambition" Factor:** Students who explicitly state a desire for higher education show a strong statistical trend toward higher final grades.
*  **Demographic Influence:** Higher maternal education (Medu) levels correlate positively with student success, likely due to increased home academic support.
*  **Lifestyle Trade-offs:** High frequency of going out with friends and workday alcohol consumption (Dalc) are the most notable non-academic activities linked to poor performance.
*  **Deployment Efficiency:** The Logistic Regression model provides the best balance of speed and accuracy, delivering a "PASS/FAIL" prediction and a confidence percentage in milliseconds via the Flask interface.

---
#### Technical Architecture
```text
[ Data Sources ]
      ↓
[ Data Structures & Storage Layer ]
      ↓
[ Data Preprocessing Pipeline ]
      ↓
[ Exploratory Data Analysis ]
      ↓
[ Feature Engineering ]
      ↓
[ ML Models (Supervised + Unsupervised) ]
      ↓
[ Deep Learning Models ]
      ↓
[ Model Optimization & Validation ]
      ↓
[ Model Serialization ]
      ↓
[ API Layer (Flask) ]
      ↓
[ User Interface / Client Applications ]
```
---
#### Deployment
The predictor is deployed as a production-ready **Flask Web Application**.
*   **Backend:** The Python server loads a serialized `student_classifier.pkl` file containing the full preprocessing (Scaling/Encoding) and modeling pipeline[cite: 1].
*   **Frontend:** A clean HTML interface accepts 30 unique student inputs.
*   **Inference:** The system processes raw data through the learned pipeline in real-time, returning a "PASS" or "FAIL" prediction along with a confidence probability[cite: 1].
*   Below is a preview of the interactive web interface, designed for intuitive data input and instant result generation.
<img width="1913" height="949" alt="Student Success Predictor Flask Interface" src="https://github.com/user-attachments/assets/46e3cff9-4214-4c80-a95c-9008f919024a" />

---
## How to Run the Project

### **1. Direct File Links**
Explore the core components of the repository:
*   [**Backend (main.py)**](main.py): The Flask application entry point.
*   [**Technical Workflow (Jupyter Notebook)**](notebooks/Student_Performance_End_to_End_.ipynb): Step-by-step documentation from Data Structures to Deep Learning[cite: 3].
*   [**Processed Dataset (CSV)**](data/student_data.csv): The cleaned data used for model training[cite: 2].

### **2. Local Setup and Execution**
To run this project on your local machine, follow these steps:

**Step 1: Clone the Repository**
```bash
git clone [https://github.com/digvijay2420/student-performance-end-to-end.git](https://github.com/digvijay2420/student-performance-end-to-end.git)
cd student-performance-end-to-end
```
**Step 2: Create a Virtual Environment**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```
**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```
**Step 4: Launch the Application**
```bash
python main.py
```

---
---

##  Academic Profile

**Developer:** Digvijay Singh  
**Affiliations:** 
*   IITM Diploma in Data Science
*   Business Analytics Fellowship  

**Connect with me:**
*   [**GitHub Profile**](https://github.com/digvijay2420)
*   [**Personal Repository**](https://github.com/digvijay2420/student-performance-end-to-end)

---
*This project was developed as a Capstone requirement to demonstrate the practical integration of Python Data Structures, Machine Learning pipelines, and Deep Learning architectures in a production environment.*
