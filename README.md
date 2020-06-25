# Plex-api library metadata mutator
Automatically mutate specified metadata of your media inside your Plex library

# How does it work?
The Python script uses the RESTFULL api of your Plex server to access your libraries and iterate over the videos in each library.
Each video will then be requested separately to get the information and metadata about it.
Then a put request will be fired to update a specefied metadata attribute.

This script can be used to update all kinds of video information or metadata, just read the script and change to your needs.

# Installation
Install requirements

Edit mutate-metadata.py for your needs and change the following consts

- DRIVES
- DRIVE_PREFIX
- SSL
- PLEX_SERVER_IP
- PLEX_SERVER_PORT
- PLEX_SERVER_URL

Run mutate-metadata.py
