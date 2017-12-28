# Budapest Data Community Overview

## Notebooks
The main notebook is the [Budapest Data Meetups.ipynb](Budapest%20Data%20Meetups.ipynb).<br>
There is another notebook ([Budapest-Meetup-Members-Graph.ipynb](Budapest-Meetup-Members-Graph.ipynb)) that creates the graph data.
Feel free to add your own notebooks.
## Crawler
The crawler is written in python. To install the dependencies run pip:
```bash
pip install -r requirements.txt
```
For usage information on the crawler, use the help.
```bash
$ python3 crawl.py -h
usage: crawl.py [-h] --apikey APIKEY {groups,members}

Meetup API Crawler

positional arguments:
  {groups,members}  The crawl command to execute

  optional arguments:
        -h, --help        show this help message and exit
        --apikey APIKEY   Meetup API Key. Check:
                      https://secure.meetup.com/meetup_api/key/
```
To query the meetup API, you need an [API key](https://secure.meetup.com/meetup_api/key/).


**Example:** To crawl the members for the data meetups into the `members.csv` file, run the following:
```bash
$ python3 crawl.py members --apikey [YOUR_API_KEY] > members.csv
```

## Data
The following prepared data sets are available:
### Meetup groups
#### All meetup groups in Budapest
Data: [data/meetup_groups_budapest_all.csv](data/meetup_groups_budapest_all.csv)
##### Headers:
`rating,name,id,urlname,membership_count`
##### Sample:
```csv
4.41;The Budapest New Technology Meetup Group;408089;newtech-42;4315
4.54;budapest.rb;1271139;budapest-rb;605
4.67;Budapest Science Meetup;1286482;BpScienceMeetup;1993
```
#### Data meetup groups in Budapest
Data: [data/meetup_groups_budapest_data.csv](data/meetup_groups_budapest_data.csv)
##### Headers:
`rating,name,id,urlname,membership_count`
##### Sample:
```csv
4.54;Budapest Data Science Meetup;1632914;budapest_data_science;2711
4.89;HUG-MSSQL;1757864;HUG-MSSQL;399
4.77;Hungarian Natural Language Processing Meetup;3418472;Hungarian-nlp;968
```
#### Graph of data meetup groups in Budapest
This graph contains meetup groups as nodes. The size of the nodes are the membership counts.
The edges are common memberships, the *Weight* is the number of common members.
### Members
#### Data meetup groups memberships
Data: [data/members_budapest_data.csv](data/members_budapest_data.csv)
##### Headers:
`country,city,joined,name,last_visited,id,group_urlname`
##### Sample:
```csv
hu;Budapest;1464271220000;A. Asbot;1500461845000;186451270;budapest_data_science
hu;Budapest;1432103533000;A.J. Lumijärvi;1478694290000;186768573;budapest_data_science
hu;Budapest;1474229938000;Ábel Fóthi;1478776809000;151890652;budapest_data_science
```
#### Graph of data meetup memberships in Budapest
The nodes are users and they are conected if they are both members in at least 5 of the same groups.

