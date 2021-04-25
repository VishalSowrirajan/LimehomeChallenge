import matplotlib.pyplot as plt


def plot_number_of_user_rooms_changed(df, year):
    y = df.iloc[:, -1].to_list()
    labels = df.iloc[:, 1].to_list()
    plt.title('PRT Month-wise room changes in '+ str(year))
    colours = {'January': 'C0',
               'February': 'C1',
               'March': 'C2',
               'April': 'C3',
               'May': 'C4',
               'June': 'C5',
               'July': 'C6',
               'August': 'C7',
               'September': 'C8',
               'October': 'C9',
               'November': 'C10',
               'December': 'C11'}
    plt.pie(y, labels=labels, autopct='%.2f', colors=[colours[key] for key in labels])
    plt.show()