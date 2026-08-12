import pandas as pd

def avarage_age_by_city(csv_filename: str) -> dict:
    return pd.read_csv(csv_filename, sep=',', encoding='utf-8').groupby('city')['age'].mean().to_dict()

def csv_to_json_without_id(csv_filename: str, json_filename: str):
    pd.read_csv(csv_filename, sep=',', encoding='utf-8').drop('id', axis=1, inplace=False).to_json(json_filename, orient='records', force_ascii=False)

print(avarage_age_by_city('users.csv'))
csv_to_json_without_id('users.csv', 'users.json')