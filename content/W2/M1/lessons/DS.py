import pandas as pd

df_titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

# print(df_titanic["Age"].mean())

# print(df_titanic["Age"].describe())

# print(df_titanic[["Age", "Fare"]].median())

# print(df_titanic[["Age", "Fare"]].describe())

# print(df_titanic[["Age", "Fare"]].agg(
#     {
#         "Age": ["min", "max", "median", "skew"],
#         "Fare": ["min", "max", "median", "mean"],
#     }
# ))

# agg = df_titanic[["Sex", "Age"]].groupby("Sex").mean()
# print(agg)