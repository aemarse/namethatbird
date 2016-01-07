from flask.ext.script import Command
from .utils import download_archive


class DownloadXenoCantoArchive(Command):
    """ Downloads sounds and metadata from the XenoCanto archive
    """

    def run(self):
        print "Downloading XenoCanto archive"
        download_archive()