# ============================================================
# Smart Grocery 100K Transaction Dataset Generator
# Project: Smart Recommendation Engine for Grocery Shopping
# Output: Smart_Grocery_100K_Transactions.xlsx
# Format:
# TransactionID | Item1 | Item2 | Item3 | Item4 | Item5 | Item6
# ============================================================

import random
import pandas as pd

# ---------------------------
# Configuration
# ---------------------------
NUM_TRANSACTIONS = 100000
OUTPUT_FILE = "Smart_Grocery_100K_Transactions.xlsx"

# ---------------------------
# Product List (50 Products)
# ---------------------------
products = [
    "Milk", "Curd", "Butter", "Cheese", "Yogurt",
    "Bread", "Bun", "Cake", "Biscuit", "Rusk",
    "Rice", "Atta", "Sugar", "Salt", "Tea",
    "Coffee", "Dal", "Oil", "Ghee", "Poha",
    "Potato", "Onion", "Tomato", "Carrot", "Cabbage",
    "Cauliflower", "Spinach", "Beans", "Peas", "Brinjal",
    "Apple", "Banana", "Orange", "Mango", "Grapes",
    "Pineapple", "Papaya", "Watermelon", "Guava", "Pomegranate",
    "Soap", "Shampoo", "Toothpaste", "Detergent", "Toothbrush",
    "Floor Cleaner", "Dishwash Liquid", "Chips", "Chocolate", "Juice"
]

# ---------------------------
# Frequently Purchased Groups
# (to improve recommendations)
# ---------------------------
frequent_combinations = [
    ["Milk", "Bread", "Butter"],
    ["Tea", "Sugar", "Milk"],
    ["Rice", "Dal", "Oil"],
    ["Atta", "Salt", "Oil"],
    ["Curd", "Potato", "Onion"],
    ["Apple", "Banana", "Orange"],
    ["Soap", "Shampoo", "Toothpaste"],
    ["Cake", "Biscuit", "Juice"],
    ["Chips", "Chocolate", "Juice"],
    ["Rice", "Ghee", "Dal"],
    ["Milk", "Curd", "Yogurt"],
    ["Tomato", "Potato", "Onion"],
]

# ---------------------------
# Generate Transactions
# ---------------------------
transactions = []

for i in range(1, NUM_TRANSACTIONS + 1):

    # 70% chance to start with a frequent combo
    if random.random() < 0.70:
        items = random.choice(frequent_combinations).copy()
    else:
        items = []

    # Total items in transaction (1–6)
    target_count = random.randint(1, 6)

    while len(items) < target_count:
        item = random.choice(products)
        if item not in items:
            items.append(item)

    random.shuffle(items)

    row = {
        "TransactionID": f"T{i:06d}",
        "Item1": items[0] if len(items) > 0 else None,
        "Item2": items[1] if len(items) > 1 else None,
        "Item3": items[2] if len(items) > 2 else None,
        "Item4": items[3] if len(items) > 3 else None,
        "Item5": items[4] if len(items) > 4 else None,
        "Item6": items[5] if len(items) > 5 else None,
    }

    transactions.append(row)

# ---------------------------
# Create DataFrame
# ---------------------------
df = pd.DataFrame(transactions)

# ---------------------------
# Save to Excel
# ---------------------------
df.to_excel(OUTPUT_FILE, index=False)

# ---------------------------
# Summary
# ---------------------------
print("=" * 50)
print("Dataset Generated Successfully!")
print(f"Transactions : {len(df):,}")
print(f"Products      : {len(products)}")
print(f"Output File   : {OUTPUT_FILE}")
print("=" * 50)

print("\nSample Data:")
print(df.head())