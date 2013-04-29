#!/usr/bin/env python

from nmapui import models, config, app, db

#u = models.User(username='ronald', password='test',  email='ronald@secaas.be', role=config.ROLE_ADMIN)
#db.session.add(u)
#db.session.commit()

app_user = models.User.query.filter_by(username='ronad').first()
print app_user.username
