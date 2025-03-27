# QR-Code-Authenticator
Overview

This project is a simple web-based QR code verification system where users can upload images from two different folders:

First Print Folder: Displays the output as "Original"

Second Print Folder: Displays the output as "Counterfeit"

The webpage allows users to upload an image and receive instant feedback on the same page.

Features

Upload QR code images from two predefined folders

Display result without refreshing the page

Responsive UI with a centered layout

Styled using CSS with a blue-themed design

Background image included for a visually appealing interface

Technologies Used

Frontend: HTML, CSS, JavaScript

Backend: Flask (for handling file uploads and QR code verification)

Setup Instructions

1. Clone the Repository
   git clone https://github.com/yourusername/qr-code-verification.git
   cd qr-code-verification

2.  Install Dependencies

If using Flask as the backend, install required packages:
pip install flask

3. Add the Background Image

Move your background image to the static/images/ directory and update the CSS in index.html:
static/images/qr_background.jpg') no-repeat center center/cover;

4. Run the Flask Server
   python app.py

5.  Open the App in a Browser

Go to http://127.0.0.1:5000 to access the web application.

File Structure -
qr-code-verification/
│── static/
│   ├── images/
│   │   ├── qr_background.jpg
│── templates/
│   ├── index.html
│── app.py
│── README.md
│── requirements.txt

Future Enhancements

Implement actual QR code scanning

Add database support for tracking verification results

Improve UI with animations and better error handling

Background Image -

![360_F_529863341_cxKCD4AdKCnQUSLxIRENxFfKSF1zjkVy](https://github.com/user-attachments/assets/c1c386c1-876d-4d7b-830f-118d788d7d7b)






