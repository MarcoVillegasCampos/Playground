from flask import Flask, render_template


app= Flask( __name__)

dictionarySports= {
    'sport1':'Football',
    'sport2':'Basketball',
    'sport3':'Soccer',
    'sport3':'Tennis'
}
listOfSports= [
    {
        'id':123,
        'name':'Football'
    },
       {
        id:456,
        'name':'Basketball'
    },   {
        'id':789,
        'name':'Soccer'
    },
    {
        'id':555,
        'name':'Tennis'
    }
]

sportsList= ['Football', ' Basketball', 'Tennis', 'Soccer']

@app.route('/home', methods=['GET'])
def loadHome():
    return render_template('index.html', firstName='Marco', sportsList=sportsList, listOfSports=listOfSports)

@app.route('/sports', methods=['GET'] )
def getSports():
    print("This is executing my first endpoint in the server")
    return dictionarySports

@app.route('/sport/<id>', methods = ['GET'])
def getSportById ( id ):
    sportID= int(id)
    for sport in listOfSports:
        if sport['id']== sportID:
            return "The sport of this id is "+sport['name']
     
        return "There is no sport with this id, try another one"



if __name__ == "__main__":
    app.run(debug=True)
    