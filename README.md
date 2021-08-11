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
  * [Flowchart](#flowchart)
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

This project comprises the development of a fictional ecommerce website where users can purchase prints by exciting new artists based in Ireland working in a range of painting styles. The website also provides a helpful platform for recently graduated artists to gain exposure and recognition of their recent work. The website allows the user to create a profile when they are making a purchase so that they have an account through which they can see their history of purchases and load their information in order to make future orders easier. There is also a super user profile through which products can be amended through CRUD (Create, Read, Update and Delete) features. In respect of the overall construction of this website, it has been designed to be fully responsive, intuitive and accessible on a range of media devices (e.g. mobile, tablet and desktop), in order to make it as easy as possible for users of the website to navigate it and make their required purchases.   

Photo of Site Represented on Various Media to highlight responsive design:

![responsive](https://user-images.githubusercontent.com/71781554/129000316-423d15a7-d1c1-4e98-9483-e8c28c0fe85b.png)

## User Experience 

### User Stories

### First Time Visitor Goals
1.  As a First Time Visitor, I want to quickly confirm what products the ecommerce website is selling (e.g. art prints).
2.  As a First Time Visitor, I want to be able to easily browse through the site pages (including About and Artists) and view the artworks that are on offer.
3.  As a First Time Visitor, I want to be able to go to the Register page and create my own account if I am considering making a purchase.

### Returning Visitor Goals
1.  As a Returning Visitor, I want to be able to be able to make purchases of art prints easily and effortlessly, as I have an account and my information will be pre-loaded to save me time. 
2.  As a Returning Visitor, I want to be able to filter my searches for artworks by genre, price, rating or specials, in order that I can purchase the artworks that best suit my taste and price range. 

### Frequent Visitor Goals
1. As a Frequent/Returning Visitor, I want to be able to easily contact Young Irish Artists if there has been any issue with my purchase, and the contact information is clearly highlighted in the Footer Section of the site. 
2. As a Frequent/Returning Visitor, I want to be able to see new artists that have joined the site and the new artworks that they have produced, as the artworks on offer will be updated on a regular basis.

## Design

### Colour Scheme
- In designing the colour scheme for this website, I focused upon using various white, black and green colours, while the buttons and toasts used a variety of colours (including blue, yellow and red) for hover, focus and active states. I ensured that these colours contrasted well in respect of the overall styling and would result in good readability and accessibility for the user, which I confirmed was in order through completing detailed testing on Google Lighthouse.

- The main colours that I used for the website are detailed in the colour chart below which I prepared on coolors.co;

![coolors](https://user-images.githubusercontent.com/71781554/129006075-7ac7e2a8-1d1c-49b6-a9d7-343a1b1e2cd8.png)

### Typography
- The Roboto font (which I downloaded from Google Fonts) is the main font used throughout the 
whole website, with Sans Serif as the fallback font in case for any reason the Roboto font fails to be 
imported correctly.
- As per its description on the Google Fonts website, Roboto has a mechanical skeleton and the forms are largely geometric, while at the same time, the font features friendly and open curves. It was designed by Christian Robertson, an interface designer at Google. 

### Imagery
- The imagery within the website is very focused upon the artworks that the site is selling. The home page has a large background image featuring a very colourful oil painting on a white canvas, which immediately captures the attention of the user. The About and Artists pages feature cards with images of the management team of Young Irish Artists and the artists represented in the site, and these give the user a visual representation of who these people are. The artworks page itself includes cards with images of the artworks so users can choose the style and design of what they wish to purchase, and there is a feature where the user can click into the artwork to see a full screen image and study it more carefully. Examples of images from the site are detailed below; 

![homepage](https://user-images.githubusercontent.com/71781554/129009918-c8f547e5-0cba-4a9b-b4d3-fcf1876bad8a.png)

![artists](https://user-images.githubusercontent.com/71781554/129009728-9808bf0b-c27b-469a-82fe-cf5629d0d0f8.png)

![artworks1](https://user-images.githubusercontent.com/71781554/129009737-0c8dac48-4d0d-42c0-a064-bfd0b0b36e29.png)

![team](https://user-images.githubusercontent.com/71781554/129009739-02c79674-f17d-4579-8c28-7955fa2f74ce.png)


### Wireframes
- My general site map and wireframes are saved to PDF and can be found [here](static/images/wireframes.pdf). I designed them at the start of the project and they served as the basis for this project. 
- In review, the wireframes stayed generally consistent with the finished design (in respect of the Home page, Phrases page, Login page and Register page). While completing the wireframes at the start of the project, I was not aware that my project would also require additional html pages in respect of the CRUD features (Profile, Add Phrase, Edit Phrase) and errors (404, 500) so these pages were not included in the original wireframes. I queried this point on the Slack channel and was advised to keep the original wireframes as they are (as they are a reflection of what my original design plan was), while optionally creating a 2nd wireframes file relating to the additional html pages. I took this advice and the wireframes for the additional 5 html pages are located [here](static/images/wireframes2.pdf).

## Features
- The website is responsive on all device sizes (and has been tested through Chrome Dev Tools on various devices including iPhone 6, iPhone X, Galaxy S5, iPad and Desktop).
- The website has several interactive elements, including three Bootstrap buttons on the home page which can be clicked to navigate to the Phrases, Login and Register pages, while there are further call to action buttons in the Add Phrase, Edit Phrase, Profile, Login, Register and Error pages. 
- Each page in the website features a responsive Bootstrap navigation bar with the site logo featured to the left and the four page links to the right (with the active page highlighted), and these pages also each contain a 3 column Bootstrap footer with a copyright message, address and contact information (email and phone). The pages contain the following features on various pages:
    - Home Page: A main jumbotron introductory section, three images relating to links to the Phrases, Login and Register pages, and two images of Korean culture and architecture. 
    - Phrases Page: A main search box at the top of the page with two buttons (reset and search), and the list of phrases below them. When logged in, the user has access to edit and delete buttons in respect of phrases which they have added.
    - Login Page: Main background hero image with a login box in the centre where users can enter their username and password, and press a login button below, as well as a link to the Register page. 
    - Register Page: Main background hero image with a registration box in the centre where users can enter their username and passeword, and press a register button below, as well as a link to the Login page for current users. 
    - Profile Page: A main jumbotron section, with two cards below with links to the Phrases and Add Phrase pages, as well as a background hero image.
    - Add Task Page: Main background hero image with an add phrase box in the centre where users can enter their phrase category, English phrase, Korean phrase and fun fact about Korean, and press an add phrase button below.
    - Edit Task Page: Main background hero image with an edit phrase box in the centre where users can edit their phrase category, English phrase, Korean phrase and fun fact about Korea, and press either the edit phrase or cancel buttons below.
    - 404 Error Page: A page with a heading "404 Error", a confirmation statement "Something went wrong" and link back to the homepage, as well as a hero image below this text. 
    - 500 Error Page: A page with a heading "500 Error", a confirmation statement "Something went wrong" and link back to the homepage, as well as a hero image below this text. 

## Database Design

- I used MongoDB as the database program for this project, and the plan of the database (which I named task_manager) is detailed below;

![database](https://user-images.githubusercontent.com/71781554/121675310-268e2400-caab-11eb-9767-8b6aa37303f8.png)

There are three collections titled "Categories", "Phrases" and "Users", and I also created an Index relating to the search function for English and Korean phrases in the phrases page.

The code for this project relating to interaction with the MongoDB database is outlined below;
1. Getting the list of phrases saved to database:
```
# App route for Phrases page
@app.route("/get_phrases")
def get_phrases():
    phrases = list(mongo.db.phrases.find())
    return render_template("phrases.html", phrases=phrases, page="get_phrases")
```
2. Searching for English or Korean phrases:
```
# App route for search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    phrases = list(mongo.db.phrases.find({"$text": {"$search": query}}))
    return render_template("phrases.html", phrases=phrases)
```
3. Checking if username already exists in respect of Register page:
```
# App route for register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
```
4. Checking if username already exists in respect of Login page:
```
# App route for login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
```
5. Grabbing username from database for login to Profile page:
```
# App route for profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, page="profile")

    return redirect(url_for("login"))
```
6. Adding new phrase to database:
```
# App route for add phrase page
@app.route("/add_phrase", methods=["GET", "POST"])
def add_phrase():
    if request.method == "POST":
        phrase = {
            "category_name": request.form.get("category_name"),
            "english_name": request.form.get("english_name"),
            "korean_name": request.form.get("korean_name"),
            "brief_description": request.form.get("brief_description"),
            "created_by": session["user"],
        }
        mongo.db.phrases.insert_one(phrase)
        flash("Phrase Successfully Added!")
        return redirect(url_for("get_phrases"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_phrase.html", categories=categories, page="add_phrase")
```
7. Editing phrase in database:
```
# App route for edit phrase page
@app.route("/edit_phrase/<phrase_id>", methods=["GET", "POST"])
def edit_phrase(phrase_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "english_name": request.form.get("english_name"),
            "korean_name": request.form.get("korean_name"),
            "brief_description": request.form.get("brief_description"),
            "created_by": session["user"],
        }
        mongo.db.phrases.update({"_id": ObjectId(phrase_id)}, submit)
        flash("Phrase Successfully Updated!")

    phrase = mongo.db.phrases.find_one({"_id": ObjectId(phrase_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_phrase.html", phrase=phrase, categories=categories)
```
8. Deleting phrase from database:
```
# App route for delete phrase function
@app.route("/delete_phrase/<phrase_id>")
def delete_phrase(phrase_id):
    mongo.db.phrases.remove({"_id": ObjectId(phrase_id)})
    flash("Phrase Successfully Deleted!")
    return redirect(url_for("get_phrases"))
```
## Technologies Used

### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks and Libraries and Programs Used

1. [Bootstrap 4](https://getbootstrap.com/): Bootstrap was utilised to assist with the responsiveness and styling of the website, specifically in respect of the Artists, Products and About pages.
2. [jQuery] (https://jquery.com/): jQuery was used to assist with the bag, checkout and payment system functionality.
3. [Google Fonts](https://fonts.google.com/): Google fonts was utilised to import the ‘Roboto’ font into the style.css file and this font is used on all pages throughout the website.
4. [Font Awesome](https://fontawesome.com/): Font Awesome was utilised in the About and Artists, as well as in the footer, for aesthetic and UX purposes. I matched the icons with the activity 
or place that they most closely represented.
5. [Stripe](https://stripe.com/ie): Stripe was used for the payment system functionality.
6. [Django]( https://www.djangoproject.com/): The website was built using Django technology.
7. [Git](https://git-scm.com/): Git was used for version control throughout the project by utilizing the Gitpod terminal to Commit to git and Push to the GitHub repository.
8. [GitPod](https://www.gitpod.io/): Gitpod hosted the VSC IDE used for this project.
9. [PIP](https://pypi.org/project/pip/): PIP was used to install the tools needed in this project.
10. [Heroku](https://www.heroku.com/): Heroku was utilised to host and deploy my website.
11. [Visual Studio Code](https://code.visualstudio.com/): Visual Studio Code was the IDE used for developing this project.
12. [GitHub](https://github.com/): GitHub was used to store the code for the project after being pushed from Gitpod.
13. [AWS – S3]( https://aws.amazon.com/console/): I used Amazon S3 to store my static files.
14. [Favicon](https://en.wikipedia.org/wiki/Favicon): I used a Favicon image of the logo and added it to all of the pages.
15. [Free Image Optimiser](http://www.imageoptimizer.net/Pages/Home.aspx): I utilised a photo 
optimiser to ensure that the high-quality images that I used from the Unsplash website would load 
quicker.
16. [Balsamiq](link to balsamiq): Balsamiq was used to create the wireframes during the initial design phase.
17. [Coolors](https://coolors.co/): I prepared the screenshot (included in this Readme) of the colours I had selected for this project using the Coolors template.

## Testing

- Testing information for this project can be found in the separate Testing File [here](testing.md). 

## Deployment

### How to run this project locally

I have created the project using Github, from there I used Gitpod to write my code. Then I used commits to git followed by "git push" to my GitHub repository. I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku.
For this project you need to create an account on Stripe for the reservation module as well as an account on AWS in order to store your static and media files.
This project can be ran locally by following the following steps: I used Gitpod for development, so the following steps will be specific to Gitpod. You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments here
To clone the project:
1.	From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal:
2.	git clone https://github.com/AnoukSmet/Casa-Pedra-Nobre.git
3.	Access the folder in your terminal window and install the application's link to required modules using the following command:
4.	pip3 install -r requirements.txt
5.	In your IDE, create a file containing your environmental variables called env.py at the root level of the application. It will need to contain the following lines and variables:
6.	import os
7.	
8.	os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
9.	os.environ["DEVELOPMENT"] = "True"
10.	
11.	os.environ["DEFAULT_FROM_EMAIL"] = 'DEFAULT_FROM_EMAIL'
12.	
13.	os.environ["STRIPE_PUBLIC_KEY"] = "STRIPE_PUBLIC_KEY"
14.	os.environ["STRIPE_SECRET_KEY"] = "STRIPE_SECRET_KEY"
15.	os.environ["STRIPE_WH_SECRET"] = "STRIPE_WH_SECRET"
16.	os.environ["STRIPE_CURRENCY"] = "EUR"
17.	
If you're not sure how to get the above Stripe variables, please visit the Stripe Documentation
If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.
18.	Migrate the database models with the following command
19.	python3 manage.py migrate
20.	Create a superuser and set up the credentials with the following command
21.	python3 manage.py createsuperuser
22.	Run the app with the following command
23.	python manage.py runserver
The address to access the website is displayed in the terminal
Add /admin to the end to access the admin panel with your superuser credentials

### Heroku Deployment

1.	Login to your Heroku account and create a new app. Choose your region.
2.	Once the app is created click on the resources button and under Add-ons, look for the Heroku Postgres to attach a postgres database to your project. Select the Hobby Dev - Free plan and click 'Submit order form'
 
3.	Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (): !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website.
4.	AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
5.	AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
6.	AWS_S3_REGION_NAME = "AWS_S3_REGION_NAME"
7.	AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"
8.	USE_AWS = True
9.	
10.	DATABASE_URL = "This variable is automatically set when adding the Postgres Add on"
11.	
12.	SECRET_KEY = "SECRET_KEY"
13.	
14.	STRIPE_PUBLIC_KEY = "STRIPE_PUBLIC_KEY"
15.	STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
16.	STRIPE_WH_SECRET = "STRIPE_WH_SECRET"
17.	STRIPE_CURRENCY = EUR
18.	
19.	DEFAULT_FROM_EMAIL = "DEFAULT_FROM_EMAIL"
20.	EMAIL_HOST = "smtp.gmail.com"
21.	EMAIL_HOST_PASS = "EMAIL_HOST_PASS"
22.	EMAIL_HOST_USER = "EMAIL_HOST_USER"
23.	EMAIL_PORT = 587
24.	EMAIL_USE_TLS = True
25.	From this screen, copy the value of DATABASE_URL
26.	After this go to your settings.py the casa_pedra_nobre directory and comment out the default database configuration and add:
27.	DATABASES = {
28.	    'default': dj_database_url.parse('Put your DATABASE_URL here'))
29.	}
30.	Migrate again with the following command
31.	python3 manage.py migrate
32.	Create a superuser for the postgres database so you can have access to the django admin by setting up the credentials with the following command
33.	python3 manage.py createsuperuser
--> Don't forget to login to the admin page and check the boxes 'Verified and primary"
34.	Load the data into your newly created database by using the following command:
35.	python3 manage.py loaddata <name of file containing the data *>
o	tourist_info_datadump.json
o	home_datadump.json
o	rooms_datadump.json
o	gallery_datadump.json
36.	After migrations are complete, change database configurations to:
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
This set up will allow your site to use Postgres in deployment and sqlite3 in development.
1.	Make sure you have your requirements.txt file and your Procfile. In case you don't, follow the below steps: Requirements:
2.	pip3 freeze --local > requirements.txt
Procfile:
echo web: python app.py > Procfile
3.	The Procfile should contain the following line:
4.	web: gunicorn <project_name>.wsgi:application
5.	
6.	Add your files and commit them to GITHUB by running the following commands:
7.	git add . 
8.	git commit -m "Your commit message"
9.	git push
10.	Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file
11.	Disable collect static so that Heroku doesn't try to collect static files when you deploy by typing the following command in the terminal
12.	heroku config:set DISABLE_COLLECTSTATIC=1
13.	Go back to HEROKU and click "Deploy" in the navigation.
14.	Scroll down to Deployment method and Select Github.
15.	Look for your repository and click connect.
16.	Under automatic deploys, click 'Enable automatic deploys'
17.	Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
18.	In order to commit your changes to the branch, use git push to push your changes.
19.	Store your static files and media files on AWS. You can find more information about this on Amazon S3 Documentation. If you would like to follow a tutorial instead, visit this tutorial on Youtube from Amazon Web Services
20.	Set up email service to send confirmation email and user verification email to the users. You can do this by following the next steps (Gmail only)
(Be aware that this migth be different for other providers or the process might have changed over time)
•	Go to your email account and go to your account settings
•	Under Security, scroll down to Signing in to Google and make sure 2 step verification is turned on
•	Under the same heading (Signing in to Google) you will see the 'App passwords' option.
•	Click on the option, select mail for the app and under device type select other and fill in 'Django'
•	You will now get a password which you should copy and set it as a config variable in Heroku:
    EMAIL_HOST_PASS = 'Password you just copied'
    EMAIL_HOST_USER = 'Your gmail account
•	Go to your settings.py in casa_pedra_nobre directory and add the following:
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

## Credits
### Code
- [Change input field to green when correct number of characters entered](https://stackoverflow.com/questions/39540302/how-to-change-the-background-color-of-an-input-field-when-text-is-entered): I studied this post in order to fully understand how to change the input field green when a correct number of valid characters had been entered, to assist with the overall validation process for my form sections.
- [Validation system for form entries](https://mdbootstrap.com/docs/b4/jquery/forms/validation/): I studied this validation feature from mdbootstrap (including a JS file) and amended it for use in my project in respect of the form sections in the Phrases, Add Phrase, Edit Phrase, Login and Register pages. 
- [Show active page when using Flask and Jinja](https://stackoverflow.com/questions/55895502/dynamically-setting-active-class-with-flask-and-jinja2): I wished to ensure that the page currently clicked on was underlined as active in the Navbar. To achieve this while using Flask, I followed the instructions listed in this Stackoverflow post. 
- I studied a comment by Ed Bradley (Ed B) on Code Institute's Slack channel in respect of how to correctly set up the 404 & 500 error pages for Python and Flask.
- I used the Bootstrap Library throughout the project to make the site more responsive through using the Bootstrap Grid System and employing Bootstrap elements for the Navbar, Footer, Jumbotron, Cards and Forms.
- I studied in detail the videos for the Code Institute mini project presented by Tim Nelson prior to starting my website, in order to get a clear understanding of how both Flask and MongoDB operate, and how to implement a fully functioning CRUD system.

### Content
- All content within this project was written by the developer.

### Media
- The images used in this project have all been sourced from Unsplash, which is a stock photography site which contains a large catalogue of high quality free to use images which are not the subject of copyright. 

### Acknowledgements
- I wish to thank my Mentor, Maranatha Ilesanmi for providing me with excellent feedback and support throughout all of the four projects for this course.
- I also wish to thank Tutor Support, Student Care and the Slack Community at Code Institute for their support and advice during the whole course, and especially while working on my MS4 project.

