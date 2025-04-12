import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '6d85f2a4-5b18-4cf2-9e1d-3f9b7a8c2d1e')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 
        'mysql+pymysql://root:g)8nE>?rq-#v3Ta@localhost/visitor_management')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHOOL_NAME = "Instituto Privado Andrés Bello CA"
    DEFAULT_CHECKIN_DURATION = 4  # hours