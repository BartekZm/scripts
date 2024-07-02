#pip install pandas json
import pandas
import json

# make sure file format is JSON, eg: 
# [[{ "from": 1, "to": 2, "x": 216, "y": 776 },
# { "from": 1, "to": 2, "x": 304, "y": 666 },
# { "from": 2, "to": 12, "x": 440, "y": 821 }]

# define file paths here
json1 = '<JSON_WITH_ROADS>'
output = '<OUTPUT>'

# find unique crossroad values
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', None)

with open(json1, encoding='utf-8') as file:
    data = json.loads(file.read())
    df = pandas.json_normalize(data)
    df_exploded = df.explode("crossroads")
    df_exploded[df_exploded.duplicated("crossroads")]

with open(output, 'w') as f:
    f.write(str(df_exploded.crossroads.unique()))

    

