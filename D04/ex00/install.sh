export PROJECT_HOME=/Users/yde-mont/Desktop/ECLIPSE/workspace/PYTHON/42Python/D04/projectD04
export ENV_HOME=~/Desktop/VIRTUAL_ENV
mkdir -p $PROJECT_HOME $ENV_HOME
python3 -m venv $ENV_HOME
cd $ENV_HOME
source ./bin/activate
pip install django
cd $PROJECT_HOME
django-admin.py startproject d04
python manage.py migrate
export PYTHONPATH=${ENV_HOME}/lib/python3.8/site-packages
python3.8 manage.py runserver

		CTRL-C

python manage.py startapp ex00

# Connaitre les pre-requis
pip freeze

#Creer un template
dan ex00/


python3 -m venv $ENV_HOME
cd $ENV_HOME
source ./bin/activate
cd $PROJECT_HOME
python3.8 manage.py runserver