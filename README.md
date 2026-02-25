# 🤖 AI-Powered Job Recommender & MCP Server

An intelligent job recommendation system that analyzes your resume (PDF) using **Google Gemini** to extract key skills and searches for matching job openings via **Apify**.

This project also includes a **Model Context Protocol (MCP)** server, allowing AI agents (like Claude Desktop or other MCP clients) to use this tool directly to fetch jobs.

## ✨ Features

* **Resume Parsing:** Extracts text from PDF resumes.
* **AI Analysis:** Uses **Gemini 2.5 Flash Lite** to identify job titles, technical skills, and experience levels.
* **Smart Search:** Converts resume data into optimized boolean search queries.
* **Job Aggregation:** Fetches real-time job listings from Naukri.com using **Apify**.
* **MCP Support:** Exposes a `fetch_jobs` tool that can be integrated into AI agent workflows.
* **Interactive UI:** A clean **Streamlit** dashboard for easy user interaction.

## 🛠️ Tech Stack

* **Core:** Python 3.12+
* **Frontend:** Streamlit
* **LLM:** LangChain + Google Gemini
* **Scraping:** Apify Client
* **Protocol:** Model Context Protocol (MCP) using `mcp` SDK
* **Dependency Management:** `uv` (or `pip`)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/GreenOrange44/JobRecommendationSystem

then make an .env file and add Apify token key and gemini token key:
APIFY_API_TOKEN=apify_api_z.......
GOOGLE_API_KEY=AIz........

