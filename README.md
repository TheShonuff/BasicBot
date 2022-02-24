# BasicBot
#### A not so basic bot. A python learning project

Welcome to my evolving project intended to learn python and the process of app deployment across various platforms. This particular iteration has been deployed on Heroku. Do deploy your version on Heroku will need to know a few things.

#### requirements.txt
This file will need to contain every pip install for your project. When you Heroku builds your project it will look at this file and determine whats needs to be installed to properly run the app.

[Heroku Requirments](https://devcenter.heroku.com/articles/python-pip) 

#### Procfile
This file will determine the process that needs to be run. For a discord bot you’ll need the “worker” process

[Heroku Procfile](https://devcenter.heroku.com/articles/procfile)

#### runtime.txt
This is the most basic file that specifies the version of python you’re running
[Heroku Runtime](https://devcenter.heroku.com/articles/python-runtimes)

Be sure to add you’re bots DISCORD_TOKEN to the settings env variables in the settings tab for you bot to come online properly. I’ve found that when working locally load_dotenv(‘.env’) works well to load your variables into your script from the external text file. When you push to the cloud you’ll need to just use load_dotenv(). 

