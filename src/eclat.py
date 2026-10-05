from collections import defaultdict


def run_eclat(transactions, min_support=0.02):

    total_transactions = len(transactions)

    item_tidset = defaultdict(set)

    for tid, transaction in enumerate(transactions):

        for item in transaction:

            item_tidset[item].add(tid)

    min_count = int(min_support * total_transactions)

    frequent_items = {}

    for item, tids in item_tidset.items():

        if len(tids) >= min_count:

            frequent_items[item] = len(tids)

    frequent_items = dict(
        sorted(
            frequent_items.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

    return frequent_items