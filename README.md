# 🧹 RemoteOK Job Scraper

A lightweight Python script to scrape and filter remote job listings from [RemoteOK](https://remoteok.com). Export results to CSV for easy analysis.

![Python](https://img.shields.io/badge/Python-3%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- **Comprehensive Scraping** - Fetches 90+ latest remote jobs in one run
- **Smart Filtering** - Search by keywords in job titles or tags (e.g., "Python", "React", "AI")
- **Clean Output** - Structured CSV format for easy processing
- **Zero Config** - Runs directly from terminal with minimal setup

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CodeAmanGhuman/job-board-scraper.git
   cd job-board-scraper

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the script with:
   ```bash
   python main.py

4. When prompted:
- Enter a keyword to filter jobs (e.g., "backend" or "javascript")
- Or press Enter to scrape all available jobs

## 📂 Output

The results will be saved to jobs.csv in the project directory.

## 🛠️ Libraries Used
- "Python 3"
- "requests" for HTTP calls
- "pandas" for CSV export
- "RemoteOK API" for job data

## ✨ Example Use Cases
- Tech job seekers filtering roles by stack
- Recruiters extracting leads
- Students learning real-world scraping

