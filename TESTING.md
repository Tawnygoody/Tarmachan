# Testing

# Contents
- [Testing User Stories](#testing-user-stories)
    - [Viewing & Navigation](#viewing-and-navigation)
    - [Registration & User Accounts](#registration-and-user-accounts)
    - [Sorting & Searching](#sorting-and-searching)
    - [Purchasing & Checkout](#purchasing-and-checkout)
    - [Admin & Store Management](#admin-and-store-management)
- [Code Validation](#code-validation)
- [Browser Compatibility](#browser-compatibility)
- [Functionality Testing](#functionality-testing)
    - [Navigation](#navigation)
    - [Home Page](#home-page)
    - [Registration & Log In](#registration-and-log-in)
    - [Adding A Recipe](#adding-a-recipe)
    - [Editing A Recipe](#editing-a-recipe)
    - [Deleting A Recipe](#deleting-a-recipe)
    - [User Profile](#user-profile)
    - [Save Recipe to Profile](#save-recipe-to-profile)
    - [Recipes Search & View](#recipes-search-and-view)
    - [Recipe Page](#recipe-page)
    - [Dashboard](#dashboard)
- [Responsive Design](#responsive-design)
- [Security Testing](#security-testing)
- [Unit Testing](#unit-testing)
- [Solved Bugs](#solved-bugs)
- [Known Issues](#known-issues)
- [Lighthouse](#lighthouse)

# Testing User Stories

## Viewing & Navigation
1. As a first time user, I would like to instinctively know what the website is offering. 
    - The home page has numerous references to being a mountain equipment store through imagery.
    - Call to action buttons give an overview of what kind of products are likely to be available. 
    - Clearance section shows that there is currently a sale on the site's products. 

    ![User Story 1](documentation/testing/testing_user_stories/user_story1.gif)

2. As a first time user, I would like an intuitive navigation system to easily move around the site. 
    - Icons in the delivery banner (large devices only) allow easy access to Log In and Sign Up functionality. These are tooltipped to provide further guidance to the user. Icons vary depending on whether a user is logged in and if the user is a superuser. 
    - There are 4 links on the left side of the logo, which opens up mega menus for user's to filter products and find out more information about the company. 
    - Search icon opens up search menu and a basket icon allows access to the shopping bag. 
    - The navigation is fixed to the top of the screen so is always accessible for users. 
    - Additional navigation links are available in the footer. 
    - At various points on the site users can redirect to return to the products / blogs page at the click of a button. 
    - On mobile devices a burger menu opens up a menu where user's can direct to various pages of the site. Scrollable dropdowns are available to allow for filtering. 

    ![User Story 2](documentation/testing/testing_user_stories/user_story2.gif)

3. As a first time user, I want to be able to view a range of products on the same page. 
    - The products page shows all the products available on the site. The mega menu options will narrow this down dependant on various categories. 
    - As nearly all user's may not be necessarily interested in all products gievn that their are products for different genders, there is no all products link in the mega menu, however this can be accessed from the footer. 

    ![User Story 3](documentation/testing/testing_user_stories/user_story3.gif)


4. As a first time user, I want to be able to view individual product detail. 
    - On the products page users can see the product image, name, price and rating (if a product has a rating). When hovering over an image an overlay with the product description can be seen.
    - When the user clicks a product from the products page they are taken to the product detail page. Here the user can see a variety information about the product, including further descriptions, specifications and reviews. 

    ![User Story 4](documentation/testing/testing_user_stories/user_story4.gif)

5. As a first time user, I want to be able to locate any special offers & deals to take advantage of any reduced prices. 
    - From the mega menu there are links for clearance items in each of the three master categories. 
    - In the footer there is a link for all products in clearance. 
    - On the home page there is large clearance image, inviting users to take advantage of products on offer. 
    - On the products page, products which are in clearance are clearly identifiable by the sale logo in the upper right corner of the product card, and by the clearance price displayed. 

    ![User Story 5](documentation/testing/testing_user_stories/user_story5.gif)

6. As a first time user, I would like to find out information about the company to see what the business can deliver. 
    - User's can go to the company tab and look at the about us section which has a breif overview of the company and its philosophy. This can also be accessed in the footer. 

    ![User Story 6](documentation/testing/testing_user_stories/user_story6.gif)

7. As a first time user, I want to be able to contact the business with any queries I may have.
    - User's are able to find a contact page for the comany on the company tab. Additional a link can be found in the footer. 
    - The contact page has company details, opening times and a contact form. Customers are notified by email when a successful contact request has been made. 

    ![User Story 7](documentation/testing/testing_user_stories/user_story7.gif)

## Registration & User Accounts
8. As a site user, I want to be able to sign up and register an account to make future purchases easier. 
9. As a site user, I want to be able to have access to a personal profile page where I'm able to see my order history and delivery details. 
10. As a site user, I want to be able to update my delivery details on my profile page. 
11. As a site user, I want to be able to leave reviews on products to inform future site users about the business's products. 
12. As a site user, I want to be able to save items to a Wishlist for ease of purchase on future visits. 

## Sorting & Searching
13. As a site user, I want to be able to see all the products that the company sells. 
14. As a site user, I want to be able to narrow down the products by categories and sub-categories. 
15. As a site user, I want to be able to sort products with various parameters. 
16. As a site user, I want to be able to search for products using keywords.  

## Purchasing & Checkout
17. As a purchasing user, I want to be able to select product sizes (on products which have sizes) and select the quantity of product I wish to purchase. 
18. As a purchasing user, I want to be able to add items to a basket should I wish to make more than one purchase. 
19. As a purchasing user, I want to be notified when I've made changes to my basket and show an updated total price. 
20. As a purchasing user, I want to be able to update items in the basket by changing the quantity or removing the item from the basket entirely. 
21. As a purchasing user, I want to be able to checkout securely. 
22. As a purchasing user, I want to be able to view a confirmation page of my order and receive an email confirmation once the purchase is sucessful.

## Admin & Store Management
23. As a site owner, I want to be able to add, edit and remove products from the site easily. 
24. As a site owner, I want access to an admin section to view and manage orders. 
25. As a site owner, I want to be able to manage blog posts and products reviews made by the customer.