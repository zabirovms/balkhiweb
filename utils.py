import datetime
import random
from sqlalchemy import func
from app import db
from models import Poem, DailyVerse

def get_random_poem():
    """Get a random poem from the database"""
    poem_count = Poem.query.count()
    if poem_count == 0:
        return None
    
    random_offset = random.randint(0, poem_count - 1)
    return Poem.query.offset(random_offset).first()

def get_random_verse_from_poem(poem):
    """Extract a random verse from a poem's content"""
    if not poem:
        return None
    
    # Split the poem content into verses (assuming verses are separated by blank lines)
    verses = [v.strip() for v in poem.content_tj.split('\n\n') if v.strip()]
    
    # If there are no clear verse separations, split by lines
    if len(verses) <= 1:
        verses = [v.strip() for v in poem.content_tj.split('\n') if v.strip()]
    
    # Select a random verse or a small group of lines
    if len(verses) <= 3:
        return poem.content_tj
    else:
        start_idx = random.randint(0, len(verses) - 3)
        selected_verses = verses[start_idx:start_idx + random.randint(1, 3)]
        return '\n\n'.join(selected_verses)

def get_daily_verse():
    """Get or create the daily verse"""
    today = datetime.date.today()
    
    # Try to get today's verse
    daily_verse = DailyVerse.query.filter_by(display_date=today).first()
    
    # If no verse for today, create a new one
    if not daily_verse:
        # Get poems that haven't been used as daily verses recently
        # (excluding last 30 days or all existing daily verses if fewer)
        recent_poem_ids = [dv.poem_id for dv in 
                           DailyVerse.query.order_by(DailyVerse.display_date.desc()).limit(30).all()]
        
        # Get a random poem, preferably one that hasn't been used recently
        if recent_poem_ids:
            eligible_poem = Poem.query.filter(~Poem.id.in_(recent_poem_ids)).order_by(func.random()).first()
            # If all poems have been used recently, just get a completely random one
            if not eligible_poem:
                eligible_poem = get_random_poem()
        else:
            eligible_poem = get_random_poem()
            
        if eligible_poem:
            verse_text = get_random_verse_from_poem(eligible_poem)
            
            # Create new daily verse
            daily_verse = DailyVerse(
                poem_id=eligible_poem.id,
                display_date=today,
                verse_text=verse_text
            )
            
            db.session.add(daily_verse)
            db.session.commit()
    
    return daily_verse
