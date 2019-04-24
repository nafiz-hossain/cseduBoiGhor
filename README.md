# cseduBoiGhor


cseduBoiGhor is a Flask-based web application that allows users to manage their book collections. The primary purpose of this application is to provide users of cseDu with a platform to organize and track their books effectively. 

## Key Features:

1. **User Authentication:** Users can register accounts using their email, password, name, phone number, and batch. Authentication is handled securely using Firebase Authentication.

2. **User Profiles:** Each user has a profile page where they can view and update their personal information, including their batch, email, name, and phone number.

3. **Book Listing:** Users can view a list of books either through a general book listing or through their individual profiles. 

4. **Adding Books:** Users can add books to their collection by providing the book's name and phone number.

5. **Error Handling:** The application incorporates error handling mechanisms for invalid input during registration, login, and book addition to ensure data integrity and security.

6. **Firebase Integration:** The application seamlessly integrates with Firebase services, including Firebase Authentication and the Firebase Realtime Database, to provide a scalable and reliable backend infrastructure.

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The idea for this project originated from personal frustration with existing book management methods. As a frequent reader and book lover, I wanted a more efficient way to organize and track my growing collection of books. Inspired by similar applications and online book databases, I decided to develop my own solution tailored to my specific needs and preferences. 

The motivation behind this project stems from a passion for both technology and literature. I envisioned a tool that would not only simplify book management tasks but also enhance the overall reading experience. By creating a centralized hub for book-related activities, users could spend less time on administrative tasks and more time enjoying their favorite books.


## Technologies Used
- Flask
- Pyrebase
- Jinja2
- Firebase Authentication
- Firebase Realtime Database

List all the technologies and libraries used in your project.

## Features
- User registration and authentication
- User profile management
- Displaying book lists
- Adding books to the database
- Error handling for invalid inputs
- Integration with Firebase services

## Configure Firebase:
- Create a Firebase project at Firebase Console
- Obtain the Firebase configuration settings and update config in app.py accordingly.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
# Usage
Run the application:
```bash
python app.py
```
- Access the application in your web browser at http://localhost:5000.
Provide instructions on how to install and use your application.

# Contributing
If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository
- Create a new branch (git checkout -b feature)
- Make your changes and commit them (git commit -am 'Add feature')
- Push to the branch (git push origin feature)
- Create a new Pull Request
- Provide guidelines for contributors who wish to contribute to your project.

