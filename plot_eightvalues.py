import matplotlib.pyplot as plt
import math
import json

def find_ideology(values):

    file_path = 'ideologies.json'

    with open(file_path, 'r') as file:
        ideologies = json.load(file)

    ideology = ""
    ideodist = float('inf')

    for ideology_data in ideologies:
        dist = 0
        dist += math.pow(abs(ideology_data['stats']['econ'] - values[0]), 2)
        dist += math.pow(abs(ideology_data['stats']['govt'] - values[1]), 2)
        dist += math.pow(abs(ideology_data['stats']['dipl'] - values[2]), 1.73856063)
        dist += math.pow(abs(ideology_data['stats']['scty'] - values[3]), 1.73856063)

        if dist < ideodist:
            ideology = ideology_data['name']
            ideodist = dist

    return ideology

def create_horizontal_bar(ax, labels, values, colors, closest_ideo):
    for i, (left, right) in enumerate(values):
        left = left * 100
        right = right * 100
        ax.barh(i, left, color=colors[0], height=0.6)
        ax.barh(i, right, left=left, color=colors[1], height=0.6)
        ax.text(left / 2, i, f'{left:.1f}%', va='center', ha='center', color='white')
        # ax.text(left + (right - left) / 2, i, f'{right:.1f}%', va='center', ha='center', color='white')

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.set_xlabel('Percentage', labelpad=10)
    ax.set_title(f"Closest Match: {closest_ideo}")

def plot_eightvalues_data(data, closest_ideo):
    categories = ['Equality <--> Markets', 'Nation <--> Globe', 'Liberty <--> Authority', 'Tradition <--> Progress']

    data = [v / 100 for v in data]
    data = [[value, 1 - value] for value in data]



    fig, ax = plt.subplots(figsize=(10, 4))

    colors = ['#f44336', '#00897b']

    create_horizontal_bar(ax, categories, data, colors, closest_ideo)

    plt.tight_layout(rect=[0, 0, 0.96, 0.96])
    plt.show()

