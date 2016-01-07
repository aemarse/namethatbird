from flask.ext.script import Command, Option
from .utils import download_archive


class DownloadXenoCantoArchive(Command):
    """ Downloads sounds and metadata from the XenoCanto archive
    """
    # option_list = (
    #     Option('--first_nr', dest='first_nr', default=1, help='First recording id to fetch'),
    #     Option('--last_nr', dest='last_nr', default=None, help='Last recording id to fetch'),
    # )

    def run(self):
        print 'Downloading XenoCanto archive'
        download_archive()