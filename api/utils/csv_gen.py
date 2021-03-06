import requests, pandas, json
from io import StringIO
from utils.nation import get_nation, get_code

def set_url(country, interval):
    code = get_code(country)
    return f'http://spotifycharts.com/regional/{code}/weekly/{interval}/download'

def generate_csv(dates, country):
    df_list = []

    for date in dates:
        chart = requests.get(set_url(country, date))
        df = pandas.read_csv(StringIO(chart.content.decode()), header=1)
        df.drop(labels=['Position', 'Streams'], axis=1, inplace=True)
        df_list.append(df)
    
    final_list = pandas.concat(df_list, ignore_index=True)
    final_list.drop_duplicates(keep='first', inplace=True)
    filtered_csv = filter_csv(final_list, country)
    return filtered_csv

def filter_csv(biglist, country):
    for index, row in biglist.iterrows():
        biglist.at[index, 'URL'] = biglist.at[index, 'URL'][31:]
        if country not in get_nation(row['Artist']):
            biglist.drop(labels=index, inplace=True)
    return biglist
