# Django-Querysets-and-Managers

We’ll be building more features for our URL shortener service.

Create a new GitHub repository with a README.md, and Python .gitignore file.

Clone it to your machine/computer, which will create a new folder on your computer with your repository’s content. Copy your Django project files from the previous task “Working with APIs”, https://github.com/Hepziba97/Django--API-with-RESTFramework to the newly created folder.

Create a new virtual environment in that folder named venv.  Activate it and install the Django python package (Hint: `pip install Django).

Also, install the Django rest framework (pip install djangorestframework)

We want users of our API to view all active links. We also want to provide users with an endpoint to view Links created during the week.

Create a new file, managers.py in your links app folder. Replace the content of links/managers.py with this starter file https://github.com/TobeTek/Zuri/blob/main/starter-files/Querysets-and-Managers/managers.py  

Add the following attributes to your Link model in links/models.py

objects = models.Manager()

public = ActiveLinkManager()

On to the views. Copy the ActiveLinkView and RecentLinkView from  https://github.com/TobeTek/Zuri/blob/main/starter-files/Querysets-and-Managers/views.py to links/views.py.


Add the following new URL paths in links/urls.py.

path("active/", ActiveLinkView.as_view(), name=’active_link’)

path("recent/", RecentLinkView.as_view(), name=’recent_link’)


Stage and Commit your Django project and push your changes to your GitHub repository. 

Ensure your final code/submission is on the default branch of your GitHub repository.

Submit the link to your Github repository e.g https://github.com/github_username/repo_name