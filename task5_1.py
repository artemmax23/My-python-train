import csv, json
from collections import defaultdict

def avarage_age_by_city(csv_filename: str) -> dict:
    grouped_data = defaultdict(list)
    
    with open(csv_filename, mode='r', encoding='utf-8', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            city = row['city']
            
            if city not in grouped_data:
                grouped_data[city] = {'sum': 0, 'count': 0}
                
            grouped_data[city]['sum'] += int(row['age'])
            grouped_data[city]['count'] += 1
            
    return {city : data['sum']/data['count'] for city, data in grouped_data.items()}
        
        #for row in csv_reader:
         #   grouped_data[row['city']].append(int(row['age']))
            
        #for key, value in grouped_data.items():
         #   grouped_data[key] = sum(value)/len(value)
            
    return dict(grouped_data)
    
def csv_to_json_without_id(csv_filename: str, json_filename: str):
    json_data = []
        
    with open(csv_filename, mode='r', encoding='utf-8', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)  
        for row in csv_reader:
            del row['id']
            json_data.append(row)
        
    with open(json_filename, mode='w', encoding='utf-8') as json_file:           
        json.dump(json_data, json_file, ensure_ascii=False)
        
print(avarage_age_by_city('users.csv'))
csv_to_json_without_id('users.csv', 'users.json')