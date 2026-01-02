# First Time Setup

## Using Pipenv

```
# Install dependencies
pipenv install

# Create a virtual environment
pipenv shell

# Initialize the database
flask --app app.web init-db

```


# Start the local file upload server

I installed the local-do-files locally on my computer.

Do not place these files inside of your current pdf project. They need to be a separate directory and will be run as a separate application.

Using your terminal, change into the local-do-files directory.

Run `pipenv shell`, then, `pipenv install`

The above commands assume that you have already installed Pipenv, something that we've been using throughout the course up until this point. After doing this, your terminal will now be running commands in the new environment managed by Pipenv.

Once inside the Pipenv shell, start the server with `python app.py`

Example:

```
(langchain-pdf) timothyfiola@Timothys-MacBook-Pro langchain-pdf % cd ..
(langchain-pdf) timothyfiola@Timothys-MacBook-Pro PycharmProjects % cd local-do-files 
(langchain-pdf) timothyfiola@Timothys-MacBook-Pro local-do-files % pipenv shell
Courtesy Notice:
Pipenv found itself running within a virtual environment,  so it will automatically use that environment, instead of  creating its own for any project. You can set
PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create  its own instead.
You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Launching subshell in virtual environment...
/Users/timothyfiola/.zshrc:5: parse error near `then'
 source /Users/timothyfiola/.local/share/virtualenvs/langchain-pdf-bv5GE1wQ/bin/activate                                                                                                                                
timothyfiola@Timothys-MacBook-Pro local-do-files %  source /Users/timothyfiola/.local/share/virtualenvs/langchain-pdf-bv5GE1wQ/bin/activate
(langchain-pdf) timothyfiola@Timothys-MacBook-Pro local-do-files % pipenv install
Installing dependencies from Pipfile.lock (708f33)...
(langchain-pdf) timothyfiola@Timothys-MacBook-Pro local-do-files % python app.py 
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8050
Press CTRL+C to quit
 * Restarting with watchdog (fsevents)
 * Debugger is active!
 * Debugger PIN: 101-228-183
247c71e5-9f2f-408c-9f8b-68f919b6e035
127.0.0.1 - - [29/Dec/2025 16:47:44] "POST /upload HTTP/1.1" 200 -
127.0.0.1 - - [29/Dec/2025 16:47:44] "GET /download/247c71e5-9f2f-408c-9f8b-68f919b6e035 HTTP/1.1" 200 -
```



# Running the app

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
flask --app app.web init-db
```
