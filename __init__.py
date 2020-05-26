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
# Show all restaurants
@app.route('/')
@app.route('/bigtv/', methods=['GET', 'POST'])
def showIndex():
    movies = session.query(Movie).order_by(asc(Movie.name))
    series = session.query(Series).order_by(asc(Series.name))
    return render_template('index.html', movies=movies, series = series)



@app.route('/bigtv/series/<int:series_id>/episodes/')
def showSMenu(series_id):
    series = session.query(Series).filter_by(id=series_id).first()    
    eposides =  session.query(Item).filter_by(series_id=series_id).all()
    #index for series notfound
    series_index = 0
    #index for eposides notfound
    eposide_index = 0
    total_index = series_index + eposide_index
    
    myid = series_id 
    if series == None and total_index < 1:
        message = "The Series with id: %s maybe deleted or not existed but there are eposides" % myid
        flash(message)
    else:
        series_index += 1    
    
    if eposides:
        eposide_index += 1
        
    else:
        if total_index < 1:
        
            message = "We are going to add the eposides soon"          
            flash(message)
            
    
    if total_index > 1:
        message = "There is no Series with id: %s" % myid    
        flash(message)
        
    return render_template('new.html', series = series, eposides = eposides)    
    
    
    
@app.route('/process', methods=['POST'])
def showprocess():    
    
    mytag = request.form['search']
    # if mytag not empty
    if mytag:
        myseries =  session.query(Series).filter_by(name=mytag).first()
        mymovie =  session.query(Movie).filter_by(name=mytag).first()
        myeposide =  session.query(Item).filter_by(name=mytag).first()
        get1 =  session.query(Item).filter_by(tag1=mytag).first()
        get2 =  session.query(Item).filter_by(tag2=mytag).first()
        get3 =  session.query(Item).filter_by(tag3=mytag).first()
        get4 =  session.query(Item).filter_by(tag4=mytag).first()
        get5 =  session.query(Item).filter_by(tag5=mytag).first()
        get6 =  session.query(Item).filter_by(tag6=mytag).first()
        get7 =  session.query(Item).filter_by(tag7=mytag).first()
        get8 =  session.query(Item).filter_by(tag8=mytag).first()
        get9 =  session.query(Item).filter_by(tag9=mytag).first()
        get10 =  session.query(Item).filter_by(tag10=mytag).first()
        get11 =  session.query(Item).filter_by(tag11=mytag).first()
        get12 =  session.query(Item).filter_by(tag12=mytag).first()
        get13 =  session.query(Item).filter_by(tag13=mytag).first()
        get14 =  session.query(Item).filter_by(tag14=mytag).first()
        get15 =  session.query(Item).filter_by(tag15=mytag).first()
        get16 =  session.query(Item).filter_by(tag16=mytag).first()
        get17 =  session.query(Item).filter_by(tag17=mytag).first()

        
        # if seires != none return json with series link
        if myseries:
            message = 'https://www.google.com/'
            cname = 'A Series Founded with name %s' %myseries.name
            # when host on AWS must edit this replace 127.0.0.1:5000 with AWS IP
            seurl = 'http://127.0.0.1:5000/bigtv/series/%s/episodes/' %myseries.id
            imge = myseries.image
            return jsonify({'search' : seurl, 'name' : cname, 'iurl' : imge})
            
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
            
            # in proudction replace 127.0.0.1:5000 with your domain or ip
            # used to return the url needed for the emposide and provide the 2 vars to url give it to AJAX
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %myeposide.series_id 
            epurl_part2 = "series/%s/eposide" %myeposide.id
            fullurl = epurl_part1 + epurl_part2
            
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})
            
        if get1:
            message = get1.server1
            imge = get1.image
            cname = 'An Eposide Founded with name %s' %get1.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get1.series_id 
            epurl_part2 = "series/%s/eposide" %get1.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get2:
            message = get2.server1
            imge = get2.image
            cname = 'An Eposide Founded with name %s' %get2.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get2.series_id 
            epurl_part2 = "series/%s/eposide" %get1.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})
 
        if get3:
            message = get3.server1
            imge = get3.image
            cname = 'An Eposide Founded with name %s' %get3.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get3.series_id 
            epurl_part2 = "series/%s/eposide" %get3.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get4:
            message = get4.server1
            imge = get4.image
            cname = 'An Eposide Founded with name %s' %get4.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get4.series_id 
            epurl_part2 = "series/%s/eposide" %get4.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get5:
            message = get5.server1
            imge = get5.image
            cname = 'An Eposide Founded with name %s' %get5.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get5.series_id 
            epurl_part2 = "series/%s/eposide" %get5.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})
 
        if get6:
            message = get6.server1
            imge = get6.image
            cname = 'An Eposide Founded with name %s' %get6.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get6.series_id 
            epurl_part2 = "series/%s/eposide" %get6.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})
 
        if get7:
            message = get7.server1
            imge = get7.image
            cname = 'An Eposide Founded with name %s' %get7.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get7.series_id 
            epurl_part2 = "series/%s/eposide" %get7.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get8:
            message = get8.server1
            imge = get8.image
            cname = 'An Eposide Founded with name %s' %get8.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get8.series_id 
            epurl_part2 = "series/%s/eposide" %get8.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get9:
            message = get9.server1
            imge = get9.image
            cname = 'An Eposide Founded with name %s' %get9.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get9.series_id 
            epurl_part2 = "series/%s/eposide" %get9.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})
            
        if get10:
            message = get10.server1
            imge = get10.image
            cname = 'An Eposide Founded with name %s' %get10.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get10.series_id 
            epurl_part2 = "series/%s/eposide" %get10.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get11:
            message = get11.server1
            imge = get11.image
            cname = 'An Eposide Founded with name %s' %get11.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get11.series_id 
            epurl_part2 = "series/%s/eposide" %get11.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get12:
            message = get12.server1
            imge = get12.image
            cname = 'An Eposide Founded with name %s' %get12.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get12.series_id 
            epurl_part2 = "series/%s/eposide" %get12.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get13:
            message = get13.server1
            imge = get13.image
            cname = 'An Eposide Founded with name %s' %get13.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get13.series_id 
            epurl_part2 = "series/%s/eposide" %get13.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get14:
            message = get14.server1
            imge = get14.image
            cname = 'An Eposide Founded with name %s' %get14.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get14.series_id 
            epurl_part2 = "series/%s/eposide" %get14.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get15:
            message = get15.server1
            imge = get15.image
            cname = 'An Eposide Founded with name %s' %get15.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get15.series_id 
            epurl_part2 = "series/%s/eposide" %get15.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})

        if get16:
            message = get16.server1
            imge = get16.image
            cname = 'An Eposide Founded with name %s' %get16.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get16.series_id 
            epurl_part2 = "series/%s/eposide" %get16.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})            

        if get17:
            message = get17.server1
            imge = get17.image
            cname = 'An Eposide Founded with name %s' %get17.name
            epurl_part1 = "http://127.0.0.1:5000/bigtv/%s/" %get17.series_id 
            epurl_part2 = "series/%s/eposide" %get17.id
            fullurl = epurl_part1 + epurl_part2
            return jsonify({'search' : fullurl, 'name' : cname, 'iurl' : imge})            
    # if mytag  empty or if no result found return error 
             
    return jsonify({'error' : 'No Result Found!'})  
        

# function for add new series
@app.route('/addprocess', methods=['POST'])
def addseries():    
    
    iname = request.form['name']
    ides = request.form['description']
    ihero = request.form['hero']
    iimage = request.form['image']
    iurl = request.form['url']
    idate = request.form['date']
    imenuid = request.form['menuid']

    # if iname ides ihero iimage iurl idate idate imenuid use CRUD

    if iname and ides and ihero and iimage and iurl and idate and idate and imenuid:
        
        newSeries = Series(name=iname, description=ides, hero=ihero,
                           image=iimage, url=iurl, date=idate,
                           menu_id=imenuid)
        session.add(newSeries)
        
        message = 'Series with Name: %s Added Successfuly' % newSeries.name
        imge = newSeries.image
        session.commit()
        return jsonify({'respond' : message, 'iurl' : imge})
    
    # if mytag  empty or if no result found return error              
    return jsonify({'error' : 'Sorry Problem Found! Please Try after 2 Minutes'})





#show speacific eposide video 

@app.route('/bigtv/<int:series_id>/series/<int:eposide_id>' , methods=['GET', 'POST'])
@app.route('/bigtv/<int:series_id>/series/<int:eposide_id>/eposide' , methods=['GET', 'POST'])
def showEposide(series_id, eposide_id):
    series = session.query(Series).filter_by(id=eposide_id).first()
    eposide = session.query(Item).filter_by(id=eposide_id).first()
    eposides = session.query(Item).filter_by(series_id=series_id).all()
   

    
    return render_template('series.html', series=series, eposide=eposide, myeposides=eposides)


# function for add new eposide
@app.route('/addeposide', methods=['POST'])
def addEposide():    
    
    iname = request.form['getname']
    myserver1 = request.form['getserver']
    myserver2 = request.form['server2']
    getid = request.form['seid']
    print('added')        

    # if iname ides ihero iimage iurl idate idate imenuid use CRUD


    
    if iname and myserver1:
        newItem = Item(name=iname, server1=myserver1, server2=myserver2, series_id=getid)        
        session.add(newItem)
        
        message = 'Series with Name: %s Added Successfuly' % newItem.name
        imge = "tyest"  
        session.commit()
        return jsonify({'respond' : message, 'iurl' : imge})
    print("aded")        
    # if mytag  empty or if no result found return error              
    return jsonify({'error' : 'Sorry Problem Found! Please Try after 2 Minutes'})   



# function for add new series
@app.route('/movieprocess', methods=['POST'])
def addmovie():    
    
    iname = request.form['mname']
    ides = request.form['mdescription']
    ihero = request.form['mhero']
    iimage = request.form['mimage']
    iurl = request.form['murl']
    idate = request.form['mdate']
    imenuid = request.form['mmenuid']

    # if iname ides ihero iimage iurl idate idate imenuid use CRUD

    if iname and ides and ihero and iimage and iurl and idate and idate and imenuid:
        
        newMovie = Movie(name=iname, description=ides, hero=ihero,
                           image=iimage, url=iurl, date=idate,
                           menu_id=imenuid)
        session.add(newMovie)
        
        message = 'New Movie with Name: %s Has Been Added' % newMovie.name
        imge = newMovie.image
        session.commit()
        return jsonify({'respond' : message, 'iurl' : imge})
    
    # if mytag  empty or if no result found return error              
    return jsonify({'error' : 'Sorry Problem Found! Please Try after 2 Minutes'})  

# function for edit series
@app.route('/series/<int:series_id>/edit/', methods=['GET', 'POST'])
def editSeries(series_id):
    SeriesToEdit = session.query(Series).filter_by(id=series_id).one()
    movies = session.query(Movie).order_by(asc(Movie.name))
    series = session.query(Series).order_by(asc(Series.name))
    
    if request.method == 'POST':
        if request.form['ename']:
            SeriesToEdit.name = request.form['ename']
        
        if request.form['edescription']:
            SeriesToEdit.description = request.form['edescription']
            
        if request.form['ehero']:
            SeriesToEdit.hero = request.form['ehero']
        if request.form['eimage']:
            SeriesToEdit.image = request.form['eimage']
        if request.form['eurl']:
            SeriesToEdit.url = request.form['eurl']
        if request.form['eurl']:
            SeriesToEdit.date = request.form['eurl']
        session.add(SeriesToEdit)
        flash('%s Successfully edited' % SeriesToEdit.name)
        session.commit()        
        return redirect(url_for('showIndex', movies=movies, series=series))    
    else:
        return render_template('edit.html', series=SeriesToEdit)


       




# Delete a series
@app.route('/series/<int:series_id>/delete/', methods=['GET', 'POST'])
def deleteSeries(series_id):
    SeriesToDelete = session.query(Series).filter_by(id=series_id).one()
    movies = session.query(Movie).order_by(asc(Movie.name))
    series = session.query(Series).order_by(asc(Series.name))

    if request.method == 'POST':
        session.delete(SeriesToDelete)
        flash('%s Successfully Deleted' % SeriesToDelete.name)
        session.commit()
        return redirect(url_for('showIndex', movies=movies, series=series))    
    else:
        return render_template('deletes.html', series=SeriesToDelete) 

# Delete a series
@app.route('/movie/<int:movie_id>/delete/', methods=['GET', 'POST'])
def deleteMovie(movie_id):
    MovieToDelete = session.query(Movie).filter_by(id=movie_id).one()
    
    movies = session.query(Movie).order_by(asc(Movie.name))
    series = session.query(Series).order_by(asc(Series.name))

    if request.method == 'POST':
        session.delete(MovieToDelete)
        flash('%s Successfully Deleted' % MovieToDelete.name)
        session.commit()
        return redirect(url_for('showIndex', movies=movies, series=series))    
    else:
        return render_template('deletem.html', movie=MovieToDelete) 
 
    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)

