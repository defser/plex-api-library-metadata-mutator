import requests

import xml.etree.ElementTree as ET

DRIVE_PREFIX = 'Hardeschijf'
DRIVES = {
    'P': 1,
    'Q': 2,
    'R': 3,
    'S': 4,
    'T': 5,
}

SSL = False
PLEX_SERVER_IP = 'localhost'
PLEX_SERVER_PORT = '32400'
PLEX_SERVER_URL = ('https://' if SSL else 'http://') + PLEX_SERVER_IP + ':' + PLEX_SERVER_PORT

librariesResponse = requests.get(PLEX_SERVER_URL + '/library/sections/').text

libraries = ET.fromstring(librariesResponse)

for library in libraries:
    if library.attrib['type'] == 'show':
        # Skip Tv show libraries
        continue

    videosResponse = requests.get(PLEX_SERVER_URL + '/library/sections/' + library.attrib['key'] + '/all/').text

    videos = ET.fromstring(videosResponse)

    for video in videos:
        videoMetaDataResponse = requests.get(PLEX_SERVER_URL + video.attrib['key']).text

        videoMetaData = ET.fromstring(videoMetaDataResponse)

        for metaData in videoMetaData:
            DRIVE_LETTER = metaData.find('./Media').find('./Part').attrib['file'][0]
            DRIVE_NUMBER = str(DRIVES[DRIVE_LETTER])

            requests.put(
                PLEX_SERVER_URL +
                video.attrib['key'] + '?type=1&contentRating.value=' + DRIVE_PREFIX + ' ' + DRIVE_NUMBER
            )

            print('Attached movie to disk ' + DRIVE_LETTER + ': ' + DRIVE_NUMBER + video.attrib['title'])
