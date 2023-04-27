from urllib.parse import urljoin
from datetime import datetime

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), unique=True, nullable=False)
    short = db.Column(db.String(256), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self, base_url):
        return dict(
            url=self.original,
            short_link=urljoin(base_url, self.short),
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
