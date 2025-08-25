import logging
import requests
from requests.auth import HTTPBasicAuth


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

        # Check if the request was successful
        if response.status_code == 200:
            with open(self.args.file, 'wb') as f:
                f.write(response.content)
            logging.info("Spreadsheet downloaded successfully.")
        else:
            logging.error("Failed to download the spreadsheet.")


