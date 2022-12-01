# 💎 CerebroHelper
[![Supported python versions](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/downloads/)
[![Supported django versions](https://img.shields.io/badge/django%20version-4.1-green)](https://pypi.org/project/Django/)
[![Coverage status](https://img.shields.io/badge/coverage-0%25-red)](https://coverage.readthedocs.io/en/6.5.0/)

This application helps to create mappings for indexes in ElasticSearch, as well as a configuration for a data source that will later become an index.

## Installing Linux (Ubuntu)
```bash
git clone https://github.com/ElveeBolt/CerebroHelper.git
cd CerebroHelper
python3 -m venv venv
source venv\bin\activate
pip install -r requirements.txt
```

## Run server
```bash
cd CerebroHelper
python manage.py runserver
```

After starting, you can go to [127.0.0.1:8000](http://127.0.0.1:8000/) and use this app

## Author
Developed and maintained by [ElveeBolt](https://github.com/ElveeBolt).

Thanks to everybody that has contributed pull requests, ideas, issues, comments and kind words.