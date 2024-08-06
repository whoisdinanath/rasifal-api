# Hamro Patro Scraper API

This project is a Django-based web application that scrapes data from Hamro Patro and provides an API to access the scraped data. The API is built using Django REST Framework.

## Features

- Scrapes daily horoscope data from Hamro Patro.
- Provides a RESTful API to access the scraped data.
- Endpoints for listing horoscopes and retrieving specific horoscope details.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/hamro-patro-scraper-api.git
    cd hamro-patro-scraper-api
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

### API Endpoints

- **List all horoscopes**
    ```http
    GET /rasifal/
    ```


### Example Requests

- To list all horoscopes:
    ```sh
    curl -X GET http://127.0.0.1:8000/rasifal/
    ```


## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.

---

Feel free to customize the description as per your project's specifics.