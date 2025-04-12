from src import db

class Staff(db.Model):
    __tablename__ = 'staff'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    phone_extension = db.Column(db.String(10))
    is_active = db.Column(db.Boolean, default=True)
    
    visitors = db.relationship('Visitor', backref='staff_contact', lazy=True)
    
    def __repr__(self):
        return f'<Staff {self.first_name} {self.last_name} ({self.department})>'