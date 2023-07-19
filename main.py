from ascii_art import ascii_presentation
from google_api import main as google_main

def main():
    # Display ASCII presentation
    ascii_presentation()

    # Call the main function from google_api.py to perform website reputation check
    google_main()

if __name__ == "__main__":
    main()