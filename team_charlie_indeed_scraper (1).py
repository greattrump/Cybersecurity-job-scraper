# -*- coding: utf-8 -*-
"""Team Charlie Indeed Scraper

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iLnJ8KsVcJZy1Dl9x0gW5TCEuJ480ZNh
"""

import requests
import json
import csv

# API URL and parameters
url = "https://indeed12.p.rapidapi.com/jobs/search"
querystring = {"query": "entrylevelcybersecurity", "location": "newyork", "page_id": "1"}
headers = {
    "x-rapidapi-key": "Your_Api_Key",
    "x-rapidapi-host": "indeed12.p.rapidapi.com"
}

# API request
try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    # Check if the response contains data
    if response.status_code == 200:
        data = response.json()

        # Debug: Print the raw data response
        print("Raw API response:", json.dumps(data, indent=4))

        # Check if 'hits' key exists and has data
        if 'hits' in data and len(data['hits']) > 0:
            # Specify the CSV file name
            csv_file = 'cyberjobs_data.csv'

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
        else:
            print("Error: No job listings found for the given criteria.")
    else:
        print(f"Error: API request failed with status code {response.status_code}")

except requests.RequestException as e:
    print(f"Error: Unable to fetch data ({e})")
