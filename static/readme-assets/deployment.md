<a href="https://github.com/RoryBr1/Milestone-4#design">Back to ReadMe</a>

* [Local GitPod Deployment](#local-gitpod-deployment)
* [Heroku Deployment](#heroku-deployment)

# Deployment

## Local GitPod Deployment

The following steps will allow you to deploy the project 'locally' in the cloud-based IDE, Gitpod.

*This procedure requires a [GitHub](https://github.com/login) account, and a [Stripe](https://dashboard.stripe.com/register) account.*
<hr>

**Step One: Creating a Gitpod workspace and installing requirements**
1. [Login to Gitpod](https://gitpod.io/login) using your GitHub account. (If a GitHub pop-up window asks you to authorize Gitpod, click Authorize).l

2. Navigate to the project's [GitHub repository](https://github.com/RoryBr1/Milestone-4) in your browser, and click "Fork" in the top right hand corner of the page. Navigate to your repositories page, and click on "Milestone 4" which has just been created. Copy the address of this page from your URL bar.
Replace ```[your_url_here]``` in the address below with the URL you have just copied.
```gitpod.io/#[your_url_here]```
This will open your new, forked repository in Gitpod.

3. Install all required packages in your Gitpod workspace, by typing 
   ``` pip3 install -r requirements.txt ```
   in the workspace terminal and pressing enter.    
   Wait until the installation processes for all packages have completed.
<hr>

**Step Two: Setting Django & Stripe SECRET_KEYs and Stripe PUBLIC_KEY**

*Reccomended reading:*  
[What is a Django Secret Key?](https://docs.gitguardian.com/secrets-detection/detectors/specifics/django_secret_key#:~:text=Summary%3A%20The%20Django%20secret%20key,cookies%20sent%20by%20the%20application.)  
[Stripe Docs: API Keys](https://stripe.com/docs/keys)


1. Create a new file in the base directory of your project, named ".env" . This file will hold your SECRET_KEY. (We have included *.env* in our *.gitignore* file, which will prevent this sensitive data from being pushed publicly to GitHub).

2. In your *.env* file, copy and paste these lines of code:

    > DEVELOPMENT=True
    > SECRET_KEY=your-django-secret-key     
    > STRIPE_PUBLIC_KEY=your-stripe-public-key      
    > STRIPE_SECRET_KEY=your-stripe-secret-key  
    > STRIPE_WH_SECRET=your-stripe-wh-secret    
    > EMAIL_HOST_PASSWORD=your-email-host-pass   
    > EMAIL_HOST_USER=your-email-host-user   

2. Use [Djecrety.ir](https://djecrety.ir/) to generate a random Django key, and click on the key to copy it to your clipboard. 

3. In your *.env* file, replace ```your-django-secret-key``` with your new key from the generator. (Do not include any quotation marks around the key).

4. Login to [Stripe](https://dashboard.stripe.com/login) and navigate to your [Stripe Dashboard](https://dashboard.stripe.com/test/dashboard).

5.  On the bottom right of the page, click on your "Publishable Key" to copy it to your clipboard.  
    Paste it into your *.env* file, replacing ```your-stripe-public-key```. 

    In Gitpod, use the Explorer to navigate to ```checkout/views.py```. On line 44, replace the existing ```stripe_public_key``` with your own, inside the quotation marks.

6. On the bottom right of your [Stripe Dashboard](https://dashboard.stripe.com/test/dashboard), click on *Secret Key* once to reveal it.  
    Click it again to copy it to your clipboard, and paste it into your *.env* file replacing ```your-stripe-secret-key```. 
<hr>

**Step Three: Running the server, adding STRIPE_WH_SECRET .env variable**

1. In your Gitpod terminal, type the following command and press enter: ```python3 manage.py runserver``` . 
    The site is now being hosted locally, and the following prompt should appear:   
    ![Gitpod preview prompt](/static/readme-assets/gitpod-runserver-prompt.png)  
    Click "*Open Browser*", and the live site will open in a new browser tab.

2. Click "*Shop Now*", then click "*View*" on any product. Click "*Add to Cart*". On the modal window that appears, click "*Check Out*". 
    Scroll to the bottom of the *Shopping Cart* page, and click "*Checkout*". 

3. Copy the URL of this *Checkout* page to your clipboard from your browser's URL bar. 

4. Navigate to [create Stripe Webhook Endpoints](https://dashboard.stripe.com/test/webhooks/create).  
    Paste the *Checkout* URL into the *Endpoint URL* field, and in the description text-area type something such as "Techzone Checkout".    
    On the "*Select events to listen to* option, click "*Account*" and "*Payment Intent*", and tick "*Select All*" for both.    
    Click "*Add Events*", and then "*Add Endpoint*".

5. Once the endpoint is created, navigate to [Stripe Webhook Endpoints](https://dashboard.stripe.com/test/webhooks), and click on the address of the new endpoint you just created. 
On the right hand corner of this page, click the webhook code to copy it to your clipboard. 
Return to your *.env* file, and replace ```your-stripe-wh-secret``` with this new webhook code. 

At this point, the basic functionality of the site as a guest user is complete. The guest user can browse the locally deployed version of the site, add products to their cart, and complete the checkout process.
    **Note**: As your Stripe account is set by default to run in *Test mode*, you can use the following *test mode* credit card details to complete the checkout process.   

     Card Number: 4242 4242 4242 4242  
     Expiry Date: 0424     
     CVC: 242  
     ZIP: 42424    

**Note:** When ```DEVELOPMENT=True``` is in our *.env* file, e-mails (such as registration and order confirmation e-mails) will be printed to the Gitpod terminal.   
If you choose to deploy the site to [Heroku](https://www.heroku.com/) following the procedure below, steps are listed which will instruct you on how to enable emails to be sent from a live Gmail account.


[⇧ Back to Top](#table-of-contents)

<hr>

## Heroku Deployment

[Reccomended Reading: What is Heroku?](https://www.heroku.com/what)

This procedure requires that you have successfully [configured your project in a Gitpod workspace](local-gitpod-deployment) as directed.

You will need a [Heroku](https://signup.heroku.com/) account.

> Important
> If you get ``` FATAL: role "somerandomletters" does not exist ``` error, run ``` unset PGHOSTADDR ``` in the terminal. This should allow you to continue.


1. In your Gitpod terminal, type ``` python3 app.py > Procfile ``` . This will create a _Procfile_, which will tell Heroku how to run our project.
Your Procfile should read ```web: gunicorn techzone.wsgi:application```. 

2. Login to [Heroku](https://signup.heroku.com/). Accept any terms and conditions which may be prompted, and navigate to [Create New app](https://dashboard.heroku.com/new-app). Give your app a name of your choice, and click "Create app".   
In the "*Resources*" tab, search for "heroku postgres". Choose the "hobby Dev - Free" option, and click "Submit Order form".

3. Back in GitPod, navigate to *techzone/settings.py*. We will need to setup our project to use this new Postgres database. Delete lines 129 to 141, and replace with the following code:   
    >   DATABASES = {
        'default': dj_database_url.parse('[your-postgres-address]', 'localhost')
        } 
You will need to replace [your-postgres-address] with the DATABASE_URL which you can find in the *Settings* tab of your Heroku project, under *Config Variables*.

4. Return to Gitpod, and in the terminal, run ```python3 manage.py makemigrations```, followed by ```python3 manage.py migrate```. This will migrate your current database to the new Postgres one. 
Then, run each of these commands in order:  
``` python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json ```   
``` python3 manage.py loaddata db.json ```  

Finally, run ```python3 manage.py createsuperuser``` and follow the steps to create a new admin user.

5. In your Gitpod terminal, run the following command   
```heroku config:set DISABLE_COLLECTSTATIC=1 --app [your-app-name]```   
Replacing ```[your-app-name]``` with your own. You may be prompted to login to Heroku; follow the steps in your terminal to do so.

6. In *techzone/settings.py*, on line 21 (ALLOWED_HOSTS), replace ```techzone-ms4.herokuapp.com``` with the address of your Heroku project, in the same format. (You can find this on the *Settings* page of your Heroku app; remove the "http://" and "/" at the start and end of the address.)

7. Add, commit and push your changes by running the following sequence of commands in your Gitpod terminal: 
```git add .``` 
```git commit -m "heroku deployment"``` 
```git push heroku master```  

8. Go to the _Settings_ page of your project in Heroku and click on "Config Vars". Click on "Reveal Config Vars".   
From your *.env* file, copy each of the *environment variables* into this interface. (For example, *SECRET_KEY* in the KEY field, and the code after the equals sign in the VALUE field on this interface.) 
We have to do this because since our *.env* file has not been made public or pushed to GitHub, and Heroku needs these values for our site to function.

9. In the *Deploy* tab of your Heroku app's page, under *Deployment Methods*, click GitHub. Scroll down, and click *Connect to GitHub*. You will be prompted to authorize Heroku. Once authorized, search for the name of your repo under the *Connect to GitHub* section. Click "*Connect*" beside the repository name. Scroll down, and click "*Enable Automatic Deploys*".

10. Go to the _Deploy_ tab in Heroku, scroll down and click "Enable Automatic Deploys". Click "Deploy Branch".

Once the app is deployed, click "Open App" in Heroku on the project page. The project should be successfully deployed and will update automatically whenever a new GitHub push is made.



