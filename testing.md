# Young Irish Artists Website - Testing details

## [Main Readme File](README.md).

[View the Live Website Here](https://jhroche-young-irish-artists.herokuapp.com/)

- [Testing](#testing)
  * [Client Stories Testing](#client-stories-testing)
  * [Testing Client Stories from UX Section of Main Readme File](#testing-client-stories-from-ux-section-of-main-readme-file)
    + [First Time Visitor Goals](#first-time-visitor-goals)
    + [Returning Visitor Goals](#returning-visitor-goals)
    + [Frequent Visitor Goals](#frequent-visitor-goals)
  * [Manual Logical Testing of all Elements and Functionality on every Page](#manual-logical-testing-of-all-elements-and-functionality-on-every-page)
    + [Home Page](#home-page)
    + [Register Page](#register-page)
    + [Login Page](#login-page)
    + [About Page](#register-page)
    + [Artworks Page](#artworks-page)
    + [Artworks Details Page](#artworks-details-page)
    + [Bag Page](#bag-page)
    + [Checkout Page](#checkout-page)
    + [Artists Page](#artists-page)
    + [SuperUser](#superuser)
    + [Additional HTML Pages](#additional-html-pages)
- [Further Testing](#further-testing)
  * [Further Testing Details](#further-testing-details)
  * [Known Bugs](#known-bugs)

## Testing
- The W3C Markup Validator and W3C CSS Validator Services were used to validate the pages of the project in order to ensure that the code was clear and clean. I used the source code of the website pages in order that the django code would be correctly rendered for the validator.

![htmlvalid](https://user-images.githubusercontent.com/71781554/129475077-fe39eaa7-9955-4157-a26e-722cd5a5e9ed.png)

![cssvalid](https://user-images.githubusercontent.com/71781554/129475075-19174bc0-83d9-4fe7-8f17-8529eaf04ec1.png)

- I tested and added comments to every HTML, CSS, Javascript file (JSHint) and every Python file (Pep8Online) in the project to ensure everything about my code was in order and clean, and my review of same is detailed in the list below;

![filereview](https://user-images.githubusercontent.com/71781554/129475076-1924d390-32cd-4c0f-b1e7-f13cb93c33cf.png)

- In order to confirm that the site has very good accessibility, I ensured that alt tags were added to all images. The site scored an accessibility score of 100 in the Google Lighthouse review (see Further Testing section below). 

### Client Stories Testing
The most direct path through the website is as follows:
- Home – Artworks – Login (if a user) or Register (if not a user).
- On the Home page, the user is presented with a prominent call to action button (as detailed below); 
    1. "Browse Artworks": From Home – Artworks
- On the About page, the user can read about the site, click a button to go to the Artworks, view the Website Team and use the navbar to go to different pages.
- On the Artworks page, the user can view all of the artworks for sale, with the option of filtering them by Price, Name, Rating and Category. There is also a navbar link to Art Styles, where the user can browse the artworks by their style of painting (e.g. Pop Art or Watercolours), and to Specials where users can browse new arrivals or deals in respect of the Artworks.
- On the Artists page, the user can read about the artists, click a button to go to the Artworks, view the Artist Profiles and use the navbar to go to different pages.
- On all of the pages, there is a search bar located in the navbar, which enables the user to search for artworks either by artist or artwork name.
- On the Home Page, there is a My Account button in the navbar, which when clicked allows the user to either login if they have an account or to register if they do not. To register, the user receives a verification email. 
- When a product is selected, it is added to the bag page, from which the user can progress to the checkout page and then make their payment. When payment is made the user receives an email confirming the purchase and they also can see their orders when signed in.
- When the user logs out, they must click a logout button and they are no longer logged in.

The information in the site is purposefully kept very structured and concise, in order that it is very easy to follow and the user does not feel overwhelmed with details.


### Testing Client Stories from UX Section of Main Readme File

#### First Time Visitor Goals
1.  As a First Time Visitor, I want to quickly confirm what products the ecommerce website is selling (e.g. art prints).
- The Home page has a general synopsis of the purpose of the website and a striking background image of a colourful artwork on a blank canvas, and there is a prominent navigation bar for clicking to the About, Artworks (Artworks, Artwork Styles, Specials) and Artists pages. 
2.  As a First Time Visitor, I want to be able to easily browse through the site pages (including About and Artists) and view the artworks that are on offer.
- The navbar is easy to understand and offers users the opportunity to easily browse through the site pages. The Home, About and Artists pages each feature a prominent call to action button to return the user to the Artworks page, while there is also a search bar located in the centre of the navbar for searching by artist or artwork name. 
3.  As a First Time Visitor, I want to be able to go to the Register page and create my own account if I am considering making a purchase.
- The My Account button on the home page drops down to a login and register link. When the register link is selected, the user enters their email, username and password to create an account. 

#### Returning Visitor Goals
1.  As a Returning Visitor, I want to be able make purchases of art prints easily and efficiently, as I now have an account and my information (e.g. billing and shipping) will be pre-loaded. 
- When an artwork is selected, the user is brought through to a more detailed page describing the artwork. They then have the option to include the quantity and add it to their bag. The system is very user friendly going from product to bag to checkout in a manner of clicks, while allowing the user to remove the product if they change their mind and to continue shopping. 
2.  As a Returning Visitor, I want to be able to filter my searches for artworks by categories including genre, price, rating or specials, in order that I can purchase the artworks that best suit my preference and price range. 
- The navbar and the main artworks page allows the user to filter the products by price, rating, category, style and special offers, in descending/ascending or alphabetical order.  

#### Frequent Visitor Goals
1. As a Frequent/Returning Visitor, I want to be able to easily contact Young Irish Artists if there has been any issue with my purchase, and the contact information is clearly highlighted in the Footer Section of the site. 
- The footer to each of the html pages lists the site's address in Dublin, their opening hours and phone/email address, so that any subsequent queries can be addressed to the site owners.
2. As a Frequent/Returning Visitor, I want to be able to see new artists that have joined the site and the new artworks that they have produced, as well as new artworks by current artists, as the artworks on offer for sale will be updated on a regular basis.
- With the site being updated on a regular basis, the Artworks page will list more and more paintings, so that the user can improve their language skills when they return to the site on a regular basis. The search functionality also enables the user to find artworks easily when they begin to increase significantly in number. 

### Manual Logical Testing of all Elements and Functionality on every Page

This is a complete account of the testing process for the site from start to finish which I completed when the site had been ready for submission.

#### Home Page
1.  Navigation bar:
    - Go to the "Home" page from a desktop.
    - Amend the screen size from desktop to tablet (e.g. iPad) to verify that the navigation bar is fully responsive and switches from the inline menu to the hamburger icon dropdown menu at the appropriate place on the left of the navbar, with search, my account and bag icons visible.
    - When checking the responsiveness of the navbar, verify that there is no overflow and that all of the items are in their correct places. 
    - Click on the Young Irish Artists logo in the left section of the navigation bar and verify that it links correctly to the Home page.
    - Click on every navigation menu item (Home, About, Artworks, Art Styles, Artists and Specials) and verify that they link to the correct page, and confirm that FontAwesome icons are working.
    - Hover over the main links and verify the hover underline feature works as expected.
    - Click on the My Account and Bag links at the top right and verify that they dropdown correctly and go to the correct pages.
    - Confirm that the main search bar in the centre of the nav bar works correctly when searched by artist or artwork name.
    - Change the screen size to mobile and click the hamburger icon in order to verify that the menu drops down correctly and that the menu items are fully visible.
    - Conclude by verifying that functionality and responsiveness is all working correctly on mobile and tablet view.

2.  Introduction Text:
    - Go to "Home" page from a desktop.
    - Confirm that the jumbotron text section is correctly appearing on screen and is fully responsive when the width of the window is reduced to tablet and mobile size.
    
3. Call to Action Button:
    - Confirm that the button "Browse Artworks" changes colour during hover, and sends the user to the Artworks page. 
    
4. Footer:
    - Confirm that the Font Awesome icons in the Footer are visible and correctly formatted and that all text is spaced and clearly visible.
    - Reduce and expand the width of window to verify that the Footer is responsive and looks as it should on all devices, in line with the Bootstrap grid system.
    - Confirm that Footer items are correctly stacked on top of one another in tablet and mobile view.

5.  Review all functionality and responsiveness on mobile and tablet for the Home Page and confirm that everything on this page is correct.

#### Register Page
1.  Navigation bar:
    - Repeat the verification steps that I completed for the Navbar on the Home page.
    - Confirm that the Navbar is appearing as identical on all html pages.

2.  Register Form:
    - Reduce and expand the width of the window to verify that the register form works and centres the way expected, that it looks good on all device widths and that the font color and size is appropriate.
    - Confirm validation is working correctly for every form input field.
    - Confirm that the user can register an account. 
    - Confirm that verification email is sent and contains link to confirm email.
    - Confirm when user clicks link that they are brought back to Young Irish Artists, they click confirm and that a toast message confirms that they are now signed in and a registered user.

3.  Footer:
    - Repeat the verification steps completed for the Footer on the Home page.
    - Confirm that the appearance of the Footer is identical on all html pages.

4.  Review all functionality and responsiveness on my mobile phone and tablet for the Register Page and confirm that everything on this page is correct.

#### Login Page
1.  Navigation bar:
    - Repeat the verification steps that I completed for the Navbar on the Home and Register pages.
    - Confirm that the Navbar is appearing as identical on all html pages.

2.  Login Form:
    - Reduce and expand the width of the window to verify that the login form works and centres the way expected, that it looks good on all device widths and that the font color and size is appropriate.
    - Confirm validation is working correctly for every form input field.
    - Confirm that user can login when correct email and password are inputted. 
    - Confirm when user clicks link that they are brought back to Young Irish Artists, and that a toast message confirms that they are now logged in.

3.  Footer:
    - Repeat the verification steps completed for the Footer on the Home and Register pages.
    - Confirm that the appearance of the Footer is identical on all html pages.

4.  Review all functionality and responsiveness on my mobile phone and tablet for the Login Page and confirm that everything on this page is correct.

#### About Page
1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on Home, Register and Login pages.
    - Confirm that the Navbar is identical on all html pages.

2.  Jumbotron:
    - Confirm that the jumbotron text section and the call to action button below are correctly appearing on screen and is fully responsive when the width of the window is reduced to mobile size.

3.  Cards:
    - Confirm that the eight management team cards are correctly spaced on screen and are fully responsive when adjusted to tablet and mobile view.

4.  Footer:
    - Repeat verification steps completed for the Footer on Home, Register and Login pages.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the About Page and confirm that everything on this page is correct.

#### Artworks Page 

(including Artworks, Art Styles and Specials in the Navbar)
1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on Home, About, Login and Register pages.
    - Confirm that the Navbar is identical on all html pages.

2. Introduction Text:
    - Confirm that the jumbotron text section is correctly appearing on screen and is fully responsive when the width of the window is reduced to mobile size.
    
3. Cards:
    - Confirm that the twenty cards are correctly spaced on screen and are fully responsive; whereby when the product image is clicked the user goes to the product details page, when the artist name is clicked the user goes to the Artists page and when the art style is clicked the user only sees artworks in that style.  
    - Confirm that filter box is correctly working for all 8 options, that the art styles and specials buttons at the top of the page link to their respective categories, and that the back to top button is working. 

4.  Footer:
    - Repeat verification steps completed for the Footer on Home, About, Login and Register pages.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Artists Page and confirm that everything on this page is correct.

#### Artworks Details Page 
1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on Home, About, Artworks, Login and Register page.
    - Confirm that the Navbar is identical on all html pages.

2. Cards:
    - Confirm that the card selected is correctly shown and that all the details, including the artwork description, are listed.
    - Click into the image to confirm that it opens as a full screen image in a new window.
    - Confirm that quantity box works and that quantity cannot go below one.
    Confirm that Add to Bag and Keep Shopping buttons are working correctly. 
    - Confirm that if Add to Bag is selected that the bag icon updates in the top right hand corner, a toast message appears and option to go to secure checkout is presented. 

4.  Footer:
    - Repeat verification steps completed for the Footer on Home, About, Artworks, Login and Register page.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Artwork Details Page and confirm that everything on this page is correct.

#### Bag Page 
1.  Navigation bar:
    - Repeat the verification steps completed for the previous html pages.
    - Confirm that the Navbar is identical on all html pages.

2. Shopping Bag:
    - Confirm that shopping bag page is correctly showing the items that have been selected.
    - Confirm that update and remove buttons are working correctly.
    - Confirm that delivery functionality is working.
    - Confirm that Keep Shopping and Progress to Checkout Buttons are both working correctly.

3.  Footer:
    - Repeat verification steps completed for the Footer on previous html pages.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Bag Page and confirm that everything on this page is correct.

#### Checkout Page 
1.  Navigation bar:
    - Repeat the verification steps completed for the previous html pages.
    - Confirm that the Navbar is identical on all html pages.

2. Checkout Form:
    - Reduce and expand the width of the window to verify that the checkout form works and centres the way expected, that it looks good on all device widths and that the font color and size is appropriate.
    - Confirm validation is working correctly for every form input field, and that the country field is working. 
    - Confirm that create account and login buttons below form inputs are working.
    - Check that validation for card number is correct and that Stripe functionality is connected.
    - Confirm when user clicks complete order that spinner shows, and that a toast message confirms that the purchase has been made and that they also receive an email confirming same.

3.  Footer:
    - Repeat verification steps completed for the Footer on previous html pages.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Checkout Page and confirm that everything on this page is correct.

#### Artists Page
1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on previous html pages.
    - Confirm that the Navbar is identical on all html pages.

2.  Jumbotron:
    - Confirm that the jumbotron text section and the call to action button below are correctly appearing on screen and is fully responsive when the width of the window is reduced to mobile size.

3.  Cards:
    - Confirm that the twelve artist cards are correctly spaced on screen and are fully responsive when amended to tablet and mobile view.

4.  Footer:
    - Repeat verification steps completed for the Footer on previous pages.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the Artists Page and confirm that everything on this page is correct.

#### SuperUser
- When logged in as SuperUser, navigate to the Product Management link.

1.  Navigation bar:
    - Repeat the verification steps completed for the Navbar on previous html pages.
    - Confirm that the Navbar is identical on all html pages.

2.  Form: 
    - Confirm validation is working correctly for every form input field.
    - Confirm when superuser clicks image and add product buttons (when form is completed), that everything works and a new product is created in the artworks page.

3.  Buttons:
    - Confirm superuser can edit and delete products on artworks page.

4.  Footer:
    - Repeat verification steps completed for the Footer on previous pages.
    - Confirm that the Footer is identical on all html pages.

5.  Review all functionality and responsiveness on my mobile phone and tablet for the SuperUser Pages and confirm that everything on this page is correct.

#### Additional HTML Pages

- Logout: Confirm that clicking the Logout link works.
- Error Pages: Confirm that 404 and 500 error html pages are correctly written (html has been validated). When user reaches the 404 and 500 page they see the heading "Something went wrong" and can click the Return to Home Page button as an option. I reviewed all the functionality and responsiveness on my mobile phone and tablet for the 404 page and confirmed that everything on this page is correct.  

## Further Testing

### Further Testing Details

- Compatibility: The website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers, and was found to operate correctly on all of these browsers.
- Performance: I also tested the website in Google Lighthouse, which returned the following scores; (i) Performance: 84, (ii) Accessibility: 100, (iii) Best Practices: 100 & (iv) SEO: 100. The result image is detailed below;

![lighthouse](https://user-images.githubusercontent.com/71781554/129335664-a133eb90-9e10-4a19-a500-0f27c8bb5f81.png)

- Responsiveness: The website was viewed on a variety of devices such as Desktop, iPad and iPhone6. All formats were in order with no sections out of line or overlapping.

- I completed a large amount of detailed testing to ensure that all links and email functionality were working correctly and that external links opened (as detailed in Manual Testing section above), and was happy that there were no broken links. This involved going into every page of the site and clicking every link/button that is available to a user and admin superuser (as part of their journey through the site) to ensure that everything was fully functional. 

- I checked the console in Devtools and confirmed that there were no error reports in respect of any of the pages.

- As part of the testing process, my family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
- N/A - No bugs were found during the testing completed before submission. 
