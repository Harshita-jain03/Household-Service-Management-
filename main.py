from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security
from application.models import db,User,Role
from config import DevelopmentConfig
from application.resources import api
from application.sec import datastore
from application.worker import celery_init_app
from celery.schedules import crontab
from application.tasks import daily_reminder, Monthly_reminder
import flask_excel as excel


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    api.init_app(app)
    excel.init_excel(app)
    app.security = Security(app, datastore)
    with app.app_context():
        import application.views
    return app

app = create_app()
celery_app = celery_init_app(app)



@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(0,0,day_of_month=1),
        Monthly_reminder.s()
    )

    sender.add_periodic_task(
        crontab(minite=0,hour=0)
    )


if __name__ == '__main__':
    app.run(debug=True)
