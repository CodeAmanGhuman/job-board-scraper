import requests
from bs4 import BeautifulSoup
import pandas as pd

import requests
import pandas as pd

def scrape_remoteok(keyword=None):
    url = "https://remoteok.com/api"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch jobs.")
        return []

    data = response.json()

    # First item is metadata; skip it
    jobs_data = data[1:]

    jobs = []
    for job in jobs_data:
        title = job.get("position") or job.get("title")
        company = job.get("company")
        link = f"https://remoteok.com/remote-jobs/{job.get('id')}"
        tags = job.get("tags", [])

        if not title or not company:
            continue

        tags_joined = " ".join(tags).lower()
        title_lower = title.lower()
        keyword_lower = keyword.lower() if keyword else ""


        if keyword_lower and keyword_lower not in title_lower and keyword_lower not in tags_joined:
            continue
        
        jobs.append({
            "Title": title,
            "Company": company,
            "Link": link,
            "Tags": ", ".join(tag.strip() for tag in tags)
        })

    return jobs


def save_to_csv(jobs, filename="jobs.csv"):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f"Saved {len(jobs)} jobs to {filename}")

if __name__ == "__main__":
    kw = input("Enter keyword to filter (or leave blank): ").strip()
    job_listings = scrape_remoteok(keyword=kw if kw else None)
    save_to_csv(job_listings)
    print("Done!")