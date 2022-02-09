## Welcome to Backoffice Automation Project!

Hi! My name is Federico Marilungo

If you are new working with python, pipenv, pytest or selenium, 
I would recommend you follow this course 
https://testautomationu.applitools.com/learningpaths.html?id=web-ui-python-path

## I dont have time! Give me the command!

---

run tests

`pipenv run python -m pytest`

---

run specific test with logs

`pipenv run python -m pytest -s ./tests/test_search.py::test_basic_duckduckgo_search`


---

run tests in parallel with report

`pipenv run python -m pytest --html=./reports/report.html --self-contained-html -n 3`


`pipenv run python -m pytest --junitxml=./reports/report.xml --self-contained-html -n 3`

---

modify config.json, browser = 'Remote' and run!

you can see tests running in remote machine :

grid : http://35.227.34.60:4444/ui/index.html#/
pass : secret

---

run tests remotely with video recording

create this folder

`C:\temp\videos`

execute selenium_video_recorders.yml (selenium_grid should have been executed)

`docker-compose -f ./docker/selenium_video_recorders.yml up`

run tests and then stop video recorders

---

## Python Setup

This project requires Python 3.8 or higher.

Also requires [pipenv](https://docs.pipenv.org/).
To install pipenv, run `pip install pipenv` from the command line.

You should also have a Python editor/IDE of your choice.
Good choices include [PyCharm](https://www.jetbrains.com/pycharm/)
and [Visual Studio Code](https://code.visualstudio.com/docs/languages/python).

## WebDriver Setup

For Web UI testing, you will need to install the latest versions of
[Google Chrome](https://www.google.com/chrome/)
or [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/).

You will also need to install the latest versions of the WebDriver executables for these browsers: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome
and [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox.

Each test case will launch the WebDriver executable for its target browser.
The WebDriver executable will act as a proxy between the test automation and the browser instance.
Please use the latest versions of both the browsers and the WebDriver executables.
Older versions might be incompatible with each other.

ChromeDriver and geckodriver must be installed on the
[system path](https://en.wikipedia.org/wiki/PATH_(variable)).

### WebDriver Setup for Windows

To install ChromeDriver and geckodriver on Windows:

1. Create a folder named `C:\Selenium`.
2. Move the executables into this folder.
3. Add this folder to the *Path* environment variable. (See [How to Add to Windows PATH Environment Variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).)

### WebDriver Setup for *NIX

To install ChromeDriver and geckodriver on Linux, macOS, and other UNIX variants,
simply move them to the `/usr/local/bin/` directory:

```bash
$ mv /path/to/ChromeDriver /usr/local/bin
$ mv /path/to/geckodriver /usr/local/bin
```

This directory should already be included in the system path.
For troubleshooting, see:

* [Setting the path on macOS](https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/)
* [Setting the path on Linux](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)

### Test WebDriver Setup

To verify correct setup on any operating system, simply try to run them from the terminal:

```bash
$ ChromeDriver
$ geckodriver
```

You may or may not see any output.
Just verify that you can run them without errors.
Use Ctrl-C to kill them.

## Project Setup

1. Clone this repository.
2. Run `cd backoffice_automation` to enter the project.
3. Run `pipenv install` to install the dependencies.
4. Run `pipenv run python -m pytest` to verify that the framework can run tests.
5. Create a branch for your code changes. (See *Repository Branching* below.)

### Project Setup Troubleshooting

A few people attempting to set up this project
encountered the following error when executing `pipenv run python -m pytest`:

```
ModuleNotFoundError: No module named 'atomicwrites'
```

I'm not exactly sure why `pipenv install` does not include `atomicwrites`.
So far, I have seen it happen only on Windows.
To resolve the error, please attempt the following:

* Upgrade Python to the latest versions. The following worked for me on Windows:
  * Python 3.8.3 (`python --version`)
  * pip 20.1 (`pip --version`)
  * pipenv 2018.11.26 (`pipenv --version`)
* Run `pipenv update` from within the project directory.

If upgrades don't work, try forcing package installation:

* Run `pipenv install pytest` from within the project directory.
* Run `pipenv install atomicwrites` from within the project directory.

If these steps don't work in your project, then try to run without pipenv:

* Install Python packages directly using `pip`.
* Run tests directly using `python -m pytest`.

## Repository Branching

The `master` branch contains the code for executing tests automation in all enviroments. Is the source of true

If you want to code something, then create a branch for your work off the `master` branch.
To create your own branch named `course/develop`, run:

    > git checkout master
    > git pull
    > git checkout -b feature_name

Then, you should create a Pull Request to integrate your tests cases into Master