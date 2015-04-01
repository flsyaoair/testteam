# -*- coding: UTF-8 -*- 

from testTeam import create_testTeam_app
from testTeam.testteamconfig import *

app = create_testTeam_app()

if __name__ == '__main__':
    app.debug = DEBUG
    app.run(host= HOST,port=PORT)
