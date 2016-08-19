# ArdynRoseWyatt
This is the code behind [ArdynRoseWyatt.com](ArdynRoseWyatt.com).

# Quickstart

_Requires: Python 3.3+_

1. Build a virtual environment. Once complete you'll want to use the ```.venv/bin/python``` interpreter.

    ```bash
    $ bash create-environment.sh
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
    $ .venv/bin/python manage.py migrate
    ```

3. Start the server

    ```bash
    $ .venv/bin/python manage.py runserver
    ```
