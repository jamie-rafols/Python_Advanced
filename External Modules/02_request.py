import requests 
r = requests.get('https://api.github.com/events')

print(r.text)

with open("tasks.txt", "w") as f:
    f.write(r.text)
    
    # Need to open this website https://requests.readthedocs.io/en/latest/