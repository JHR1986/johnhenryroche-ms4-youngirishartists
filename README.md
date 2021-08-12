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
- My general site map and wireframes are saved to PDF and can be found [here](media/wireframes.pdf). I designed them at the start of the project and they served as the basis for this project. 
- In review, the wireframes stayed generally consistent with the finished design (in respect of the Home page, About Page, Artworks page, Artists page, Specials page, Login page and Register page), however I did add jumbotron sections into several pages of the website, in order to provide more information to the user and to provide a button for going to the artworks page.
- While building my website, I also prepared user stories (based on the structure of the User Stories prepared for the tutorial project), to examine how the user would progress through my site, and this is detailed in the chart below;
![userstories](https://user-images.githubusercontent.com/71781554/129165735-a5bbba96-b755-44e0-909c-5ab58e7d766d.png)

## Features
- The website is responsive on all device sizes (and has been tested through Chrome Dev Tools on various devices including iPhone 6/7/8, iPhone X, Galaxy S5, iPad and Desktop).
- The website has several interactive elements, including a large Bootstrap button on the Home, About and Artists pages which can be clicked to navigate to the Artworks page, and links in the card section for each artwork to go to the artists page and to see a specific category of art (e.g. pop art).   
- Each page in the website features a responsive Bootstrap navigation bar with the site logo featured to the left, a search bar in the centre top, the account and bag icons to the right, and the six page links below. Each page also contains a 3 column Bootstrap footer with a copyright message, address and contact information (email and phone). The pages contain the following features on various pages:
    - Home Page: Main background hero image (oil painting on a white canvas) with a large heading and a button to the Artworks page. 
    - About Page: A main jumbotron about section containing a link to the Artworks page, and 8 cards below detailing the management team of Young Irish Artists with their names and contact information.
    - Artworks Page: A main jumbotron section with filtering options, and cards below detailing the artworks on offer.
    - Art Styles Page: A main jumbotron section and cards below detailing the artworks on offer in respect of a certain style of art.
    - Art Styles Page: A main jumbotron section and cards below detailing the special offers on sale in respect of the artworks.
    - Artworks Detail Page: When an artworks is selected, a prominent image of the artwork with details and buttons to add the item to bag, increase quantity or keep shopping.
    - Shopping Bag Page: Details of the item to be purhased, as well as the cost information, and buttons to keep shopping or to continue to secure checkout.
    - Checkout Page: Form to the be filled out (with information already populated if logged in) in respect of address and card number, and details of the purchase. 
    - Success Page: Confirmation page that product has been purhcased, which confirms that email has been sent to user and details of purchaser are clearly listed.
    - A main jumbotron artists section containing a link to the Artworks page, and 12 cards below detailing the artists represented by Young Irish Artists with their names and education information (college, graduation year).
    - Register Page: Form to be filled out in order to be registered, with two buttons allowing user to go back to login or to register.
    - Allauth Pages: Allauth has various pages relating to email verification, logout etc.
    - Login Page: Username and Password to be filled out in order login, with two buttons allowing user to go back to home page or to login.
    - 404 Error Page: A page with a heading "404 Error", a confirmation statement and link back to the homepage. 
    - 500 Error Page: A page with a heading "500 Error", a confirmation statement and link back to the homepage. 

## Database Design

For the project I set up 7 database Models which you can see in the image below. I have also highlighted the relationships between the various models.

![database](https://user-images.githubusercontent.com/71781554/129186496-36d89200-73c7-4565-8ab5-26d9c8e4af95.png)



## Technologies Used

### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks and Libraries and Programs Used

1. [Bootstrap 4](https://getbootstrap.com/): Bootstrap was utilised to assist with the responsiveness and styling of the website, specifically in respect of the Artists, Products and About pages.
2. [jQuery](https://jquery.com/): jQuery was used to assist with the bag, checkout and payment system functionality.
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
16. [Balsamiq](https://balsamiq.com/): Balsamiq was used to create the wireframes during the initial design phase.
17. [Coolors](https://coolors.co/): I prepared the screenshot (included in this Readme) of the colours I had selected for this project using the Coolors template.

## Testing

- Testing information for this project can be found in the separate Testing File [here](testing.md). 

## Credits
### Code
- I studied a comment by Naoise Gaffney on Code Institute's Slack channel in respect of how to correctly set up the 404 & 500 error pages for a Django project.
- I studied a comment by Ed B_alum on Code Institute's Slack channel in respect of resolving an issue I had when trying to login to Heroku through the CLI before launching my Heroku app. 
- On the recommendation of my tutor, I studied Anouk Smet's MS4 Readme (Casa Pedra Nobre), in respect of its structure and layout, especially in respect of the deployment section. 
- I used the Bootstrap Library throughout the project to make the site more responsive through using the Bootstrap Grid System and employing Bootstrap elements for the Navbar, Footer, Jumbotron and Cards.
- I studied in detail the videos and code for the Code Institute Django Project (Boutique Ado) presented by Chris Zielinski while completing my website, in order to get a clear understanding of how the various elements of Django, Stripe and AWS work, and how to implement a fully functioning Django website. While following the structure of Chris' site, I at all time tried to integrate my own ideas, styling and custom models, while completing my coding. I followed Chris's code closely in respect of the Stripe payments section, as I had not encountered this functionality previously.  


### Content
- All content within this project was written by the developer.

### Media
- The images used in this project (in respect of the Home, About, Artists and Artworks pages) have all been sourced from Unsplash, which is a stock photography site which contains a large catalogue of high quality free to use images which are not the subject of copyright. To improve the speed of the site, all of the images were put through an image optimiser. 

### Acknowledgements
- I wish to thank my Mentor, Maranatha Ilesanmi for providing me with excellent feedback and support throughout all of the four projects for this course, which really helped my overall coding confidence. 
- I also wish to thank Tutor Support, Student Care and the Slack Community at Code Institute for their support and advice during the whole course, and especially while working on my MS4 project when I had any queries.
