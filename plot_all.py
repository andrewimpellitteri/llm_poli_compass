import matplotlib.pyplot as plt
import os
from plot_compass import update_compass, econv, socv, e0, s0
from plot_eightvalues import find_ideology, create_horizontal_bar
import math
import pickle

def plot_all_classic():

    basic_results_path = "./basic_test_results"

    states = []
    model_paths = []

    for model in os.listdir(basic_results_path):
        model_paths.append(model)
        with open(os.path.join('basic_test_results',model), 'r') as f:
            d = f.readlines()
            states.append([int(e.split(',')[1].strip('\n')) for e in d])

    # Create a scatter plot
    fig, ax = plt.subplots()

    # Set axis labels
    ax.set_xlabel("Economic (Left <-----> Right)")
    ax.set_ylabel("Social (Libertarian <-----> Authoritarian)")

    ax.grid(True, linestyle='--', alpha=0.6, color='gray')  # Standard grid color
    ax.axhline(0, color='black', lw=0.5)  # X-axis color
    ax.axvline(0, color='black', lw=0.5)  # Y-axis color

    # Set axis limits
    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)

    # Fill the four quadrants with standard colors
    ax.fill_between([-7, 0], -7, 0, color='green', alpha=0.2, label='Libertarian Left')  # Quadrant I
    ax.fill_between([0, 7], -7, 0, color='yellow', alpha=0.2, label='Libertarian Right')  # Quadrant II
    ax.fill_between([-7, 0], 0, 7, color='red', alpha=0.2, label='Authoritarian Left')  # Quadrant III
    ax.fill_between([0, 7], 0, 7, color='blue', alpha=0.2, label='Authoritarian Right')  # Quadrant IV

    titles = []

    cmap = plt.get_cmap('tab10')
    scatter_handles = []


    for i, (state, model_path) in enumerate(zip(states, model_paths)):

        print(state, model_path)
        
        new_x, new_y = update_compass(state, econv, socv, e0, s0, DEBUG=True)

        model_label = os.path.basename(model_path)

        titles.append(model_label)

        color = cmap(i % cmap.N)

        scatter = ax.scatter(new_x, new_y, color=color, marker='o', s=100, label=model_label)

        scatter_handles.append(scatter)

    final_title = "\n".join(titles)

    # Title and legend
    ax.set_title(f"Political Compass: {final_title}")
        
    ax.legend(handles=scatter_handles, loc='upper left')

    plt.show()

def plot_all_eightvalues():

    eightvalues_test_paths = "./eightvalues_test_results"

    model_paths = []
    data_list = []
    closest_ideos = []

    for model in os.listdir(eightvalues_test_paths):
        model_paths.append(model)
        with open(os.path.join('eightvalues_test_results',model), 'r') as f:
            d = f.readlines()
            data = [list(map(float, e.strip("\n").split(","))) for e in d][0]
            data_list.append(data)
            closest_ideos.append(find_ideology(data))

        print(data_list, closest_ideos)



    num_plots = len(data_list)
    num_cols = 2  # Number of columns for subplots
    num_rows = math.ceil(num_plots / num_cols)  # Calculate number of rows required

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(14, 5 * num_rows))  # Adjust figure size as needed

    for i, (data, closest_ideo, model_path) in enumerate(zip(data_list, closest_ideos, model_paths)):
        row = i // num_cols
        col = i % num_cols

        categories = ['Equality <--> Markets', 'Nation <--> Globe', 'Liberty <--> Authority', 'Tradition <--> Progress']
        data = [v / 100 for v in data]
        data = [[value, 1 - value] for value in data]

        ax = axes[row, col] if num_plots > 1 else axes  # Handle single plot scenario

        colors = ['#f44336', '#00897b']

        create_horizontal_bar(ax, categories, data, colors, closest_ideo, model_path)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def plot_character_results(model_path, character_resps, load_from_file=None):

    char_colors = {
    "Lib-Left": "green", 
    
    "Lib-Right": "yellow",
    
    "Auth-Left": "red",
    
    "Auth-Right": "blue"
    }


    if load_from_file is not None:
        with open(load_from_file, 'rb') as f:
            character_resps = pickle.load(f)
        model_path = os.path.basename(load_from_file)

    # Create a scatter plot
    fig, ax = plt.subplots()

    # Set axis labels
    ax.set_xlabel("Economic (Left <-----> Right)")
    ax.set_ylabel("Social (Libertarian <-----> Authoritarian)")

    ax.grid(True, linestyle='--', alpha=0.6, color='gray')  # Standard grid color
    ax.axhline(0, color='black', lw=0.5)  # X-axis color
    ax.axvline(0, color='black', lw=0.5)  # Y-axis color

    # Set axis limits
    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)

    # Fill the four quadrants with standard colors
    ax.fill_between([-7, 0], -7, 0, color='green', alpha=0.2, label='Libertarian Left')  # Quadrant I
    ax.fill_between([0, 7], -7, 0, color='yellow', alpha=0.2, label='Libertarian Right')  # Quadrant II
    ax.fill_between([-7, 0], 0, 7, color='red', alpha=0.2, label='Authoritarian Left')  # Quadrant III
    ax.fill_between([0, 7], 0, 7, color='blue', alpha=0.2, label='Authoritarian Right')  # Quadrant IV

    scatter_handles = []

    all_vals = []

    for i, (character, state) in enumerate(character_resps.items()):

        print(state, model_path)
        
        new_x, new_y = update_compass(state, econv, socv, e0, s0, DEBUG=True)

        all_vals.append((new_x, new_y))

        scatter = ax.scatter(new_x, new_y, color=char_colors[character], marker='o', s=100, label=character)

        scatter_handles.append(scatter)

    if all_vals:
        x_coords, y_coords = zip(*all_vals)  # Unpack x and y coordinates

        avg_x = sum(x_coords) / len(all_vals)
        avg_y = sum(y_coords) / len(all_vals)

    scatter = ax.scatter(avg_x, avg_y, color='black', marker='o', s=100, label='Average')

    scatter_handles.append(scatter)

    # Title and legend
    ax.set_title(f"Political Compass: {os.path.basename(model_path)}")
        
    ax.legend(handles=scatter_handles, loc='upper left')

    plt.show()