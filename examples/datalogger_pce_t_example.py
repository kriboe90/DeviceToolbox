file = 'TMB01017.XLS'
data = DataLogger(file, delimiter='\t')


data.show_info()

dataset = data.get_data(14)
for i in range(1,9):
    plt.plot(dataset.index, dataset[f'Channel_{i}'])
plt.grid()
plt.ylim(0, 150)
plt.show()