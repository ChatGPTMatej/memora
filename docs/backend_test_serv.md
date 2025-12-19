backend/memora/settings.py
SECRET_KEY se nachází v repository secret, snad tam není žádný další klíč, moc nevím upřímně.

# zapnutí production serveru MAC
```
cd ./backend/
source ./venv/bin/activate
python3 ./manage.py runserver
```

# zapnutí production serveru Windows
```
cd .\backend\
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python .\manage.py runserver
```
