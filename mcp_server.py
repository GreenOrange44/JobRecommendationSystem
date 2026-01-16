from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_naukri_jobs

mcp = FastMCP("Job Recommender")

@mcp.tool()
async def get_naukri_jobs(listofkeys):
    """
    Fetch Naukri jobs based on the provided list of keywords.
    1. listofkeys: A string of keywords separated by commas.
    Returns a list of job dictionaries.
    """
    jobs = fetch_naukri_jobs(listofkeys)
    return jobs

if __name__ == "__main__":
    mcp.run( ) 