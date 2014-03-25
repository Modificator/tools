#!/usr/bin/python
# Filename: config.py

### File Information ###
"""
Configuration
"""

__author__ = 'duanqz@gmail.com'



import os.path

import sys


class Config:
    """ Configuration.
    """

    # Whether in debug mode or not
    DEBUG = False

    # Whether to revise OPTION feature, default to be True
    REVISE_OPTION = True


### Root directory   
    # Root directory of current project
    PRJ_ROOT = os.curdir

    # Root directory plug-in, like diff-patch.sh
    PLUG_ROOT = sys.path[0]

    # Root directory of reject files
    REJ_ROOT = os.path.join(PRJ_ROOT, "out/reject/")

### DIFF-PATCH Directory
    # We need to hold three directory because diff_patch.sh
    # incorporate changes from newer to older into target.

    AUTOPATCH_DIR = os.path.join(PRJ_ROOT, "autopatch/")

    # Older directory
    OLDER_DIR = os.path.join(AUTOPATCH_DIR, "aosp/")

    # Newer directory
    NEWER_DIR = os.path.join(AUTOPATCH_DIR, "bosp/")

### Upgrade Directory
    # Upgrade directory contains all the upgrade patches.

    UPGRADE_DIR = os.path.join(AUTOPATCH_DIR, "upgrade/")

    UPGRADE_LAST_BAIDU_DIR = os.path.join(UPGRADE_DIR, "last_baidu/")

    UPGRADE_BAIDU_DIR  = os.path.join(UPGRADE_DIR, "baidu/")

### Patches directory
    # Default patchall.xml to be parsed
    PATCH_XML = os.path.join(AUTOPATCH_DIR, "changelist/patchall.xml")

    PATCH_XML_DIR = os.path.dirname(PATCH_XML)



    @staticmethod
    def setup(argv):
        """ Setup the configuration.
            arguments list is (PATCH_XML, OLDER_DIR, NEWER_DIR)
        """

        argc = len(argv)
        if argc > 0: Config.setPatchXML(argv[0])
        if argc > 1: Config.setReviseOption(argv[1])

        Config.toString()

    @staticmethod
    def setPatchXML(patchXML):
        Config.PATCH_XML = patchXML
        Config.PATCH_XML_DIR = os.path.dirname(Config.PATCH_XML)

    @staticmethod
    def setDiffDir(olderDir, newerDir):
        Config.OLDER_DIR = olderDir
        Config.NEWER_DIR = newerDir

    @staticmethod
    def setReviseOption(option):
        option = option.lower()
        if option == "true":
            Config.REVISE_OPTION = True
        elif option == "false" :
            Config.REVISE_OPTION = False

    @staticmethod
    def toString():
        Log.d("-----------------------------------------------------------")
        Log.d("PRJ_ROOT:\t" + Config.PRJ_ROOT)
        Log.d("PLUG_ROOT:\t" + Config.PLUG_ROOT)
        Log.d("---")
        Log.d("OLDER_DIR:\t" + Config.OLDER_DIR)
        Log.d("NEWER_DIR:\t" + Config.NEWER_DIR)
        Log.d("---")
        Log.d("PATCH_XML:\t" + Config.PATCH_XML)
        Log.d("REVISE_OPTION:\t" + str(Config.REVISE_OPTION))
        Log.d("-----------------------------------------------------------")

# End of class Config

class Log:

    BUFF = []

    @staticmethod
    def d(message):
        if Config.DEBUG: print message

    @staticmethod
    def i(message):
        print message

    @staticmethod
    def w(message):
        Log.record(message)
        print " Waring: ",
        print message

    @staticmethod
    def e(message):
        Log.record(message)
        print " Error: ",
        print message

    @staticmethod
    def record(message):
        Log.BUFF.append(message)


if __name__ == "__main__":
    Config.toString()