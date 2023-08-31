

# Protected Website with Passcode

This project demonstrates a password protected website that requires a passcode for access. It consists of a simple frontend interface and a backend HTTP server implemented in Python.

## Description

The website project showcases a basic implementation of password-protected content. It includes a frontend interface where users can enter a passcode, and a backend server that validates the passcode and grants access to protected content if the passcode is correct.

## Features

- User-friendly frontend with an HTML form for entering the passcode.
- Backend server that validates the passcode and provides access to password locked content.
- Protection against unauthorized access to the secret content.

## Prerequisites

To run this project, you need:

- Python 3.x

## Installation

Follow the steps below to install and run the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/DataDeity/Password-Protected-Website
   ```

2. Navigate to the project directory:
   ```bash
   cd Password-Protected-Website
   ```

## Usage

To use the website:

1. Update the `do_GET` method in `main.py` to specify the correct path to your `index.html` file. Modify the following line:
   ```python
   self.path = "path/to/index.html"
   ```
   Replace `"path/to/index.html"` with the actual path to your `index.html` file.

2. Start the HTTP server by running the `main.py` script:Fcf
   ```bash
   python main.py
   ```

3. Open a web browser and visit `http://localhost:8000` to access the website.

4. Enter the correct passcode to unlock the secret content.

5. If the passcode is incorrect, the page will be reloaded to try again.

## Code Explanation

### Frontend (index.html)

The `index.html` file represents the frontend of the website. It contains an HTML form where users can enter a passcode. Upon submission, the passcode is sent to the server for validation.

### Backend (main.py)

The `main.py` file represents the backend of the website. It sets up an HTTP server using Python's `HTTPServer` and `SimpleHTTPRequestHandler` classes.

#### CustomHandler Class

The `CustomHandler` class extends the `SimpleHTTPRequestHandler` class to override the default request handling behavior.

##### `do_GET` Method

The `do_GET` method is responsible for handling GET requests. In this project, it is modified to serve the `index.html` file when a GET request is received. You need to update the `self.path` variable to specify the correct path to your `index.html` file.

##### `do_POST` Method

The `do_POST` method is responsible for handling POST requests. It reads the passcode sent from the frontend and compares it with a predefined password. If the passcode matches, the server sends a "success" response back to the client. Otherwise, it sends a "failure" response.

##### `start_http_server` Function

The `start_http_server` function is responsible for starting the HTTP server. It creates an instance of the `HTTPServer` class, passing the server address and `CustomHandler` as parameters. The server is then started using the `serve_forever` method.

## Customization

You can customize the project in the following ways:

- Passcode: To change the passcode, modify the `password` variable in the `do_POST` method of the `CustomHandler` class in `main.py`.

- Content: Customize the content of the protected website by modifying the `index.html` file.

## TODO

Here are

 some potential improvements and additions that you can consider:

- Implement user authentication for more secure access.
- Enhance the frontend design and user experience.
- Implement encryption for storing and validating passcodes to enhance security.
- Secure the second page to prevent viewing the HTML code before entering the correct password.


## Acknowledgments

The project was inspired by the TheInvasionHasBegun.com

## Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to submit a pull request.

## Contact

If you have any questions or suggestions, please feel free to reach out.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).
