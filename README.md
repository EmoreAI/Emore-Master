# Emore AI

![Emore](Emore.jpg)

Emore AI is an innovative application designed to streamline the process of conducting meta-analyses on academic whitepapers within the medical field. By leveraging cutting-edge AI technology, Immutable AI automates the extraction, analysis, and dissemination of insights from scholarly articles. The application scrapes relevant papers from bioRxiv and medRxiv, performs a sophisticated analysis using OpenAI's ChatGPT, and shares the synthesized findings on Twitter, making it easier for researchers and the public to access and understand complex scientific data.

## Project Structure

```
Emore/
│
├── scrapers/
│   ├── __init__.py
│   ├── biorxiv_scraper.py
│   ├── medrxiv_scraper.py
│   └── pdf_downloader.py
│
├── analysis/
│   ├── __init__.py
│   ├── ai_analysis.py
│   └── insights_extractor.py
│
├── twitter/
│   ├── __init__.py
│   └── twitter_poster.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── tests/
│   ├── __init__.py
│   ├── test_scrapers.py
│   ├── test_analysis.py
│   ├── test_twitter.py
│   └── test_helpers.py
│
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

## Technology Stack

Emore AI is built using a robust stack of modern technologies:

- **Python**: The primary programming language used for developing the application.
- **BeautifulSoup**: Utilized for web scraping to efficiently gather academic papers from bioRxiv and medRxiv.
- **OpenAI API**: Powers the AI-driven analysis, enabling the extraction of novel insights from the papers.
- **Tweepy**: Facilitates interaction with the Twitter API, allowing the application to post analysis results seamlessly.
- **SQLite**: A lightweight database used to store metadata and results of the analyses, ensuring data persistence.
- **Docker**: Containerizes the application, promoting ease of deployment and scalability across different environments.

## Usage

### Prerequisites

Ensure you have Docker and Docker Compose installed on your machine. Additionally, obtain API keys for OpenAI and Twitter, which should be stored securely in a `.env` file located in the root directory.

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Emore-Project/Emore
   cd Emore
   ```

2. Build the Docker container:
   ```bash
   docker-compose build
   ```

3. Start the application with a specific topic:
   ```bash
   docker-compose run app start <topic-key>
   ```

   Replace `<topic-key>` with the desired medical topic for analysis.

4. Stop the application:
   ```bash
   docker-compose run app stop
   ```

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```
API_KEY=<your_openai_api_key>
TWITTER_API_KEY=<your_twitter_api_key>
TWITTER_API_SECRET=<your_twitter_api_secret>
TWITTER_ACCESS_TOKEN=<your_twitter_access_token>
TWITTER_ACCESS_TOKEN_SECRET=<your_twitter_access_token_secret>
```

### Running Tests

To ensure the application is functioning correctly, run the tests using:

```bash
docker-compose run app pytest
```

## Contributing

We welcome contributions to Immutable AI! If you have ideas for enhancements or have identified bugs, please fork the repository and submit a pull request. We appreciate your input and collaboration.

## License

Emore AI is licensed under the MIT License. For more details, please refer to the `LICENSE` file.

---

With Emore AI, accessing and understanding complex medical research has never been easier. By automating the analysis and dissemination process, this application empowers researchers and the public to stay informed and make data-driven decisions.