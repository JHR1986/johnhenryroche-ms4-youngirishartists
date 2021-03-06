# Young Irish Artists

- [Art Ecommerce Website - Milestone Project 4](#art-ecommerce-website---milestone-project-4)
- [User Experience](#user-experience)
  * [User Stories](#user-stories)
  * [First Time Visitor Goals](#first-time-visitor-goals)
  * [Returning Visitor Goals](#returning-visitor-goals)
  * [Frequent Visitor Goals](#frequent-visitor-goals)
- [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
- [Features](#features)
- [Database Design](#database-design)
  * [Database](#database)
- [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks and Libraries and Programs Used](#frameworks-and-libraries-and-programs-used)
- [Testing](#testing)
- [Deployment](#deployment)
  * [How to run this project locally](#how-to-run-this-project-locally)
  * [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

## Art Ecommerce Website - Milestone Project 4

[View the Live Website Here](https://jhroche-young-irish-artists.herokuapp.com/)

This project comprises the development of a fictional ecommerce website where users can purchase prints by exciting new artists based in Ireland working in a range of painting styles. The website also provides a helpful platform for recently graduated artists to gain exposure and recognition of their recent work thus improving their profile in the Irish art world. The website allows the user to create a profile when they are making a purchase so that they have an account through which they can see their history of previous purchases and load their billing and shipping information in order to make future orders easier. There is also a superuser profile for the site administrator through which artworks can be amended through CRUD (Create, Read, Update and Delete) functionality. In respect of the overall construction of this website, it has been designed to be fully responsive, intuitive and accessible on a range of media devices (e.g. mobile, tablet and desktop), in order to make it as easy as possible for users of the website to navigate it and make their required purchases.   

Photo of Site Represented on Various Media to highlight responsive design:

![responsive](https://user-images.githubusercontent.com/71781554/129000316-423d15a7-d1c1-4e98-9483-e8c28c0fe85b.png)

## User Experience 

### User Stories

### First Time Visitor Goals
1.  As a First Time Visitor, I want to quickly confirm what products the ecommerce website is selling (e.g. art prints).
2.  As a First Time Visitor, I want to be able to easily browse through the site pages (including About and Artists) and view the artworks that are on offer.
3.  As a First Time Visitor, I want to be able to go to the Register page and create my own account if I am considering making a purchase.

### Returning Visitor Goals
1.  As a Returning Visitor, I want to be able make purchases of art prints easily and efficiently, as I now have an account and my information (e.g. billing and shipping) will be pre-loaded. 
2.  As a Returning Visitor, I want to be able to filter my searches for artworks by categories including genre, price, rating or specials, in order that I can purchase the artworks that best suit my preference and price range. 

### Frequent Visitor Goals
1. As a Frequent/Returning Visitor, I want to be able to easily contact Young Irish Artists if there has been any issue with my purchase, and the contact information for the company is clearly highlighted in the Footer Section of the site. 
2. As a Frequent/Returning Visitor, I want to be able to see new artists that have joined the site and the new artworks that they have produced, as well as new artworks by current artists, as the artworks on offer for sale will be updated on a regular basis.

## Design

### Colour Scheme
- In designing the colour scheme for this website, I focused upon using various white, black and green colours, while the buttons and toast messages use a variety of colours (including blue, yellow and red) for hover, focus and active states. I ensured that these colours contrasted well in respect of the overall styling and would result in good readability and accessibility for the user, which I confirmed was in order through completing detailed testing on Google Lighthouse (accessibility = 100).

- The main colours that I used for the website are detailed in the colour chart below which I prepared on coolors.co;

![coolors](https://user-images.githubusercontent.com/71781554/129006075-7ac7e2a8-1d1c-49b6-a9d7-343a1b1e2cd8.png)

### Typography
- The Roboto font (which I downloaded from Google Fonts) is the main font used throughout the 
whole website, with Sans Serif as the fallback font in case for any reason the Roboto font fails to be 
imported correctly. I used this font because I liked its structure, easy to read style and modern appearance.
- As per its description on the Google Fonts website, Roboto has a mechanical skeleton and the forms are largely geometric, while at the same time, the font features friendly and open curves. It was designed by Christian Robertson, an interface designer at Google. 

### Imagery
- The imagery within the website is very focused upon the artworks that the site is selling. The home page has a large background image featuring a very colourful oil painting on a white canvas, which immediately captures the attention of the user. The About and Artists pages feature cards with images of the management team of Young Irish Artists and the artists represented in the site, and these give the user a visual representation of who these people are. The artworks page itself includes cards with images of the artworks so users can choose the style and design of what they wish to purchase, and there is a feature where the user can click into the artwork to see a full screen image (which opens in a new tab) and study it more carefully. Examples of images from the site are detailed below; 

Home Page:
![homepage](https://user-images.githubusercontent.com/71781554/129009918-c8f547e5-0cba-4a9b-b4d3-fcf1876bad8a.png)

Artists:
![artists](https://user-images.githubusercontent.com/71781554/129009728-9808bf0b-c27b-469a-82fe-cf5629d0d0f8.png)

Artwork Prints:
![artworks1](https://user-images.githubusercontent.com/71781554/129009737-0c8dac48-4d0d-42c0-a064-bfd0b0b36e29.png)

Team Members:
![team](https://user-images.githubusercontent.com/71781554/129009739-02c79674-f17d-4579-8c28-7955fa2f74ce.png)


### Wireframes
- My wireframes (for 10 pages) are saved to PDF and can be found [here](media/wireframes.pdf). I designed them at the start of the project and they served as the basis for this project. 
- In review, the wireframes stayed generally consistent with the finished design, however I did add jumbotron sections into several pages of the website, in order to provide more information to the user and to provide a button in order to keep the user returning to the artworks page, and in several places positioning and spacing of buttons, navigation links etc. also changed. 
- While building my website, I also prepared user stories (based on the structure of the User Stories prepared for the tutorial project), to examine how the user would progress through my site, and this is detailed in the chart below;

![userreview](https://user-images.githubusercontent.com/71781554/129694455-709f0c3e-1a9e-419d-b35f-8dbeda4926bc.png)

## Features
- The website is responsive on all device sizes (and has been tested through Chrome Dev Tools on various devices including iPhone 6/7/8, iPhone X, Galaxy S5, iPad and Desktop).
- The website has several interactive elements, including a large Bootstrap button on the Home, About and Artists pages which can be clicked to navigate to the Artworks page, and links in the card section for each artwork to go to the artists page and to see a specific category of art (e.g. pop art).   
- Each page in the website features a responsive Bootstrap navigation bar with the site logo featured to the left, a search bar in the centre top, the account and bag icons to the right, and the six page links below. Each page also contains a 3 column Bootstrap footer with a copyright message, address and contact information (email and phone). The pages contain the following features on various pages:
    - Home Page: Main background hero image (oil painting on a white canvas) with a large heading and a button to the Artworks page. 
    - About Page: A main jumbotron about section containing a link to the Artworks page, and 8 cards below detailing the management team of Young Irish Artists with their names and contact information.
    - Artworks Page: A main jumbotron section with filtering options, and cards below detailing the artworks on offer.
    - Art Styles Page: A main jumbotron section and cards below detailing the artworks on offer in respect of a certain style of art.
    - Specials Page: A main jumbotron section and cards below detailing the special offers on sale in respect of the artworks.
    - Artworks Detail Page: When an artworks is selected, a prominent image of the artwork with details and buttons to add the item to bag, increase quantity or keep shopping.
    - Shopping Bag Page: Details of the item to be purchased, as well as the cost information, and buttons to keep shopping or to continue to secure checkout.
    - Checkout Page: Form to the be filled out (with information already populated if logged in) in respect of address and card number, and details of the purchase. 
    - Success Page: Confirmation page that product has been purchased, which confirms that email has been sent to user and details of purchaser are clearly listed.
    - Artists Page: A main jumbotron artists section containing a link to the Artworks page, and 12 cards below detailing the artists represented by Young Irish Artists with their names and education information (college, graduation year).
    - Register Page: Form to be filled out in order to be registered, with two buttons allowing user to go back to login or to register.
    - Allauth Pages: Allauth has various pages relating to email verification, logout etc.
    - Login Page: Username and Password to be filled out in order login, with two buttons allowing user to go back to home page or to login.
    - My Profile Page: A page which details the user's autosaved delivery information and their previous order history.
    - 404 Error Page: A page with a heading "404 Error", a confirmation statement and link back to the homepage. 
    - 500 Error Page: A page with a heading "500 Error", a confirmation statement and link back to the homepage.
- Future features that could be considered for the website to expand its capability would be to implement a comment section in respect of the artworks and to include a monthly blog or newsletter email to users in respect of new artworks that have been recently added to the site. 

## Database Design

For the project I set up 7 database Models which you can see in the image below. I have also highlighted the relationships between the various models. I studied five models contained in the tutorial videos and updated, expanded and amended them to suit the requirements of an ecommerce art store, while I also added two fully custom models (Team and Artists), with fully customised python code. 

### Database 

![database](https://user-images.githubusercontent.com/71781554/129186496-36d89200-73c7-4565-8ab5-26d9c8e4af95.png)

## Technologies Used

### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks and Libraries and Programs Used

1. [Bootstrap 4](https://getbootstrap.com/): Bootstrap was utilised to assist with the responsiveness and styling of the website, specifically in respect of the Artists, Artworks and About pages.
2. [jQuery](https://jquery.com/): jQuery was used to assist with the bag, checkout and payment system functionality.
3. [Google Fonts](https://fonts.google.com/): Google fonts was utilised to import the ???Roboto??? font into the style.css file and this font is used on all pages throughout the website.
4. [Font Awesome](https://fontawesome.com/): Font Awesome was utilised in the Home, About and Artists pages, as well as in the footer, for aesthetic and UX purposes. I matched the icons with the activity 
or place that they most closely represented.
5. [Stripe](https://stripe.com/ie): Stripe was used for the payment system functionality.
6. [Django]( https://www.djangoproject.com/): The website was built using Django technology.
7. [Git](https://git-scm.com/): Git was used for version control throughout the project by utilizing the Gitpod terminal to Commit to git and Push to the GitHub repository.
8. [GitPod](https://www.gitpod.io/): Gitpod hosted the VSC IDE used for this project.
9. [PIP](https://pypi.org/project/pip/): PIP was used to install the tools needed in this project.
10. [Heroku](https://www.heroku.com/): Heroku was utilised to host and deploy my website.
11. [Visual Studio Code](https://code.visualstudio.com/): Visual Studio Code was the IDE used for developing this project.
12. [GitHub](https://github.com/): GitHub was used to store the code for the project after being pushed from Gitpod.
13. [AWS ??? S3]( https://aws.amazon.com/console/): I used Amazon S3 to store my static files.
14. [Favicon](https://en.wikipedia.org/wiki/Favicon): I used a Favicon image of the logo and added it to all of the pages.
15. [Free Image Optimiser](http://www.imageoptimizer.net/Pages/Home.aspx): I utilised a photo 
optimiser to ensure that the high-quality images that I used from the Unsplash website would load 
quicker.
16. [Balsamiq](https://balsamiq.com/): Balsamiq was used to create the wireframes during the initial design phase.
17. [Coolors](https://coolors.co/): I prepared the screenshot (included in this Readme) of the colours I had selected for this project using the Coolors template.

## Deployment

### How to Run This Project Locally

I created this project using Github, and wrote all of my code in Gitpod. I committed my code regularly to my Github repository, and after deploying the project to Heroku, I updated Heroku to complete automatic updates.

For this project you need to create a Stripe account for the checkout module, as well as an AWS account in order to store the static and media files (including all of the artwork, team and artists images).

This project can be run locally by completing the following steps:
(Note: I used Gitpod for development, so the following steps will be specific to Gitpod, but you can adjust them depending on your IDE). 

To clone the project you must complete the following steps:

1. From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can also clone the repository using the following command in your terminal:

```git clone https://github.com/JHR1986/johnhenryroche-ms4-youngirishartists.git```

2. Access the folder in your terminal window and install the application's link to required modules using the following command:

```pip3 install -r requirements.txt```

3. In your IDE, create a file called env.py which contains your environmental variables at the root level of the application. It will need to contain the following lines and variables:

``` 
import os

os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
os.environ["DEVELOPMENT"] = "True"

os.environ["DEFAULT_FROM_EMAIL"] = 'DEFAULT_FROM_EMAIL'

os.environ["STRIPE_PUBLIC_KEY"] = "STRIPE_PUBLIC_KEY"
os.environ["STRIPE_SECRET_KEY"] = "STRIPE_SECRET_KEY"
os.environ["STRIPE_WH_SECRET"] = "STRIPE_WH_SECRET"
```
If you are not sure how to get the above Stripe variables, please visit the Stripe Documentation for guidance. 

Also, if you are planning to push this application to a public repository, please ensure that env.py is added to your .gitignore file.

4. Migrate the database models with the following terminal command: 

```python3 manage.py migrate```

5. Create a superuser account and set up your credentials with the following command: 

```python3 manage.py createsuperuser```

6. Run the app with the following command: 

```python manage.py runserver```

The address to access the website will then be displayed in the terminal. You can then add /admin to the end of the url to access the admin panel with your superuser credentials.

### Heroku Deployment

1. Login to your Heroku account and create a new app. You can then choose your region (I used Europe).

2. Once the app is created, click on the Resources button and under Add-ons, look for the Heroku Postgres to attach a postgres database to your project, as the SQLite database that was originally used will no longer be used for the deployed version. Select the Hobby Dev - Free plan and click 'Submit Order Form'.

3. Scroll back up the page and click "settings". Scroll down and click "Reveal Config Vars". Then set up the same variables as in your env.py (as detailed below). Note: You should not set the DEBUG variable in config vars in Heroku in order to prevent DEBUG being active on the live website.

```
AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"

DATABASE_URL = "This variable is automatically set when adding the Postgres Add on"

SECRET_KEY = "SECRET_KEY"

STRIPE_PUBLIC_KEY = "STRIPE_PUBLIC_KEY"
STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
STRIPE_WH_SECRET = "STRIPE_WH_SECRET"

DEFAULT_FROM_EMAIL = "DEFAULT_FROM_EMAIL"
EMAIL_HOST_PASS = "EMAIL_HOST_PASS"
EMAIL_HOST_USER = "EMAIL_HOST_USER"
USE_AWS = "True"
```

4. From this screen, copy the value of DATABASE_URL.

5. After this, go to your settings.py file to the young_irish_artists directory and comment out the default database configuration and add:

``` 
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('Put your DATABASE_URL here'))
} 

```

6. Migrate again with the following command:

```python3 manage.py migrate```

7. Create a superuser account for the postgres database, so that you can have access to the django admin section by setting up the credentials with the following command:

```python3 manage.py createsuperuser```

Note: Do not forget to login to the admin page and check the boxes 'Verified and Primary"

8. Load the data into your newly created database. I added all of my database items manually, as I had only created a few examples in the SQLite database, but I could load the new items into a json file which would be available for use.

9. After migrations are complete, change the database configurations to:
```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```
This set up will allow your site to use Postgres in deployment and SQLite in development.

1. Make sure that you have your requirements.txt file and your Procfile. 
In case you do not have them set up, follow the below steps: 

Requirements:
``` pip3 freeze --local > requirements.txt ```

Procfile:
``` echo web: python app.py > Procfile ```

2. The Procfile should contain the following line so that it knows which program to run:

``` web: gunicorn <project_name>.wsgi:application ```

3. Add your files and commit them to Github by running the following commands:

```
git add . 
git commit -m "Your commit message"
git push
```

4. Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file.

5. Disable collect static so that Heroku does not try to collect static files when you deploy by typing the following command in the terminal;

``` heroku config:set DISABLE_COLLECTSTATIC=1 ```

6. Go back to Heroku and click "Deploy" in the navigation.

7. Scroll down to Deployment method and Select Github.

8. Look for your repository (Young Irish Artists) and click connect.

9. Under the automatic deploys section, click 'Enable automatic deploys'.

10. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.

11. In order to commit your changes to the branch, use Git Push to push your changes to Github and Heroku.

12. Store your static files and media files in AWS.

13. Set up your email service to send confirmation emails and user verification emails to the users of the site when they register and make a purchase. You can do this process by following the next steps (this process is for Gmail accounts only);

- Go to your email account and go to your account settings.
- Under Security, scroll down to Signing in to Google and make sure that the 2 step verification functionality is turned on.
- Under the same heading (Signing in to Google) you will see the 'App Passwords' option.
- Click on the option, select mail for the app and under device type select 'other' and fill in 'Django'.
- You will now receive a password which you should copy and set it as a Config Variable in Heroku:
```
    EMAIL_HOST_PASS = 'Password you just copied'
    EMAIL_HOST_USER = 'Your gmail account'
```
- Go to your settings.py in the Young Irish Artists directory and add the following:
```
    if "DEVELOPMENT" in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
```
- Your email functionality has now been set up.

## Testing

- Testing information for this project can be found in the separate Testing File [here](testing.md). 

## Credits
### Code
- I studied a comment by Naoise Gaffney on Code Institute's Slack channel in respect of how to correctly set up the 404 & 500 error pages for a Django project.
- I studied a comment by Ed B_alum on Code Institute's Slack channel in respect of resolving an issue I had when trying to login to Heroku through the CLI before launching my Heroku app. 
- On the recommendation of my tutor, I studied Anouk Smet's MS4 Readme (Casa Pedra Nobre), in respect of its structure and layout, especially in respect of the deployment section. 
- I used the Bootstrap Library throughout the project to make the site more responsive through using the Bootstrap Grid System and employing Bootstrap elements for the Navbar, Footer, Jumbotron and Cards.
- I studied in detail the videos and code for the Code Institute Django Project (Boutique Ado) presented by Chris Zielinski while completing my website, in order to get a clear understanding of how the various elements of Django, Stripe and AWS work, and how to implement a fully functioning Django website. While studying the structure of Chris' site, I at all times tried to use my own ideas, styling and custom models, while completing the coding in order to create my art ecommerce website. I followed Chris's code closely in respect of the checkout and Stripe payments section, as I had not encountered this functionality previously on the course.  


### Content
- All content within this project was written by the developer.

### Media
- The images used in this project (in respect of the Home, About, Artists and Artworks pages) have all been sourced from Unsplash, which is a stock photography site which contains a large catalogue of high quality free to use images which are not the subject of copyright. To improve the speed of the site, all of the images were put through an image optimiser. 

### Acknowledgements
- I wish to thank my Mentor, Maranatha Ilesanmi for providing me with excellent feedback and support throughout all of the four projects for this course, which really helped my overall coding confidence. 
- I also wish to thank Tutor Support, Student Care and the Slack Community at Code Institute for their support and advice during the whole course, and especially while working on my MS4 project when I had any queries.
