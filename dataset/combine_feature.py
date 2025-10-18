import pandas as pd

train = pd.read_csv(r"C:\Users\apiwi\OneDrive\Documents\GitHub\CAICAMP_ALL_Recommend\dataset\features_all_train.csv")
valid = pd.read_csv(r"C:\Users\apiwi\OneDrive\Documents\GitHub\CAICAMP_ALL_Recommend\dataset\features_all_valid.csv")

combined = pd.concat([train, valid], axis=0, ignore_index=True)

combined.to_csv("features_all_combined.csv", index=False)
print("Combined dataset saved to features_all_combined.csv")
print("Shape:", combined.shape)