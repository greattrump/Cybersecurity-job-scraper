![1398313](1398313.jpg)
# Cybersecurity_Jobscraper

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

```url = "https://indeed12.p.rapidapi.com/jobs/search"
querystring = {"query": "entrylevelcybersecurity", "location": "newyork", "page_id": "1"}
```

## Headers
The API request headers contain:
- **x-rapidapi-key**: Your RapidAPI key for authentication (a sample key is shown in the script but should be replaced with your own key).
- **x-rapidapi-host**: The host for the API.

```
headers = {
    "x-rapidapi-key": "Your_Api_Key",
    "x-rapidapi-host": "indeed12.p.rapidapi.com"
}
```


## Main Functionality

### Step 1: API Request
The script sends an HTTP GET request to the Indeed Job Search API using the `requests.get()` function, passing the query parameters and headers.

```
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # Raises an HTTPError for bad responses
```

### Step 2: Response Handling
- If the response status code is 200 (successful):
  - The script parses the response JSON data.
  - If the response contains job data (`hits` key in the JSON), the script proceeds to write the data to a CSV file.
- If the response contains no data or the `hits` key is missing, an error message is printed.

```
# Check if the response contains data
    if response.status_code == 200:
        data = response.json()

        # Debug: Print the raw data response
        print("Raw API response:", json.dumps(data, indent=4))

        # Check if 'hits' key exists and has data
        if 'hits' in data and len(data['hits']) > 0:
            # Specify the CSV file name
            csv_file = 'cyberjobs_data.csv'
```

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

```
# Open CSV file for writing
            with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(["company_name", "formatted_relative_time", "id", "link", "locality", "location", "pub_date_ts_milli", "salary"])

                # Write data rows
                for job in data.get('hits', []):  # Use .get() to avoid KeyError
                    salary_info = job.get('salary', {})
                    writer.writerow([
                        job.get('company_name', ''),
                        job.get('formatted_relative_time', ''),
                        job.get('id', ''),
                        job.get('link', ''),
                        job.get('locality', ''),
                        job.get('location', ''),
                        job.get('pub_date_ts_milli', ''),
                        f"{salary_info.get('min', '')}-{salary_info.get('max', '')} {salary_info.get('type', '')}"
                    ])

            print(f"Data successfully written to {csv_file}")
```


### Step 4: Error Handling
- If the API request fails, a `requests.RequestException` is raised, and an error message is printed.

```
else:
            print("Error: No job listings found for the given criteria.")
    else:
        print(f"Error: API request failed with status code {response.status_code}")

except requests.RequestException as e:
    print(f"Error: Unable to fetch data ({e})")
```

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

- ## Credits
- Khaj Thompson
- Elaine John

## FAQ - Cybersecurity Jobscraper

### 1. What is the purpose of this script?
This Python script scrapes job listings for entry-level cybersecurity positions in New York using the Indeed Job Search API. It collects data such as company name, location, job ID, and salary, and saves the results in a CSV file for further analysis or job searching.

### 2. How does the script connect to the Indeed API?
The script connects to the Indeed Job Search API using the `requests` library. It sends an HTTP GET request with specified query parameters (job type and location) to retrieve relevant job listings.

### 3. What do I need to run the script?
To run the script, you'll need:
- Python 3.x installed on your machine.
- The `requests` library (`pip install requests`).
- A valid RapidAPI key to access the Indeed API.

### 4. How do I get a RapidAPI key?
You can obtain a RapidAPI key by signing up at [RapidAPI](https://rapidapi.com). Once you have the key, replace the placeholder key in the script with your own key to authenticate the API requests.

### 5. How does the script handle errors or empty responses?
If the API request fails (e.g., due to an invalid API key or server issues), the script raises an exception and prints an error message. If no job listings are found for the query, it will display:  
*Error: No job listings found for the given criteria.*

### 6. How can I customize the job search criteria?
To modify the search:
- Change the `query` parameter in the `querystring` dictionary to search for different job roles.
- Adjust the `location` parameter to search in other cities or regions.

Example:
```python
querystring = {"query": "cybersecurity", "location": "california", "page_id": "1"}
```

### 7. Where is the data saved, and what format is used?
The job data is saved in a CSV file named `cyberjobs_data.csv`. Each row in the CSV contains fields such as company name, job ID, location, and salary.

### 8. What kind of data does the script extract from job listings?
For each job listing, the script extracts:
- Company name
- Relative posting time
- Job ID
- Job link
- Locality and location (e.g., Manhattan, New York)
- Salary information (minimum, maximum, and type)
  
### 9. Can I use this script for locations outside New York?
Yes, you can search for jobs in different locations by changing the `location` parameter in the querystring. For example, to search for jobs in California, set `"location": "california"`.

### 10. What should I do if the script encounters issues?
Check for the following:
- Ensure your RapidAPI key is valid and has sufficient quota.
- Verify that you have an active internet connection.
- Double-check that the query parameters are correctly set.

### 11. Is there a limit on how many jobs I can scrape?
This depends on the API limitations set by RapidAPI and Indeed. Make sure to review their usage quotas, and adjust your script accordingly to avoid excessive requests.

### 12. How can I update the API query for pagination?
If you want to scrape more than one page of results, you can modify the `page_id` parameter in the querystring to fetch subsequent pages.

Example:
```python
querystring = {"query": "entrylevelcybersecurity", "location": "newyork", "page_id": "2"}
```

### 13. What ethical considerations should I keep in mind when using this script?
The script is intended for responsible usage:
- It abides by Indeed’s terms of service and avoids overloading their servers.
- It only scrapes publicly available job data and does not collect personal user information.
- The data should be used for legitimate purposes like job searching or data analysis, not for spamming or other malicious activities.
