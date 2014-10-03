#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.logger import logger
from flask.ext.babel import gettext as _
from app import config, plex

from apscheduler.schedulers.background import BackgroundScheduler

def currentlyPlaying():
    print "job fired"
    logger.info("running job")

def startScheduler():
    #in debug mode this is executed twice :(
    #DONT run flask in auto reload mode when testing this!
    scheduler = BackgroundScheduler()
    scheduler.add_job(notifyer, 'interval', seconds=10, max_instances=1)
    print scheduler.get_jobs()
    scheduler.start()

def statistics():
    pass


def getPercentage(viewed, duration):
    percent = "%2d" % ((float(viewed) / float(duration)) * 100)

    if int(percent) >= 90:
        return 100
    return percent

def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    if float(time):
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    else:
        diff = now - now

    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return _("just now")
        if second_diff < 60:
            return _("%(int)s seconds ago", int=second_diff)
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return _("%(int)s minuten ago", int=second_diff / 60)
        if second_diff < 7200:
            return _("an hour ago")
        if second_diff < 86400:
            return _("%(int)s hours ago", int=second_diff / 3600)
    if day_diff == 1:
        return _("Yesterday")
    if day_diff < 7:
        return _("%(int)s days ago", int=day_diff)
    if day_diff < 31:
        return _("%(int)s weeks ago", int=day_diff / 7)
    if day_diff < 365:
        return _("%(int)s months ago", int=day_diff / 30)
    return _("%(int)s years ago", int=day_diff / 365)

def notifyer():
    ### onyl basic tests here
    # TODO: move this to a extra file and include DB support!
    p = plex.Server(config.PMS_HOST, config.PMS_PORT)
    sessions = p.currentlyPlaying()
    print "start shit"
    print sessions.items()
    for session in sessions:
        if session.get("type") == "episode":
            title = '%s - "%s"' % (session.get("grandparentTitle"), session.get("title"))
        else:
            title = session.get("title")

        offset = int(session.get("viewOffset")) / 1000 / 60
        username = session.find("User").get("title")
        platform = session.find("Player").get("platform")
        product = session.find("Player").get("product")
        player_title = session.find("Player").get("product")

        message = config.START_MESSAGE % {"username": username, "platform": platform, "title": title, "product": product, "player_title": player_title, "offset": offset}
        print config.NOTIFY_PUSHOVER
        if config.NOTIFY_PUSHOVER:
            from app.providers import pushover
            pushover.send_notification(message)


def playerImage(platform):
    if platform == "Roku":
        return "images/platforms/roku.png"
    elif platform == "Apple TV":
        return "images/platforms/appletv.png"
    elif platform == "Firefox":
        return "images/platforms/firefox.png"
    elif platform == "Chromecast":
        return "images/platforms/chromecast.png"
    elif platform == "Chrome":
        return "images/platforms/chrome.png"
    elif platform == "Android":
        return "images/platforms/android.png"
    elif platform == "Nexus":
        return "images/platforms/android.png"
    elif platform == "iPad":
        return "images/platforms/ios.png"
    elif platform == "iPhone":
        return "images/platforms/ios.png"
    elif platform == "iOS":
        return "images/platforms/ios.png"
    elif platform == "Plex Home Theater":
        return "images/platforms/pht.png"
    elif platform == "Linux/RPi-XBMC":
        return "images/platforms/xbmc.png"
    elif platform == "Safari":
        return "images/platforms/safari.png"
    elif platform == "Internet Explorer":
        return "images/platforms/ie.png"
    elif platform == "Unknown Browser":
        return "images/platforms/default.png"
    elif platform == "Windows-XBMC":
        return "images/platforms/xbmc.png"
    else:
        return "images/platforms/default.png"
