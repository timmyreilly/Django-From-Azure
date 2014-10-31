Django
=====

This guide was designed to help a young developer get started developing for the web. It provides tools and configuration before deep diving into the Model, View, Controller architecture. 

Getting started with MVC is easy, and this was designed to make it even easier. This guide will also provide a context to practice source code management, tooling configuration, and working with repositories. 

As with most things technology, there will be a focus on the cloud. This means that our deployment will live in the cloud. Every change we make will be pushed to a live and active site that you can visit from anywhere in the world!

So once you learn how to build, you will be familiar with deploying and managing.  

There are 6 pieces to this lesson.  

1. Your Box
2. The Cloud
3. Local Repository
4. Making a change
5. Deployment
6. Learning

1. Configuring your box
2. Spinning up your site
3. Pulling from the cloud
4. Configuring

Ingredients for this workflow:

- Python 2.7 (Configure so you can run the REPL
- A text editor (Sublime is good)
- An Azure Subscription (Bizspark or free trial)
- Git and a Git shell
- Terminal or powershell

**Your Box**

-  You should be able to do these things before we continue
	1. Open files with Sublime
	2. Change to your GitHub directory with powershell
	3. Run Python's REPL in powershell

**The Cloud**

1. Go to the Azure Portal
2. Select new in the lower left corner
3. Select Website
4. Select From Gallery
5. Find Django
6. Next 
7. Give at URL (eg: 'FirstMVC')
8. Hit the checkmark

Azure is now creating a complete Django website hosted in the cloud. 

Were going to begin treating this Django existence as a repository. Or a place to hold and manage our code.

1. Click on that instance
2. Find 'Integrate source control' on the Quick Start page
3. Select 'Set up deployment from source control'
4. 

**Local Repository**



**Making a change**

**Deployment**

**Learning **
 

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
