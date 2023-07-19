from pyfiglet import Figlet

def ascii_art_generation(text):
    ascii_letter_type = Figlet(font='doh', width=100)
    ascii_text = ascii_letter_type.renderText(text)
    return ascii_text

def ascii_presentation():
    separator = '-' * 100  # Adjust the number of dashes for the desired width
    program_info = """
    SiteCheck - URL Reputation Checker with Google API
    Created by: OneForAll
    Year: 2023
    """
    
    ascii_presentation_text = ascii_art_generation("SiteCheck")
    
    # Print program information
    print(program_info)
    
    # Print the separator line above the ASCII art
    print(separator)
    print(ascii_presentation_text)
    
    # Print the separator line below the ASCII art
    print(separator)

#if __name__ == "__main__":
 #   ascii_presentation()
