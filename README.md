# Customer Segmentation Predictor 🚀

An end-to-end Machine Learning web application that predicts customer segments based on their financial profiles. This project trains an unsupervised **K-Means Clustering** model on customer data and serves predictions through an interactive, live **Flask** web dashboard.

---

## 📊 Project Overview
Understanding customer behavior allows businesses to optimize marketing strategies. This application takes raw metrics—**Annual Income** and **Spending Score**—and classifies the user into one of five distinct behavioral clusters.

### The 5 Discovered Customer Personas:
* **Standard Class:** Average Income, Average Spend
* **High-Value Target:** High Income, High Spend
* **Careless Spender:** Low Income, High Spend
* **Careful Saver:** High Income, Low Spend
* **Sensible Shopper:** Low Income, Low Spend

---

## 🛠️ Tech Stack
* **Machine Learning:** Python, Scikit-Learn (K-Means)
* **Data Processing:** Pandas, NumPy
* **Web Backend:** Flask, Gunicorn
* **Frontend UI:** HTML5, CSS3