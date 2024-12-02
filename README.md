# **CardioRisk Project**

CardioRisk is a web-based application designed to visualize and analyze the relationship between BMI levels and heart disease risk using various sorting algorithms. Users can dynamically generate and view bar charts for data sorted by **Heap Sort**, **Quick Sort**, **Merge Sort**, or **Bubble Sort**.
![image](https://github.com/user-attachments/assets/fbc814d8-aff5-444d-9524-0a4cdb146050)

## **Features**
- **Dynamic Sorting**: Visualize heart disease risk based on BMI levels sorted using different algorithms.
- **Interactive Interface**: Select a sorting algorithm and generate a graph directly on the website.
- **Responsive Charts**: Data visualization powered by Matplotlib, dynamically rendered and displayed.

---
## **Installation**

Follow these steps to set up the project locally:

### **Prerequisites**
- Python 3.8 or higher installed.
- Git installed.

### **Clone the Repository**
```bash
git clone https://github.com/<your-username>/Project3.git
cd Project3
```

### **Install Dependencies**
Use `pip` to install the required dependencies:
```bash
pip install -r requirements.txt
```

---

## **Running the Project Locally**

1. Run the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Use the dropdown menu to select a sorting algorithm and click **Play** to generate and display the corresponding graph.

---

## **Project Structure**

```
Project3/
│
├── static/
│   ├── css/
│   │   └── main.css               # Styling for the application
│   ├── images/
│   │   ├── heap_sort_chart.png    # Generated chart for Heap Sort
│   │   ├── quick_sort_chart.png   # Generated chart for Quick Sort
│   │   ├── merge_sort_chart.png   # Generated chart for Merge Sort
│   │   └── bubble_sort_chart.png  # Generated chart for Bubble Sort
│   └── heart_2020_cleaned.csv     # Dataset used for BMI and heart disease analysis
│
├── templates/
│   ├── base.html                  # Base HTML template
│   └── index.html                 # Main page for the application
│
├── app.py                         # Main Flask app to run the server
├── heart_heap.py                  # Heap Sort implementation
├── heart_quick.py                 # Quick Sort implementation
├── heart_merge.py                 # Merge Sort implementation
├── heart_bubble.py                # Bubble Sort implementation
├── requirements.txt               # Python dependencies
├── Procfile                       # Render deployment configuration
└── README.md                      # Project documentation
```

---

## **How It Works**

1. **Frontend**:
   - Built with HTML and CSS, providing a user interface to select sorting algorithms.
   - Uses JavaScript to dynamically update and load charts.

2. **Backend**:
   - Flask handles the server-side logic and routing.
   - Sorting algorithms are implemented in separate Python files (`heart_heap.py`, `heart_quick.py`, etc.).
   - Matplotlib generates and saves bar charts for each sorting algorithm.

3. **Visualization**:
   - The bar charts display BMI levels (up to 40) on the Y-axis.
   - Colors represent heart disease status: green for no heart disease, red for heart disease.

---

## **License**

This project is open-source and available under the MIT License.
