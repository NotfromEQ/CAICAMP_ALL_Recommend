import pandas as pd

# โหลดไฟล์ CSV
df = pd.read_csv(r"C:\Users\apiwi\OneDrive\Documents\GitHub\CAICAMP_ALL_Recommend\dataset\features_all_combined.csv")

df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

df_shuffled.to_csv("features_all_combined_shuffled.csv", index=False)

print("ไฟล์ถูกสลับแถวและบันทึกเรียบร้อยแล้ว!")
print("แถวทั้งหมด:", len(df_shuffled))