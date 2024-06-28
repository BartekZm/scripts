#pip install pandas json re

import pandas
import json
import re

# make sure file format is JSON, eg: 
# [[{ "from": 1, "to": 2, "x": 216, "y": 776 },
# { "from": 1, "to": 2, "x": 304, "y": 666 },
# { "from": 2, "to": 12, "x": 440, "y": 821 }]

# define file paths here
json1 = '<PATH_TO_JSON>'
csv1 = '<PATH_TO_CSV_TO_BE_MERGED>'
csv2 = '<CONVERTED_JSON_TO_CSV_PATH>'
output = '<COMBINED_CSVs>'
raw_json = '<RAW_JSON_PATH>'
final_json = '<FINAL_JSON_PATH>'

# convert JSON to CSV
with open(json1, encoding='utf-8') as file:
    data = json.loads(file.read())
    df = pandas.json_normalize(data)
    df.to_csv(csv1, index=False, encoding='utf-8')

# merge CSVs and sort by y
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', None)

df1 = pandas.read_csv(csv1)
df2 = pandas.read_csv(csv2)

df3 = pandas.merge(df1, df2, how='outer', on=['from','to'])
df4 = df3.sort_values(by='y', ascending=True)

# convert merged JSON to CSV
with open(output, 'w') as f:
    f.write(str(df4.to_json(raw_json, indent=0, orient='records', lines=True)))

# correct last true/false value malformat and make final JSON human readable
repldict = {'"true "':'true ' , '"false "':'false ' , '}' : '},' , ':' : ' : ', ',' : ' , ', '{"' : '{ "'}
def replfunc(match):
    return repldict[match.group(0)]

regex = re.compile('|'.join(re.escape(x) for x in repldict))
with open(raw_json) as fin, open(final_json,'w') as fout:
    for line in fin:
        fout.write(regex.sub(replfunc,line))
