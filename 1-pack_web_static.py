#!/usr/bin/python3
"""
Fabric script"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    Generates a tgz archive
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        archive = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive))
        return archive
    except:
        return None


if __name__ == "__main__":
    do_pack()
