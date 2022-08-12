# If you haven't pipenv package to manage virtual environment
pip install pipenv

# To activate virtual environment
pipenv shell

# To install all required packages
pipenv sync

# To start the server
cd app && uvicorn app.asgi:application && cd ..


# Login & password for admin
# friend - 123