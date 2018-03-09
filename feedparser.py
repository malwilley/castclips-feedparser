import podcastparser
import urllib.request
import json


def parse_feed(event, context):
  feedurl = event['queryStringParameters']['feedUrl']
  parsed = podcastparser.parse(feedurl, urllib.request.urlopen(feedurl))

  body = {
    'title': parsed['title'],
    'link': parsed['link'],
    'description': parsed['description'],
    'episodes': [ {
        'title': e['title'],
        'description': e['description'],
        'published': e['published'],
        'mediaUrl': e['enclosures'][0]['url']
      } for e in parsed['episodes'] ]
  }

  response = {
    'statusCode': 200,
    'headers': {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json'
    },
    'body': json.dumps(body),
    'isBase64Encoded': False
  }

  return response
