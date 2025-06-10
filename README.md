# 🧹 RemoteOK Job Scraper

This is a simple Python script that scrapes job listings from [RemoteOK](https://remoteok.com) and saves them to a CSV file. You can filter results by keyword in **job titles or tags**.

## 🚀 Features

- ✅ Scrapes 90+ latest remote jobs from RemoteOK
- 🔍 Filter jobs by keyword (e.g., "Python", "React", "AI")
- 💾 Saves clean data to `jobs.csv`
- 📦 Easy to run from terminal — no setup hassle

## 📸 Sample Output (CSV)

Title, Company, Link, Tags
Senior Python Developer, Blotato, https://remoteok.com/remote-jobs/remote-senior-python-developer-blotato-123456, Python,Backend,Remote

## ⚙️ How to Use

1. Clone this repo:
git clone https://github.com/CodeAmanGhuman/job-board-scraper.git
cd job-board-scraper

2. Install dependencies:
pip install -r requirements.txt

3. Run it:
python main.py

4. Enter a keyword (e.g., python) or leave blank to scrape all jobs.

