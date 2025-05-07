import datetime
from app import db

class Book(db.Model):
    """Model representing a book collection of Rumi's works"""
    id = db.Column(db.Integer, primary_key=True)
    title_tj = db.Column(db.String(200), nullable=False)
    description_tj = db.Column(db.Text, nullable=True)
    volumes = db.relationship('Volume', backref='book', lazy=True)
    
    def __repr__(self):
        return f'<Book {self.title_tj}>'

class Volume(db.Model):
    """Model representing a volume within a book"""
    id = db.Column(db.Integer, primary_key=True)
    title_tj = db.Column(db.String(200), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    sections = db.relationship('Section', backref='volume', lazy=True)
    
    def __repr__(self):
        return f'<Volume {self.title_tj}>'

class Section(db.Model):
    """Model representing a section within a volume"""
    id = db.Column(db.Integer, primary_key=True)
    title_tj = db.Column(db.String(200), nullable=False)
    volume_id = db.Column(db.Integer, db.ForeignKey('volume.id'), nullable=False)
    poems = db.relationship('Poem', backref='section', lazy=True)
    
    def __repr__(self):
        return f'<Section {self.title_tj}>'

class Poem(db.Model):
    """Model representing a poem by Rumi"""
    id = db.Column(db.Integer, primary_key=True)
    title_tj = db.Column(db.String(255), nullable=False)
    content_tj = db.Column(db.Text, nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    
    def __repr__(self):
        return f'<Poem {self.title_tj}>'

class DailyVerse(db.Model):
    """Model to track which poems have been shown as daily verses"""
    id = db.Column(db.Integer, primary_key=True)
    poem_id = db.Column(db.Integer, db.ForeignKey('poem.id'), nullable=False)
    display_date = db.Column(db.Date, nullable=False, default=datetime.date.today)
    verse_text = db.Column(db.Text, nullable=False)
    
    poem = db.relationship('Poem', backref='daily_verses')
    
    def __repr__(self):
        return f'<DailyVerse for {self.display_date}>'

class BiographySection(db.Model):
    """Model for sections of Rumi's biography"""
    id = db.Column(db.Integer, primary_key=True)
    title_tj = db.Column(db.String(255), nullable=False)
    content_tj = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<BiographySection {self.title_tj}>'
