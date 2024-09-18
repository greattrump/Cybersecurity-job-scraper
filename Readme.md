![1398313](1398313.jpg)
# Cybersecurity_Jobscraper
by Khaj Thompson & Elaine John

## Overview
This Python script fetches job listings for entry-level cybersecurity positions in New York using the Indeed Job Search API and saves the data in a CSV file. It uses the `requests` library to make an HTTP GET request to the API and writes the job data into a CSV file using the `csv` library.

## Requirements
- Python 3.x
- External libraries:
  - `requests`: For making HTTP requests.
  - `csv`: For writing data to CSV files.

You can install the `requests` library using the following command if not already installed:

```bash
pip install requests
```

## API Details
The script connects to the Indeed Job Search API hosted on RapidAPI with the following key components:
- **API URL**: `https://indeed12.p.rapidapi.com/jobs/search`
- **API Query Parameters**:
  - `query`: Search term for jobs (set to "entrylevelcybersecurity").
  - `location`: Location of jobs (set to "newyork").
  - `page_id`: Page number for pagination (set to 1).

``` url = "https://indeed12.p.rapidapi.com/jobs/search"
querystring = {"query": "entrylevelcybersecurity", "location": "newyork", "page_id": "1"}
```

## Headers
The API request headers contain:
- **x-rapidapi-key**: Your RapidAPI key for authentication (a sample key is shown in the script but should be replaced with your own key).
- **x-rapidapi-host**: The host for the API.

```headers = {
    "x-rapidapi-key": "f016c95904mshcb5f883e445ac1ep1b864ejsn4a7ffae93426",
    "x-rapidapi-host": "indeed12.p.rapidapi.com"
}
```


## Main Functionality

### Step 1: API Request
The script sends an HTTP GET request to the Indeed Job Search API using the `requests.get()` function, passing the query parameters and headers.

```    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # Raises an HTTPError for bad responses```

### Step 2: Response Handling
- If the response status code is 200 (successful):
  - The script parses the response JSON data.
  - If the response contains job data (`hits` key in the JSON), the script proceeds to write the data to a CSV file.
- If the response contains no data or the `hits` key is missing, an error message is printed.

### Step 3: Writing to CSV
- The script creates a CSV file named `cyberjobs_data.csv`.
- It writes the following fields for each job listing into the file:
  - `company_name`: The name of the company offering the job.
  - `formatted_relative_time`: The relative time of the job posting.
  - `id`: The unique job identifier.
  - `link`: The link to the job posting.
  - `locality`: The locality of the job.
  - `location`: The job location (city, state).
  - `pub_date_ts_milli`: The job posting timestamp in milliseconds.
  - `salary`: A combination of minimum and maximum salary, along with the salary type (e.g., "hourly", "annual").

### Step 4: Error Handling
- If the API request fails, a `requests.RequestException` is raised, and an error message is printed.

## Usage Instructions
1. Replace the placeholder RapidAPI key (`x-rapidapi-key`) in the script with your own valid key.
2. Run the script in a Python environment. If successful, it will fetch job listings and save them into a CSV file named `cyberjobs_data.csv`.
3. The raw API response is printed to the console for debugging purposes.

## Example CSV Output
The generated CSV will have a header row with the following fields:

```
company_name, formatted_relative_time, id, link, locality, location, pub_date_ts_milli, salary
```

Example data might look like:

```
Tech Corp, 2 days ago, 12345, http://example.com/job/12345, Manhattan, New York, 1631505600000, 60000-80000 annual
```

## Error Handling
- If no job listings are found: `"Error: No job listings found for the given criteria."`
- If the API request fails: `"Error: Unable to fetch data (specific error message)"`

## Notes
- Ensure you have an active and valid RapidAPI key.
- Modify the `querystring` dictionary to search for different job types or locations.

## Ethical Considerations

This script is designed to be used responsibly and ethically. Here are some key points to consider:

- Respect for Indeed and Users: We respect Indeed's terms of service and will not overload their servers with excessive requests.
- This script only scrapes publicly available job listings and does not collect any personal user data.

## Responsible Data Usage:
- The data scraped from Indeed should only be used for legitimate purposes such as personal job searching or data analysis.

## Avoiding Misuse: 
- This script is not intended for any malicious purposes such as spamming applicants.
Additional Notes

- users should obtain their own RapidAPI key to avoid relying on the placeholder key in the script.
