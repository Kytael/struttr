import os
from flask import *
import sqlalchemy as sa

app = Flask(__name__)

app.debug = True

engine = sa.create_engine('postgresql://wolf@localhost/struttr')
conn = engine.connect()

metadata = sa.MetaData()
boasts = sa.Table("boasts", metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('description', sa.String))

metadata.create_all(engine)

@app.route('/')
def root():
    return render_template('root.html', hello="hhhh")

@app.route('/boast', methods=['GET', 'POST'])
def boast():
    ins = boasts.insert().values(description=request.args.get('brag'))
    conn.execute(ins)
    return redirect(url_for('root'))