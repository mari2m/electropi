import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data_file(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    if file_extension == '.csv':
        return pd.read_csv(file_path)
    elif file_extension == '.xlsx':
        return pd.read_excel(file_path)
    else:
        raise ValueError("Check the file type")


def preprocess_data(data):
    data.fillna(data.median(), inplace=True)
    return data


def make_visualizations(data, columns):
    for col in columns:
        if col in data.columns:
            if data[col].dtype == 'int64' or data[col].dtype == 'float64':
                plt.figure(figsize=(12, 6))

                # Histogram
                plt.subplot(1, 3, 1)
                data[col].hist()
                plt.title(f'Histogram of {col}')
                plt.xlabel(col)
                plt.ylabel('Frequency')

                # Box Plot
                plt.subplot(1, 3, 2)
                data[col].plot(kind='box')
                plt.title(f'Box Plot of {col}')
                plt.ylabel(col)

                # Scatter Plot
                plt.subplot(1, 3, 3)
                plt.scatter(data.index, data[col])
                plt.title(f'Scatter Plot of {col}')
                plt.xlabel('Index')
                plt.ylabel(col)

                plt.tight_layout()
                plt.show()


                sns.catplot(1,3,4)
                sns.title(f'catplot of {col}')
                sns.ylabel(col)
                sns.show()



            else:
                print(
                    f"Column '{col}' is neither int64 nor float64, skipping visualization.")
        else:
            print(f"Column '{col}' not found in the data.")


file_path = input("Enter the file path: ")
file_data = load_data_file(file_path)
file_data.head()
print(file_data.head())

columns_to_visualize = input(
    "Enter column names to visualize (separate them with comma): ")
columns_to_visualize = [col.strip() for col in columns_to_visualize.split(',')]


preprocessed_data = preprocess_data(file_data)
make_visualizations(preprocessed_data, columns_to_visualize)