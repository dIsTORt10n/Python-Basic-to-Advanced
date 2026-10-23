import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Function to scrape data using Requests and BeautifulSoup


def scrape_with_requests(url):
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.text  # Return the HTML content of the page
    else:
        # Print an error message if the request failed
        print("Failed to retrieve the webpage.")
        return None  # Return None to indicate failure

# Function to extract questions from HTML content


def extract_questions(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all elements that match the specified class name (adjust as needed)
    questions = soup.find_all('div', class_='question')

    # Extract the text from each question element and return as a list
    return [question.get_text() for question in questions]

# Function to save data to a CSV file


def save_to_csv(data):
    # Create a DataFrame from the list of questions
    df = pd.DataFrame(data, columns=['Questions'])

    # Save the DataFrame to a CSV file
    df.to_csv('questions.csv', index=False)
    print("Data saved to questions.csv")  # Print a confirmation message

# Function to scrape data using Selenium


def scrape_with_selenium(url):
    # Set up Chrome options for headless browsing (no GUI)
    options = Options()
    options.add_argument('--headless')  # Run Chrome in headless mode

    # Specify the path to the ChromeDriver executable
    # Adjust the path to your ChromeDriver
    service = Service('/usr/bin/chromedriver')

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(service=service, options=options)

    # Open the specified URL in the browser
    driver.get(url)

    # Wait for a few seconds to allow the page to load (adjust as necessary)
    time.sleep(10)

    # Example: Extract questions using Selenium
    # Find all elements that match the specified class name (adjust as needed)
    questions = driver.find_elements(By.CLASS_NAME, 'question')

    # Extract the text from each question element and return as a list
    extracted_questions = [question.text for question in questions]

    # Close the browser
    driver.quit()

    return extracted_questions  # Return the list of extracted questions

# Main function to orchestrate the scraping process


def main():
    # Prompt the user to enter a URL
    url = input("Enter a URL: ")  # Replace with your target website

    # First, try scraping with Requests
    html_content = scrape_with_requests(url)

    # If HTML content is successfully retrieved, extract questions
    if html_content:
        questions = extract_questions(html_content)
    else:
        # If Requests fails, fall back to Selenium for scraping
        questions = scrape_with_selenium(url)

    # Check if any questions were extracted
    if questions:
        print("Extracted Questions:")  # Print a header for the output
        for question in questions:
            print(question)  # Print each extracted question

        # Save the extracted questions to a CSV file
        save_to_csv(questions)


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
