import argparse

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

CUSTOMERS = np.array([
    [120, 3], [180, 4], [250, 5], [900, 15], [1100, 18], [1300, 20],
    [3000, 35], [3400, 40], [3800, 45], [150, 2], [1000, 16], [3200, 38],
], dtype=float)


def build_model() -> tuple[StandardScaler, KMeans]:
    scaler = StandardScaler()
    scaled = scaler.fit_transform(CUSTOMERS)
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    model.fit(scaled)
    return scaler, model


def assign_segment(spend: float, visits: int) -> int:
    if spend <= 0 or visits <= 0:
        raise ValueError("Spend and visits must be positive")
    scaler, model = build_model()
    label = int(model.predict(scaler.transform([[spend, visits]]))[0])
    return label


def main() -> None:
    parser = argparse.ArgumentParser(description="Assign a customer to a spending segment.")
    parser.add_argument("--spend", type=float, required=True, help="Annual spend")
    parser.add_argument("--visits", type=int, required=True, help="Annual visits")
    args = parser.parse_args()
    print(f"Assigned segment: {assign_segment(args.spend, args.visits)}")


if __name__ == "__main__":
    main()
