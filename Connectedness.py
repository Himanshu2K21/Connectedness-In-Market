import numpy as np

# Provided covariance values
covariance_values = {
    '10/21/2022': 13278.88016,'10/24/2022': 8751.61806,'10/25/2022': 8646.46485,'10/27/2022': 8131.04756,'10/28/2022': 7626.64531,'10/31/2022': 3130.77244,'11/1/2022': 777.65672,'11/2/2022': 797.74078,'11/3/2022': 2311.45354,'11/4/2022': 1300.75773,'11/7/2022': 278.83494,'11/9/2022': 96.85445,'11/10/2022': 1974.22299,
    '11/11/2022': -44.43306,
    '11/14/2022': 35.80257,
    '11/15/2022': 126.01873,
    '11/16/2022': 229.40055,
    '11/17/2022': 43.73312,
    '11/18/2022': -0.29099,
    '11/21/2022': 257.79770,
    '11/22/2022': 223.47440,
    '11/23/2022': -13.38849,
    '11/24/2022': 62.37283,
    '11/25/2022': 1163.82515,
    '11/28/2022': 790.96342,
    '11/29/2022': 1957.74959,
    '11/30/2022': 3711.56635,
    '12/1/2022': 7428.19648,
    '12/2/2022': 4493.40953,
    '12/5/2022': 4210.76142,
    '12/6/2022': 2538.46906,
    '12/7/2022': 2169.12780,
    '12/8/2022': 2048.85482,
    '12/9/2022': 1737.60773,
    '12/12/2022': 445.92867,
    '12/13/2022': 1672.74534,
    '12/14/2022': 3326.37478,
    '12/15/2022': 850.38744,
    '12/16/2022': -6.58154
}

# Define a threshold (you can adjust this as needed)
threshold = 1000

# Assess connectedness and construct the connectedness matrix
dates = list(covariance_values.keys())
connectedness_matrix = np.zeros((len(dates), len(dates)), dtype=int)

for i, date1 in enumerate(dates):
    for j, date2 in enumerate(dates):
        if i != j:  # Avoid comparing a date with itself
            covariance = covariance_values[date1]
            if abs(covariance) > threshold:
                connectedness_matrix[i, j] = 1

# Print the connectedness matrix
print("Connectedness Matrix:")
print(connectedness_matrix)
