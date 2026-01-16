from apify_client import ApifyClient
import os 
from dotenv import load_dotenv
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))


# Fetch Naukri jobs based on search query and location
def fetch_naukri_jobs(search_query, location = "india", rows=50):
    run_input = {
        "keyword": search_query,
        "maxJobs": 50,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }
    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
    dataset_items = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    # Normalize data for your frontend
    jobs = []
    for item in dataset_items:
        jobs.append({
            "title": item.get("title", "Job Title N/A"),
            "companyName": item.get("companyName", "Company N/A"),
            "location": item.get("location", "Location N/A"),
            
            # New Fields
            "salary": item.get("salary", "Not Disclosed"), 
            "experience": item.get("experience", "Not Specified"),
            
            # URL Handling (checking multiple common keys)
            "jdURL": item.get("jobUrl")
        })
    return jobs