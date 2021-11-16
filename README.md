<h1 align="center">Tarmachan</h1>

![Mock-Up](documentation/wireframes/mock-up/mock_up.png)

View the repository in GitHub [here](https://github.com/Tawnygoody/Tarmachan)

View the live project [here](https://tarmachan.herokuapp.com/)

# Contents

1. [User Experience (UX)](#user-experience-(ux))
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
2. [Information Architecture](#information-architecture)
    - [Database](#database)
    - [Data Model](#data-model)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Database Creation](#database-creation)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. [Acknowledgments](#acknowledgments)


# User Experience (UX)

## Strategy

### User Stories

#### Viewing & Navigation
1. As a first time user, I would like to instinctively know what the website is offering. 
2. As a first time user, I would like an intuitive navigation system to easily move around the site. 
3. As a first time user, I want to be able to view a range of products on the same page. 
4. As a first time user, I want to be able to view individual product detail. 
5. As a first time user, I want to be able to locate any special offers & deals to take advantage of any reduced prices. 
6. As a first time user, I would like to find out information about the company to see what the business can deliver. 
7. As a first time user, I want to be able to contact the business with any queries I may have. 

#### Registration & User Accounts
8. As a site user, I want to be able to sign up and register an account to make future purchases easier. 
9. As a site user, I want to be able to have access to a personal profile page where I'm able to see my order history and delivery details. 
10. As a site user, I want to be able to leave reviews on products to inform future site users about the business's products. 
11. As a site user, I want to be able to save items to a Wishlist for ease of purchase on future visits. 

#### Sorting & Searching
12. As a site user, I want to be able to see all the products that the company sells. 
13. As a site user, I want to be able to narrow down the products by categories and sub-categories. 
14. As a site user, I want to be able to sort products with various parameters. 
15. As a site user, I want to be able to search for products using keywords. 

#### Purchasing & Checkout
16. As a purchasing user, I want to be able to select product sizes (on products which have sizes) and select the quantity of product I wish to purchase. 
17. As a purchasing user, I want to be able to add items to a basket should I wish to make more than one purchase. 
18. As a purchasing user, I want to be notified when I've made changes to my basket and show an updated total price. 
19. As a purchasing user, I want to be able to update items in the basket by changing the quantity or removing the item from the basket entirely. 
20. As a purchasing user, I want to be able to checkout securely. 
21. As a purchasing user, I want to be able to view a confirmation page of my order and receive an email confirmation once the purchase is sucessful. 

#### Admin & Store Management
22. As a site owner, I want to be able to add, edit and remove products from the site easily. 
23. As a site owner, I want access to an admin section to view and manage orders. 
24. As a site owner, I want to be able to manage blog posts and products reviews made by the customer. 
25. As a site owner, I want to be able to delete product reviews if they are unsuitable for the site. 


## Scope

The key features of the website were developed based on the user stories

### For any site user: 
- Home page, with dramatic imagery and to quickly help user's understand the purpose of the site.
- Products Page, where users can view all the products, or products based on filtering criteria. 
- Product Detail Page, detailing information about the product. From here user's can read reviews from other customers and add products to their bags. 
- Shopping Bag page, where users can see what products have been added to their bag. 
- Checkout page, allowing users to purchase products. 
- Confirmation page, allowing users to see a confirmation of their order. 
- Blog Page, where users can look at all the blog posts that have been uploaded by the site owner. 
- Blog Detail Page, where users can find out more information about each blog post.
- Contact Page, where users can contact the company with any queries.
- Newsletter Subscriber, available on all pages where users can subscribe to the company newsletter. 
- Sign Up Page, where users can register to become a registered user. 
- About Us Page, where users can find out more about the company. 

### For registered users: 
All of the above plus: 
- Wishlist page, where users can store products in their wishlist. 
- Profile Page, where users can update their default delivery information allowing for ease at checkout. 
- Order History, from the profile page users can see the previous orders they have made. 
- Product Reviews, on the product detail page, users can leave a rating and a message about a product. 
- Log Out Page, where users can log out of their account. 

### For Site Admin:
All of the above plus: 
- Site management page, where admin users can add products, blog, and review contact messages from other users. 
- Add Product / Blog page, where admin can add products / blogs. 
- Edit Product / Blog Page, where admin can update products / blogs. 
- Product Reviews, admin can delete reviews from any user has left a review. 

## Structure

## Skeleton

Below you can find the links for my wireframes, showing how I would like the pages to be structured, and how the site will appear on different device sizes. 

The wireframes have been created using Balsamiq and show for Desktop, iPad and iPhone. 

- Home Page
    - [Desktop](documentation/wireframes/home-page/home-page-desktop-r.png)
    - [iPad](documentation/wireframes/home-page/home-page-ipad-r.png)
    - [iPhone](documentation/wireframes/home-page/home-page-iphone-r.png)
- All Products Page
    - [Desktop](documentation/wireframes/all-products-page/all-products-page-desktop-r.png)
    - [iPad](documentation/wireframes/all-products-page/all-products-page-ipad-r.png)
    - [iPhone](documentation/wireframes/all-products-page/all-products-page-iphone-r.png)
- View Product Page
    - [Desktop](documentation/wireframes/view-product-page/product-page-desktop-r.png)
    - [iPad](documentation/wireframes/view-product-page/product-page-ipad-r.png)
    - [iPhone](documentation/wireframes/view-product-page/product-page-iphone-r.png)
- Basket Page
    - [Desktop](documentation/wireframes/basket-page/basket-page-desktop-r.png)
    - [iPad](documentation/wireframes/basket-page/basket-page-ipad-r.png)
    - [iPhone](documentation/wireframes/basket-page/basket-page-iphone-r.png)
- Checkout Page
    - [Desktop](documentation/wireframes/checkout-page/checkout-page-desktop-r.png)
    - [iPad](documentation/wireframes/checkout-page/checkout-page-ipad-r.png)
    - [iPhone](documentation/wireframes/checkout-page/checkout-page-iphone-r.png)
- Confirmation Page
    - [Desktop](documentation/wireframes/confirmation-page/confirmation-page-desktop-r.png)
    - [iPad](documentation/wireframes/confirmation-page/confirmation-page-ipad-r.png)
    - [iPhone](documentation/wireframes/confirmation-page/confirmation-page-iphone-r.png)
- About Us Page
    - [Desktop](documentation/wireframes/about-us-page/about-us-desktop-r.png)
    - [iPad](documentation/wireframes/about-us-page/about-us-ipad-r.png)
    - [iPhone](documentation/wireframes/about-us-page/about-us-iphone-r.png)
- Contact Us Page
    - [Desktop](documentation/wireframes/contact-us-page/contact-us-desktop-r.png)
    - [iPad](documentation/wireframes/contact-us-page/contact-us-ipad-r.png)
    - [iPhone](documentation/wireframes/contact-us-page/contact-us-iphone-r.png)
- Blog Page
    - [Desktop](documentation/wireframes/blog-page/blog-page-desktop-r.png)
    - [iPad](documentation/wireframes/blog-page/blog-page-ipad-r.png)
    - [iPhone](documentation/wireframes/blog-page/blog-page-iphone-r.png)
- Blog Story Page
    - [Desktop](documentation/wireframes/blog-story-page/blog-story-desktop-r.png)
    - [iPad](documentation/wireframes/blog-story-page/blog-story-ipad-r.png)
    - [iPhone](documentation/wireframes/blog-story-page/blog-story-iphone-r.png)

## Surface

### Design

#### Colour Scheme

- Inspiration for my colour scheme has been taken from [Rab's website](https://rab.equipment/uk/mens/fleece-midlayer). I've decided to go for a slighter darker green to allow further contrast for the white text. As Tarmachan is an outdoors store this colour choice reflects the link between products sold and the Scottish countryside. 

- From there I have used complimentary shades of green to create a softer pallette highlighting different sections of the site. 

- I have decided to use a white background throughout the majority of the site. This is to keep the visual design clean and means the emphasis is on the products and imagery to bring vibrance to the site. This design follows that of similar Mountain equipment retailers such as [Rab](https://rab.equipment/uk/mens/fleece-midlayer), [North Face](https://www.thenorthface.co.uk/) and [Mountain Equipment](https://www.mountain-equipment.co.uk/). 

![Chosen Colour Scheme](documentation/colour-scheme/colour_scheme.png)

- (#002929) - Used for Delivery Banner and footer credits
- (#003838) - Used accross the site, primarily seen in the footer, on buttons, tooltips, color text etc.
- (#177373) - Used on product details tabs, icons and stars. 
- (#ffffff) - Used throughout the site as a background, and white text. 


#### Additional Colours Used

- (#0DCAF0) - Used for information toasts
- (#198754) - Used for success toasts
- (#FFC107) - Used for warning toasts
- (#DC3545) - Used for danger toasts and delete icons
- (#1b7945) - Used for discount text
- (#AAB7C4) - Used a placeholder text colour
- (#CCCCCC) - Used for unchecked stars
- (#B1B1B1) - Used for Box shadows

#### Typography

- I have used Cantata One as the logo font which has been used throughout the whole site. This was dictated when deciding what font to use on the products themselves. I wanted a font which was bold yet readable and looked uniform when it's formatted to be uppercase. The same font has therefore been used for headings, subheadings and some buttons. 

![Cantata One](documentation/typography/cantata.png)

- I have used Crimson Text throughout the rest of the site for longer passages of text and paragraph use. Two font weights have been used to allow for emphasise at certain points on the site. This text is the same text used on the [Mountain Equipment](https://www.mountain-equipment.co.uk/) which was used as an inspiration for my site. 

![Crimson Text](documentation/typography/crimson.png)

#### Imagery

- Due to the nature of the products sold I have had to rely on other retailers products and modify them for use on my site. For the most part product images have come from [Mountain Equipment](https://www.mountain-equipment.co.uk/) and other online retailers (credited in the credits section).

- I have used a hero image on the home page to the give the site a dramatic appearance. Category images have been used for the featured products section on the home page to give a visual representation of what the companies products are intended for. Parallax images and product detail background images are in keeping with the company name. 

- Image credits can be found in the credit section of the README.

#### Icons

- Ive made use of icons in various section on the site. They have been used for navigation (on larger devices), social media links, wishlist, product tags and stars. All icons have been obtained from FontAwesome. 

# Information Architecture

## Database

- SQLite relational database management system (pre-installed with Django) has been used in development to store the data for this project. 
- PostgreSQL relational database management system has been used in production. 
- Note: The user model is provided by [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html).

## Data Model

The following Entity-Relationship diagram shows the relationships between the models. 

![DBDiagram](documentation/data-model/database_model.png)

### Blog App
- Blog Model
    - Contains the details of the blog post and is linked to the User model by the 'author' field. 

### Checkout App
- Order Model
    - Contains details of the of the user's orders, their delivery details, and the items they've order. It is linked to the UserProfile Model by the 'user_profile' field

- OrderLineItem Model
    - Contains details for the customer order, quantity and product total. It is linked to the Order Model by the 'order' field and the Product Model by the 'product field'.
### Products App
- MasterCategory
    - Contains Master Categories options for products. It is linked to the Product Model using a foreign key.

- ProductCategory
    - Contains Product Categories options for products. It is linked to the Product Model using a foreign key.

- ProductSubCategory
    - Contains Product Sub Categories options for products. It is linked to the Product Model using a foreign key.

- Clearance
    - Contains clearance options for products. Currently only 2 options, but further options could be added such as "Limited time offer" etc. It is linked to the Product Model using a foreign key.

- Product
    - Contains detailed product information for each product. 

- Comment
    - Contains the review information for each product. It is linked to the Product Model by the 'product' field and the User Model by the 'user' field. The rating field also updates the product rating each time a review is left. 
### Contact App
- NewsletterSubscription
    - Contains the email of users who have signed up to the newsletter
- Contact
    - Contains the details of users and their queries from the contact form. 
### Profiles App
- UserProfile
    - Contains the user's details for future orders. 
### Wishlist App
- user_wishlist
    - Although this is not a Model, I have built a one-to-one link between the User Model and Product Model, which creates a "link table" allowing user's to add products to their wishlist. 
### Django Allauth
- User
    - The User model is provided by default from Django Allauth and contains the username, email, and password for each user. 

### Fixtures

Fixtures were created for the following:
- MasterCategory
- ProductCategory
- ProductSubCategory
- Clearance
- Product

Using JSON files enabled the large amount of product and category data to be loaded easily into both the database in development and the database in production. 

# Technologies Used

## Languages Used

- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) 
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

## Libraries & Integrations
- [Django](https://www.djangoproject.com/)
    - This was the primary framework used for the project
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - This has been used to render the forms on the site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
    - This has been used for user authentication on the site.
- [Django Countries](https://pypi.org/project/django-countries/)
    - Used to populate the countries select field on the order form and profile form
- [Coverage](https://pypi.org/project/coverage/)
    - Used to produce a testing report
- [Stripe](https://stripe.com/gb)
    - This has been used to handle payments.
- [Bootstrap](https://getbootstrap.com/)
    - Used as a framework for styling and to make the site responsive
- [Amazon Web Services](https://aws.amazon.com/)
    - Used to store all static files and images
- [SQLite](https://www.sqlite.org/index.html)
    - Database used in development
- [PostgreSQL](https://www.postgresql.org/)
    - Database used in production
- [Heroku](https://id.heroku.com/login)
    - Online Cloud Platform used to deploy the live site
- [Gunicorn](https://gunicorn.org/)
    - Used for deploying the project to Heroku
- [Fontawesome](https://fontawesome.com/)
    - Fontawesome has been used for icons across the website. 
- [Google Fonts](https://fonts.google.com/)
    - Google Fonts has been used to import "Cinzel" & "Montserrat" fonts used across the website. 
- [jQuery](https://jquery.com/)
    - Has been used to ease DOM manipulation. 
- [Balsamiq](https://balsamiq.com/)
    - This has been used to create the wireframes for the project. 
- [Canva](https://www.canva.com/)
    - Canva has been used to design the websites logo.
- [Photopea](https://www.photopea.com/)
    - This has been used to make changes to the product images.
- [Dbdiagram](https://dbdiagram.io/home) 
    - Used to create the database schema illustration.
- [Techsini](https://techsini.com/multi-mockup/)
    - Techsini has been used to generate mock images on different devices, and help with responsiveness.
- [Github](https://github.com/)
    - GitHub is used to store the project code after being pushed from Git.
- [Git](https://git-scm.com/) 
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [Owl Carousel](https://owlcarousel2.github.io/OwlCarousel2/)
    - This has been used for the home page carousel for the blogs.

# Testing

All testing carried out on the website can be found in the following file: 

## [TESTING.md](TESTING.md)