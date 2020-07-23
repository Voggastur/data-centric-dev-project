# HeroesDB

[Deployed website](https://heroes84.herokuapp.com/)
[Project Repository](https://github.com/Voggastur/data-centric-dev-project)

The aim of this website is to present my skills in Python Flask and Jinja to present information from a backend database (mongoDB).


## Table of Contents

1. [UX](#UX)

    I. [User stories](#UX2)
    
    II. [Wireframes](#UX3)

    II. [Development Progress](#UX4)
    
2. [Features](#Features)
3. [Features for the future](#Features2)
4. [Technologies used](#Technologies)
5. [Testing](#Testing)

    I. [Testing functionality](#Testing2)
    
    II. [Testing user stories](#Testing3)
    
6. [Deployment](#Deployment)

    I. [How to clone this project locally](#Deployment2)

7. [Credits](#Credits)


## 1. UX <a name="UX"></a>

The primary target audience are collaborators/employers who wish to see my knowledge in Python/Flask/Jinja.


#### I. User Stories: <a name="UX2"></a>

1. As an employer who recieved a link to Johans website, I want to see the page to see if it can handle backend database management, so that I can assess if Johan is eligible for a position handling databases.

2. As an assessor I will judge the website on the totality of looks, documentation, semantics and other things, so that I can assess his score.

3. As a collaborator I want to see if Johan can be of use in a Flask project, so I want to see Johans website. Additionally I want to see his repository to evaluate the level of the Python code.

4. As another type of collaborator I want to see if Johan can make use of dynamic content, so I will visit Johans website and try to add some content.

5. As a fan of roleplaying in Johans roleplay group, I want to update my heroes possessions of gold coins every round we play, because the game-master objected to my amount of gold in an earlier game.


#### II. Wireframes: <a name="UX3"></a>

* [Wireframes.pdf](wireframes/wireframes(mobile_desktop).pdf)

* [DBschema.pdf](wireframes/DBschema.pdf)


1. Initially I struggled to come up with an idea for a website, but settled on a character database that had actually been on my mind for a while.
    I play roleplay games with a few friends from time to time, and one day I got the idea to make a website like this one.
    The website could be made better by adding a user database with a login layout, so each hero would be connected to its creator,
    who would have the sole privilege of editing his own creations.

2. The Navbar is a Materialize component, which replaces itself by a only-icons version below 992px. I added media queries to avoid overlapping on small screens

3. The slider is a materialize component, and presents my website with images and captions explaining the purpose of the website

4. The cards are sorted as 2 in every row for large screens and 1 every row for small screens, a change from the 3 as shown in the wireframes.
    I felt that the content was too crowded for 3 so I changed it.

5. Materialize framework was used to achieve responsiveness


#### III. Development Process: <a name="UX4"></a>

* I started by using material from earlier projects we already developed, like the task manager project and the Flask chat app.

* It took some time for me to realize I have to declare variables in render_template to make use of variables in the templates, like the view_header and heroes.

* The testing process was more difficult than a regular HTML/CSS/JS page since the static links doesn't pull in the latest css/js files. So while developing I used regular links and partial html in a placeholder.html file to pull the newest css/js files.

* I added a fourth link for the add_adventure template to make it similar to creating heroes.

* I learned alot during the development of this project, I had to read up on a lot of articles and many youtube tutorials, it has been a learning experience.

* For every developing session I learned to set it up by doing 3 things,
1. Recreate the env.py file with my SECRET_KEY variable in it.
2. pip3 install -r requirements.txt ( to install python dependencies ).
3. python3 app.py ( to get a fullscreen preview window ).
And I always tried to leave the project in a functioning manner, but this was not always true for the python file, as I tried to import flash at one point but ended up being unable to update collections.


## 2. Features <a name="Features"></a>

* The website is an online storage of heroes for role-play gamers who meet from time to time to play through an adventure that one friend will be the storyteller of.
Upon completion of an adventure updating is needed for the heroes equipment and experience, and this is what the website is providing.

* The website uses Python to import cards into the base.html between the slider component and the footer

* 2 Collections were created in MongoDB in anticipation of the development, originally I had less content per collection but I added more attributes for each hero later.

* Heroes can be read, edited and deleted from the front page, another tab in the Nav leads to the add hero page which presents a form to insert a new hero into the database

* Similarly Adventures can be read, edited and deleted from its' own link in the Nav, and similarly to heroes have its own Add adventure link


## 3. Features for the future <a name="Features2"></a>

* A user collection could be added which connects heroes to the user that created them

* In addition users should be restricted to editing only their own creations, but could be able to have a restricted view of other peoples heroes for inspiration

* A user implementation would also mean some kind of login page, with encrypted password management, which would check against the password field

* Numericals for typical roleplay attributes such as strength, perception, endurance, charisma, intelligence, agility, luck should be added in the future, there would be a max numeral available to distribute among these attributes.


## 4. Technologies used <a name="Technologies"></a>

* HTML

* CSS

* Javascript

* jQuery

* Python

* Flask

* Jinja

* Materialize

* MongoDB

* Github Deployment

* Gitpod IDE

* Google Fonts

* W3C Validator

* Autoprefixer

* PEP8 Python Validator


## 5. Testing <a name="Testing"></a>

#### I. Testing Functionality <a name="Testing2"></a>

1. Testing was done manually throughout development.
2. I have validated the Python code with http://pep8online.com/checkresult
3. I have validated the HTML code with [W3C HTML Validator](https://validator.w3.org)
4. I have validated the CSS code with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
5. I added vendor prefixes to my css with the help of [Autoprefixer](https://autoprefixer.github.io/)


#### II. User stories testing <a name="Testing3"></a>

1. As an employer I go to see Johans website, if he's really as good as he postulated in his CV.

    * I click the Add hero link to change view, and input a hero. Afterwards I check that the hero appears in the list of heroes.

2. As an assessor I go to Johans website determined to check every nook and cranny among which..

    * Test if all links work.
    * Try to submit a new hero.
    * Try to submit a new adventure.
    * Try to edit a hero.
    * Try to edit an adventure.

3. As collaborator number 1 I check out Johans website to evaluate his skills, to measure his eligibility for developing a Flask project in a team.

    * I go to the website and click Add hero and submit a new hero with the name Spiderman. Afterwards I see that Spiderman appears on the page. 
    Afterwards I use the link to the repository and check the python file. I scroll down to see @app.route for insert_hero, which dictates how Spiderman was posted to mongo.db.heroes.

4. As collaborator 2 I want to see Johans website to see if he can show database content.

    * I go to the website and input a new adventure. Afterwards I will see the new adventure on the adventure tab.
    * I will also use google developer mode to check the responsiveness of the page, and the css and javascript source.

5. As a player in Johans roleplay group, I want to be able to store variables for my hero for the upcoming roleplay session.

    * Firstly I click the add adventure link to add context for the hero I am about to enter.
    * Secondly using paper sheets from the last roleplay session, I enter information about my hero. I make sure to add the 7 silver coins I made hunting rabbits in the last game into my possessions.
    * I check that my new hero appears at the bottom of the list of heroes


## 6. Deployment <a name="Deployment"></a>

This project was developed in Gitpod.
The project has been deployed to Heroku Pages - [Deployed Website](https://voggastur.github.io/data-centric-dev-project/)
The repository for this website can be found at this GitHub link: [Data Centric Repository](https://github.com/Voggastur/data-centric-dev-project)

The following process was used to deploy the project:
1. Create an app on Heroku webpage with name Heroes84
2. Go to Github webpage and log in
3. Select Voggastur/data-centric-dev-project
4. Open gitpod
5. Create requirements.txt file with $ pip3 freeze --local > requirements.txt
6. Create Procfile, open it and add: web: python app.py
7. git add requirements.txt, git add Procfile
8. git commit -m "Added requirements.txt and Procfile"
9. Login into heroku via the git CLI with $ heroku login
10. Add remote repo to git repo with: $ heroku git:remote -a heroes84
11. Push git repo to heroku: $ git push -u heroku master
12. Retrieve link from push message https://heroes84.herokuapp.com/


## 7. Credits <a name="Credits"></a>

* The slider images and the helmet picture was taken from a free library on google search.

* The letters J and K for my favicon.ico were found on google picture search, upon finding them I combined them and made converted it into my favicon.ico.
