import pandas as pd
import matplotlib.pyplot as plt
import time

file_path = 'static/heart_2020_cleaned.csv'
data = pd.read_csv(file_path)

bmi_data = data[['BMI', 'HeartDisease']]
bmi_data['HeartDisease'] = bmi_data['HeartDisease'].apply(lambda x: 1 if x == 'Yes' else 0)

bmi_data_grouped = bmi_data.groupby('BMI')['HeartDisease'].mean().reset_index()
bmi_data_grouped['BMI'] = bmi_data_grouped['BMI'].astype(float)

def main():
    def quick_sort(arr, paired_list):
        if len(arr) <= 1:
            return arr, paired_list

        pivot = arr[len(arr) // 2]
        left = [arr[i] for i in range(len(arr)) if arr[i] < pivot]
        left_paired = [paired_list[i] for i in range(len(arr)) if arr[i] < pivot]
        middle = [arr[i] for i in range(len(arr)) if arr[i] == pivot]
        middle_paired = [paired_list[i] for i in range(len(arr)) if arr[i] == pivot]
        right = [arr[i] for i in range(len(arr)) if arr[i] > pivot]
        right_paired = [paired_list[i] for i in range(len(arr)) if arr[i] > pivot]

        left_sorted, left_paired_sorted = quick_sort(left, left_paired)
        right_sorted, right_paired_sorted = quick_sort(right, right_paired)

        return left_sorted + middle + right_sorted, left_paired_sorted + middle_paired + right_paired_sorted

    bmi_heart_list = list(zip(bmi_data_grouped['BMI'], bmi_data_grouped['HeartDisease']))

    bmi_values = [item[0] for item in bmi_heart_list]
    heart_values = [item[1] for item in bmi_heart_list]

    start_time = time.time()
    sorted_bmi_values, sorted_heart_values = quick_sort(bmi_values, heart_values)
    end_time = time.time()
    elapsed_time = end_time - start_time

    sorted_bmi_data = pd.DataFrame({
        'BMI': sorted_bmi_values,
        'HeartDisease': sorted_heart_values
    })
    sorted_bmi_data['Index'] = range(1, len(sorted_bmi_data) + 1)

    soft_colors = ['#6BAF92' if value == 0 else '#D36C6C' for value in sorted_bmi_data['HeartDisease']]

    filtered_data_40 = sorted_bmi_data[sorted_bmi_data['BMI'] <= 40]

    plt.figure(figsize=(12, 6))
    plt.bar(filtered_data_40['Index'], filtered_data_40['BMI'], color=soft_colors[:len(filtered_data_40)], width=1.0, alpha=1.0)
    plt.text(
        x=len(filtered_data_40) * 0.7, y=35,
        s=f"Quick Sort: {elapsed_time:.6f} seconds",
        fontsize=12, bbox=dict(facecolor='white', alpha=0.7, edgecolor='black')
    )
    plt.title("BMI Levels with Heart Disease Status (Quick Sort, Up to BMI 40)", fontsize=16)
    plt.xlabel("Sorted Index by BMI", fontsize=14)
    plt.ylabel("BMI Levels", fontsize=14)
    plt.xticks([])
    plt.yticks(fontsize=12)
    plt.tight_layout()
    output_path = 'static/images/quick_sort_chart.png'
    try:
        plt.savefig(output_path)
        print("Plot saved successfully.")
    except Exception as e:
        print(f"Error saving plot: {e}")
