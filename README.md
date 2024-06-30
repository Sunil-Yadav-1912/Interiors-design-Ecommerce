# Flask Web App - Digital Deals

## Dependencies

- Python 3.11
- Flask

## Overview

Elegant Interiors is a full-stack web application built to cater to users interested in purchasing high-quality interior design products such as furniture, decor items, lighting fixtures, and more. The platform offers a user-friendly interface that allows customers to browse a wide range of products, customize them according to their preferences, and securely make purchases online.


## Features

--  Secure user registration and login functionalities.

--  Comprehensive product listings with detailed descriptions, images, and pricing information.

--  Seamless shopping cart experience with add, remove, and update functionalities.

--  Order tracking and status updates for customers.

--  Fully responsive design ensuring optimal performance on desktops, tablets, and mobile devices.


## Installation

- Clone the repository
- Install the dependencies
- Run the app
  

## Usage

- Run the app
- Navigate to http://localhost:5000/
  

## Technologies Used

### Backend:
- Flask (Python web framework)

### HTML5, CSS3
- JavaScript (AJAX for dynamic updates)
- Bootstrap (Responsive CSS framework)

### Database:
- Firebase


## Architecture

Made in a traditionally used worldwide MVC Architecture. Below is the architecture of the project.

### Models : Connections and all database operations are declared in models.

### Views : UI and UX files are included inside views which is arranged systematically here. Html files are inside templates and all the css, js and images are included in static directory.

### Controllers : Logical part and calls to database operations are defined inside controllers.

## Project Structure


### App : Main file of the project. It includes all the routes as well as their logical output.

### Config : All the configuration values as well as credentials are ectracted from env here for ensuring the security of credentials.

### Database : All the database operations are included here.

### Environment : Whole project depends on the environment module and it's variables defined in the env file but due to privacy I have cleared the env values you need to put your database credentials and keys for proper running of the project.

