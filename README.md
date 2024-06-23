![image](https://github.com/alimalek80/weather_forecast_django_app/assets/21648858/88dfa8b3-41c3-40ac-9d4e-d27ad4415c1f)

# Weather Forecast Django App
This is a Django application that allows users to compare the weather forecast for two different cities.
## Features
- Users can enter the names of two cities.
- The application retrieves the current weather and 7-day forecast for each city from the Weather API (https://www.weatherapi.com/docs/).
- The application displays the weather data for each city side-by-side.
## Requirements
- Python 3.6 or later
- Django framework (https://www.djangoproject.com/)
- requests library (https://pypi.org/project/requests/)
## Installation
1- Clone the repository:
```bash
git clone https://github.com/alimalek80/weather_forecast_django_app.git
```
2- Navigate to the project directory:
```bash
cd weather-forecast-app
```
3- Create and activate a virtual environment (optional but recommended).
4- Install the required dependencies:
```bash
pip install requests
```
5- Create a file named `API_KEY` in the project root directory and store your Weather API key in it. **Important:** Do not commit this file to your version control system.
6- Run the following command to create a Django project and app:
```bash
python manage.py startapp weather_forecast_app
```
7- Update the ```settings.py``` file of your Django project to include the ```weather_forecast_app``` app:
```python
INSTALLED_APPS = [
    # ... other installed apps
    'weather_forecast_app',
]
```
8- Run the following command to start the development server:
```bash
python manage.py runserver
```
## Usage
- Visit http://127.0.0.1:8000/ in your web browser.
- Enter the names of two cities in the text boxes.
- Click the "Compare Weather" button.
- The application will display the current weather and 7-day forecast for each city.

