import pandas as pd
import numpy as np

# =====================================
# 1. CREATE DATAFRAME
# =====================================
data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 21, 22, 23],
    "Marks": [85, 90, 95, 80]
}

df = pd.DataFrame(data)

print("===== ORIGINAL DATA =====")
print(df)


# =====================================
# 2. PRINT / VIEW DATA
# =====================================
print("\n===== BASIC INFO =====")
print("Head:\n", df.head())
print("Tail:\n", df.tail())
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Data Types:\n", df.dtypes)


# =====================================
# 3. ACCESS DATA
# =====================================
print("\n===== ACCESS DATA =====")
print("Column:\n", df["Name"])
print("Row (iloc):\n", df.iloc[1])
print("Value (loc):", df.loc[1, "Age"])


# =====================================
# 4. ADD / UPDATE
# =====================================
df["Grade"] = ["B", "A", "A", "C"]   # add column
df.loc[0, "Age"] = 25               # update value

print("\n===== AFTER ADD/UPDATE =====")
print(df)


# =====================================
# 5. DELETE OPERATIONS
# =====================================
df_drop_col = df.drop("Grade", axis=1)   # delete column
df_drop_row = df.drop(0, axis=0)         # delete row

print("\n===== AFTER DELETE COLUMN =====")
print(df_drop_col)

print("\n===== AFTER DELETE ROW =====")
print(df_drop_row)


# =====================================
# 6. FILTER DATA
# =====================================
filtered = df[df["Marks"] > 85]

print("\n===== FILTERED (Marks > 85) =====")
print(filtered)


# =====================================
# 7. SORTING
# =====================================
sorted_df = df.sort_values(by="Marks")

print("\n===== SORTED BY MARKS =====")
print(sorted_df)


# =====================================
# 8. AGGREGATE FUNCTIONS
# =====================================
print("\n===== AGGREGATE =====")
print("Mean:", df["Marks"].mean())
print("Max:", df["Marks"].max())
print("Min:", df["Marks"].min())
print("Sum:", df["Marks"].sum())


# =====================================
# 9. GROUPBY
# =====================================
group = df.groupby("Grade")["Marks"].mean()

print("\n===== GROUPBY =====")
print(group)


# =====================================
# 10. MISSING VALUES
# =====================================
df.loc[2, "Marks"] = np.nan

print("\n===== WITH MISSING VALUES =====")
print(df)

print("\nIs Null:\n", df.isnull())

df.fillna(0, inplace=True)

print("\n===== AFTER FILL NA =====")
print(df)


# =====================================
# 11. APPLY FUNCTION
# =====================================
df["Marks_Squared"] = df["Marks"].apply(lambda x: x**2)

print("\n===== APPLY FUNCTION =====")
print(df)


# =====================================
# 12. MERGE
# =====================================
data2 = {
    "Name": ["A", "B", "C", "D"],
    "City": ["Hyd", "Vizag", "Delhi", "Mumbai"]
}

df2 = pd.DataFrame(data2)

merged = pd.merge(df, df2, on="Name")

print("\n===== MERGED DATA =====")
print(merged)


# =====================================
# 13. CONCAT
# =====================================
concat_df = pd.concat([df, df])

print("\n===== CONCAT DATA =====")
print(concat_df)


# =====================================
# 14. UNIQUE & VALUE COUNTS
# =====================================
print("\n===== UNIQUE =====")
print(df["Name"].unique())

print("\n===== VALUE COUNTS =====")
print(df["Name"].value_counts())


# =====================================
# END
# =====================================
