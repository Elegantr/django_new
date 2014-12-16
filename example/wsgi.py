    # +++++++++++ DJANGO +++++++++++
    import os
    import sys

    ## assuming your Django settings file is at '/home/my_username/projects/my_project/settings.py'
    path = '/home/my_username/projects'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'my_project.settings'

    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()
