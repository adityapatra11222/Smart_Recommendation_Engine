import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


def run_apriori(transactions):

    # ==========================================
    # Transaction Encoding
    # ==========================================

    te = TransactionEncoder()

    te_array = te.fit(transactions).transform(
        transactions
    )

    basket = pd.DataFrame(
        te_array,
        columns=te.columns_
    )

    # ==========================================
    # Frequent Itemsets
    # ==========================================

    frequent_items = apriori(
        basket,
        min_support=0.02,
        use_colnames=True
    )

    # ==========================================
    # Association Rules
    # ==========================================

    rules = association_rules(
        frequent_items,
        metric="confidence",
        min_threshold=0.20
    )

    # ==========================================
    # Create Apriori Output
    # support + confidence + itemset
    # ==========================================

    apriori_output = []

    for _, rule in rules.iterrows():

        itemset = (
            set(rule["antecedents"])
            |
            set(rule["consequents"])
        )

        apriori_output.append(
            {
                "itemset": ", ".join(
                    sorted(itemset)
                ),
                "support": round(
                    rule["support"],
                    5
                ),
                "confidence": round(
                    rule["confidence"],
                    5
                )
            }
        )

    apriori_df = pd.DataFrame(
        apriori_output
    )

    apriori_df = apriori_df.sort_values(
        by="confidence",
        ascending=False
    )

    # ==========================================
    # Clean Association Rules
    # ==========================================

    rules["antecedents"] = rules[
        "antecedents"
    ].apply(
        lambda x: ", ".join(sorted(list(x)))
    )

    rules["consequents"] = rules[
        "consequents"
    ].apply(
        lambda x: ", ".join(sorted(list(x)))
    )

    rules = rules[
        [
            "antecedents",
            "consequents",
            "support",
            "confidence",
            "lift"
        ]
    ]

    rules = rules.sort_values(
        by="confidence",
        ascending=False
    )

    return apriori_df, rules