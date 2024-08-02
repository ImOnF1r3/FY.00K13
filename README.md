Cookie Extractor and Manipulator

The Cookie Extractor and Manipulator is a tool written in Python that allows you to extract, view, and modify cookies from a specific web page. This tool is particularly useful for security analysis, session manipulation, and simple CTFs (Capture The Flag) or for experimentation purposes.

Features:

- Cookie Extraction: Displays cookies received from a web page.
- Cookie Injection: Allows custom cookies to be set in HTTP requests.
- Header Display: Displays the HTTP headers of the response.
- Redirect Support: Automatically handles redirects.
- Retry Requests: Configures retry for failed requests due to temporary server errors.
- Credit Information: Displays the author's credits.

Prerequisites:

Make sure you have Python 3 installed on your system. You can check the version of Python with the command:

python3 --version

Installation:

1. Clone the repository:

   git clone https://github.com/ImOnF1r3/cookie-extractor.git
   cd cookie-extractor

2. Install the requirements:

   Use pip to install the required libraries. It is recommended to use a virtual environment:

   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   Include the following dependencies in the requirements.txt file:

   requests
   beautifulsoup4
   colorama

Usage:

Run the tool from the terminal using the following commands:

python3 C00K13.py [options].

Available Options:

-u, --url: The URL of the web page to be parsed.
-c, --cookies: Custom cookies to be set (name=value).
-inj, --inject: Inject custom cookies into the request.
-ext, --extract: Extracts and displays cookies from the response.
--key: Additional headers to set (name=value).
-cc, --credits: Displays the author's credits.

Examples of Use with PicoCTF (http://mercury.picoctf.net:17781/):

- Extract Cookies from a Web Page:

```
python edit_C00K13.py -u http://mercury.picoctf.net:17781/ -ext

Example Output:

Fetched http://mercury.picoctf.net:17781/ with status code 200.
Response Headers:
Content-Type: text/html; charset=utf-8
Content-Length: 2048
----------------------------------------
Cookies:
Name: name
Value: -1
Domain: mercury.picoctf.net
Path: /
Expires: None
Secure: False
HttpOnly: False
----------------------------------------
Page Title: Cookies
Page Snippet:

Cookies

Home

Cookies

Welcome to my cookie search page. See how much I like different kinds of cookies!

© PicoCTF
----------------------------------------
```

- Inject Personalized Cookies:

```
python edit_C00K13.py -u http://mercury.picoctf.net:17781/ -inj -c "name=18"

Example Output:

Fetched http://mercury.picoctf.net:17781/check with status code 200.
Response Headers:
Content-Type: text/html; charset=utf-8
Content-Length: 1184
----------------------------------------
Page Title: Cookies
Page Snippet:

Cookies

Home

Cookies

Flag: picoCTF{Check The CTF on PicoCTF}

© PicoCTF
----------------------------------------
```

Credits:

Author: ImOnF1r3
GitHub: https://github.com/ImOnF1r3

This tool is intended for educational and research purposes only. Use it responsibly and only on websites for which you have permission.

Translated with DeepL.com (free version)
