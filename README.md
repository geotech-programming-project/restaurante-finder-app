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
The main page is the home page. The home page displays the restaurants near the various campuses. These restaurants are obtained from the database which contains the restaurants that were obtained from the google api and the ones that were added by the admin. The addition of restaurants by the admin would be explained further in this Read Me. The user can filter the restaurants that are being displayed by searhing by the restaurant name. The user additionally has the choice to select the university they want to explore for nearby restaurants, along with specifying the rating of the restaurants they wish to view.The restaurants that meet the requirments are displayed when the user clicks on the submit form button. The other parts of the website just gives additional information on what the user can do with the app such as leaving a review, finding a restaurant near him and requesting an addition of a new restaurant.

- About
