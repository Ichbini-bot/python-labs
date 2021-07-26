'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 (1: Django) packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7. Create a new virtual environment and install the packages from the requirements.txt file.

differently re Windows / VSC: And btw, machs im Git GUI! Dort funktionierts... (weder im Git Bash noch im VSC Terminal...)
1.1 mkdir virtual_test (then change into directory with cd virtual_test)
1.2 python -m venv firstenv (venv is the command, firstenv the name of the directory the venv sits in)

2.1 Git GUI: first env\scripts\activate

3.1 pip install django
3.2 pip freeze => shows all dependencies in the venv (in my case: asgiref==3.4.1, Django==3.2.5, pytz==2021.1, sqlparse==0.4.1)

4.1 pip freeze > requirements.txt

6. and 7.: Discuss with Jon (re 6: I just delete the env folder?, re 7, is there a way to use the .txt file directly - guess so)

Discuss as well virtual environments variables


'''