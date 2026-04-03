import pandas as pd

# بيانات تجريبية فوضوية
data = {
    "name": ["Alice", None, "Charlie", "Diana", "Alice", "eve"],
    "age": [25, 30, None, 28, 25, 35],
    "email": ["alice@email.com", "bob@email.com", "charlie@email.com", None, "alice@email.com", "EVE@EMAIL.COM"],
    "salary": [50000, 60000, None, 75000, 50000, 80000]
}

df = pd.DataFrame(data)

print("قبل التنظيف:")
print(df)

# 1. حذف الصفوف المكررة
df = df.drop_duplicates()

# 2. تعبئة الخلايا الفارغة
df["name"] = df["name"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].median())

# 3. توحيد الأسماء إلى حروف كبيرة
df["name"] = df["name"].str.title()
df["email"] = df["email"].str.lower()

# 4. حفظ الملف النظيف
df.to_csv("cleaned_output.csv", index=False)

print("\nبعد التنظيف:")
print(df)
print("\nتم حفظ الملف النظيف في cleaned_output.csv")