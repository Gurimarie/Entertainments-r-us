# Entertainments'R'Us
## A website where people can find and connect to freelance artists like singers, actors and entertainers in order to hire them for entertainment at celebrations, weddings and other festive occations.

This project is only just begun, and I have used instructions from the Code Institute "Boutique Ado"-project to set it up. This is most evident in main.py, main.css and index.html. I have started to adapt the code to my project, but they are still mainly the same as in that project. 

I was hoping to get at least the first page deployed and working for this assignment deadline, but sadly I have not been able to fix my bug(s) in time, so I have to submit as it is.

![Picture of different view-port-displays](static/readme_pictures/different-view-port-displays.PNG)

Click [here](https://entertainments-r-us.herokuapp.com/) to view the website

## User Experience (UX)
### User stories:
There will be three types of users on this website; 
the customers, the artists and the admins.

### First time customer-users goals
A customer-user wants to explore the artists work in order to find someone they like. If they are looking for something particular, they want to be able to sort the artists by main-category (singer, toastmaster, clown etc) and by sub-categories (like opera, jazz and rock for instance, for singers).

### First time artist-users goals
Artist-users wants it to be easy to set up a profile and add info, pictures and links to videos on YouTube etc. They want to be hired for jobs with certainty of being paid.

### Returning customer-user goals
A customer-user wants to be able to contact the artist they wish to hire, to assess price and availability. They want to know what feedback the artist has had from previous customers, and perhaps be able to sort artists by that feedback. They want to have a logg of the artists they have looked at before. They want to leave a feedback for artists they have already hired. They want a secure payment-system (the artist should not be paid before they have performed).

### Returning artist-user goals
Artist-users want a secure payment-system. The payment should be confirmed received by the app before they perform (but not delivered to the artist until the job is done). They want to be able to give feedback about customers who have hired them, and they want only people who have actually hired them to be able to leave feedback about their performance.

### Admin-user goals
The admin-user wants to update and take care of the page when needed. They will also need to take out "reports" for accounting and analytics-purposes.

### Site owner goals
The main goal for the site-owner is to make live entertainment more accessible and to make it easier for customers to find artists they want to hire, and for freelance-artists to be able to connect with the larger public. Also to make a small profit pr transaction in order to pay for maintenance to keep the site up-to-date, functioning and secure and for other overhead-costs.

## Design

### Colour scheme:
The colours are kept quite neutral. As there may be many different colours in the pictures and videos the artists add to the page, it is best for the background to be a bit toned down. The artists are the ones who should be the senter of attention, not the website in itself. 

### Typography:
Font-family: 'Nunito', sans-serif.
![Picture of font Nunito](static/readme_pictures/Font-Nunito-sans.PNG )
Ref. https://www.figma.com/; the "Nunito is a well balanced sans-serif typeface created by Vernon Adams. Its a rounded terminal sans-serif font for display that pairs well with Alegreya, Lora, Open Sans, and Roboto."
https://www.figma.com/google-fonts/nunito-font-pairings/
I like it for this project because it is light, without being flimsy, and I feel it's the perfect blend between serious and joyful, for this project. It is certainly well-readable, but the rounded bends, on the f and the t and the l makes it seem a bit playful, almost like it's doing it's own thing, and not quite bending to everyone elses needs, and I think that suits this app. Trustworthy, but still playful and happy :) 

### Imagery:
The backgroundimage for the home-page is meant to be a gesture to invite people in to the website. The image is from Shutterstock. 
https://image.shutterstock.com/image-photo/showman-young-male-entertainer-presenter-600w-1062295226.jpg 



## Features

- Ability to browse artists/performances and to buy products 
- Some of the pages, like the artists-details (more info) are only availabe if you are logged in.
- Ability to add products to shoppingbag and go to secure checkout to pay through stripe.
- A login-feature with profile-page for each user.
- Order-history and form to update shipping-info available on profile-page for logged-in users.
- Users that have "staff-user"-rights (between customer and superuser) can add, edit and delete artists, performances and products. This is the usertype used by the artists offering their services on the website, so that they can add new performances and edit info as they wish, without having to go through a website-admin. Link to add_ pages are in the dropdown under the login-button on the top-nav (only visible for logged in users with usertype staff or superuser). Link to edit and delete artists are on the bottom of the artist_detail-page, for artists, they are at the bottom of each performance-card on the artist_page, and for products, they are on the bottom of the card in the artist_product_detail-page.
- Users can search for keywords in performances-name and description, and get the related performance.
- Users may choose to see only artist of a particular type (choir or bands for instance), og to see performances of a certain genre (f.ex. jazz). Or to sort performances by artist, or artists by artist-rating, etc
- When you sort by a category, a box with the chosen genre is shown under the page-title, to inform the user of what choice has been made.
- How many results the page has, is shown descretely on the right side of the page.
- The main-nav buttons for "All artists" and for "All performances" have a direct link on the button to a page with all the instances, but also have a dropdown-menu on the side, to see the page sorted by for ex. by name or by artist.


#### Future features:
- The search-function currently only searches through titles and descriptions in the performances-model. The search will in the future also include artists, categories, artisttypes etc. to span all the information contained in the website.
- There will also be a possibility to sort artists by how much their cheapest and most costly products are (price low-high and high-low), and to sort performances by how many views they have had.
- Currently all the users with "artist-user-type" (staff) has access to delete and edit all the performances, artists and products on the website. They should naturally only be able to add, edit and delete items regarding their own artist (or artists). The plan is to add a owner-field to the artist-model, so that only the user that creates an artist has the right to edit that artist and all performances and products related to that artist.
- Artist ratings are now entered when you add a new artist, but this will in the future be something coming from customer-replies, and not from the artist themselves.

## Issues overcome
### Challenge with link from "all performances"-page to "artist-page"
There is a difficulty retreiving the django-artist.id at the all performances-page in order to link to the individual artist-page, because the performances-class only had the artist_id-field, and not the actual artist-id. The artist-page-view takes primary key artist.id (an integer) as input, but when retrieving the artist_id from "all performances"-page, it comes up as Artist: Artist object (6), instead of as 6. Whith sting-method on Artist-class "return self.artist_name" it comes up as the artist_name ex. Lucia Popp. Neither option works in the url and view for artist-page. The issue was solved by correct dotnotation.

### Links to edit and delete should not be clicked by accident
The edit and delete-links were at first so small and so close together, and also close to other links, that they could very easily be clicked by accident. The problem was sorted in a few different ways, by adding some distance to orther links, and by adding a horisontal line between these links at the bottom, and the rest of the content.
![Picture of edit and delete-links](static/readme_pictures/Edit_and_delete.PNG)



## Technology used
### Programming languages:
- HTML
- CSS
- JS
- Python
- Github
- Heroku
- Postgres database
- AWS Amazon Web Services

### Frameworks, libraries and programs:
- Bootstrap
- Google Fonts
- Font-awsome
- Django (incl. django-allauth, dj-database-url, django-crispy-forms)
- Werkzeug
- Stripe payments


## Testing

### Validation:

#### CSS validation
CSS-files checked with https://jigsaw.w3.org/css-validator/validator, and all is well.

#### JS validation, with https://jshint.com/
Some semicolons were missing, that are now fixed.


### Testing for user stories in UX-section:
Everything has been tested, and I've checked that all links are working. The only big problem is when you try to pay for an order, and then the page gets a server-error-message. I have not been able to fix that.

### Further testing:

#### Test on different browsers:
The site has been tested on chrome and on Firefox, and functions on both, but on Firefox the text is white for some reason. May just be a delay in updating?


### Fixed bugs:
#### Bug 1
![Picture of problem]()
Problem when deplying to Heroku "Error while running '$ python manage.py collectstatic --noinput'. Push rejected, failed to compile Python app." Heroku suggests the error has to do with static assets and directs to article: https://devcenter.heroku.com/articles/django-assets, where entereing a code-snippet into my settings.py-file is suggested as answer to problem. That fix did not change anything, so I connect directly to Heroku to try to disable the collect-static with "heroku config:set DISABLE_COLLECTSTATIC=1" as suggested by the article "if all else fails". But that just crashed the whole thing... I'll try to return the code for DATABASE in settings.py back to original (local database). Still not working.
In the log at Heroku I found the error h10, so I searched it and found this thread (https://stackoverflow-com.translate.goog/questions/14322989/first-heroku-deploy-failed-error-code-h10?_x_tr_sl=en&_x_tr_tl=no&_x_tr_hl=no&_x_tr_pto=op,sc) that suggests it may be something wrong with the Procfile. I removed a "space" from the Procfile, as suggested, and now there is still an error in Heroku, but it has changed from "crashed" do "down", and the new error is h14 "No web-processes running". I have worked back and forth with the Procfile to try to get it working, but still no luck, and my hard deadline is today, so I will leave it for now and fix  it before the resubmission.  

#### Bug 2
Problem missing fields in artist-admin and performance-admin. Artist name and several other fields are added in the artist-class, but does not show up in the django-admin.
![Picture of problem](static/readme_pictures/Artist_admin_missing_fields1.JPG)
![Picture of problem](static/readme_pictures/Artist_admin_missing_fields2.JPG)
![Picture of problem](static/readme_pictures/Artist_admin_missing_fields3.JPG)
The problem turned out to be some missing migrations that did not go through because of missing info in required fields. After temporary adding "default='MISSING'" to the required fields (artist_name, performance_name and artist_id), the migrations went through, and the correct fields are showing in the admin. The default-value has been removed again, so that input is required on new entries.
![Picture fixed](static/readme_pictures/Artist_admin_missing_fields4.JPG)

#### Bug 3 Overlay doesn't cover the home-page background-image
I tried so many things to fix the overlay-div that did not cover the page underneath. Working with css and html, but nothing made any difference. In the end, the problem was solved super-simply, by removing two classes from the overlay-div (100% and container). 
![Picture of non_covering_overlay](static/readme_pictures/Overlay_doesnt_cover_homepage_image1.png)




### Unfixed bugs:
### Problem with Stripe payments
When pressing the complete order-button, to pay for the order, there is a pause while the payment is processes, but then there is an error that brings up the Server-error-blank screen. In Stipe it seems to be working, and many "payments" have been received, but there are some problems with the webhooks. I have not yet been able to solve this problem, so when the server-error occurs, the only we to keep moving is unfortunately to press the back-button. Error message says the problem in in views.py line 63, but I cannot find what is wrong there. 




## Deployment
This project was created from a github-repository-template, and developed using Gitpod. It was regularily committed to git and pushed to GitHub using git-extensions in Gitpod. It has been deployd to postgres relational database through Heroku, and the media and static-files are hosted on AWS (Amazon Web Services). I use S3 (simple storage solution), 
To deploy: 
* First sign in to Heroku and choose to create a new app, with name similar to the project in Git. Go to the Resources-tab, and find the add-on for Postgres database (Heroku Postgres) (the free plan is sufficient). *
* Before using Postgres, go back to gitpod and install dj_database_url and psycopg2-binary (python3 install ...), and freeze the requirements (pip3 freeze > requirements.txt).
* Go to settings.py and add install Heroku database (import dj_database_url at the top and comment out the default "DATABASES"-settings, and add   DATABASES = {'default': dj_database_url.parse{}}   instead. For now you may add the DATABASE_URL from Heroku (find it at Heroku-Settings-Reveal Config Vars) into this, but make sure to NOT commit to git whis this key visible! Save it in the settings at Gitpod Dashboard (under your profile) as soon as possible. 
* Connect to Heroku through the terminal (heroku logon -i) and to stop Heroku from uploading the statis-files with the database (since they are going to be deployd on AWS), use command  "$ heroku config:set DISABLE_COLLECTSTATIC=1".
* Then migrate as usual (no need to makemigrations, as they are already ready). 
* Create Procfile, and go to Heroku to add deployment through GitHub.
* Create a user on AWS Amazon, create a bucket and a user (staticfilesuser). Add the credentials to Heroku.
* Allow Heroku to collect staticfiles by DISABLE_COLLECTSTATIC=0


### Steps to deploy this page on Heroku from GitHub repository:

### Forking the GitHub repository:
Go to the project-page in Github https://github.com/Gurimarie/Entertainments-r-us/tree/main and click on the fork-symbol in the top-right corner of the page.
![Picture of fork-symbol](static/readme_pictures/Fork1_Fork_symbol.JPG)
On GitHub.com, navigate to your fork, open it, and click the Code-button. 
![Picture of code-button](static/readme_pictures/Fork2_Code_button.JPG)
Choose your preferred way of cloning the repository (HTTPS, SSH or Github CLI), and then open Git Bash. Change the current working directory to the location where you want the cloned directory.
Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub username instead of YOUR-USERNAME: "$ git clone https://github.com/YOUR-USERNAME/Entertainments-r-us". Press Enter. Your local clone will be created.


## Credits

### Code:
- https://github.com/PaulFrankling/discover-north-yorks used for README-structure.
- In setting up this project I have followed closely the sequence of the run-through-project "Project Boutique Ado" in the Code Institute courses. The structure and scope of my database is different from the one in the school-project, and therefore my models and views and forms are also different. 

### Content:

### Media used:
Images for "artists" from https://pikwizard.com/ ("Free Stock Photos")

