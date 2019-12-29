[![Build Status](https://travis-ci.org/lubaninondo/issue-tracker.svg?branch=master)](https://travis-ci.org/lubaninondo/issue-tracker)

#**ISSUE TRACKER**

This application allows the user to create feature requests and bugs. Submission of bug reports is free while submission of feature request will cost 30 Euro. Feature requests will be worked on first. Stripe was incorporated for easy payments. Voting for bugs and features is also included in the application

#**UX**

The user will be able to:
raise bugs
upvote bugs
Raise feature requests for thirty euro
Upvote feature request for 5 euro
Can view statistics of bugs and features
Read the blog
Create the blog if she is the administrator


#**FEATURES**

The application contains the following features:

**##Registration and sign in**: The user will need to register using the email and password. These will be used for signing in. A user will need to sign in to create bugs and feature requests

**##Sign Out** : The user can sign out after using the site

**##Tickets Creation**: The two issues that can be created are bugs and features. The user can create a bug for free and features for a fee. A user can delete or edit the issue that she has created.

**##Upvote**: The user can upvote for the bug and features she believes should be worked on first. Voting for a bug is free and for features is 5 euro

**##Filter**: The user can choose to only view either bugs or features

**##User Rights**: A registered user can delete and edit the tickets that he created. The superuser can edit, delete and change status of any ticket

**##Blog**: Any person can access the blog but only the superuser can create new content

**##Statistics**: Any person visiting the website has access to the statistics, that is the bug with the highest votes, feature with the highest votes, number of bugs and features created and the progress of features and bugs

The following features are yet to be added:

##**comments**

##**Profile Picture**

#**TECHNOLOGY USED**

[JQUERY](https://jquery.com/) was used to simplify DOM manipulation

[HTML5](https://html.spec.whatwg.org/multipage/) for structuring the page

[CSS](https://www.w3schools.com/css/) for styling the project

[Django](https://www.djangoproject.com/) framework for building a useful website

[Bootstrap](https://getbootstrap.com/docs/3.3/getting-started/) to provide a better UX and simplify grid layout

[Python3](https://docs.python.org/release/3.4.3/) to handle POSTs and manipulate data presented from the user

[AWS(S3)](https://docs.aws.amazon.com/index.html#lang/en_us) for storing images and static

[Stripe](https://stripe.com/) to enable payments

[SQLite](https://www.sqlite.org/docs.html) as a local database

[PostgreSQL](https://www.postgresql.org/) as a global database


#**TESTING**

##**Login Page**: Fill the login page using the username/email address and password

1. invalid username/email address or password message indicates username does not exist or wrong password

2. correct login details you get username and successful login message

3. Submit an empty document message about required field missing appears

##**Registration Form**##: Fill the registration form

1. Input an existing username a message saying username already exist appears

2. Correct registration directs to home page/index.html

3. Submit an empty document message about required field missing appears

##**Blog**: Superuser fills blog form and submit

##**Create Feature Request**:

1. Try to create without login- redirected to login page

2. Click Create Feature Request and Fill the Feature Request Form and Payment card (test card) details correct- Feature Request appears with all details

3. Missing Create Feature Request Form or Payment Details message about required field missing appears

4.Wrong payment details- message unable to take card appears


##**Create Bug**

1. Try to create without login- redirected to login page

2. Click Create Bug and Fill the Create Bug Form and Bug appears with all details

3. Missing Create Bug Form  message about required field missing appears

##**UpVote Feature** : Click the upvote feature icon and fill the payment card details

1. Try to vote without login- redirected to login page

2. Wrong information on the payment card message unable to take card appears

3. Correct card details message Feature upvoted appears and feature details

##**Upvote Bug**: Click the Upvote Bug icon

1. Try to vote without login- redirected to login page

2.Click the Upvote Bug icon and Bug upvoted appears with bug details

##**Statistics**: Click statistics and view all statistics

##**Admin**: If logged as a admin and /admin in front of the website instead of ticket.

Assess tickets, change the progress of tickets, delete ticket and edit ticket

##**Sign Out**: Click Sign out and message Successful logged out appears

##**Filter**: Click downward Arrow in Filter and choose to view both bugs and features by selecting All, only Features by selecting Feature Request and only bugs by selecting Bugs

#**DEPLOYMENT**:

This project has been deployed to [Github](https://github.com/lubaninondo/issue-tracker/) and hosted on [Heroku](https://lubani-issue-tracker.herokuapp.com/tickets/) 

#**CREDIT**:

This project has been inspired by [Code Institute](https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce/tree/master/03-HostingYourEcommerceWebApp/07-heroku_hosting), [Itoulou](https://github.com/itoulou/unicorn-attractor), [ShaunZA](https://github.com/ShaunZA/django-issue-tracker), [neon-flights](https://github.com/neon-flights/unicorn-attractor)

Many credits to my Mentor Ali Ashik and Code Institute tutors



