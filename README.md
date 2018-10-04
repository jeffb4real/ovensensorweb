# ovensensorweb

## Overview

This repository contains a Django tutorial project directory, 'mysite'. There is one web application in the project, named 'polls'. The Django tutorial was completed up to and including part 05:

https://docs.djangoproject.com/en/2.1/intro/tutorial01/

This repository is planned to be integrated into chrisxkeith's repository of the same name.

## Tools Dependencies and Installation Instructions

The following sections detail all steps required to run the polls app in this Django project, mysite.

### Install Python

Download and install Python for your platform:
https://www.python.org/downloads/

Python 3.7.0 was used for this the Django tutorial.

__Note:__ Depending on your system environment, and whether or not you've also installed Python 2.x, you may need to call Python 3 specifically, e.g. '$ python3 my-script.py'. Regardless, wherever 'python' appears below, we are intending to use Python 3.

### Set up your virtual environment

__Note:__ The pyvenv script has been deprecated as of Python 3.6 in favor of using 'python -m venv' to help prevent any potential confusion as to which Python interpreter a virtual environment will be based on.

Virtual environments are typically created on each user's PC and are not added to source control.

Issue this command to create our virtual environment _outside of_ any local repository directory (I recommend the parent directory of the repository directory - in our case, ~/mygithub), so that your new virtual environment won't be added to source control. We'll call our virtual environment 'my-env':

	~/mygithub $ python -m venv /path/to/new/virtual/environment
	or just
	~/mygithub $ python -m venv my-venv

### Activate your Virtual Environment

Do this from _within_ the mysite project root directory:

	Mac / Linux
	~/mygithub/ovensensorweb/mysite $ source ../../my-venv/bin/activate

	Windows
	C:\Users\jeffb4real\mygithub\ovensensorweb\mysite $ ..\..\my-env\scripts\activate.bat	

You should now see a command line prompt that is pre-pended with the name of the virtual environment, "(my-venv)" as shown below. Here we're checking that our python resides within our virtual environment and that it is the proper version (Python 3 or greater).

	(my-venv) ~/mygithub/ovensensorweb/mysite $ which python
	/Users/jeffb4real/mygithub/my-venv/bin/python
	(my-venv) ~/mygithub/ovensensorweb/mysite $ python --version
	Python 3.7.0
	
__Note:__ It is possible and sometimes advisable to have two instances of the same virtual environment, within two separate terminal windows (aka Command Prompt or cmd.exe on Windows). See more on this below, under 'Running the Django Server'.

### Install the Django Python Package

__Note:__ pip is the preferred package installer program for Python. Starting with Python 3.4, it is included by default with the Python binary installers.

This step assumes you've completed the previous step, Activate your Virtual Environment, and that the virtual environment is active.

The only additional package we need for the Django tutorial is Django itself. To install it into our virtual environment:

	(my-env) ~/mygithub/ovensensorweb/mysite $ python -m pip install django

_Feel free to skip ahead to the next section if you don't want to install any optional packages or update pip._

I also like the following package, which can give pop-up tips and extra color-coding while in the Python interactive shell:

	(my-env) ~/mygithub/ovensensorweb/mysite $ python -m pip install bpython

The version of pip included with Python might be out-of-date. You can optionally update pip with the following command:

	(my-venv) ~/mygithub/ovensensorweb/mysite $ python -m pip install --upgrade pip
	
Here's a before and after of pip versions:

	(my-venv) ~/mygithub/ovensensorweb/mysite $ pip --version
	pip 10.0.1 from /Users/jeffb4real/mygithub/my-venv/lib/python3.7/site-packages/pip (python 3.7)
	
	(my-venv) $ python -m pip install --upgrade pip
	Collecting pip
	  Using cached https://files.pythonhosted.org/packages/5f/25/e52d3f31441505a5f3af41213346e5b6c221c9e086a166f3703d2ddaf940/pip-18.0-py2.py3-none-any.whl
	Installing collected packages: pip
	  Found existing installation: pip 10.0.1
	    Uninstalling pip-10.0.1:
	      Successfully uninstalled pip-10.0.1
	Successfully installed pip-18.0

### Running the Django Server

The Django web framework includes its own web server and backend database (SQLite). To utilize these features we must first run the server.

Many Django tools (e.g. creating a Django project, create an application, run tests, etc.) are available through manage.py, which was created at the root of our project directory, when we created the Django project. For a complete list of Django capabilities, type 'python manage.py --help'.

You _must_ be inside the mysite project root directory (e.g. mysite/...) You can tell which directory is the correct directory, because it will contain manage.py.

	(my-env) ~/mygithub/ovensensorweb/mysite $ python manage.py runserver

	Performing system checks...

	System check identified no issues (0 silenced).
	September 24, 2018 - 16:22:46
	Django version 2.1.1, using settings 'mysite.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.

__Note:__ It is recommended to use two separate terminal windows (cmd.exe on Windows), both of which can simultaneouly invoke the same virtual environment, in our case 'my-venv'. Run the Django server as shown above, in one terminal, which will display relevant Django server status information. Use the other terminal with the same 'my-venv' virtual environment (you don't have to create it - just invoke it) to access Django's interactive shell commands, or to utilize manage.py.

The Django server will continue to run until it is killed with Ctrl+C, or else some other error occurs (e.g. remove or adversely change one or more critical project files).

### Running our Django Web Application

When you run the Django webserver, you will see a URL, as shown in the previous step (likely http://127.0.0.1:8000/). Copy this URL and paste it into your browser's address bar. Try loading the page and notice it fails. Append 'polls' to the end of the URL (http://127.0.0.1:8000/polls/) and reload the page. You should now be seeing the polls app.

### Viewing the Django Admin Site

Paste the following into your browser:

	http://127.0.0.1:8000/admin/
	
__Note:__ 127.0.0.1 is an alias for localhost


### References

Virtual Environments
https://docs.python.org/3/library/venv.html?highlight=venv

Pip
https://docs.python.org/3/installing/index.html

Markdown
https://www.markdownguide.org/basic-syntax/

