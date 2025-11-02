import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression

# Q1 - Find the M slope+ and the b for the table with the lowest mse
# Our data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
Y = np.array([60, 65, 70, 75, 80, 85, 90, 92, 95])


min_mean_error = None 
a_min = None 
b_min = None 
def f1(x):
    return a*x +b

for a in np.arange(-50, 50, 0.5):
    for b in np.arange(-50, 50, 0.5): 
        y1 = f1(X)
        error = []
        for i in range (len(X)):
            error_i = math.pow(Y[i] - f1(X[i]),2)
            error.append(error_i)
        error_mean = sum(error)/len(error)

        if min_mean_error == None or error_mean < min_mean_error:
            min_mean_error = error_mean
            a_min = a
            b_min = b
            
print(f"The min MSE is: {min_mean_error:.3f}\nThe slope (m): {a_min:.2f}\nThe intercept (b): {b_min:.2f}")
equation = f"y = {a_min:.2f}x + {b_min:.2f}"
print(f"Line equation: {equation}")


# Our data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1) #hours Learned
Y = np.array([60, 65, 70, 75, 80, 85, 90, 92, 95])  #Grade

# Create regression model
model = LinearRegression()
model.fit(X, Y)

m = model.coef_[0] # (x)Slope 
b = model.intercept_ # (b)
y_pred = m * X + b

for i in range (len(X)):
    plt.scatter(X[i],Y[i]) 

#MSE Loop
error = []
for i in range (len(X)):
    error_i = m * X[i ,0] + b
    error.append((Y[i] - error_i)**2)
    error_mean = sum(error)/len(error)
    
print(f"MSE (loop): {error_mean:.3f}")

# Print results
print(f"Slope (m): {model.coef_[0]:.2f}")
print(f"Intercept (b): {model.intercept_:.2f}")

# Calculate equation
equation = f"y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}"
print(f"Line equation: {equation}")

plt.axhline(50, color='black', linewidth=0.8, linestyle="--")  # x-axis
plt.axvline(0, color='black', linewidth=0.8, linestyle="--")  # y-axis
plt.plot(X, y_pred, label=equation)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.show()



#Q2 -from sklearn.linear_model import LinearRegression
# Our data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1) #hours Learned
Y = np.array([60, 65, 70, 75, 80, 85, 90, 92, 95])  #Grade

# Create regression model
model = LinearRegression()
model.fit(X, Y)

m = model.coef_[0] # (x)Slope 
b = model.intercept_ # (b)
y_pred = m * X + b

for i in range (len(X)):
    plt.scatter(X[i],Y[i]) 

#MSE Loop
error = []
for i in range (len(X)):
    error_i = m * X[i ,0] + b
    error.append((Y[i] - error_i)**2)
    error_mean = sum(error)/len(error)
    
print(f"MSE (loop): {error_mean:.3f}")

# Print results
print(f"Slope (m): {model.coef_[0]:.2f}")
print(f"Intercept (b): {model.intercept_:.2f}")

# Calculate equation
equation = f"y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}"
print(f"Line equation: {equation}")

plt.axhline(50, color='black', linewidth=0.8, linestyle="--")  # x-axis
plt.axvline(0, color='black', linewidth=0.8, linestyle="--")  # y-axis
plt.plot(X, y_pred, label=equation)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.show()


#Q3 grade 100 study 9.6

m = 4.52
b = 56.53

Q = input("Would you like to choose between Grade (g) to get or Hours (h) to study?: ").lower()

if Q == "g":
    y = float(input("Please enter the Grade you would like to get: "))
    while y < 60:
        print("You need to think again about your choices.\n")
        y = float(input("Please enter the Grade you would like to get: "))

    study_time = (y - b) / m
    hours = int(study_time)
    minutes = int((study_time - hours) * 60)
    print(f"Your minimum study time will be: {hours} hours and {minutes} minutes.")

elif Q == "h":
    x = float(input("Please enter how much time you plan to study (in hours): "))
    while x <= 0:
        print("Study time must be positive!\n")
        x = float(input("Please enter how much time you plan to study (in hours): "))

    End_grade = (m * x) + b
    print(f"The grade you will get is: {End_grade:.2f} points.")

else:
    print("Invalid choice. Please enter 'g' for grade or 'h' for hours.")

