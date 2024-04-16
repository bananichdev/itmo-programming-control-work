# Programming ITMO project
## How to start?
1. Clone repo:
```
git clone https://github.com/bananichdev/itmo-programming-control-work.git 
```
2. Create venv:
```
python -m venv .venv
```
3. Activate venv:
```
source .venv/bin/activate
```
4. Install requirements:
```
pip install -r requirements.txt
```
5. Run main.py:
```
python main.py
```
NOTE: you should create .env file and add DB_USER, DB_PASS, DB_URL, DB_NAME variables for PostgreSQL connection, and do migration:
```
alembic upgrade 7157451c637d
```