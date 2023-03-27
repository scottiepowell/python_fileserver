This is a simple Flask application that allows users to upload and download files. The application is containerized using Docker, and can be run using docker-compose.

## Requirements

-   Docker
-   Docker Compose

## Usage

1.  Clone this repository to your local machine.
2.  Create a `.env` file in the root directory of the project and add the following variables:
    
    `FLASK_HOST=localhost FLASK_PORT=5000`
    
    You can change the values of these variables to suit your needs.
3.  Build the Docker image by running the following command in the root directory of the project:
    
    `docker build -t fileserver .`
    
4.  Start the application by running the following command in the root directory of the project:
    
    `docker-compose up`
    
    This will start the application and make it available at [http://localhost:5000](http://localhost:5000/).
5.  To stop the application, run the following command:
    
    `docker-compose down`
    
## Endpoints

-   `/` - The index page of the application.
-   `/upload` - The page where users can upload files.
-   `/download` - The page where users can download files that have been uploaded.

## Notes

-   Uploaded files will be stored in the `UPLOAD_FOLDER` directory.
-   The allowed file extensions for uploads are set in the `ALLOWED_EXTENSIONS` set.
-   The Flask application is set to run on the host and port specified in the `.env` file. If these variables are not set, the defaults are `localhost` and `5000`, respectively.
-   The Dockerfile uses the official Python 3.8 image as the base image and installs any needed packages specified in `requirements.txt`.
-   The `flask run` command is used to start the Flask application. The `--host=0.0.0.0` option is used to allow connections from outside the container.
