# Secure HTML Encryptor 🔒
## Overview
Secure HTML Encryptor is a powerful tool designed to encrypt HTML files with a password, ensuring your static HTML content is secure and private. This tool encrypts your HTML and allows it to 'self-decrypt' upon entering the correct password, making it an ideal solution for hosting static, secure web content.

## Features
🔐 Password Protection: Encrypt your HTML files with a strong password.

🔓 Self-Decryption: Automatically decrypts content upon entering the correct password.

🌐 Static Hosting Compatibility: Ideal for secure hosting on any static web hosting service.

🚀 Easy to Use: Simple and user-friendly interface for encryption and decryption.

🛡️ Enhanced Privacy: Keep your HTML content private and secure.

## How It Works
Encrypt Your HTML: Use our tool to encrypt your HTML file with a password of your choice.
Host Your File: Upload the encrypted file to your static web hosting platform.
Access Securely: When accessing the website, you'll be prompted to enter the password.
Automatic Decryption: Upon entering the correct password, the HTML content is decrypted and displayed.
## Advantages
🔄 Self-contained: No need for server-side processing for decryption.

🕵️‍♂️ Privacy-focused: Ensures your HTML content is only accessible to those with the password.

⚡ Speed: Fast decryption process without any noticeable delay.

🛠️ Developer-friendly: Easy integration into your existing workflow.

🌍 Accessibility: Access your secure content from anywhere, on any device.

## Usage
Clone this repository and install the required packages:
```
pip install -r requirements.txt
```

Run the following commands to encrypt the HTML file with the specified password:
```
python embed.py <your-html.html> embedded.html
python -m http.server
python encrypt.py embedded.html <your-password> encrypted.html
```

Replace <your-html.html> and <your-password> with the appropriate values for your use case.
This tool allows you to securely encrypt an HTML file and require a password for access, ensuring that the content remains protected and not publicly accessible.