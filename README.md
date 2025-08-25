# NBIS Staff List

These scripts are made for handling the NBIS staff list.

## Installation

Clone this repo:

```bash
git clone https://github.com/NBISweden/staff-list.git
cd staff-list
```

Set up a virtual python environment and install python deps:

```bash
python3 -m venv venv             # create venv
source venv/bin/activate         # activate it
pip install -U pip               # update pip
pip install -r requirements.txt  # install deps
```

## Create config

Make a copy of the example config and fill in your values.

```bash
cp config.yaml.dist config.yaml  # make a copy
vim config.yaml                  # edit copy
```

## Scripts

Short explaination of the scripts. Run the scripts with `-h` to see more details.

### update_confluence_list.py
Will download the staff list spreadsheet from Nextcloud and recreate it as a page in Confluence.

### check_warnings.py
Will download the staff list spreadsheet from Nextcloud and run sanity checks on it. Things like email accounts still being active after a person has left NBIS etc.



