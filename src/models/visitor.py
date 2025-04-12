from datetime import datetime
from src import db

class Visitor(db.Model):
    __tablename__ = 'visitors'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    id_type = db.Column(db.String(50))  # e.g., 'Driver License', 'Passport'
    id_number = db.Column(db.String(50))
    company = db.Column(db.String(100))
    vehicle_number = db.Column(db.String(20))
    check_in = db.Column(db.DateTime, default=datetime.utcnow)
    check_out = db.Column(db.DateTime)
    purpose = db.Column(db.Text, nullable=False)
    staff_contact_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    status = db.Column(db.String(20), default='checked_in')
    
    def __repr__(self):
        return f'<Visitor {self.first_name} {self.last_name}>'