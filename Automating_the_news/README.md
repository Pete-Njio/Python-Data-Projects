# Automating the News

A Python web scraper that automatically collects football headlines from The Sun's football section and saves them to a CSV file.

## What It Does

- Scrapes the latest football headlines, subtitles, and article links from The Sun
- Runs in headless mode (no browser window opens)
- Saves results to a date-stamped CSV file (e.g. `headlines-28-06-2026.csv`)

## Technologies Used

- Python
- Selenium (headless Firefox)
- Pandas
- Datetime / OS (standard library)

## Requirements

- Python 3.x
- Firefox browser installed
- Geckodriver installed and in PATH

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git

2. Install dependencies:
pip install selenium pandas
3. Run the script:
python "Automating the News.py"

Output

A CSV file named headlines-DD-MM-YYYY.csv saved in the project directory with columns:
- titles — article title
- subtitles — article subtitle
- links — full URL to the article

Use Case

This project demonstrates automated data collection using web scraping — useful for tracking news trends, sports coverage, or building a headlines dataset over time.