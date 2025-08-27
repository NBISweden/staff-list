import logging
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from email.utils import parsedate_to_datetime
import pdb
import os

class Nextcloud:

    def __init__(self, config, args): 
        """
        Initialize the Nextcloud class with self.configuration.
        """
        self.config = config
        self.args = args


    def download_spreadsheet(self):
        """
        Download a spreadsheet from a given URL using basic authentication.
        """

        logging.debug("Starting download_spreadsheet function...")

        # Download the spreadsheet
        logging.info("Downloading spreadsheet...")
        logging.debug(f"Using URL: {self.config['nextcloud']['base_url']}/remote.php/dav/files/{self.config['nextcloud']['username']}/{self.config['nextcloud']['remote_file_path']}")
        response = requests.get(f"{self.config['nextcloud']['base_url']}/remote.php/dav/files/{self.config['nextcloud']['username']}/{self.config['nextcloud']['remote_file_path']}", auth=HTTPBasicAuth(self.config['nextcloud']['username'], self.config['nextcloud']['password']))

        # Extract the last-modified date from headers
        last_modified_header = response.headers.get('Last-Modified')

        if last_modified_header:
            # Parse the HTTP date format
            last_modified_dt = parsedate_to_datetime(last_modified_header)
            # Convert to timestamp
            modification_time = last_modified_dt.timestamp()
        else:
            modification_time = None

        # Check if the request was successful
        if response.status_code == 200:
            with open(self.args.file, 'wb') as f:
                f.write(response.content)
            logging.info("Spreadsheet downloaded successfully.")
        else:
            logging.error("Failed to download the spreadsheet.")
            return False

        # Set the file's modification time to match the server's last-modified time
        if modification_time:
            os.utime(self.args.file, (modification_time, modification_time))
            logging.debug(f"Set file modification time to {last_modified_dt.isoformat()}")
        else:
            logging.debug("No Last-Modified header found; file modification time not set.")

        return True
