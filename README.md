# Customer Segmentation

A small educational AI project that groups customers into segments using K-Means clustering based on annual spending and visit frequency.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python customer_segmentation.py --spend 1200 --visits 18
```

## Test

```bash
python -m unittest test_customer_segmentation.py
```

The dataset is synthetic and intentionally small so the project remains self-contained and easy to understand.
