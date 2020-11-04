web: python oc_8_projet_nutella/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT oc_8_projet_nutella/settings.py 
