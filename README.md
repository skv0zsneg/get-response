![PyPI](https://img.shields.io/pypi/v/get-response)
![example workflow](https://github.com/skvozsneg/get-response/actions/workflows/get-response-tox.yml/badge.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/skvozsneg/get-response/badge)](https://www.codefactor.io/repository/github/skvozsneg/get-response)
[![codebeat badge](https://codebeat.co/badges/6c135ed9-2c57-4ba3-980b-1bb9c9a2c83b)](https://codebeat.co/projects/github-com-skvozsneg-get-response-main)
# api-response
Api response tool for easy parsing REST and SOAP responses.

___
### Quick start
```python
import requests
from get_response import get_response

response = requests.get('https://your-api.com')
gr = get_response(response, 
                  'REST', 
                  {'my_name': ['person', 'name']})

gr['my_name']  # Contains value from JSON (...{'person': {'name': 'NAME'}}...)
```
