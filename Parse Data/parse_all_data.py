from pathlib import Path
import json
from tqdm import tqdm
import requests
from utils import data_path, root_path, trials_path, save_json, load_json
from concurrent.futures import ThreadPoolExecutor

# Define the function to process and save a single trial
def process_and_save_trial(trial, trials_path):
    nctID = trial['protocolSection']['identificationModule']['nctId']
    save_path = trials_path.joinpath(f'{nctID}')
    save_path.mkdir(parents=True, exist_ok=True)
    save_json(trial, save_path.joinpath('record.json'))

# Main function to fetch and process data
def fetch_and_save_trials():
    fields = 'protocolSection%7CresultsSection%7CAnnotationSection%7CDocumentSection%7CDerivedSection%7CHasResults'
    url = f"https://clinicaltrials.gov/api/v2/studies?fields={fields}"

    with ThreadPoolExecutor() as executor:  # Use ThreadPoolExecutor for parallelism
        for i in tqdm(range(550)):
            if i == 0:
                params = {'pageSize': 1000}
            else:
                params = {'pageSize': 1000, 'pageToken': token}
            
            # Fetch data from the API
            response = requests.get(url, params=params)
            data = response.json()

            # Get the next page token
            token = data.get('nextPageToken', None)
            if not token:
                break  # Exit the loop if there is no next page
            
            # Extract and process trials in parallel
            trials = data['studies']
            executor.map(lambda trial: process_and_save_trial(trial, trials_path), trials)

# Execute the function
if __name__ == "__main__":
    fetch_and_save_trials()
