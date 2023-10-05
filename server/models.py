from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('name')
    def validate_name(self, key, name):
        names = db.session.query(Author.name).all()
        if not name:
            raise ValueError("Name if required")
        elif name in names:
            raise ValueError("Name must be unique")
        return name
    
    
    @validates('phone_number')
    def validates_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("Phone Numbers Need Ten Digits")
        return phone_number

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validates_title(self, key, title):
        if not title:
            raise ValueError("Must Have a Title")
        return title
    
    @validates('content')
    def content_length(self, key, content):
        if len(content) > 250:
            raise ValueError("Must Be 250 Characters or less")
        return content
    
    @validates('category')
    def validate_category(self, key, category):
        if category not in ['Fiction', 'Non-Fiction']:
            raise ValueError("Must Be Either Fiction or Non-Fiction")
        return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
