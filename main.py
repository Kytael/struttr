import os
from flask import *
import sqlalchemy as sa

app = Flask(__name__)
app.debug = True

#connect to the db all 12factor.net -like
engine = sa.create_engine(os.environ["DATABASE_URL"])
conn = engine.connect()

#define our tables
#this will physically create the table if it doesn't exist.
#don't know what it does if table doesn't match schema exists but doesn't match
metadata = sa.MetaData()
boasts = sa.Table("boasts", metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('description', sa.String))

boats = sa.Table("boats", metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('boast', sa.Integer, sa.ForeignKey("boasts.id")))

#need to add some tables for ubots

#actually the action happens here I guess but whatevs,
#the control surface is the above
metadata.create_all(engine)

#root is a static angular page
@app.route('/')
def root():
    return app.send_static_file('index.html')

#json boasts fetch entry point
@app.route("/boasts")
def bsts():
    #this black incantation summons the latest 10 boasts from the netherbase
    res = conn.execute(boasts.select().limit(10).order_by(boasts.c.id.desc()))
   # boastid = 8
   # boatcount = boats.select().where(boats.c.boast == boastid).count()
    #can't serialize rows to json automatically; SQLalchemy sux
    return jsonify({'json': [{'id': r.id, 'description': r.description, 'boats': 5 } for r in res]})

#boastan post entry point
@app.route('/boast', methods=['POST'])
def boast():
    #flask expects urlencoded posts, but angular uses json
    #thus have to manually decode
    data = json.loads(request.data)
    #we want to insert the "boasts" post arg into out database as a boast
    ins = boasts.insert().values(description=data['boast'])
    conn.execute(ins)
    #flask needs an actual response for some reason:
    return "whatever, man"

@app.route('/boat', methods=['POST'])
def boat():
    payload = request.data
    data = json.loads(payload)
    boat = data['boat']
    ins = boats.insert().values(boast=boat)
    conn.execute(ins)
    return "cool story bro"
