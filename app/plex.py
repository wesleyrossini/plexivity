#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import config
from app.logger import logger
import requests
from xml2json import xml2json


class Server(object):
    def __init__(self, host, port):
        if host.startswith("http://"):
            self.host = host.replace("http://", "")
        else:
            self.host = host
        self.port = port
        self.session = requests.session()
        self.url = "http://%s:%d/" % (host, port)
        self.token = False
        self.status = 0


    def test(self):
        status = self._request("status")
        if len(status):
            self.status = 1
        else:
            self.status = 0

        return self.status


    def _request(self, url, args=dict()):
        if self.token:
            args["X-Plex-Token"] = self.token
        result = self.session.get("%s%s" % (self.url, url), params=args)
        logger.debug(u"PLEX => requested url: %(url)s" % {"url": url})

        if result.status_code == 401 and config.PMS_USER != "username" and config.PMS_PASS != "password":
            logger.debug(u"request failed, trying with auth")
            self.session.headers.update({'X-Plex-Client-Identifier': 'plexivity'})
            self.session.headers.update({'Content-Length': 0})

            self.session.auth = (config.PMS_USER, config.PMS_PASS)
            x = self.session.post("https://my.plexapp.com/users/sign_in.xml")
            if x.ok:
                json = xml2json(x.content, strip_ns=False)
                self.token = json["user"]["authentication-token"]
                args["X-Plex-Token"] = self.token
                logger.debug(u"auth successfull, requesting url %(url)s again" % {"url": url})
                result = self.session.get("%s%s" % (self.url, url), params=args)
            else:
                return False

        if result and "xml" in result.headers['content-type']:
            import xml.etree.ElementTree as ET
            #json = xml2json(result.content, strip_ns=False)
            json = ET.fromstring(result.content)
            return json
        else:
            return result.content

    def getThumb(self, url):
        if self.token:
            return "http://%(host)s:%(port)s%(url)s?X-Plex-Token=%(token)s" % {"host": self.host, "port": self.port,
                                                                               "url": url, "token": self.token}
        else:
            return "http://%(host)s:%(port)s%(url)s" % {"host": self.host, "port": self.port, "url": url}

    def get_thumb_data(self, url):
        return self._request(url)

    def currentlyPlaying(self):
        return self._request("status/sessions")

    def getSections(self):
        return self._request("library/sections")

    def recentlyAdded(self, count=6):
        args = {"X-Plex-Container-Start": 0, "X-Plex-Container-Size": count}
        return self._request("library/recentlyAdded", args)

    def getInfo(self, mediaId):
        return self._request("library/metadata/%s" % mediaId)

    def libraryStats(self):
        sections = self.getSections()
        for section in sections:
            section.set("extra", self._request("library/sections/%s/all" % section.get("key")))

        return sections