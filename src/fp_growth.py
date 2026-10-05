import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth


def run_fpgrowth(transactions):

    te = TransactionEncoder()

    te_array = te.fit(transactions).transform(
        transactions
    )

    basket = pd.DataFrame(
        te_array,
        columns=te.columns_
    )

    frequent_items = fpgrowth(
        basket,
        min_support=0.02,
        use_colnames=True
    )

    # Convert frozenset -> readable text
    frequent_items["itemsets"] = frequent_items[
        "itemsets"
    ].apply(
        lambda x: ", ".join(sorted(list(x)))
    )

    frequent_items = frequent_items.sort_values(
        by="support",
        ascending=False
    )

    return frequent_items