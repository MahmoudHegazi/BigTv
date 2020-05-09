#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Menu, Series, Movie, Item
from flask import session as login_session
import random
import string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
app = Flask(__name__)


engine = create_engine('sqlite:///bigtv.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/bigtv/<int:item_id>/series/<int:menu_id>/JSON')
def menuSeriesSON(item_id, menu_id):
    Menu_Item = session.query(Series).filter_by(id=menu_id).one()
    return jsonify(Menu_Item=Menu_Item.serialize)

@app.route('/bigtv/<int:item_id>/movies/<int:menu_id>/JSON')
def menuMoviesJSON(item_id, menu_id):
    Menu_Item = session.query(Movie).filter_by(id=menu_id).one()
    return jsonify(Menu_Item=Menu_Item.serialize)


@app.route('/bigtv/JSON')
def bigtvJSON():
    content = session.query(Menu).all()
    return jsonify(Content=[r.serialize for r in content])



# Show all restaurants
@app.route('/')
@app.route('/bigtv/', methods=['GET', 'POST'])
def showIndex():
    movies = session.query(Movie).order_by(asc(Movie.name))
    series = session.query(Series).order_by(asc(Series.name))
    return render_template('index.html', movies=movies, series = series)


@app.route('/bigtv/series/<int:series_id>/episode/<int:content_id>/')
def showSeries(series_id, content_id):
    series = session.query(Series).filter_by(id=series_id).first()
    boots =  session.query(Item).filter_by(series_id=1).all()
    episode = session.query(Item).filter_by(id=1).first()
    print('1' + str(series))
    print('2' + str(boots))
    print(u'hi %s' %episode.name)
    return render_template('video.html', series = series, boots = boots, episode=episode)
    
    
@app.route('/mform')
def index():
	return render_template('form.html')   


    
    
@app.route('/process', methods=['POST'])
def showprocess():    
    
    mytag = request.form['search']
    # if mytag not empty
    if mytag:
        myseries =  session.query(Series).filter_by(name=mytag).first()
        mymovie =  session.query(Movie).filter_by(name=mytag).first()
        myeposide =  session.query(Item).filter_by(name=mytag).first()
        
        # if seires != none return json with series link
        if myseries:
            message = 'https://www.google.com/'
            cname = 'A Series Founded with name %s' %myseries.name
            imge = myseries.image
            return jsonify({'search' : message, 'name' : cname, 'iurl' : imge})
            
        # if mymovie != none return json with movie link    
        if mymovie:
            message = mymovie.image
            imge = mymovie.image
            cname = 'A Movie Founded with name %s' %mymovie.name
            return jsonify({'search' : message, 'name' : cname, 'iurl' : imge})
            
        # if myeposide != none return json with eposide link
        if myeposide:
            message = myeposide.server1
            imge = myeposide.image
            cname = 'An Eposide Founded with name %s' %myeposide.name
            return jsonify({'search' : message, 'name' : cname, 'iurl' : imge})
            
    # if mytag  empty or if no result found return error 
             
    return jsonify({'error' : 'No Result Found!'})  
        
        
    
    
    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
