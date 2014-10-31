Dango
=====

Django with Azure 

Did you know you can pull a site from Azure, manage it in a Git repository, and commit changes back into Azure?

Well you can! And I'm gonna show you how. 

A quick change

First thing: 
Download Git
	(We'll be using the shell)
Download Python
	Configure Python C:\Python27\python.exe
Download Sublime

Activate your Azure trial or subscription: Check out BizSpark for $150 a month for young companies!
Go to the portal
Websites
New Website
From Gallery
Django Site
Name it something and put in your region!

Wait for it deploy!
Once deployed...
Set up deployment from Source Control
Select a repository or file management system that you like. 
I'll be using LocalRepository to keep it simple. 

Open up your git shell 
CD to your favorite development folder. 
Clone that sucker. 

New Directory created. 
Cool, We'll now initialize the azure site as our remote repository

Let's make a quick change: 
Add a new view
Add file: views.py

	
Add a new template

Add a new route

Change your settings
Add import os.path
Add Static path
Configure TEMPLATE_DIRS


Add the new files
Commit the changes
And push back to Azure!

Alright! Now you're ready to create with Django and Azure in a real website. 
These tutorials will get you started creating!
When you're ready for a daddybase on Azure 
