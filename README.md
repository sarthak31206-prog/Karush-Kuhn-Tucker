# 📊 KKT Solver — Optimization Tool

**EM-4 Assignment 9 | INFT Engineering | BSC07**

---

## 🚀 Project Overview

This project implements the **Karush–Kuhn–Tucker (KKT) conditions** using Python to solve constrained optimization problems.

The application allows users to:

* Define an objective function (maximize/minimize)
* Add inequality and equality constraints
* Provide an initial guess
* Compute optimal values and KKT multipliers

A modern interactive interface is built using **Streamlit** for ease of use and visualization.

---

## 🎯 Objectives

* Implement KKT conditions computationally
* Solve real-world constrained optimization problems
* Build an interactive UI for user input and results
* Ensure accuracy, readability, and usability

---

## 🛠️ Technologies Used

* Python
* NumPy
* SciPy
* SymPy
* Streamlit

---

## ⚙️ Features

* Supports both **maximization and minimization**
* Handles:

  * Inequality constraints (≤, ≥)
  * Equality constraints (=)
* Multi-start optimization for better accuracy
* Numerical gradient-based approximation for KKT multipliers
* Clean and interactive UI

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```bash
pip install streamlit numpy scipy sympy
```

### 2. Run the Application

```bash
python -m streamlit run main.py
```

### 3. Open in Browser

```
http://localhost:8501
```

---

## 📌 Example Input

**Objective Function:**

```
8*x1 + 10*x2 - x1^2 - x2^2
```

**Constraints:**

```
3*x1 + 2*x2 <= 6
x1 >= 0
x2 >= 0
```

---

## 📈 Sample Output

```
x1 ≈ 0.3077  
x2 ≈ 2.5385  
λ ≈ 2.4615  
Z ≈ 15.3846  
```

---

## 🧠 Methodology

1. Convert symbolic expressions using SymPy
2. Transform constraints into standard form
3. Use SciPy (SLSQP) for optimization
4. Apply multi-start technique for global optimum
5. Approximate gradients numerically
6. Compute KKT multipliers using least squares

---

## 👥 Team Contribution

* The project was developed collaboratively by all team members.
* **Each team member has contributed exactly 2 commits** to the project repository.
* Contributions include:

  * Algorithm implementation
  * UI development
  * Testing and debugging
  * Documentation

---

## 📊 Evaluation Criteria Covered

* ✔ Correct implementation of KKT conditions
* ✔ Clean and readable code
* ✔ Robust handling of constraints
* ✔ Interactive and user-friendly UI
* ✔ Proper documentation

---

## 💡 Future Improvements

* Graphical visualization of feasible region
* Step-by-step KKT explanation
* Support for higher-dimensional problems
* Export results as PDF

---

## 📎 Notes

* Ensure correct syntax for constraints (`<=`, `>=`, `=`)
* Use `^` or `**` for powers
* Provide a reasonable initial guess for best results

---

## 🎉 Conclusion

This project demonstrates the practical implementation of optimization techniques using KKT conditions and provides a strong foundation for solving real-world engineering problems.

---

