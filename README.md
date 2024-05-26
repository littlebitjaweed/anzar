# POS-system-with-Django-
This is a Point of Sale (POS) system using Python's Django Framework.

# Django POS System

This is a simple Point of Sale (POS) system built with the Django framework. The application allows you to manage products, record sales, print sales receipts, and process payments using Stripe.

## Features

- Manage products (add, edit, delete)
- Record sales transactions
- Print sales receipts
- Integrate with Stripe for payment processing

## Requirements

- Python 3.6+
- Django 3.0+
- Stripe API keys

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/django-pos-system.git
    cd django-pos-system
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Stripe API keys:**

    In `pos_system/settings.py`, add your Stripe API keys:

    ```python
    STRIPE_PUBLIC_KEY = 'your-public-key'
    STRIPE_SECRET_KEY = 'your-secret-key'
    ```

5. **Run database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser for the admin interface:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

### Admin Interface

1. Go to `http://127.0.0.1:8000/admin/`.
2. Login with the superuser credentials you created.
3. Add and manage products from the admin interface.

### POS Functionality

1. **View Products:**

    Go to `http://127.0.0.1:8000/` to see the list of products.

2. **Add a Sale:**

    Click on the "Add Sale" link next to a product. Enter the quantity and submit the form.

3. **Process Payment:**

    After adding a sale, you will be redirected to the payment page. Click on the "Checkout" button to process the payment using Stripe.

4. **Print Receipt:**

    After a successful payment, you will be redirected to the receipt page. Click the "Print" button to print the sales receipt.

### Custom Filters

A custom template filter for multiplication is included in `pos_app/templatetags/multiplication.py`.

## Project Structure

- `pos_system/` - Django project settings and configurations.
- `pos_app/` - Main application with models, views, and templates.
- `templates/pos_app/` - HTML templates for the application.
- `static/` - Static files (CSS, JavaScript).
- `requirements.txt` - List of Python dependencies.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Stripe](https://stripe.com/)

## Contact

If you have any questions or feedback, please contact davidomuga@gmail.com.


