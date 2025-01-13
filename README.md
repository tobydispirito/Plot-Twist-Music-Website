# Music Portfolio Website

A responsive and dynamic website showcasing all my music releases, designed to streamline updates and develop my coding skills.

---

## Live Website

The website is live at [https://plottwistmusic.uk/](https://plottwistmusic.uk/)

<br/>
<br/>

The website is hosted with a custom domain using [https://www.cloudflare.com/](https://www.cloudflare.com/) and [https://render.com/](https://render.com/)

---

## Description

This project was an excellent challenge to advance my coding skills and web development. The website is designed to:
- Host all my current and future music releases.
- Provide a seamless, responsive user experience across all devices and resolutions.

To efficiently manage new music releases, the website dynamically generates pages based on data stored in a SQL database. This eliminates the need to manually code new pages for each release, making the process scalable and efficient.

An admin panel with secure login functionality enables CRUD (Create, Read, Update, Delete) operations on the database. User credentials are hashed and salted using **Werkzeug** for added security.

<br/>

See below for an idea of how the website scales with resolution, when many track entries are available:

![scaling](/static/images/scaling_in_action.gif)

---

## Features

- Dynamic page generation for music releases.
- Fully responsive design across all devices.
- Secure admin login with hashed and salted credentials.
- Admin panel for managing music release data (CRUD operations).
- Hosted on a custom domain for accessibility and branding.

---

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**  
   Use the following command to clone the repository to your local machine:  
   ```bash
   git clone https://github.com/tobydispirito/Plot-Twist-Music-Website.git

2. **Install dependencies**
    Navigate to the project directory and install the required Python packages from requirements.txt:
    ```bash
    cd Plot-Twist-Music-Website
    pip install -r requirements.txt

3. **Set up environment variables**
    Configure the required environment variables for the project:

    - APP_CONFIG_DATABASE_URI: The URI for the database used in the project.
    - APP_CONFIG_SECRET_KEY: The secret key for the Flask application.

4. **Run the project**
    Open the project in your preferred IDE and run the application
