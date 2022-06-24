import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')

"""
# Saving PNG File
with open('comic.png', 'wb') as f: # wb = write byte
    f.write(r.content)

# Getting Status Code
print(r.status_code)


# Get explanation of methods
print(help(r))

# Get headers
print(r.headers)

# Get information
print(r.text)
"""

# TESTING REQUESTS in GET
payload = {'page': 2, 'count': 25} # URL Parameters
request = requests.get('https://httpbin.org/get', params=payload)

print(request.text)
print(request.url)

# TESTING REQUESTS in POST
params_list = {'username': 'corey', 'password': 'testing'}

r = requests.post('https://httpbin.org/post', data=params_list)

r_dict = r.json() # Get information in json format
print(r_dict['form'])










