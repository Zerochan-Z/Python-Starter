import pandas as pd

df = pd.read_csv(r"Revision\Day 006 (Exception Handling)\students.csv")

print("--- First 5 lines ---")
print(df.head(5))

print("\n=== 列名 ===\n")
print(df.columns)

print("\n=== Mean Score ===\n")
print(df['Score'].mean())

print("\n=== Score > 80 lines ===\n")
print(df[df['Score'] > 80])