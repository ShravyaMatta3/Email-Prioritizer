# Email Prioritizer App

## Overview
The Email Prioritizer App is a web application that helps users manage their emails more effectively by categorizing them based on priority. It integrates with Gmail for user authentication and provides a simple dashboard to view and prioritize emails.

## Features
- User Authentication: Users can log in to the app using their Gmail accounts.
- Dashboard: Upon logging in, users are presented with a dashboard displaying their email inbox.
- Prioritization: Emails are categorized as urgent or normal based on their received time.
- Logout: Users can log out of the app to securely end their session.

## Technologies Used
- Backend: Python with Flask framework
- Authentication: Google OAuth for Gmail integration
- Frontend: HTML and CSS for basic UI
- Google OAuth Libraries: `google-auth`, `google-auth-oauthlib`

## Getting Started
1. Clone this repository to your local machine.
2. Set up a Google OAuth 2.0 client ID and client secret.
3. Create a `client_secret.json` file with your client secret.
4. Install the required Python packages using pip: `pip install flask google-auth google-auth-oauthlib`.
5. Run the Flask app by executing `python app.py` in your terminal.
6. Open your web browser and navigate to `http://localhost:5000` to use the app.

## Usage
- Click on the "Login with Google" button to authenticate with your Gmail account.
- Once logged in, you'll be directed to the dashboard where you can view your emails categorized by priority.
- Click on the "Logout" button to securely log out of the app.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
