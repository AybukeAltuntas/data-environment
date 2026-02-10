

import os

def start():

    """
    Determines the application start mode based on the FLASK_ENV
    environment variable.

    Returns:
        str: A message indicating whether the app is running in
        development mode, production mode, or empty mode.
    """
    flask_env= os.getenv("FLASK_ENV")
    if flask_env == "development":
        return "Starting in development mode..."
    elif flask_env == "production":
        return "Starting in production mode..."
    else:
        return "Starting in empty mode..."


if __name__ == "__main__":
    print(start())
