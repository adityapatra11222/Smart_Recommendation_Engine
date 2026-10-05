import pandas as pd


def get_recommendations(product_name):

    try:

        df = pd.read_csv(
            "results/association_rules.csv"
        )

    except:

        return []

    recommendations = []

    product_name = product_name.strip().lower()

    for _, row in df.iterrows():

        antecedent = str(
            row["antecedents"]
        ).strip().lower()

        consequent = str(
            row["consequents"]
        ).strip()

        confidence = float(
            row["confidence"]
        )

        lift = float(
            row["lift"]
        )

        if antecedent == product_name:

            recommendations.append(
                (
                    consequent,
                    confidence,
                    lift
                )
            )

    recommendations = sorted(
        recommendations,
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations


if __name__ == "__main__":

    print(
        "===== SMART RECOMMENDATION ENGINE ====="
    )

    product = input(
        "\nEnter Product Name: "
    )

    results = get_recommendations(
        product
    )

    if results:

        print(
            "\nRecommended Products:\n"
        )

        for item, confidence, lift in results[:10]:

            print(
                f"{item} | Confidence: {confidence:.2%} | Lift: {lift:.2f}"
            )

    else:

        print(
            "\nNo recommendations found"
        )