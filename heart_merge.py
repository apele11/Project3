import pandas as pd
import matplotlib.pyplot as plt
import time

file_path = 'static/heart_2020_cleaned.csv'
data = pd.read_csv(file_path)

bmi_data = data[['BMI', 'HeartDisease']]
bmi_data['HeartDisease'] = bmi_data['HeartDisease'].apply(lambda x: 1 if x == 'Yes' else 0)

bmi_data_grouped = bmi_data.groupby('BMI')['HeartDisease'].mean().reset_index()
bmi_data_grouped['BMI'] = bmi_data_grouped['BMI'].astype(float)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] < right_half[j][0]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    bmi_heart_list = list(zip(bmi_data_grouped['BMI'], bmi_data_grouped['HeartDisease']))

    start_time = time.time()

    merge_sort(bmi_heart_list)

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
        s=f"Merge Sort: {elapsed_time:.6f} seconds",
        fontsize=12, bbox=dict(facecolor='white', alpha=0.7, edgecolor='black')
    )

    plt.title("BMI Levels with Heart Disease Status (Up to BMI 40)", fontsize=16)
    plt.xlabel("Sorted Index by BMI", fontsize=14)
    plt.ylabel("BMI Levels", fontsize=14)
    plt.xticks([])
    plt.yticks(fontsize=12)
    plt.tight_layout()
    
    output_path = 'static/images/merge_sort_chart.png'
    try:
        plt.savefig(output_path)
        print("Plot saved successfully.")
    except Exception as e:
        print(f"Error saving plot: {e}")