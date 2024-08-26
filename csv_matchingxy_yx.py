import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', None)

#data format X,Y,Z
df = pandas.read_csv("<INPUT_FILE_PATH>")

for i, row in df.iterrows():
    match=df[(df['Y'] == row['Z']) & (df['Z'] == row['Y'])]

    if not match.empty:
        df.at[i,'A'] = str(match['X'].values[0]).rstrip(".0")

print(df)
