from libnmap import NmapParser, NmapReport, NmapProcess, ReportDecoder
from libnmap.plugins.mongodb import NmapMongoPlugin
from nmapui import config
import json

class NmapManager(object):
    def __init__(self):
        self.upload_folder = config.UPLOAD_FOLDER

    def get_reports(self):
        robjlist = []
        mongodb = NmapMongoPlugin()
        rlist = mongodb.db_get()
        for r in rlist:
            robj = r['__NmapReport__']
            robjlist.append(robj)
        return robjlist
