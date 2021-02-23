# Welcome to the project "Imagine a Github Profile Finder"
---------------------------------------------------------

## Introduction to Flask
------------------------

if you are using Microsoft Windows, make sure you open a command prompt window using the “Run as Administrator” option, and then run this command:

```
$> pip install virtualenv
```

If you are using Linux or macOS, the command is:

```
$> sudo pip install virtualenv
```
The virtualenv command takes the name of the virtual environment as its argument. Make sure your current directory is set to *flasky*, and then run the following command to create a virtual environment called *venv*:

```
$ virtualenv venv
```

## Working with a Virtual Environment
-------------------------------------

When you want to start using a virtual environment, you have to *activate* it

If you are using Microsoft Windows, the activation command is:

```
$> venv\Scripts\activate
```

If you are using a Linux or macOS computer, you can activate the virtual environment with this command:

```
$> source venv/bin/activate
```

When a virtual environment is activated, the location of its ```Python``` interpreter is added to the ```PATH``` environment variable in your current command session, which determines where to look for executable files. To remind you that you have activated a virtual environment, the activation command modifies your command prompt to include the name of the environment:
```
(venv) $>
```

After a virtual environment is activated, typing python at the command prompt will invoke the interpreter from the virtual environment instead of the system-wide interpreter. If you are using more than one command prompt window, you have to activate the virtual environment in each of them.

When you are done working with the virtual environment, type **deactivate** at the command prompt to restore the PATH environment variable for your terminal session and the command prompt to their original states.

## Installing Requirements with pip
-----------------------------------

To install requirements into the virtual environment, make sure the venv virtual environment is activated, and then run the following command:

```
(venv) $>pip install -r requirements.txt
```

When you execute this command, ```pip``` will install all dependencies. ou can check what packages are installed in the virtual environment
at any time using the  ```pip freeze ``` command:

```
(venv) $>pip freeze
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
decorator==4.4.2
dnspython==1.16.0
docopt==0.6.2
docutils==0.16
fett==0.3.2
Flask==1.1.2
Flask-WTF==0.14.3
...
...
...
watchdog==1.0.2
Werkzeug==1.0.1
WTForms==2.3.3
```

## Extensions used
------------------

- [Flask-WTF](http://pythonhosted.org/Flask-WTF/) for forms.

## Development Web Server
--------------------------
Flask applications include a development web server that can be started with the flask run command. This command looks for the name of the Python script that contains the application instance in the FLASK_APP environment variable.
To start the hello.py application from the previous section, first make sure the virtual environment you created earlier is activated and has Flask installed in it. For Linux and macOS users, start the web server as follows:

```
(venv) $ export FLASK_APP=main.py
(venv) $ flask run
 * Serving Flask app "main"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

For Microsoft Windows users, the only difference is in how the ```FLASK_APP``` environment variable is set:

```
(venv) $ set FLASK_APP=main.py
(venv) $ flask run
 * Serving Flask app "main"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Once the server starts up, it goes into a loop that accepts requests and services them. This loop continues until you stop the application by pressing ```Ctrl+C```.

With the server running, open your web browser and type ```http://localhost:5000/``` in the address bar.

## My favorite option for the Development Web Server
----------------------------------------------------

To declare the ```FLASK_APP``` variable we must modify the activate file of our Python environment.

On Windows it is located in ```venv\Scripts\activate.bat```. At the end of the file we add the following:

```
set "FLASK_APP=main.py"
```

On Linux/MacOS it is in ```venv/bin/activate```. At the end of the file we add the following:

```
export FLASK_APP="main.py"
```

For the changes made to be taken into account, we must exit the Python environment and enter again. To exit, you have to run in the terminal ```deactivate```.

Next, we activate the environment again with ```env\Scripts\activate.bat``` if we are on Windows or ```source env/bin/activate``` if we are on Linux/MacOS

### Debug mode
--------------

To activate debug mode, simply add the ```FLASK_ENV``` environment variable and assign it the value ```development```.

On Windows:

```
set "FLASK_ENV=development"
```

On Linux/MacOS:

```
export FLASK_ENV="development"
```

### Remark: Don't use debug mode in a production environment
----------------------------------------------------

## Deafult command

Running the following commands:

```
(venv) $> flask

```

The commands for version and help:

```
Options:
  flask --version  Show the flask version
  flask --help     Show this message and exit.
```

The rest of commands is more conventional:

```
Commands:
  flask routes  Show the routes for the app.
  flask run     Run a development server.
  flask shell   Run a shell in the app context.
```

By default the site is hosted at `localhost:5000`.

## Testing with Unittest

### Extensions used

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html) for Unit testing.
- [Flask Docs](https://flask.palletsprojects.com/en/1.1.x/testing/) for Testing Flask Applications.
- [API - GitHub](https://api.github.com/users/juniors90) for data.


Running the following commands:

```
(venv) $>python -m unittest
.....
----------------------------------------------------------------------
Ran 5 tests in 4.505s

OK

```

### Remark: As it is an API, the testing data is variable.

Use your own account to consume the API. For example, change

```
https://api.github.com/users/juniors90
```
for
```
https://api.github.com/users/my-username
```

```python
def test_access_to_finder(self):
        user_data = self.finder_user(dict(username='my-username', ))
        res = self.client.get('/')
        self.assertEqual(200, user_data.status_code)
        self.assertIn(b'my-username', user_data.data)
        self.assertIn(b'Public: X', user_data.data) # X = number of my public repositories
        self.assertIn(b'Followers: Y', user_data.data) # Y = number of my Followers
```