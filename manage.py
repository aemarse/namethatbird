from flask.ext.script import Manager
from namethatbird.app import app

manager = Manager(app)

from namethatbird.modules.sounds.scripts import DownloadXenoCantoArchive
manager.add_command('download_xc', DownloadXenoCantoArchive())

if __name__ == "__main__":
    manager.run()