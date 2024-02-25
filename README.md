# restaurante-finder-app
GeoTech group programming course repo

Sirak
Joesph
Gullimer

About the App
Resturante locator is a website created to help Geospatial Technology student to locate a suitable restaurant near the campus. It allows users to filter by certain pefernces and also allows users to comment on their experience in a restaurant they visited. Users also have an additional feature where they can use the website to get directions to a chosen restaurant. Restaurants close to Nova Information Management School (NOVA IMS), Lisbon and University of Münster (UM), Institute for Geoinformatics (IFGI), Munster were considered for the app since these will be the two campuses that students will be on during their program.

Functionality of the Website.
The entire process of the website can be divided into three many components namely:
1. Extract, Transform and Load.
2. Utilizing APIs with the Django framework to make and receive API calls
3. Create, Read, Update and Delete.
4. Docker


#1. Extract, Transform and Load
Google Places API was used to retrieve resturants within a distance of 1000 meters  from both NOVA IMS and igfi schools. The API call returned a json with restaurants that met this requirements alongside the various information about them such as the type of food they sell.The data was then stored into an excel sheet in order to understand the data properly. A code was then implemented to extract the information from the excel sheet automatically. The data was cleaned (TRANSFORM) and the refined data was then loaded in a database created with postgres(LOAD). ## Sirak- talk about the various column names that were created in the database ##.

#2 Utilizing APIS with the Django framework to make and receive API calls
In order to prevent users  from editing information directly from the database, APIs was used as an intermediary between the user and the database. The Django framework was utilized in achieving this. API calls were made when the user navigated from one page to another as well as when they made, edited and deleted comments. This improved the security of the database and prevented the database from being infiltrated.

#3 Create Read Update and Delete
A comment section was created under each restaurant. Users can CREATE comments, READ other users comments, UPDATE their comments by making edits to it as well as DELETE their comments.

#4 The various parts of the website was put in a docker container which was used to fetch various parts of the websites.


# Additional Functions
Open Streets Map and Leaflet Js was used to create a map where users could navigate from their current location to a selected restaurant. The user has the option of getting directions to a selcted restaurant. The is created on the map and the route gets updated as the user moves. The routing guides the user on the path to take untill he finally gets to his destination


# The Website.
The website is made of different pages. The pages are as follows:
- Home
- About
- Map
- Restaurants
- Register ( If the user is not logged in)
- Login (If the user is not logged in)
- Logout Button (If the user is logged in)

- HOME
The main page is the home page. The home page initially displays few top highly rated restaurants.The user additionally has the choice to select the university they want to explore for nearby restaurants, along with specifying the rating of the restaurants they wish to view.The restaurants that meet the requirments are displayed when the user clicks on the submit form button.
   These restaurants are obtained from the database which contains the restaurants that were obtained from the google api and the ones that were added by the admin. The addition of restaurants by the admin would be explained further in this Read Me. The user can filter the restaurants that are being displayed by searhing by the restaurant name. The other parts of the website just gives additional information on what the user can do with the app such as leaving a review, finding a restaurant near him and requesting an addition of a new restaurant.

- About
This page gives a brief overview of what the website is about. It also shows the people who developed the website namely, Joseph, Guilherme and Sirak alongside their respective email accounts. This will allow the user to contacdt any of the developers if they experience a problem with the website or want to add their restaurant on to the website. There is also a button named "View Restaurants" which users can use to go the "Restaurants" page directly.

- Map
This page shows a map that was created with leaflet. The default base map is Opem Street Up. The user can use the layer control icon on the top right to change the base map to Satellite Map, Google Street Map or Hybrid ( which combines the satellite map and the google street map). The user can utilize the dropdown button located below the layer control to determine which university they wish to observe regarding restaurants around the school they intend to locate.
When the user selects a university from the drop down list, the map is zoomed to that particular university and the university can be seen with a green marker while the restaurants near the university are displayed with a green marker. The Location of the user is displayed with a blue circle. Additionally, the user can click on a restaurant icon to display the name of the restaurant. This is to give the user an idea of the

- Restaurants
This page lets users see all the restaurants in our database without any limits. Users can explore freely without needing to set any rules or conditions. It's like opening a door to a world of different places to eat.

-Register
This button is used for registering new users on to the platform. Users must provide their name, username, email and password in order to register. An email is automatically sent to the user after they register to welcome them to the platform.

- Login
  A user who has already been registered on the platform can login in with his user name and password.

- Logout
A user who is logged in can log out of the website using the logout button.

# Website Functionality


