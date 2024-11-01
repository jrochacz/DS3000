import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('extracted_data_updated.csv')

y_true = df['actual_delay']
X = df[['actual_time', 'scheduled_time', 'id']]

X_train, X_test, y_train, y_test = train_test_split(X, y_true, test_size=0.2)

poly = PolynomialFeatures(degree=3)  # Use degree=3 for a cubic fit; adjust as needed
X_poly_train = poly.fit_transform(X_train[['actual_time']])
X_poly_test = poly.transform(X_test[['actual_time']])

model = LinearRegression()
model.fit(X_poly_train, y_train)

y_pred = model.predict(X_poly_test)

X_curve = np.linspace(X['actual_time'].min(), X['actual_time'].max(), 100).reshape(-1, 1)
X_curve_poly = poly.transform(X_curve)
y_curve = model.predict(X_curve_poly)

plt.figure(figsize=(10, 6))
plt.scatter(X_test['actual_time'], y_test, label="Actual Delay", alpha=0.5)
plt.scatter(X_test['actual_time'], y_pred, color="red", label="Predicted Delay", alpha=0.5)
plt.plot(X_curve, y_curve, color="green", label="Curve of Best Fit", linewidth=2)

plt.title("Scatter Plot with Curve of Best Fit for Delay Based on Actual Time")
plt.xlabel("Actual Time")
plt.ylabel("Delay")
plt.legend()
plt.show()
