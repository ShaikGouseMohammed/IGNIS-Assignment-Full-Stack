Project Overview

This project is a full-stack web application designed to scrape product data and display it through a frontend interface. The backend is powered by Django and Scrapy, while the frontend is built using modern web technologies.
Prerequisites

Ensure you have the following installed:

    Python 3.x
    Django
    Scrapy
    requests
    beautifulSoup
    react
    react-bootsraps
    djangorestframework
    

Getting Started
Step 1: Scrape the Data

To begin, navigate to the backend root folder of the project and execute the following command:


   scrapy crawl nobero

This command will initiate the data scraping process. Upon completion, a product.json file containing the scraped data will be created in the backend root folder.
Step 2: Start the Backend Server

After scraping the data, you need to start the backend server. Navigate to the backend folder and run:



  python manage.py runserver

This will launch the Django development server, making the backend API available for the frontend to consume.
Step 3: Start the Frontend

With the backend server running, the next step is to start the frontend. Navigate to the root folder of the frontend (where package.json is located) and run:



   npm start

This will start the frontend development server, allowing you to view and interact with the scraped data through your web browser.
Additional Notes

    Ensure that both the backend and frontend servers are running concurrently to see the full functionality of the application.
    The product.json file is essential for the frontend to display the scraped data correctly, so make sure it is generated before starting the servers.

Conclusion

With everything set up, your application should now be fully functional, scraping data and displaying it through a user-friendly interface.
