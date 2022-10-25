# **_Second Scoop_**

<a href="#" target="_blank" rel="noopener">Second Scoop</a>(press for Live DEMO) is a website designed as a "real world application", the website is devided into two parts. One part is for users to see a appealing front-end website which shows them information about the restaurant, allows them to create an account, make a reservations, write a post, contact the admin and more. The other part of the website is a management system for admin of SecondScoop. If an account has the correct permissions, the admin will be able to see special features which will allow them to manage posts,reservations,comments and approve reservations.

# Table of contents
1. <strong>[Objective](#objective)</strong>
2. <strong>[User Experience UX](#experience)</strong>:
    * [User Stories](#user)
    * [FlowChart](#flow)
    * [Site Structure](#structure)
    * [Typography](#typo)
    * [Color Scheme](#color) 
    * [Project Management](#management)
3. <strong>[Existing Features(User)](#user-features)</strong>:
    * [Site Navigation](#nav)
    * [Welcome Modal](#modal)
    * [Registration for user](#user-reg)
    * [Presentation Slider](#slider)
    * [Menu Page](#menu)
    * [Events Reservations](#events)
    * [Contact page](#contact)
    * [Dropdown Account button](#dropdown)
    * [Blog](#blog) 
4. <strong>[Existing Features(Admin)]</strong>:
    * [Admin Panel](#admin)
    * [View All Reservations](#view-reservations)
    * [View All Messages](#view-messages)
    * [Delete Comments](#delete)
5. <strong>[Future Features](#future-features)</strong>:
    * [Improve Reservations Features](#improve)
    * [Add Automatic Emails](#emails)
    * [Better User Profile](#better-profile)
    * [More features for Admin section](#more-feat)
6. <strong>[Technologies Used](#technologies)</strong>
7. <strong>[Python Packages](#packages)</strong>
8. <strong>[Testing](#testing)</strong>
9. <strong>[Deployment To Heroku](#deploy)</strong>
10. <strong>[Cloning This Project](#clone)</strong>
11. <strong>[Credits](#credits)</strong>:
    * [Content](#content-credits)
    * [Media](#media)
12. <strong>[Acknowledgments](#acknoledge)</strong>



# Objective <a name="objective"></a>

* The major goal is to prove  a high level of expertise in HTML, CSS, JavaScript, Python, and the Django Framework, as well as how important it is to conduct testing throughout.

# UX

## User Stories <a name="experience"></a>

## Flowchart <a name="flow"></a>

 The Flowchart for Second Scoop was made in Lucidchart.
 ![lucidchart]()
 
## Site Structure <a name="structure"></a>

 Second Scoop purpose is to bring together all dessert lovers and improve their services through customer opinions and interactions,offering blog option and also reservation system so users can experience themselvesthe delicious desserts .

## Typography <a name="typo"></a>


## Color Scheme <a name="color"></a>
Color scheme was created on <a href="https://coolors.co/">Coolors</a>
![color-scheme](/templates/images/colors.png)
## Project Management <a name="management"></a>

## Existing Features(User) <a name="user"></a>
 
Second Scoop is set up to be easy to use . It contains features that a user would be fimiliar with such as user login,user log out,reservations and contact forms, blog posts all offering options to create,read,update and delete(CRUD).

## Site Navigation
 * ## Heading and Title
 
## Modal <a name="modal"></a>
 * Displays Modals of Welcome to direct user to log in or create a new account.

 ![modal](/templates/images/modal.png)

## Slider  <a name="slider"></a>
 * Includes the name of the website and a slider showing their delicious desserts .

 ![slider](/templates/images/slider.png)

 * ## User Area

 * User Registration -  has built-in authentication and authorization to check certain criteria is met before an account is validated. All passwords are hidden for security purposes.
 ![register]()
 * Log In - existing users will ahve to pass authorisation with entering their current username and password to match the database.
 ![login](/templates/images/signin.png)
 * Log Out - Users can log out easily and a warning message will be displayed .
 ![logout](/templates/images/signout.png)

 Once logged in, user will see:

 * Menu - a display of some of their recipes with pictures gallery and description.
 * Event Reservations -CRUD - offering options to create new request with authorisations criteria including : name,date(as a pop up calendar),phone number,number of guests,and message. Once created the reservations will show in Check reservations,there will show if it was approved by the admin or not and also giving options of updated or delete it .
 ![events-page]()
* Contact page - CRUD - displaying a map, offering option of sending a message, after the message is sent in the check you messages tab user can see the messages send and if it was read by admin or not, also can edit or delete any message. 
![contact-page]()
* A Drop Down button with specific username and under that tab will be options to check event,messages or LogOut.
* Blog - CRUD - this button will display all the posts by other users and each post will have details and offer comment sections to allow users to interact. Every comment or post will be approved by the user before displayed.Users can delete or edit their own post only.
![posts-page]()


 * ## Admin Area - SuperUser
 * From the Pop Up Modal Admin can LogIn .
 * As Admin :
 1.Can manage all the users.
 2.Can check and approve or disapprove posts.
 3.Can answer messages.
 4.Can approve events for specific number of guests

 ![admin-page]()

 # Future Features
 * In future I am planning on adding Gallery page for images from specific events to attract users.
 * Adding special events where you can book your spot through the site.

 * ## Technologies Used
# FRONT-END:
* [HTML5](https://www.w3schools.com/html/) - provides the content and structure for the website.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) - provides the styling.
*[BOOTSTRAP](https://getbootstrap.com/) - provides specific styling.
* [JavaScript](https://www.w3schools.com/js/)-provides interactivity.
* [Gitpod](https://www.gitpod.io/#get-started) - used to deploy the website.
* [Github](https://github.com/) - used to host and edit the website.


# BACK-END:
* [PYTHON](https://www.w3schools.com/python/) to get details from the user and validate the inputs with python logic.
# Heroku : used for app hosting.


# Testing:

# Lighthouse

# Browser Compatibility

# Known bugs:

# Deployment: 
The site was deployed to Heroku pages.
1. First we have to create our app on heroku website.
![createapp](/images/createapp1.png)
2. Name the app.
![create2](/images/nameapp2.png)

3. Setup config vars.
![config](/images/setupconfig.png)

4. Select Buildpacks.
![buildpacks](/images/buildpack.png)

5. Choose Deploy Section and Heroku CLI.
![heroku](/images/deploy1.png)

7. Follow the steps bellow.
   To install into terminal:
   Log into heroku : heroku login - i
   * Next command : heroku apps
   * Next command: <app-name> with the actual app name and remove <> : heroku git: remote -a <app_name>
   * Now we have remote control over the app and we can push our changes straight to heroku terminal.
   * MFA/2FA enabled? - click Account setting on heroku website.
                - scroll down to API and click Reveal and Copy the key.
                - command: heroku config and enter api key
                -enter heroku username
                enter api key and press entered.
    After installation I followed the next steps:
![deploy2](/images/deploycli.png)

# Credits

### Content
* Tutors for directing me for some of the functions.
* Some of the code ideas came from  [Stack Overflow](https://stackoverflow.com/).


 # Acknowledgements
The site was completed as a Portfolio 4 Project  Full Stack Software Developer at the [Code Institute](https://codeinstitute.net/). As such I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) , Slack community and Code Institute Tutor Support for their help and support.

Mihaela Younas 2022.
