import requests
from datetime import datetime, timedelta, timezone

no_commit = True
commit_7_old = False
page = 0
now = datetime.now(timezone.utc)
delta = timedelta(days=7)

while True:
    params = {'per_page': 100, 'page': page}
    try:
        response = requests.get('https://api.github.com/repos/python/cpython/commits', timeout=500, params=params)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к Github API: {e}")
        break
    
    if response.status_code == 200:
        data = response.json()
 
        for i in data:
            d = datetime.strptime(i['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            if (now - delta) < d:
                no_commit = False 
                print(f"Author : {i['commit']['author'].get('name', 'Unknowm'): ^20} \\ Date: {d} \\ Message: {i['commit']['message']}")
            else:
                commit_7_old = True
                break
                
    if commit_7_old:
        break
    
    page += 1
    
if no_commit:
    print('Нет коммитов за последние 7 дней')
