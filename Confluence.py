import logging
import pdb
import requests
import json
import textwrap
from requests.auth import HTTPBasicAuth
from datetime import date
from pprint import pprint


class Confluence:
    def __init__(self, config, args, dry_run=False):
        """
        Initialize the Confluence class with self.configuration.
        :param config: Dictionary containing configuration parameters.
        :param args: Command-line arguments.
        :param dry_run: If True, do not upload changes to Confluence.
        """
        self.base_url = config["confluence"]["base_url"]
        self.auth     = requests.auth.HTTPBasicAuth(config["confluence"]["username"], config["confluence"]["api_key"])
        self.dry_run  = dry_run

    def update_staff_list_page(self, space_key, page_id, html_content):
        """
        Update the Confluence page with the given space name and page ID with the provided HTML content.
        :param space_name: Name of the Confluence space.
        :param page_id: ID of the Confluence page to update.
        :param html_content: HTML content to update the page with.
        :return: True if the page was updated, False if no update was needed.
        """
        url = f"{self.base_url}/wiki/api/v2/pages/{page_id}"
        # Retrieve current page
        params = {"body-format": "storage"}
        response = requests.get(url, params=params, auth=self.auth).json()
        text = response["body"]["storage"]["value"]


        # Build the new page content
        content = {
            "id": response["id"],
            "status": "current",
            "title": response["title"],
            "body": {
                "storage": {"value": html_content, "representation": "storage"}
            },
            "version": {"number": response["version"]["number"] + 1},
        }

        # If we are in dry run mode, just return the content without uploading
        if self.dry_run:
            logging.info("Dry run mode: Not uploading changes to Confluence.")
            logging.debug("Content to be uploaded:")
            pprint(content)
            return True


        # upload the new content to Confluence
        r = requests.put(
            url,
            auth=self.auth,
            data=json.dumps(content),
            headers={"Content-Type": "application/json", "Accept": "application/json",},
        )
        r.raise_for_status()
        return True

