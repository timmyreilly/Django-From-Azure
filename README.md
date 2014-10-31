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

(You can visit the site by navigating to this URL: http://YOUR-WEBSITE-NAME.azurewebsites.net)

Were going to begin treating this Django existence as a repository. Or a place to hold and manage our code.

1. Click on that instance
2. Find 'Integrate source control' on the Quick Start page
3. Select 'Set up deployment from source control'
4. Select 'Local Git repository'

The page will refresh with instructions. 
We'll be copying text from this page, so keep it handy. 
 

**Local Repository**

We'll now set up our local repository. Where changes will be recorded and managed then pushed towards our remote repository hosted on Azure. 

With GitShell change to your github folder. 

We'll be creating the repository here. 

1. Copy the line that begins: git clone https:// 
2. Paste this into your git shell and press enter

We're now cloning the repo into a new directory. 
Open file explorer and take a look at the new file. Retry 'git clone' it if hangs or takes too long. You're moving 6000ish files.  

**Making a change**

Now we can develop! We can practice and learn with this file-set.

To demonstrate we are going to begin with making a very simple site from code we copy and paste. 

And show how this change comes to fruition. 

1. Open a text editor
	1. Try opening from the root file by selecting -> File -> Open Folder
2. Take a look at all those files! (You'll learn more about these if you follow the tutorials in the learning section. 
3.  In the DjangoApplication Directory create a new folder named 'templates'
4.  In that folder add a new file named home.html

Now we'll be inserting the code that lies within the repo that this README.md exists in. You can either fork the changes, type it in, or copy the changes from the raw files on GitHub. 

There are 5 total files to edit. And these five are the only you'll need to edit to make an entire site! You'll learn more advaced topics if you continue, but everything else is just extra layers to these 5 building and configuration blocks. 

1. Copy and paste the code from home.html into your newly created home.html file 
	1. This is a template: It provides the html to generate on your browser. 
2. Copy the paste the code from settings.py into your settings.py
	1. This is the configuration file that helps django know what settings you'd like on your files. 
3. Copy and paste the code from urls.py into your urls.py
	1. This is the routing file. It acts as the telephone operator for requests
4. Copy and paste the code from views.py into your views.py. 
	1. This is the logic of the matter. Its the fun part. 

Alright you're sites all ready save all your changes! We're about to deploy. 




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
