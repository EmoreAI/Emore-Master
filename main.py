import argparse
import time
from scrapers.biorxiv_scraper import scrape_biorxiv_papers
from scrapers.medrxiv_scraper import scrape_medrxiv_papers
from scrapers.pdf_downloader import download_pdfs
from analysis.ai_analysis import extract_text_from_pdfs, analyze_texts
from analysis.insights_extractor import generate_insights
from twitter.twitter_poster import post_insights_to_twitter
from config.settings import DEFAULT_TOPIC, PDF_DOWNLOAD_DIR

def start_search(topic: str, interval: int = 3600):
    print(f"Starting search for topic: {topic}")
    while True:
        try:
            # Scrape papers from bioRxiv and medRxiv
            biorxiv_papers = scrape_biorxiv_papers(topic)
            medrxiv_papers = scrape_medrxiv_papers(topic)

            # Select two papers from each source
            selected_papers = (biorxiv_papers[:2] + medrxiv_papers[:2]) if biorxiv_papers and medrxiv_papers else []

            # Extract PDF links
            pdf_links = [paper['link'] for paper in selected_papers]

            # Download PDFs
            downloaded_pdfs = download_pdfs(pdf_links, PDF_DOWNLOAD_DIR)

            # Extract text from PDFs
            texts = extract_text_from_pdfs(downloaded_pdfs)

            # Analyze texts
            analysis_results = analyze_texts(texts)

            # Generate insights
            insights = generate_insights(analysis_results)

            # Post insights to Twitter
            post_insights_to_twitter(insights)

            print(f"Completed cycle for topic: {topic}. Waiting for next interval...")
            time.sleep(interval)  # Wait for the specified interval before the next cycle

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(interval)  # Wait before retrying

def stop_search():
    print("Stopping search process.")
    exit(0)

def main():
    parser = argparse.ArgumentParser(description="Immutable AI: Automated Whitepaper Analysis and Posting")
    parser.add_argument('command', choices=['start', 'stop'], help="Command to start or stop the search process")
    parser.add_argument('--topic', type=str, default=DEFAULT_TOPIC, help="Topic to search for whitepapers")
    parser.add_argument('--interval', type=int, default=3600, help="Interval in seconds between each search cycle")

    args = parser.parse_args()

    if args.command == 'start':
        start_search(args.topic, args.interval)
    elif args.command == 'stop':
        stop_search()

if __name__ == "__main__":
    main()