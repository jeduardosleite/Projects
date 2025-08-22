<h1 style="color:blue;">Project: Classification of Breast Tumors with Random Forest</h1>

<img width="1019" height="526" alt="image" src="https://github.com/user-attachments/assets/7f69f940-bf5d-4e35-bc89-9b9c0b61c985" />

- [1. Objective](#1-objective)
- [2. Context](#2-context)
- [3. Project stages](#3-project-stages)
- [4. Results](#4-results)
  - [Main variables for forecasting](#main-variables-for-forecasting)
  - [Meaning of columns](#meaning-of-columns)
  - [Main columns](#main-columns)
- [5. Insights from the Model](#5-insights-from-the-model)
- [6. Applicability Insights](#6-applicability-insights)
- [Summary](#7-summary)


### 1. Objective

Develop a machine learning model capable of classifying breast tumors as malignant or benign with high accuracy, using the Random Forest algorithm.
The idea is to show how an ensemble model can be applied to health problems, helping to detect breast cancer early.

### 2. Context
Breast cancer is one of the leading causes of death among women worldwide. Early detection is essential to increase the chances of effective treatment. This project uses the Breast Cancer Wisconsin dataset, which is widely used in the scientific community to test classification models.

### 3. Project stages
- Data collection and loading — use of scikit-learn's load_breast_cancer dataset.
- Exploratory analysis — visualization of distributions and correlations between variables.
- Training/testing split — 70% of data for training, 30% for testing.
- Model training — application of Random Forest with 100 trees.
- Model evaluation — calculation of accuracy, precision, recall and F1-score.
- Interpretation of results — identification of the most important variables.
- Conclusions — analysis of the impact of variables and applicability of the model.
---
### 4. Results
Accuracy: 97.07% on the test set. The model showed high recall for malignant tumors, reducing the risk of false negatives.

#### Main variables for forecasting
Characteristics related to the shape and size of the tumor, such as **mean concave points**, **worst concave points** and **worst area**.

#### Meaning of columns
The dataset has 30 numerical variables derived from the digital analysis of images of breast masses obtained by biopsy. Each variable represents a geometric or textural characteristic of the tumor cell.
The measurements were calculated in three ways:

- mean
- if (standard error)
- worst (highest observed value)

#### Main columns:

1. radius — average distance from the center to the perimeter of the tumor.

2. texture — variation in the gray intensity of the image.

3. perimeter — length of the tumor contour.

4. area — area occupied by the tumor.

5. smoothness — variation in the length of the rays, indicating surface irregularity.

6. compactness — relationship between the perimeter and the area, measuring compactness.

7. concavity — degree of concavity in parts of the contour.

8. concave points — number of concave points in the contour.

9. symmetry — symmetry of form.

10. fractal dimension — contour complexity.

The set also includes the target variable:

- 0 → Malignant

- 1 → Benign

### 5. Insights from the Model

1. **High Predictive Performance**  
   - The model achieved **97.07% accuracy** and a high **recall for malignant tumors**, meaning it is very effective at identifying cancer cases while reducing **false negatives** (the most critical risk in medical diagnostics).  
   - This suggests that Random Forest is a strong choice for healthcare problems where **patient safety** is the top priority.  

2. **Most Important Variables**  
   - The main predictive features are related to **tumor shape and size**:  
     - **Mean concave points**  
     - **Worst concave points**  
     - **Worst area**  
     - **Mean concavity**  
     - **Worst radius**  
   - This indicates that **irregularities in tumor contours** and **tumor dimensions** are critical factors in detecting malignancy.  

3. **Clinical Interpretation**  
   - Malignant tumors tend to have **more irregular borders and less uniform shapes**, reflected in the concave points.  
   - Larger and more aggressive tumors typically show higher values in **area** and **radius**.  
   - Therefore, the model reinforces known findings in medical literature, which increases its credibility.  

---

### 6. Applicability Insights

1. **Clinical Decision Support**  
   - The model can be used as a **decision-support tool** for physicians, assisting in initial screening and prioritization of more detailed exams.  

2. **Model Explainability**  
   - Random Forest allows for interpreting feature importance, which is crucial in medical applications (where the “why” behind a decision is almost as important as the decision itself).  

3. **Integration Potential**  
   - The model could be integrated into **hospital systems** for automatic analysis of exam data, helping reduce diagnosis time and increasing early detection rates.  

---

### 7. Summary
The model not only delivered **excellent technical performance**, but also highlighted **tumor characteristics already known in oncology** (irregularity and size), which increases its reliability and shows real potential for practical application.

