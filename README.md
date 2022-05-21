![PyPI](https://img.shields.io/pypi/v/get-response)
![CI status](https://github.com/skv0zsneg/get-response/actions/workflows/get-response-tox.yml/badge.svg)
[![codebeat badge](https://codebeat.co/badges/6c135ed9-2c57-4ba3-980b-1bb9c9a2c83b)](https://codebeat.co/projects/github-com-skvozsneg-get-response-main)
# get-response
 Parsing Tool for json-like, xml-like and etc Types of Response for Humans.
 
## Quick Start
**Install**

```pip install get-response```

**Use**
```
import get_response
import requests


response = requests.get("https://your-awesome-api.com/users")
parser = get_response.get_json(response.text)

parser.get_objects('name')
# ('Alex', 'Sam', 'Jane', ... )
```

## Requirements 
- Python >=3.8

If you whant to do a pull request make sure that to using `mypy`,  `pytets` and `tox`. All versions described in `requirements_dev.txt`.

## Summary
This Python package is made for easy parsing data from messages that comes from API's. For example you have a REST API and you need to get all data from value 'id'. All you need to get raw json message and put it in `get_response.get_json()` and than call a `.get_objects('id')` method. Algorithm will go through json and return every value that corresponds to 'id' key.

It can be used for tests or scrapping tasks.

### Message types

Package supports next types of message:
- json
- soap

That package sets next methods for every type of messages:

| Method | Message Types | Description |
| --- | --- | --- |
| `get_objects(key)` | `json`, `soap` | Return every found value in the message that corresponds to key. | 

## Versions
- v 0.1.0
	- New structure of the project.
	- Change goals and prospects of project.

- v 0.0.2
	- First version of the project.
