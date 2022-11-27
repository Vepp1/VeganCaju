# VeganCaju

VeganCaju is an online vegan truffles store. The main goal of the company is to provide a harmless and tasty solution to vegans and those who are trying to adopt this philosophy. The target users are between 17-40 years old, which is the average age of more than 50% of vegans. The website consists of an application that allows users to choose between different box sizes and truffles flavors, and a pick-up date (since the company yet does not provide delivery). after an account was created. After the order was created on the ORDER page, users can check and modify orders that are not yet approved on MY ORDERS page. 
![Desktop View](assets/images/desktopview-min.png)

----

## Features 

### Colour Palette
- The colors chosen for this project are based on the colors of VeganCaju's logo, which was created using similar colors to a real Caju fruit.

### Home Page
- The first thing a user sees accessing the side is a hero image with a delicious box of truffles. This page contains information about the product and the company. 

### Navigation Bar
- To navigate through the website, users can use the nav bar. When users are not logged in, the navbar can take users to Login, Signup, or Order page (that will automatically redirect to the login page). When logged in, the nav bar options are Order, My Orders, and Logout. The navigation bar options collapse into a burger menu, in small screen sizes.

### Footer with Google Maps API
- On all pages, users can find the footer. The footer shows contact information, such as telephone, email, and address. Also, a Google Maps API was added to display a real and interactive map of the company's location.

### Sign up/ Login / Logout
- To be able to use all website features, users must be logged in. Allauth was used to create this feature and handles all the authentication.

### Order
- This page contains a crispy form, for users to create their order. Users can choose between 3 different sizes, 5 different flavors, and a pick-up date, that is at least 3 days in the future. The form is validated on the views class Edit_Order.

### My Orders
- Here, logged users can check their orders and access options to delete or edit orders that are not approved yet. The order ID, size, flavor, creation date, pick-up date, and current status are displayed on this page. When the order status is Approved or Cancelled, the buttons to edit and delete are not displayed.

### Edit Order
- After accessing the My Orders page and selecting the edit option, users are taken to the Edit Order page. On this page, the same crispy form as the Order page is shown and the same validation rules apply here.

### Delete Order
- After accessing the My Orders page and selecting the delete option, users are prompted with a modal. The modal is to assure that the users want to delete the order, to avoid accidental deletions, since this can not be undone.

### Confirmation and error Messages
- When a user logs in, signs up, logs out, creates or updates an order, a confirmation message is displayed. When a user tries to select a past date as a pick-up date, an error message is displayed. The messages were created using Django messages with bootstrap5.

To check all features and future features, access:

----

## Testing and Validation

### Manual Testing

### Choose a past date as a pick-up date.
 - On the Order page, make an order and insert a past date as a pick-up date.
 - Result: A Django message is displayed, telling the user to choose a date at least 3 days in the future. This was made by building the validate_date function on Models.py.

### Access the Order or My Orders page without being logged in, through the address bar.
  - On the address bar, type order/ or my_orders/ after the website's URL.
  - Result: Using LoginRequiredMixin, when users try to access this page, they are automatically redirected to the Login page.

### Edit or delete an order from another user.
 - 2 accounts are needed. In one account, make an order and save its id. Log out and log in into a new account. Then, go to the address bar and type after the site's URL: edit_order/order id from the other account - to try to edit. delete_order/order id from the other account - to try to delete.
 - Result: An error query page will be displayed, because a validation method was added to views.py, to allow the user to only edit or modify orders that were created by the current logged user's username.

 ### Edit or delete an order that is not on "Waiting for Approval" status.
  - After logging into an account with approved orders, go to the address bar and type:
  edit_order/your approved order id/ - to try to edit. delete_order/your approved order id/ - to try to delete.
  - Result: Users are redirected to the 404 page. This was made using an if Clause on the edit and delete order class. The if clause checks the order status, and if it is not 0 ('waiting for approval'), it redirects users to the 404 page.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)
- JS
  - No errors were found when passing through the official.
- PEP8
  - No errors were found when passing through the official.

### Unfixed Bugs

None. 

----

## Deployment

- The site was deployed to Heroku pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://vepp1.github.io/indians-live/index.html

----

## Credits 

### Content 

- The initial template is a StartBootstrap template called One Page Wonder.
- The loader template was created by.
- The 404-page template was created by. 
- The animated background effect was built by.
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)


### Media

- The logo image was created by my great designer and wife Luiza Meirelles.
- All images were taken from [Pexels].