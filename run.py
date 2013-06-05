#!/usr/bin/env python

from flask.ext.restful import Api
#from nmapworker import nmapapi, task_manager
from nmapui import app

#api = Api(app)
#api.add_resource(nmapapi.NmapTasksListResource, '/nmaptasks')
#api.add_resource(nmapapi.NmapTaskResource, '/nmaptasks/<string:task_id>')

app.run(host='0.0.0.0', port=80, debug=True)
