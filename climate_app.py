# Import dependencies
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect all the things
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Reference all the things
Measurement = Base.classes.measurement
Station = Base.classes.station

# Python -> database
session =  Session(engine)

app = Flask(__name__)

@app.route("/")
def homepage():
    """List of all available API routes"""
    return(

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.tobs).\
        filter
