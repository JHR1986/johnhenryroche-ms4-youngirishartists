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
    + [Phrases Page](#phrases-page)
    + [Login Page](#login-page)
    + [Register Page](#register-page)
    + [Profile Page](#profile-page)
    + [Add Phrase Page](#add-phrase-page)
    + [Edit Phrase Page](#edit-phrase-page)
    + [Additional HTML Pages](#additional-html-pages)
- [Further Testing](#further-testing)
  * [Further Testing Details](#further-testing-details)
  * [Known Bugs](#known-bugs)


### Client Stories Testing
The most direct path through the website is as follows:
- Home – Artworks – Login (if a user) or Register (if not a user).
- On the Home page, the user is presented with a prominent call to action button (as detailed below); 
    1. "Browse Artworks": From Home – Artworks
- On the About page, the user can read about the site, click a button to go to the Artworks, view the Website Team and use the Navbar to go to different pages.
- On the Artworks page, the user can view all of the artworks for sale, with the option of filtering them by Price, Name, Rating and Category. There is also a navbar link to Art Styles, where the user can browse the artworks by their style of painting (e.g. Pop Art or Watercolours), and to Specials where users can browse new arrivals or deals in respect of the Artworks.
- On the Artists page, the user can read about the artists, click a button to go to the Artworks, view the Artist Profiles and use the Navbar to go to different pages.
- On all of the pages, there is a search bar located in the navbar, which enables the user to search for artworks either by artist or artwork name.
- On the Home Page, there is a My Account button in the navbar, which when clicked allows the user to either login if they have an account or to register if they do not. To register, the user receives a verification email. 
- When a product is selected, it is added to the bag page, from which the user can progress to the checkout page and then make their payment. When payment is made the user receives an email confirming the purchase and they also can see their orders when signed in.
- When the user logs out, they must click a logout button and they are no longer logged in.
The information in the site is kept very structured and to concise, in order that it is very easy to follow and the user does not feel overwhelmed with details.


### Testing Client Stories from UX Section of Main Readme File

#### First Time Visitor Goals
1.  As a First Time Visitor, I want to quickly confirm what products the ecommerce website is selling (e.g. art prints).
- The Home page has a general synopsis of the purpose of the website and a striking background image of a colourful artwork on a blank canvas, and there is a prominent navigation bar for clicking to the About, Artworks (Artworks, Artwork Styles, Specials) and Artists pages. 
2.  As a First Time Visitor, I want to be able to easily browse through the site pages (including About and Artists) and view the artworks that are on offer.
- The Navbar is easy to understand and offers users the opportunity to easily browse through the site pages. The Home, About and Artists pages each feature a prominent call to action button to return the user to the Artworks page, while there is also a search bar located in the centre of the navbar for searching by artist or artwork name. 
3.  As a First Time Visitor, I want to be able to go to the Register page and create my own account if I am considering making a purchase.
- The My Account button on the home page dropsdown to a login and register link. When the Register link is selected, the user enters their email, username and password to create an account. 

#### Returning Visitor Goals
1.  As a Returning Visitor, I want to be able to be able to make purchases of art prints easily and effortlessly, as I have an account and my information will be pre-loaded to save me time. 
- When an artwork is selected, the user is brought through to a more detailed page describing the artwork. They then have the option to include the quantity and add it to their bag. The system is very user friendly going from product to bag to checkout in a manner of clicks, while allowing the user to remove the product if they change their mind and to continue shopping. 
2.  As a Returning Visitor, I want to be able to filter my searches for artworks by genre, price, rating or specials, in order that I can purchase the artworks that best suit my taste and price range.
- The Navbar and the main artworks page allows the user to filter the products by price, rating, category, style and special offers, in descending/ascending or alphabetical order.  

#### Frequent Visitor Goals
1. As a Frequent/Returning Visitor, I want to be able to easily contact Young Irish Artists if there has been any issue with my purchase, and the contact information is clearly highlighted in the Footer Section of the site. 
- The footer to each of the html pages lists the site's address in Dublin, their opening hours and phone/email address, so that any subsequent queries can be addressed to the site owners.
2. As a Frequent/Returning Visitor, I want to be able to see new artists that have joined the site and the new artworks that they have produced, as the artworks on offer will be updated on a regular basis.
- With the site being updated on a regular basis, the Artworks page will list more and more phrases, so that the user can improve their language skills when they return to the site on a regular basis. The search functionality also enables the user to find phrases easily when they begin to increase significantly in number. 


## Further Testing

### Further Testing Details

- Compatibility: The website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers, and was found to operate correctly on all of these browsers.
- Performance: I also tested the website in Google Lighthouse, which returned the following scores; (i) Performance: 84, (ii) Accessibility: 100, (iii) Best Practices: 100 & (iv) SEO: 100. The result image is detailed below;

![lighthouse](https://user-images.githubusercontent.com/71781554/129335664-a133eb90-9e10-4a19-a500-0f27c8bb5f81.png)

- Responsiveness: The website was viewed on a variety of devices such as Desktop, iPad and iPhone6. All formats were in order with no sections out of line or overlapping.

- I completed a large amount of detailed testing to ensure that all links and email functionality were working correctly and that external links opened (as detailed in Manual Testing section above), and was happy that there were no broken links. This involved going into every page of the site and clicking every link/button that is available to a user (as part of their journey through the site) to ensure that everything was fully functional. 

- I checked the console in Devtools and confirmed that there were no error reports in respect of any of the pages.

- As part of the testing process, my family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
- N/A - No bugs were found during the testing completed before submission. 
