# import OG dependencies
import datetime as dt 
import numpy as np 
import pandas as pd 

# import SQLalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import Flask dependencies
from flask import Flask, jsonify

# setup database engine
engine = create_engine('sqlite:///hawaii.sqlite')

# reflect existing database
Base = automap_base()

# reflect tables in database
Base.prepare(engine, reflect=True)

# save references to each table
Measurement = Base.classes.measurement 
Station = Base.classes.station 

# create session link from Python to DB
session = Session(engine)

# define Flask app
app = Flask(__name__)

# set up welcome route
@app.route('/')

# define welcome route
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br>
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/temp/start/end
    ''')

# set up precipitation route
@app.route('/api/v1.0/precipitation')

# define precipitation function
def precipitation():
    #set prev_year variable for one year of data
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query precipitation data for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    #create dictionary of date: precipitation 
    precip = {date: prcp for date, prcp in precipitation}
    # jsonify
    return jsonify(precip)


# set up stations route
@app.route("/api/v1.0/stations")

# define stations function
def stations():
    #query all stations
    results = session.query(Station.station).all()
    #unravel results into 1D array
    stations = list(np.ravel(results))
    #jsonify
    return jsonify(stations=stations)

# set up tobs route
@app.route("/api/v1.0/tobs")

# define temp_monthly function
def temp_monthly():
    #set time period for previous year
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query data for temperature at station with most recordings
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= prev_year).all()
    #covnert temps into a list
    temps = list(np.ravel(results))
    #jsonify the temps list
    return jsonify(temps=temps)

# set up temp/start and temp/start/end route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# define temp/start/end function
def stats(start=None, end=None):
    #create list of aggregate queries to be peformed: min, avg, and max
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    #use if not end to query only start date
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        #unravel list and jsonify
        temps = list(np.ravel(results))
        return jsonify(temps)

    #query for both start and end date
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    #unravel list and jsonify
    temps = list(np.ravel(results))
    return jsonify(temps)