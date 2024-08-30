from datetime import datetime

from yacut import db, app



class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now(), index=True)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=app.config['PREFIX_URL'] + self.short
        )