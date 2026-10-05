import pandas as pd

from apriori_model import run_apriori
from fp_growth import run_fpgrowth
from eclat import run_eclat
from recommendation import get_recommendations

# ==================================================
# PANDAS SETTINGS
# ==================================================

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_excel(
    "dataset/Smart_Grocery_100K_Transactions.xlsx"
)

print("===== ORIGINAL DATASET =====")
print(df.head())

# ==================================================
# MISSING VALUES
# ==================================================

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# ==================================================
# DUPLICATES
# ==================================================

print("\n===== DUPLICATE ROWS =====")
print("Duplicates:", df.duplicated().sum())

df = df.drop_duplicates()

print("\n===== DATASET SHAPE AFTER CLEANING =====")
print(df.shape)

# ==================================================
# TRANSACTION LIST
# ==================================================

transactions = []

for _, row in df.iterrows():

    items = []

    for col in df.columns[1:]:

        if pd.notna(row[col]):
            items.append(str(row[col]))

    transactions.append(items)

print("\n===== FIRST 5 TRANSACTIONS =====")
print(transactions[:5])

# ==================================================
# APRIORI
# ==================================================

print("\n===== APRIORI RESULTS =====")

apriori_result, rules = run_apriori(
    transactions
)

print(apriori_result)

print(
    "\nTotal Apriori Itemsets:",
    len(apriori_result)
)

apriori_result.to_csv(
    "results/apriori_results.csv",
    index=False
)

print(
    "Apriori Results Saved Successfully!"
)

# ==================================================
# ASSOCIATION RULES
# ==================================================

if not rules.empty:

    print("\n===== ASSOCIATION RULES =====")

    print(
        rules[
            [
                "antecedents",
                "consequents",
                "support",
                "confidence",
                "lift"
            ]
        ]
    )

    rules.to_csv(
        "results/association_rules.csv",
        index=False
    )

    print(
        "\nAssociation Rules Saved Successfully!"
    )

    print(
        "Total Rules:",
        len(rules)
    )

else:

    print(
        "\nNo Association Rules Found"
    )

# ==================================================
# FP-GROWTH
# ==================================================

print("\n===== FP-GROWTH RESULTS =====")

fp_result = run_fpgrowth(
    transactions
)

print(fp_result)

print(
    "\nTotal FP-Growth Itemsets:",
    len(fp_result)
)

fp_result.to_csv(
    "results/fp_growth_results.csv",
    index=False
)

print(
    "FP-Growth Results Saved Successfully!"
)

# ==================================================
# ECLAT
# ==================================================

print("\n===== ECLAT RESULTS =====")

eclat_result = run_eclat(
    transactions
)

print(eclat_result)

print(
    "\nTotal ECLAT Items:",
    len(eclat_result)
)

eclat_df = pd.DataFrame(
    list(eclat_result.items()),
    columns=[
        "Item",
        "Frequency"
    ]
)

eclat_df.to_csv(
    "results/eclat_results.csv",
    index=False
)

print(
    "ECLAT Results Saved Successfully!"
)

# ==================================================
# ALL FILES SAVED
# ==================================================

print(
    "\n===== ALL RESULTS SAVED IN RESULTS FOLDER ====="
)

# ==================================================
# RECOMMENDATION ENGINE
# ==================================================

print(
    "\n===== SMART RECOMMENDATION ENGINE ====="
)

product = input(
    "\nEnter Product Name: "
)

results = get_recommendations(product)

if results:

    print(
        "\nRecommended Products:\n"
    )

    for item, confidence, lift in results[:10]:

        print(
            f"- {item} | Confidence: {confidence:.2%} | Lift: {lift:.2f}"
        )

else:

    print(
        "\nNo recommendations found"
    )