![Keyper logo](./logo-full-dark.svg)

# Keyper

Easily manage and track your keys

---

Keyper helps you in managing and tracking multiple keys especially in University where there are many rooms and keys to handle and keep track on the borrowed and returned keys.

# Program Requirements
- [git @any version](https://git-scm.com/downloads) 
- [python at least v3.11.0](https://www.python.org/downloads/)
Once these programs are successfully installed, you can proceed 

# How to Contribute?

> **Note**
> Before proceeding on how to contribute, you must install the prerequisite programs first.

1. Fork the main repository
2. Clone the forked repo (from your account) using this command:<br>
   `git clone git@github.com:<your-username>/Keyper.git`<br>
   > change the `<your-username>` with your github username including the angle brackets
3. Create a new branch to easily track and manage changes:<br>
   `git checkout -b <your-username>/<feature-to-change>`<br>
   > again, change the `<your-username>` with your username and change the `<feature-to-change>` with the feature you want to change
   > sample branch name would be `marc/update-landing-page`
4. Create some changes based on the desired feature.
5. Add your changes `git add .` or `git add <specific-file(s)>`
6. Commit your added changes `git commit -m "add: feature"` or `git commit -m "update: feature"`
7. Push to your remote repo `git push -u origin <branch-name>` example: `git push -u origin marc/update-landing-page`
8. Open your github repo and notice the new `Compare and Create Pull Request` button, click it and `create pull request`
9. Wait for it to be merged! Thank you!

# How to Install?

> **Note**
> Before proceeding on the installation, you must install the prerequisite programs first.

1. Clone the repository if not yet cloned to your local machine.
2. `cd Keyper` 
3. Create a python virtual environment:
   1. `python -m venv .venv` or `py -m venv .venv`<br>
      > **Note**
      > You must name your virtual environment folder as `.venv` to include it in the `.gitignore` files or name it any name you like and include it in `.gitignore`
    2. activate your venv script by `.venv\Script\activate.bat` or `.venv\Script\Activate.ps1` if your using powershell
4. Once you've created and activated your python virtual environment, install the necessary python libraries:<br>
    `pip install django djangorestframework`
5. You can now run `python manage.py runserver` and view the website through this link [127.0.0.1:8000/](http://127.0.0.1:8000/)