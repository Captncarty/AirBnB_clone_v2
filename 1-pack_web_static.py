#!/usr/bin/python3
"""A Fabric script to create an archive file"""

# Imported the necessary modules
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create an archive file of the web_static"""

    # Get the current timestamp and format it as a string
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Created the filename by concatenating
    file_path = "versions/web_static_{}.tgz".format(time_now)

    try:
        # Created a directory called "versions" if it doesn't already exist
        local("mkdir -p versions")

        # Created an archive file using the "tar" command
        local("tar -cvzf {} web_static/".format(file_path))

        # Return the path to the archive file
        return file_path

    except Exception as e:
        # Return None if an error occurs
        return None
