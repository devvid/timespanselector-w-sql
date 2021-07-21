from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime

# Test query string
# select * from view_history where post_id = 4 and CONVERT(varchar, created ,103) BETWEEN '01/06/2020' AND '23/06/2020' and CONVERT(varchar, created, 108) BETWEEN '00:00:01.00' AND '12:00:01.00'



"""
Extensions
"""
db = SQLAlchemy()
migrate = Migrate()

from src.models import User, Post, ViewHistory

"""
Application
"""
def create_app():
    app = Flask(__name__)

    # load the instance config, if it exists, when not testing
    app.config.from_object('src.config.BaseConfiguration')

    db.init_app(app)
    migrate.init_app(app, db)
    cors = CORS(app, resources={r"*": {"origins": app.config['CORS']}})
     
    # All the posts are displayed
    # Start
    @app.route('/api/post/all')
    def all_posts():
        posts = Post.query.join('author').all()
        
        _posts = {
            'posts': []
        }
        for p in posts:
            print(p)
            _posts['posts'].append({
                'id': p.id,
                'title': p.title,
                'body': p.body,
            })
        return jsonify(_posts)
    # End

    # Search posts by date range & time.
    # Start
    @app.route('/api/post-history/search', methods=['POST'])
    def search_post():
        id = request.json.get('id')
        date_time_from = request.json.get('date_time_from')
        date_time_to = request.json.get('date_time_to')
        date_from = date_time_from[:10]
        date_from = date_from[:4]+"-"+date_from[5:7]+"-"+date_from[8:]
        date_to = date_time_to[:10]
        date_to = date_to[:4]+"-"+date_to[5:7]+"-"+date_to[8:]
        time_from = date_time_from[11:19:1]
        time_to = date_time_to[11:19:1]

        print( 'from: ' + date_from + ' ' + time_from + ' to: ' + date_to + ' ' + time_to )
        sql = text("select * from view_history where post_id = "+str(id)+" and created::timestamp::date BETWEEN '"+date_from+"' AND '"+date_to+"' and created::time BETWEEN '"+time_from+"' AND '"+time_to+"'")
        print(sql)
        history = db.engine.execute(sql)
        # history = db.Session.query(ViewHistory).from_statement(sql)
        _history = {
            "history": []
        }
        for p in history:
            _history['history'].append({
                'id': p.id,
                'ipAddress': p.ip_address,
                'created': p.created.strftime("%d/%m/%Y, %H:%M:%S"),
            })
        print(_history)
        return jsonify(_history)
    # End

    # Specific post by id
    # Start
    @app.route('/api/post/<post_id>')
    def detail_post(post_id):
        post = Post.query.filter_by(id=post_id).first()
        if post == None:
            return jsonify({'error': 'No post for the id: {}'.format(post_id)})
        _post = {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'author': {
                'id': post.author.id,
                'name': post.author.name,
            },
            'history': []
            
        }
        return jsonify({'post': _post})

    return app
    # End