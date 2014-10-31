Get Started with Django from Azure
=====

This guide was designed to help a young developer get started developing for the web. It provides tools and configuration before deep diving into the Model, View, Controller architecture. 

Getting started with MVC is easy, and this was designed to make it even easier. This guide will also provide a context to practice source code management, tooling configuration, and working with repositories. 

As with most things technology, there will be a focus on the cloud. This means that our deployment will live in the cloud. Every change we make will be pushed to a live and active site that you can visit from anywhere in the world!

So once you learn how to build, you will be familiar with deploying and managing.  

## There are 6 pieces to this lesson.  

1. Your Box
2. The Cloud
3. Local Repository
4. Making a change
5. Deployment
6. Learning


## Ingredients for this work-flow:

- [Python 2.7](https://www.python.org/download/releases/2.7/) (Configure so you can run the REPL
- [A text editor](http://www.howtogeek.com/112385/the-best-free-text-editors-for-windows-and-linux/ "How To Geek has good guide") ([Sublime](http://www.sublimetext.com/ "Sublime's site") is good)
- An Azure Subscription ([Bizspark](http://www.microsoft.com/bizspark/ "Gotta get me some of that bizspark. I can hook you up as well @timmyreilly") or [free trial](http://azure.microsoft.com/en-us/pricing/free-trial/ "Free trial site. Let me know if it's changed @timmyreilly"))
- [Git](https://github.com/) and a Git shell
- [Powershell](http://en.wikipedia.org/wiki/Windows_PowerShell "This wikipedia is excellent ") or Terminal 

## Your Box 

-  You should be able to do these things before we continue
	1. Open files with Sublime
	2. Change to your GitHub directory with powershell
	3. Run Python's REPL in powershell

## The Cloud

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
 

##Local Repository

We'll now set up our local repository. Where changes will be recorded and managed then pushed towards our remote repository hosted on Azure. 

With GitShell change to your github folder. 

We'll be creating the repository here. 

1. Copy the line that begins: git clone https:// 
2. Paste this into your git shell and press enter

We're now cloning the repo into a new directory. 
Open file explorer and take a look at the new file. Retry 'git clone' it if hangs or takes too long. You're moving 6000ish files. 

Now we'll connect our repo to Azure's

1. CD into newly created directory
2. Copy the line that begins: git push azure master ...
3. Run this command

Now two repos are setup and connected! 
Source control is in your hands! 

## Making a change

Now we can develop! We can practice and learn with this file-set.

To demonstrate we are going to begin with making a very simple site from code we copy and paste. 

And show how this change comes to fruition. 

1. Open a text editor
	- Try opening from the root file by selecting -> File -> Open Folder
2. Take a look at all those files! (You'll learn more about these if you follow the tutorials in the learning section. 
3.  In the DjangoApplication Directory create a new folder named 'templates'
4.  In that folder add a new file named home.html

Now we'll be inserting the code that lies within the repo that this README.md exists in. You can either fork the changes, type it in, or copy the changes from the raw files on GitHub. 

There are 5 total files to edit. And these five are the only you'll need to edit to make an entire site! You'll learn more advaced topics if you continue, but everything else is just extra layers to these 5 building and configuration blocks. 

1. Copy and paste the code from home.html into your newly created home.html file 
	- This is a template: It provides the html to generate on your browser. 
2. Copy the paste the code from settings.py into your settings.py
	- This is the configuration file that helps django know what settings you'd like on your files. 
3. Copy and paste the code from urls.py into your urls.py
	- This is the routing file. It acts as the telephone operator for requests
4. Copy and paste the code from views.py into your views.py. 
	- This is the logic of the matter. Its the fun part. 

Alright you're sites all ready. Save your changes! We're about to deploy. 


## Deployment

This is a common git flow. For personal git controlled code this is a very simple way to get your head wrapped around the process. Start here and you'll work your way into the git mastery. 

Run these commands in this order

- git add . 	
	- Will return nothing	
- git commit -a -m "Description of Commit"
	- Will info about changes made returned
- git push azure master
	- Info about pushing will be returned.

Now those changes exist in the cloud. 

Refresh your website! You can see the changes.  

Your tools are setup, your files are in line and you're ready to learn without configuration headaches. 

From here on out, every 15 minutes as you learn and work simply run those three commands in the GitShell to see what your website looks like and keep you code safe and in a cozy cloud. 


##Learning

This is just the start. You are now ready to open your mind to the fascinating and wonderful world of web development. 

This guide was built with these tutorials in mind, and are a natural extension of this work.  

**Python the hard way**

[http://learnpythonthehardway.org/](http://learnpythonthehardway.org/)

This tutorial will teach you so much, and is right in line with this project. I would suggest getting as far through this as possible. Not only is it a great introduction to Python, but also an incredibly effective way to begin thinking like a computer scientist.

**djangobook**

[http://www.djangobook.com/en/2.0/index.html](http://www.djangobook.com/en/2.0/index.html)

Welcome to application development in the web. This will not only teach you how to build a simple app. But will give you context for web development. It is well done, articulate, and includes great descriptions and philosophies for why things are done. Not only fascinating, but a great foundation for other web development frameworks. Get some good music going and start jamming through.

Hope this tutorial helps. 

Please let me know if anything is unclear, 
you need help, or feel like geeking out.

[@timmyreilly](https://twitter.com/timmyreilly)
or
[timmyreilly.com](http://timmyreilly.com/)


 

