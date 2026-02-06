from epl import app, db
from flask import render_template, redirect, url_for, flash, request
from epl.models import Club, Player

@app.route('/')
def home():
  return render_template('index.html',
                         title='Home Page')

@app.route('/clubs')
def all_clubs():
  query = db.select(Club)
  clubs = db.session.scalars(query).all()
  return render_template('clubs/index.html',
                         title='Clubs Page',
                         clubs=clubs)

@app.route('/clubs/new', methods=['GET', 'POST'])
def new_club():
  if request.method == 'POST':
    name = request.form['name']
    stadium = request.form['stadium']
    year = int(request.form['year'])
    logo = request.form['logo']

    club = Club(name=name, stadium=stadium, year=year, logo=logo)
    db.session.add(club)
    db.session.commit()

    flash('add new club successfully', 'success')
    return redirect(url_for('all_clubs'))
  
  return render_template('clubs/new_club.html',
                         title='New Club Page',
                         )

@app.route('/clubs/search', methods=['GET', 'POST'])
def search_club():
  if request.method == 'POST':
    club_name = request.form['club_name']
    query = db.select(Club).where(Club.name.like(f'%{club_name}%'))
    clubs = db.session.scalars(query).all()

    return render_template('clubs/search_club.html',
                           title='Search Club Page',
                           clubs=clubs)
  
@app.route('/clubs/<int:id>/info')
def info_club(id):
  club = db.session.get(Club, id)
  return render_template('clubs/info_club.html',
                         title='Info Club Page',
                         club=club)

@app.route('/clubs/<int:id>/update', methods=['GET', 'POST'])
def update_club(id):
  club = db.session.get(Club, id)
  if request.method == 'POST':
    name = request.form['name']
    stadium = request.form['stadium']
    year = int(request.form['year'])
    logo = request.form['logo']

    club.name = name
    club.stadium = stadium
    club.year = year
    club.logo = logo

    db.session.add(club)
    db.session.commit()

    flash('update club successfully', 'success')
    return redirect(url_for('all_clubs'))
  
  return render_template('clubs/update_club.html',
                         title='Update Club Page',
                         club=club)


@app.route('/players')
def all_players():
  query = db.select(Player)
  player = db.session.scalars(query).all()
  return render_template('players/index.html',
                         title='Players Page',
                         players=players)

@app.route('/players/new', methods=['GET', 'POST'])
def new_player():
  query = db.select(Club)
  clubs = db.session.scalars(query).all()

  if request.method == 'POST':
    name = request.form['name']
    position = request.form['position']
    naytionlity = request.form['naytionlity']
    goals = request.form['goals']
    squad_no = request.form['squad_no']
    img = request.form['img']
    club_id =request.form['club_id']
    
  
    player = player(name=name,
                    position=position,
                    naytionlity=naytionlity,
                    goals=goals,
                    squad_no=squad_no,
                    img=img,
                    club_id=club_id,
                    )
    db.session.add(club)
    db.session.commit()

    flash('add new club successfully', 'success')
    return redirect(url_for('all_clubs'))
  
  return render_template('players/new_player.html',
                         title='New Player Page',
                         clubs=clubs)

@app.route('/clubs/search', methods=['GET', 'POST'])
def search_player():
  if request.method == 'POST':
    club_name = request.form['player_name']
    query = db.select(Player).where(Player.name.like(f'%{player_name}%'))
    Player = db.session.scalars(query).all()

    return render_template('players/search_player.html',
                           title='Search Player Page',
                           players=players)