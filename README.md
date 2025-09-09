# Tashrifat Saadat - Event Management Website

Hey there! Welcome to the repository for the Tashrifat Saadat project. This is a website for an event management company, designed to showcase their services and provide a point of contact for potential clients. It's built with Django and has a clean, modern frontend.

## What's Inside?

This project is a fully functional website that allows the company to manage and display their event services. It's designed to be easy to navigate for users and simple to manage for the site administrators.

### Key Features

*   **Service Listings**: Add, edit, and display various event services. Each service can have its own detailed description, pricing model (fixed, price range, or by agreement), and guest capacity.
*   **Dynamic Menus**: Create and attach specific menus to each service. If you're offering a catering package, you can list all the food and drink items right on the service page.
*   **Image Galleries**: Upload and manage a gallery of photos for each service. You can categorize images to create different showcases, like main galleries, sliders, or featured images.
*   **Contact Form**: A simple and effective contact form for potential clients to get in touch.
*   **Custom Admin Panel**: The Django admin panel is customized for a more intuitive content management experience, all in Persian.

## Getting Started

Ready to run the project locally? Here’s how you can get it up and running.

### Prerequisites

*   Python 3.8+
*   npm

### Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/init050/Tashrifat-Saadat.git
    cd Tashrifat-Saadat
    ```

2.  **Set up a Python virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the Python dependencies:**

    This project was built with Django 5.1.2. You'll also need a couple of other packages. You can install them with pip:

    ```bash
    pip install Django==5.1.2 django-render-partial django-jalali
    ```
    *A `requirements.txt` file was not included, but these are the main dependencies.*

4.  **Install the frontend dependencies:**

    ```bash
    npm install
    ```

5.  **Build the CSS:**

    The project uses Tailwind CSS. Run the following command to compile the CSS. You can keep this running in a separate terminal to automatically rebuild the CSS when you make changes.

    ```bash
    npm run build-css
    ```

6.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

7.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The site should now be running at `http://127.0.0.1:8000/`.

## How to Use It

*   **Main Website**: Just navigate to `http://127.0.0.1:8000/` to see the live site.
*   **Admin Panel**: To access the admin panel, you'll first need to create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create your admin account. Then, you can log in at `http://127.0.0.1:8000/admin/`.

## Technologies We Used

*   **Backend**: Python, Django
*   **Frontend**: HTML, CSS, JavaScript, Tailwind CSS, DaisyUI, Flowbite
*   **Database**: SQLite3 (for development)

## Future Ideas

This project is a great starting point, but there's always room to grow. Here are a few ideas for future improvements:

*   **Client Accounts**: Add a user registration and login system for clients to track their inquiries or bookings.
*   **Online Booking**: Implement a full-fledged booking system where clients can reserve services directly on the site.
*   **Add Tests**: Write unit and integration tests to ensure the application is robust and reliable.

Thanks for checking out the project! If you have any questions, feel free to open an issue.
