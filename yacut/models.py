from datetime import datetime
from typing import Any

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self) -> dict[str, Any]:
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp
        )

    def from_dict(self, data: dict[str, str]) -> None:
        api_column_mapping = {
            'url': 'original',
            'custom_id': 'short'
        }
        for field in ['url', 'custom_id']:
            setattr(self, api_column_mapping[field], data[field])