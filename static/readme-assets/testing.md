[ 🠔 Back to ReadMe ](https://github.com/RoryBr1/Milestone-4#testing)

# Table of Contents 
1. [Code Validators](#code-validators)
    - [Python](#python)
    - [JavaScript](#javascript)
    - [HTML](#html)
2. [User Stories](#user-stories)
3. [Feedback](#feedback)

<hr>
<hr>

# Code Validators
## Python
* All Python files are PEP8 compliant, with no errors. All *.py* files in the project have been checked using the [PEP8 online](http://pep8online.com/) tool. No errors are reported by the IDE linter used in development.

<hr>

## JavaScript
* *statc/js/main.js* has been passed through the [JavaScript Validator](https://beautifytools.com/javascript-validator.php) when "jQuery" option is selected, with two errors:

 - ```"updateBtns' is defined but never used."```   
 - ```"goBack' is defined but never used."```

However, these functions are called on using buttons related to event triggers in the JavaScript file - therefore they are not redundant, should not be removed, and the error should be ignored.
(```updateBtns``` is used to update cart items, and ```goBack``` is used throughout the site on multiple pages to support "*Back*" buttons).

<hr>

## HTML
[W3C HTML validator](https://validator.w3.org/nu/)

Deployed versions of each page in the project have been tested against the (Nu Html Checker)[https://validator.w3.org/nu/?doc=https%3A%2F%2Ftechzone-ms4.herokuapp.com%2F] returning no errors. 
Warnings are returned on several pages regarding unnecessary ```type``` attributes for JavaScript files, but due to time constraints a development decision was made not to correct these. In future developments, these warnings can be rectified, but do not affect the function of the site.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# User Stories

Each of the user stories was used as a starting point to test features on the site.

1. **As a site administrator, I want to upload products to the site for the end-user to view and purchase. I want to be able to edit and delete these products if needed.**
    
    ✔  Once logged in, the _admin_ drop-down menu button appears in the top right corner of the site.

    ✔  The _Manage Products_ button directs the user to the relevant page, where an intuitive form allows them to add a new product.

    ✔  Once the form is submitted, a confirmation flash message appears, and the product is successfully added to the site.

    ✔  _Edit_ and _Delete_ buttons are visible overlaying the image of each product when logged in as an admin.

    ✔  The _Edit_ button directs the admin user to the relevant page where they can easily edit the properties of the product.

    ✔  The _Delete_ button deletes the button and a flash message is displayed confirming this to the admin user. (In future developments, a confirmation modal would be highly valuable to prevent accidental deletes).

2. **As a _site administrator_, I want to categorise products for ease of management and end-user browsing.** 
    ✔  On the _Add New Product_ form, a drop-down select menu allows the admin user to categorise the product.

3. **As a _site administrator_, I want to ensure that only I can alter the content of the website.**

    ✔  At the top of each page when logged in as an admin, the _Admin_ menu link is visible. When not logged in as an admin, these features are not accessible.

    ✔ On the _Products_ page, and individual _product pages_, the _Edit_ and _Delete_ buttons are only visible and functional for _admin_ users.

    ✔ On the _Blog_ page, the _New Post_, _Edit_ and _Delete_ buttons are only visible and functional for _admin_ users.

4. **As a site administrator, I want to post reviews, news and opinion pieces on subject matter related to the site.**
    ✔ When logged in as an _admin_ user, navigate to the _Blog_ page using the site navbar. Click _New Post_; complete the relevant fields, and select an image to upload. Click "*Post*"; the post is added, and the admin is redirected to the main _Blog_ page where the new post is visible at the top. 

5. **As an _end-user_, I want to browse products relevant to me; including searching through them using search terms, sort by price, and view items in specific relevant categories.**

    ✔  Product list pages are loaded by clicking the _All Products, Laptops, Phones, Tablets_ links on the site navbar.. The _search_ function is intuitive, functional and finds products according to user search queries. The category buttons successfully load products in the chosen category.

    ✔  When clicked, a new page will load for each product displaying the full details of the product.

6. **As an _end-user_, I want to be able to add multiple items to my cart and checkout for them with one payment.**

    ✔  By navigating to any of the _Products_ pages, (for example, _Phones_), the user clicks the product name. An individual product page is loaded, where the user can click "_Add to Cart_". The item is added to the user's cart, and a prompt appears allowing them to "_Check Out_". The user can repeat this process to add multiple items to their cart.

    ✔  By clicking on the _Cart_ button at any point, the user is directed to the _Cart_ page. All items in the cart, as well as their price and the subtotal of the cart, are visible.    
    The user can click "_Check Out_" to continue to the "_Checkout_" page.

    ✔  When the user completes the _Shipping Address_ form, inputs their card details, and clicks "_Check Out_", the payment process is initiated. Once complete, the user is shown a confirmation page, and a confirmation e-mail is sent to their inbox. 
    The following *test* credit card details can be used to test the checkout process:

     Card Number: 4242 4242 4242 4242  
     Expiry Date: 0424     
     CVC: 242  
     ZIP: 42424    
  
    ✔  This procedure can be completed by both *guest* and *logged-in* users.

7.  **As an end-user, I want to send an e-mail to the site owner about an order (or potential order).**
    ✔  By scrolling to the bottom of any page and clicking _Contact_, the user is directed to an intuitive contact form. Once completed and submitted, a confirmation page is shown to the user notifying them that their message has been received by the admin.

    ✔  The e-mails are successfully received in the associated inbox.

8. **As an _end-user_, I want to register an account so that I can save my shipping details and post comments on the Blog**.

    ✔ The _Login_ and _Register_ links are both visible when a user is not logged in.

    ✔ _Login_ works successfully for existing users and authenticates them.

    ✔ _Registration_ is fully functional. Users can register, receive an e-mail asking them to confirm their account, and continue to login with that account. (Note: in local deployment, this e-mail will print to the terminal. It is better to test its functionality on the Heroku-deployed site.)

    ✔ Users can save their shipping details when. These can be edited, when logged in, by clicking their _username_ on the navbar and selecting _My Account_.

    ✔ Previous orders can be viewed on the _My Account_ page when logged in as a _non-admin_ user.

    ✔ By navigating to the _Blog_ page, and clicking _Continue Reading_ on any blog post, the user is redirected to the post (once logged in).
    By scrolling to the bottom of this page, completing the _Comment_ form, and clicking _Comment_, the user can successfully post a comment below the post.    
    The page is reloaded and the user's new comment is visible.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>