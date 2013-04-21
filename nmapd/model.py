from libnmap import NmapParser, NmapReport, NmapProcess
from libnmap.plugins.mongodb import NmapMongoPlugin
from nmapd.config import nmapp_config

class NmapManager(object):
    def __init__(self):
        self.upload_folder = nmapp_config['upload_folder']

    def get_reports(self):
        robjlist = []
        mongodb = NmapMongoPlugin()
        rlist = mongodb.db_get()
        for r in rlist:
            robj = json.loads(r, cls=NmapReportDecoder)
            robjlist.append(robj)
        return robjlist
