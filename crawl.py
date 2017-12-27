import json
import argparse
import requests


def get_groups(apikey):
    group_results = []
    params = {
        "country": "hu",
        "state": "hu",
        "city": "Budapest",
        "format": "json",
        "lon": 19.0799999237,
        "lat": 47.5099983215,
        "radius": 25.0,
        "page": 25,
        "desc": False,
        "offset": 0,
        "key": apikey,
        "only": ",".join(["rating", "members", "id", "name", "urlname"])
    }
    nurl = "https://api.meetup.com/2/groups"
    while nurl:
        resp = requests.get(nurl, params=params)
        params = None
        res = json.loads(resp.text)
        for group in res["results"]:
            group_results.append(group)
        if "meta" in res and "next" in res["meta"]:
            nurl = res["meta"]["next"]
        else:
            nurl = False
    return group_results


def get_members(groups, apikey):
    for group in groups:
        params = {
            "offset": 0,
            "format": "json",
            "page": 50,
            "desc": False,
            "order": "name",
            "key": apikey,
            "group_urlname": group,
            "only":
            ",".join(["country", "city", "joined", "name", "id", "visited"])
        }
        nurl = "https://api.meetup.com/2/members"
        while nurl:
            resp = requests.get(nurl, params=params)
            params = None
            if resp.text == "":
                break
            res = json.loads(resp.text)
            for members in res["results"]:
                element = ";".join([str(r) for r in members.values()])
                element += ";" + group
                print(element)
            if "meta" in res and "next" in res["meta"]:
                nurl = res["meta"]["next"]
            else:
                nurl = False


GROUPIDS = [
    "budapest_data_science", "HUG-MSSQL", "Hungarian-nlp", "KURT_Akademia",
    "Big-Data-Meetup-Budapest", "Budapest-Database-Meetup",
    "Budapest-Cassandra-Users", "Pro-Bono-Analytics",
    "Budapest-Users-of-R-Network", "MongoDB-Budapest", "Budapest-BI-Meetup",
    "Budapest-Data-Visualization-Meetup", "Budapest-network-science",
    "Big-Data-Budapest", "Budapest-Machine-Learning-Meetup",
    "Budapest-Data-Projects-Meetup", "Budapest-Analytics-Rockstars",
    "neo4j-budapest-users", "Snowplow-Analytics-Budapest",
    "Budapest-Spark-Meetup", "Budapest-NOSQL",
    "Budapest-dataSTREAM-Meetup-Series", "futureofdata-budapest",
    "Excel-tippek-es-trukkok-tips-and-tricks-Budapest-Meetup",
    "R-Ladies-Budapest",
    "NLP-Nyilt-est-Karizmatikus-kommunikacio-NLP-bevezető", "Budapest-GraphQL",
    "DataFest", "PyData-Budapest", "Budapest-Deep-Learning-Reading-Seminar",
    "Neurons-AI-Hungary-Budapest"
]


def main():
    parser = argparse.ArgumentParser(description='Meetup API Crawler')
    parser.add_argument(
        '--apikey',
        type=str,
        required=True,
        help='Meetup API Key. Check: https://secure.meetup.com/meetup_api/key/'
    )
    parser.add_argument(
        'command',
        type=str,
        help='The crawl command to execute',
        choices=["groups", "members"])
    args = parser.parse_args()

    if args.command == "members":
        get_members(GROUPIDS, args.apikey)
    elif args.command == "groups":
        results = get_groups(args.apikey)
        for result in results:
            print(",".join(result))


if __name__ == "__main__":
    main()
