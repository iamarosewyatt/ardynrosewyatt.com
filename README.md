# ArdynRoseWyatt
This is the code behind [ArdynRoseWyatt.com](ArdynRoseWyatt.com).

# Development Install

_Requires: Python 3.3+_

1. Build a virtual environment. Once complete you'll want to use the ```.venv/bin/python``` interpreter.

    ```bash
    $ bash create-python-environment.sh
    Collecting pip
      Using cached pip-8.1.2-py2.py3-none-any.whl
    Installing collected packages: pip
      Found existing installation: pip 7.1.2
        Uninstalling pip-7.1.2:
          Successfully uninstalled pip-7.1.2
    Successfully installed pip-8.1.2
    Collecting Django==1.10.0 (from -r requirements.txt (line 1))
      Using cached Django-1.10-py2.py3-none-any.whl
    Installing collected packages: Django
    Successfully installed Django-1.10
    ```

2. Setup the database

    ```bash
    $ bash populate-database.sh
    Operations to perform:
      Synchronize unmigrated apps: ckeditor, messages, staticfiles
      Apply all migrations: about, admin, auth, contenttypes, journal, sessions, sites, tagging, whats_coming
    Synchronizing apps without migrations:
      Creating tables...
        Running deferred SQL...
    Running migrations:
      Rendering model states... DONE
      Applying about.0001_initial... OK
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying journal.0001_initial... OK
      Applying sessions.0001_initial... OK
      Applying sites.0001_initial... OK
      Applying sites.0002_alter_domain_unique... OK
      Applying tagging.0001_initial... OK
      Applying tagging.0002_on_delete... OK
      Applying whats_coming.0001_initial... OK
    Installed 1 object(s) from 1 fixture(s)
    Installed 30 object(s) from 1 fixture(s)
    Installed 59 object(s) from 1 fixture(s)
    Creating a super user account (user: iamarosewyatt) ...
    Password:
    Password (again):
    Superuser created successfully.
    ```

4. Gather all of the assets into the static directory

    ```bash
    $ .venv/bin/python manage.py collectstatic

    You have requested to collect static files at the destination
    location as specified in your settings:

        /var/www/ArdynRoseWyatt/static

    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes
    ... snipped a bunch of copies for brevity ...

    1182 static files copied to '/var/www/ArdynRoseWyatt/static'.

    ```

5. Start the development server

    ```bash
    $ .venv/bin/python manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    October 13, 2016 - 17:42:53
    Django version 1.10, using settings 'settings'
    Starting development server at http://localhost:8080/
    Quit the server with CONTROL-C.
    ```

## Production Deployment

The intended platform is Ubuntu 16.04, Python 3.5, Apache 2.4 w/ WSGI, MySQL 5.7, and Django 1.10. See the three shell scripts at the root of the repository for more information.
