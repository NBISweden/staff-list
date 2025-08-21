class Nextcloud:

    def __init__(self, config, args): 
        """
        Initialize the Nextcloud class with configuration.
        """
        self.config = config
        self.args = args
        self.setup_logging()


    def download_spreadsheet(self):
        """
        Download a spreadsheet from a given URL using basic authentication.
        """

        logging.debug("Starting download_spreadsheet function...")

        # Download the spreadsheet
        logging.info("Downloading spreadsheet...")
        logging.debug(f"Using URL: {self.config['base_url']}/remote.php/dav/files/{self.config['username']}/{self.config['remote_file_path']}")
        response = requests.get(f"{self.config['base_url']}/remote.php/dav/files/{self.config['username']}/{self.config['remote_file_path']}", auth=HTTPBasicAuth(self.config['username'], self.config['password']))

        # Check if the request was successful
        if response.status_code == 200:
            with open(self.args.file, 'wb') as f:
                f.write(response.content)
            logging.info("Spreadsheet downloaded successfully.")
        else:
            logging.error("Failed to download the spreadsheet.")


    def setup_logging(self):
        """
        Set up logging configuration.
        """
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler("nextcloud.log"),
                logging.StreamHandler()
            ]
        )
        logging.debug("Logging is set up.")
