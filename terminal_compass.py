import matplotlib.pyplot as plt

e0 = 0.38
s0 = 2.41

econv = [
[.5, 2.5, -2.5, -4.5],
    [7, 5, 0, -2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [7, 5, 0, -2],
    [-7, -5, 0, 2],
    [6, 4, 0, -2],
    [7, 5, 0, -2],
    [-8, -6, 0, 2],
    [8, 6, 0, -2],
    [8, 6, 0, -1],
    [7, 5, 0, -3],
    [8, 6, 0, -1],
    [-7, -5, 0, 2],
    [-7, -5, 0, 1],
    [-6, -4, 0, 2],
    [6, 4, 0, -1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [-8, -6, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [-10, -8, 0, 1],
    [-5, -4, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [-9, -8, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

socv = [
    [0, 0, 0, 0],
    [-8, -6, 0, 2],
    [7, 5, 0, -2],
    [-7, -5, 0, 2],
    [-7, -5, 0, 2],
    [-6, -4, 0, 2],
    [7, 5, 0, -2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [-6, -4, 0, 2],
    [7, 6, 0, -2],
    [-5, -4, 0, 2],
    [0, 0, 0, 0],
    [8, 4, 0, -2],
    [-7, -5, 0, 2],
    [-7, -5, 0, 3],
    [6, 4, 0, -3],
    [6, 3, 0, -2],
    [-7, -5, 0, 3],
    [-9, -7, 0, 2],
    [-8, -6, 0, 2],
    [7, 6, 0, -2],
    [-7, -5, 0, 2],
    [-6, -4, 0, 2],
    [-7, -4, 0, 2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [7, 5, 0, -3],
    [-9, -6, 0, 2],
    [-8, -6, 0, 2],
    [-8, -6, 0, 2],
    [-6, -4, 0, 2],
    [-8, -6, 0, 2],
    [-7, -5, 0, 2],
    [-8, -6, 0, 2],
    [-5, -3, 0, 2],
    [-7, -5, 0, 2],
    [7, 5, 0, -2],
    [-6, -4, 0, 2],
    [-7, -5, 0, 2],
    [-6, -4, 0, 2],
    [0, 0, 0, 0],
    [-7, -5, 0, 2],
    [-6, -4, 0, 2],
    [-7, -6, 0, 2],
    [7, 6, 0, -2],
    [7, 5, 0, -2],
    [8, 6, 0, -2],
    [-8, -6, 0, 2],
    [-6, -4, 0, 2]
]


def update_compass(state, econv, socv, e0, s0, DEBUG=False):
    sumE = 0
    sumS = 0

    for i in range(62):
        if state[i] != -1:
            sumE += econv[i][state[i]]
            sumS += socv[i][state[i]]

    if DEBUG:
        print(f"{sumE:.2f} {sumS:.2f}")

    valE = sumE / 8.0
    valS = sumS / 19.5

    valE += e0
    valS += s0

    valE = round(valE, 2)
    valS = round(valS, 2)

    print(valE, valS)
    valE = (valE + 50) / 100 * 14 - 7;
    valS = (50 - valS) / 100 * 14 - 7;


    # Print the values (replace this with your actual HTML updating logic)
    # print(f"Economic {displayEcon} Social {displaySoc}")
    print(f"CX: {valE}, CY: {valS}")

    return valE, valS

# Example usage:
state = [0] * 62  # Replace with your actual state list

new_x, new_y = update_compass(state, econv, socv, e0, s0, DEBUG=True)

# Define data points for political figures or ideologies
data = {
    "Libertarian Left": (-5, -5),
    "Libertarian Right": (5, -5),
    "Authoritarian Left": (-5, 5),
    "Authoritarian Right": (5, 5),
}

# Create a scatter plot
fig, ax = plt.subplots()

# Add labels for data points
for label, (x, y) in data.items():
    ax.text(x, y, label, fontsize=12, ha='center', va='center')

# Set axis labels
ax.set_xlabel("Economic (Left <-----> Right)")
ax.set_ylabel("Social (Libertarian <-----> Authoritarian)")

# Customize grid and tick marks with standard colors
ax.grid(True, linestyle='--', alpha=0.6, color='gray')  # Standard grid color
ax.axhline(0, color='black', lw=0.5)  # X-axis color
ax.axvline(0, color='black', lw=0.5)  # Y-axis color

# Set axis limits
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)

# Title and legend
ax.set_title("Political Compass")
ax.legend(["Political Ideologies"])


ax.scatter(new_x, new_y, color='red', marker='o', s=100, label='Your Red Dot')


# Fill the four quadrants with standard colors
ax.fill_between([-7, 0], -7, 0, color='green', alpha=0.2, label='Libertarian Left')  # Quadrant I
ax.fill_between([0, 7], -7, 0, color='yellow', alpha=0.2, label='Libertarian Right')  # Quadrant II
ax.fill_between([-7, 0], 0, 7, color='red', alpha=0.2, label='Authoritarian Left')  # Quadrant III
ax.fill_between([0, 7], 0, 7, color='blue', alpha=0.2, label='Authoritarian Right')  # Quadrant IV

plt.show()
