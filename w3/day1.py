import requests
r = requests.get('https://api.github.com/users/xinghe-602')
print(r.status_code)
data = r.json()
print(data['bio'], data['name'], data['following'])
print(data['public_repos'],data['followers'])

r = requests.get('https://api.github.com/users/xinghe-603')
print(r.status_code)
