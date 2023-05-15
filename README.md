<img src="./logo-full-dark.svg" alt="keyper logo" width="250"/>
Easily manage and track your keys

---

Keyper helps you in managing and tracking multiple keys especially in University where there are many rooms and keys to handle and keep track on the borrowed and returned keys.

# How does Keyper works?

Keyper has 3 main parts:
1. **API**,
2. **Web Client**, and
3. **Keyper Device**

# Program Requirements
- [git @any version](https://git-scm.com/downloads) 
- [python at least v3.11.0](https://www.python.org/downloads/)
- Add SSH Key of your machine to your github account. Below are the steps:
1. Generate SSH Key Pair

   In the Git Bash terminal, enter the following command to generate a new SSH key pair:

   ```bash
   ssh-keygen -o -t rsa -C "your_email@example.com"
   ```

   Replace "your_email@example.com" with your email address associated with GitHub.
   Press Enter to accept the default file location and name (generally, it will be saved in ~/.ssh/id_rsa).
   When prompted, enter a secure passphrase (optional but recommended) and press Enter. Remember this passphrase, as you will need it later.

2. Copy Public Key

   To display the contents of your public key, run the following command in the Git Bash terminal:

   ```bash
   cat ~/.ssh/id_rsa.pub
   ```

   The output should be the public key. Select the entire key and copy it to the clipboard.

3. Add Public Key to GitHub

   1. Open your web browser and go to GitHub (https://github.com/).
   2. Log in to your GitHub account.
   3. Click on your profile picture in the top-right corner and select "Settings" from the dropdown menu.
   4. In the left sidebar, click on "SSH and GPG keys".
   5. Click on the "New SSH key" button.
   6. Provide a title for the SSH key (e.g., "My Windows SSH Key").
   7. Paste the copied public key into the "Key" field.
   8. Click the "Add SSH key" button.
   9. If prompted, enter your GitHub account password to confirm.

That's it! You've successfully generated an SSH key on Windows and added the public key to GitHub. You can now proceed on how to contribute or the installation.

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
    `pip install -r requirements.txt`
5. You can now run `python manage.py runserver` and view the website through this link [127.0.0.1:8000/](http://127.0.0.1:8000/)
