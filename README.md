# IMDb Sci-Fi Movies Scrapy Project

Welcome! This project is about scraping Sci-Fi movie data from IMDb using the start URL from [IMDb Sci-Fi genre](https://www.imdb.com/search/title/?title_type=movie&genres=sci-fi&explore=genres). Navigating through IMDb's structure can be intricate, but we've managed to create a spider that does the job!

## 🚀 Quick Start

1. **Install necessary packages**

    Ensure you've installed all the required packages. The list is available in the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Spider**

    Move to the project directory and initiate the `imdb_spider`.

    ```bash
    scrapy crawl imdb_spider -O output.csv
    ```

## 📦 Output

The scraped movie data will be stored in a CSV format. Open the file with spreadsheet software like Microsoft Excel or Google Sheets to review and analyze the movie details.

## 📋 Data Columns

The scraper extracts the following columns:
- TITLE
- RELEASED YEAR
- RATING
- GENRES
- LENGTH
- CERTIFICATION
- DIRECTORS
- WRITERS
- STARS

## 🔍 Challenges Faced

- **Complex HTML Structure:** IMDb's website layout is known for its intricacies. We took the challenge head-on and designed our spider to fetch data precisely.

- **Rate Limiting:** IMDb sometimes limits the number of requests, leading to temporary blocks. We've employed strategies like changing user-agents and introducing delays to handle this.

## 📚 Resources

- **Scrapy Documentation:** For further information or if any challenges arise, refer to the official Scrapy documentation: [Scrapy Documentation](https://docs.scrapy.org/en/latest/).

## 🙌 Contributions

Dive in and contribute! Whether you're opening an issue, suggesting enhancements, or fixing potential bugs, your input is greatly appreciated!

## 📃 License

This scraper is open-source and available for all. Feel free to utilize, alter, and distribute as you see fit. Happy scraping!

