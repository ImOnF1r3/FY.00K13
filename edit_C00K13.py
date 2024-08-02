import requests
from bs4 import BeautifulSoup
import argparse
from colorama import init, Fore, Style
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Initialize colorama
init(autoreset=True)

def print_banner():
    """Prints the banner for the tool."""
    banner = f"""
    {Fore.RED}                                                      

888888 Yb  dP      dP"Yb   dP"Yb  88  dP   .d 88888 
88__    YbdP      dP   Yb dP   Yb 88odP  .d88   .dP 
88""     8P   .o. Yb   dP Yb   dP 88"Yb    88 o `Yb 
88      dP    `"'  YbodP   YbodP  88  Yb   88 YbodP       

				     ImOnF1r3                               
                                                   
    {Style.RESET_ALL}
    """
    print(banner)

def print_credits():
    """Prints author credits."""
    credits = f"""
    {Fore.GREEN}Author: ImOnF1r3
    GitHub: https://github.com/ImOnF1r3
    {Style.RESET_ALL}
    """
    print(credits)

def validate_url(url):
    """Ensure the URL has a scheme."""
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Default to http if no scheme is provided
    return url

def fetch_page_with_cookies(url, custom_cookies=None, custom_headers=None, inject_mode=False):
    """Fetch the page and return response and cookies."""
    session = requests.Session()

    # Set retry strategy
    retries = Retry(total=5, backoff_factor=0.3, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))

    if custom_cookies:
        for name, value in custom_cookies.items():
            session.cookies.set(name, value)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    if custom_headers:
        headers.update(custom_headers)

    if inject_mode:
        headers['Cookie'] = '; '.join([f"{name}={value}" for name, value in custom_cookies.items()])

    try:
        response = session.get(url, headers=headers, timeout=15, allow_redirects=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error fetching the page {url}: {e}")
        return None, None
    
    return response, session.cookies

def print_cookies(cookies):
    """Print detailed cookie information."""
    if not cookies:
        print(f"{Fore.RED}No cookies received.")
        return

    print(f"{Fore.CYAN}Cookies:")
    for cookie in cookies:
        print(f"{Fore.YELLOW}Name: {cookie.name}")
        print(f"{Fore.YELLOW}Value: {cookie.value}")
        print(f"{Fore.YELLOW}Domain: {cookie.domain}")
        print(f"{Fore.YELLOW}Path: {cookie.path}")
        print(f"{Fore.YELLOW}Expires: {cookie.expires}")
        print(f"{Fore.YELLOW}Secure: {cookie.secure}")
        print(f"{Fore.YELLOW}HttpOnly: {cookie.has_nonstandard_attr('HttpOnly')}")
        print("-" * 40)

def print_headers(response):
    """Print response headers."""
    print(f"{Fore.CYAN}Response Headers:")
    for key, value in response.headers.items():
        print(f"{Fore.YELLOW}{key}: {value}")
    print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Cookie extractor and inserter for web pages.")
    parser.add_argument('-u', '--url', type=str, help='The URL of the web page.')
    parser.add_argument('-c', '--cookies', nargs='*', help='Custom cookies to set (name=value).')
    parser.add_argument('-inj', '--inject', action='store_true', help='Inject custom cookies into the request.')
    parser.add_argument('-ext', '--extract', action='store_true', help='Extract and display cookies from the response.')
    parser.add_argument('--key', nargs='*', help='Additional headers to set (name=value).')
    parser.add_argument('-cc', '--credits', action='store_true', help='Display author credits.')

    args = parser.parse_args()

    # Print credits if requested
    if args.credits:
        print_credits()
        return

    # Validate and fix URL schema if needed
    if args.url:
        url = validate_url(args.url)
    else:
        print(f"{Fore.RED}URL is required unless displaying credits.")
        return

    # Parse custom cookies from input
    custom_cookies = {}
    if args.cookies:
        for cookie in args.cookies:
            name, value = cookie.split('=', 1)
            custom_cookies[name] = value

    # Parse additional headers from input
    custom_headers = {}
    if args.key:
        for header in args.key:
            name, value = header.split('=', 1)
            custom_headers[name] = value

    # Fetch page with cookies and headers
    response, cookies = fetch_page_with_cookies(url, custom_cookies, custom_headers, args.inject)

    if not response:
        return

    # Print response status and headers
    print(f"{Fore.GREEN}Fetched {response.url} with status code {response.status_code}.")
    print_headers(response)

    # Extract cookies if requested
    if args.extract:
        print_cookies(cookies)

    # Parse page content
    soup = BeautifulSoup(response.content, 'lxml')
    title = soup.title.string if soup.title else "No title"
    print(f"{Fore.CYAN}Page Title: {Fore.YELLOW}{title}")

    # Print a snippet of the page content for context
    snippet = soup.get_text()[:500]  # Show the first 500 characters
    print(f"{Fore.CYAN}Page Snippet:\n{Fore.YELLOW}{snippet}\n{'-' * 40}")

if __name__ == "__main__":
    print_banner()
    main()
