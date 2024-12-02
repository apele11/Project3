import pandas as pd
import matplotlib.pyplot as plt
import time

file_path = 'static/heart_2020_cleaned.csv'
data = pd.read_csv(file_path)

bmi_data = data[['BMI', 'HeartDisease']]
bmi_data = data[['BMI', 'HeartDisease']]

bmi_data['HeartDisease'] = bmi_data['HeartDisease'].apply(lambda x: 1 if x == 'Yes' else 0)

bmi_data_grouped = bmi_data.groupby('BMI')['HeartDisease'].mean().reset_index()

bmi_data_grouped['BMI'] = bmi_data_grouped['BMI'].astype(float)

def main():
    def heapify(arr, n, i):
        largest = i  
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left][0] > arr[largest][0]:
            largest = left

        if right < n and arr[right][0] > arr[largest][0]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heap_sort(arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    bmi_heart_list = list(zip(bmi_data_grouped['BMI'], bmi_data_grouped['HeartDisease']))

    start_time = time.time()

    heap_sort(bmi_heart_list)

    end_time = time.time()

    elapsed_time = end_time - start_time

    sorted_bmi_data = pd.DataFrame(bmi_heart_list, columns=['BMI', 'HeartDisease'])

    sorted_bmi_data['Index'] = range(1, len(sorted_bmi_data) + 1)

    soft_colors = ['#6BAF92' if value == 0 else '#D36C6C' for value in sorted_bmi_data['HeartDisease']]

    filtered_data_40 = sorted_bmi_data[sorted_bmi_data['BMI'] <= 40]

    plt.figure(figsize=(12, 6))
    plt.bar(filtered_data_40['Index'], filtered_data_40['BMI'], color=soft_colors[:len(filtered_data_40)], width=1.0, alpha=1.0)

    plt.text(
        x=len(filtered_data_40) * 0.7, y=35, 
        s=f"Heap Sort: {elapsed_time:.6f} seconds",
        fontsize=12, bbox=dict(facecolor='white', alpha=0.7, edgecolor='black')
    )

    plt.title("BMI Levels with Heart Disease Status (Up to BMI 40)", fontsize=16)
    plt.xlabel("Sorted Index by BMI", fontsize=14)
    plt.ylabel("BMI Levels", fontsize=14)
    plt.xticks([])  
    plt.yticks(fontsize=12)
    plt.tight_layout()
    
    output_path = 'static/images/heap_sort_chart.png'
    try:
        plt.savefig(output_path)
        print("Plot saved successfully.")
    except Exception as e:
        print(f"Error saving plot: {e}")


