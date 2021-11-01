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
