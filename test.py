
import pandas as pd
import fuzzy_pandas as fpd

df1 = pd.read_csv("masterFile.csv")
df2 = pd.read_csv("exampleFile.csv")
print(df2)

matches = fpd.fuzzy_merge(df2, df1,
                          left_on=['Player Name'],
                          right_on=['Name'],
                          ignore_case=True,
                          keep='match',
                          method='levenshtein',
                          threshold=0.6)

print(matches)