import pandas as pd
import numpy as np
import os

# Define 7 spiritual gifts
gifts = [
    "Teaching", "Prophecy", "Evangelism",
    "Service", "Giving", "Leadership", "Mercy"
]

# Generate synthetic data
num_samples = 200
num_questions = 30

data = []
np.random.seed(42)

for _ in range(num_samples):
    # Simulate answers: random 1-5 Likert scale
    answers = np.random.randint(1, 6, size=num_questions)

    # Randomly assign a dominant gift
    gift = np.random.choice(gifts)

    row = list(answers) + [gift]
    data.append(row)

# Create DataFrame
columns = [f"Q{i+1}" for i in range(num_questions)] + ["DominantGift"]
df = pd.DataFrame(data, columns=columns)

# Save
os.makedirs("data", exist_ok=True)
df.to_csv("data/gifts_training_data.csv", index=False)
print("✅ Dataset saved at data/gifts_training_data.csv")
print(df.head())
