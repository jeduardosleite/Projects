<h1 style="color:blue;">Project: Classification of Breast Tumors with Random Forest</h1>

<img width="1019" height="526" alt="image" src="https://github.com/user-attachments/assets/7f69f940-bf5d-4e35-bc89-9b9c0b61c985" />


#### Objective

Develop a machine learning model capable of classifying breast tumors as malignant or benign with high accuracy, using the Random Forest algorithm.
The idea is to show how an ensemble model can be applied to health problems, helping to detect breast cancer early.

#### Context
Breast cancer is one of the leading causes of death among women worldwide. Early detection is essential to increase the chances of effective treatment. This project uses the Breast Cancer Wisconsin dataset, which is widely used in the scientific community to test classification models.

#### Project stages
- Data collection and loading — use of scikit-learn's load_breast_cancer dataset.
- Exploratory analysis — visualization of distributions and correlations between variables.
- Training/testing split — 70% of data for training, 30% for testing.
- Model training — application of Random Forest with 100 trees.
- Model evaluation — calculation of accuracy, precision, recall and F1-score.
- Interpretation of results — identification of the most important variables.
- Conclusions — analysis of the impact of variables and applicability of the model.
---
### Results
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
