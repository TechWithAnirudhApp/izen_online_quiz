cd backend
python -m pip install --upgrade pip
python -m pip install Django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate