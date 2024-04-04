#!/usr/bin/python3
"""
 Deletes out-of-date archives
"""

from fabric.operations import local, run, put, sudo
import os
from fabric.api import env


env.hosts = ["3.84.238.226", "54.84.245.120"]


def do_clean(number=0):
    """Deletes out-of-date archives"""
    files = local("ls -1t versions", capture=True)
    file_names = files.split("\n")
    n = int(number)
    if n in (0, 1):
        n = 1
    for i in file_names[n:]:
        local("rm versions/{}".format(i))
    dir_server = run("ls -1t /data/web_static/releases")
    dir_server_names = dir_server.split("\n")
    for i in dir_server_names[n:]:
        if i == 'test':
            continue
        run("rm -rf /data/web_static/releases/{}"
            .format(i))
