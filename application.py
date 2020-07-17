import mysql.connector

from flask import Flask,render_template,request

conn=mysql.connector.connect(host="database-1.cv3euuchz6qz.us-east-2.rds.amazonaws.com",user="admin",password="admin1234",database="moviedb")
mycursor=conn.cursor()

#to create database

# mycursor.execute("CREATE DATABASE moviedb")

#create first table

# mycursor.execute("CREATE TABLE movies (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL,actor VARCHAR(100) NOT NULL,year VARCHAR(50),poster VARCHAR(255))")

# Insert Data

# mycursor.execute("INSERT INTO movies (id,name,actor,year,poster) VALUES (NULL,'3 idiots','Aamir Khan','2009','https://m.media-amazon.com/images/M/MV5BNTkyOGVjMGEtNmQzZi00NzFlLTlhOWQtODYyMDc2ZGJmYzFhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg')")

# conn.commit()

# mycursor.execute("SELECT * FROM movies")
# data=mycursor.fetchall()
# print(data)

# mycursor.execute("DELETE FROM movies WHERE id = 5")

# conn.commit()


application=Flask(__name__)

@application.route('/')

def index():
	mycursor.execute("SELECT * FROM movies")
	
	data=mycursor.fetchall()

	return render_template('index.html',data=data)



@application.route('/add')
def add():
	return render_template('addmovie.html')

@application.route('/insert',methods=['POST'])
def insert():
	name=request.form.get('name')
	actor=request.form.get('actor')
	year=request.form.get('year')
	poster=request.form.get('poster')	

	mycursor.execute("INSERT INTO movies (id,name,actor,year,poster) VALUES (NULL,'{}','{}','{}','{}')".format(name,actor,year,poster))

	conn.commit()

	return render_template('addmovie.html')


if __name__=="__main__":
	application.run(debug=True)
