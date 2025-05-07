import datetime
import random
from sqlalchemy.sql.expression import func
from flask import render_template, request, redirect, url_for, jsonify

from extensions import db
from models import Book, Volume, Section, Poem, DailyVerse, BiographySection
from utils import get_daily_verse

def register_routes(app):
    @app.route('/')
    def index():
        """Home page route"""
        daily_verse = get_daily_verse()
        books = Book.query.all()
        return render_template('index.html', daily_verse=daily_verse, books=books)

    @app.route('/poems')
    def poems():
        """View all poems with filters and search"""
        # Get filter parameters
        book_id = request.args.get('book_id', type=int)
        volume_id = request.args.get('volume_id', type=int)
        section_id = request.args.get('section_id', type=int)
        search_term = request.args.get('search_term', '').strip()
        
        # Query books for filter dropdown
        books = Book.query.all()
        
        # Query volumes based on selected book
        volumes = []
        if book_id:
            volumes = Volume.query.filter_by(book_id=book_id).all()
        
        # Query sections based on selected volume
        sections = []
        if volume_id:
            sections = Section.query.filter_by(volume_id=volume_id).all()
        
        # Query poems with filters
        poems_query = Poem.query
        
        # Apply search term if provided
        if search_term:
            poems_query = poems_query.filter(
                Poem.content_tj.ilike(f'%{search_term}%') | 
                Poem.title_tj.ilike(f'%{search_term}%')
            )
        
        # Apply hierarchical filters
        if section_id:
            poems_query = poems_query.filter_by(section_id=section_id)
        elif volume_id:
            poems_query = poems_query.join(Section).filter(Section.volume_id == volume_id)
        elif book_id:
            poems_query = poems_query.join(Section).join(Volume).filter(Volume.book_id == book_id)
        
        # Paginate results
        page = request.args.get('page', 1, type=int)
        poems = poems_query.paginate(page=page, per_page=12, error_out=False)
        
        return render_template(
            'poems.html',
            poems=poems,
            books=books,
            volumes=volumes,
            sections=sections,
            selected_book_id=book_id,
            selected_volume_id=volume_id,
            selected_section_id=section_id,
            search_term=search_term
        )

    @app.route('/poem/<int:poem_id>')
    def poem_detail(poem_id):
        """View a specific poem"""
        poem = Poem.query.get_or_404(poem_id)
        return render_template('poem_detail.html', poem=poem)

    @app.route('/biography')
    def biography():
        """Rumi's biography page"""
        biography_sections = BiographySection.query.order_by(BiographySection.order).all()
        return render_template('biography.html', biography_sections=biography_sections)

    @app.route('/search')
    def search():
        """Search for poems"""
        query = request.args.get('q', '')
        if not query:
            return render_template('search.html', results=None, query=None)
        
        # Search in poem titles and content
        results = Poem.query.filter(
            (Poem.title_tj.ilike(f'%{query}%')) | 
            (Poem.content_tj.ilike(f'%{query}%'))
        ).all()
        
        return render_template('search.html', results=results, query=query)

    @app.route('/get_volumes/<int:book_id>')
    def get_volumes(book_id):
        """AJAX endpoint to get volumes for a book"""
        volumes = Volume.query.filter_by(book_id=book_id).all()
        return jsonify([{'id': v.id, 'title_tj': v.title_tj} for v in volumes])

    @app.route('/get_sections/<int:volume_id>')
    def get_sections(volume_id):
        """AJAX endpoint to get sections for a volume"""
        sections = Section.query.filter_by(volume_id=volume_id).all()
        return jsonify([{'id': s.id, 'title_tj': s.title_tj} for s in sections])
