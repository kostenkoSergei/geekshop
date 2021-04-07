###Geekshop
###django-basic course

###django optimization instruments course (continue with Django==2.2.17) (media folder and database are in .gitignore)

lesson 1:
sending email and context processors

lesson8:
authapp/management/report.py command is for creation report about
sold products depending on the discount

to solve dumpdata problems with pk and id during loading from fixtures use:
python manage.py dumpdata --natural-foreign -e=contenttypes -e=auth -o test_db.json
