import matplotlib.pyplot as plt

def create_horizontal_bar(ax, labels, values, colors):
    for i, (left, right) in enumerate(values):
        left = left * 100
        right = right * 100
        ax.barh(i, left, color=colors[0], height=0.6)
        ax.barh(i, right, left=left, color=colors[1], height=0.6)
        ax.text(left / 2, i, f'{left:.1f}%', va='center', ha='center', color='white')
        ax.text(right + (100 - right) / 2, i, f'{right:.1f}%', va='center', ha='center', color='white')


    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.set_xlabel('Percentage', labelpad=10)
    ax.set_title('8values Results')

def plot_eightvalues_data(data):
    categories = ['Equality <--> Markets', 'Nation <--> Globe', 'Liberty <--> Authority', 'Tradition <--> Progress']

    data = [v / 100 for v in data]
    data = [[value, 1 - value] for value in data]



    fig, ax = plt.subplots(figsize=(10, 4))

    colors = ['#f44336', '#00897b']

    create_horizontal_bar(ax, categories, data, colors)

    plt.tight_layout(rect=[0, 0, 0.96, 0.96])
    plt.show()

with open('/Users/andrew/Documents/dev/llm_poli_compass/llm_poli_compass/eightvalues_test_results/Marx-3B-V2-Q4_1-GGUF.csv', 'r') as f:
    f = f.readlines()

data = list(map(float,f[0].split(',')))

plot_eightvalues_data(data)