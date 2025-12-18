import json
import matplotlib.pyplot as plt

def show_pie_chart():
    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No data found. Please add expenses first.")
        return

    # Aggregate totals by category
    category_totals = {}
    for entry in data:
        cat = entry['category']
        amt = entry['amount']
        category_totals[cat] = category_totals.get(cat, 0) + amt

    # Prepare data for the chart
    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    # Create the chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Expenses by Category")
    plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
    
    print("Generating chart...")
    plt.show()

if __name__ == "__main__":
    show_pie_chart()
