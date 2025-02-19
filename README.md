# Django bug

This is a basic repo to demonstrate how broken @override_settings is in the latest version of Django. It causes cross-test contamination.

Running locally:


```
git clone https://github.com/Pachwenko/django_bug_repo_override_settings.git
pip install django==4.2.19
python manage.py test
```
