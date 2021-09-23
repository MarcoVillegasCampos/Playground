from flask import Flask, render_template


app= Flask( __name__)


@app.route('/play', methods=['GET'])
def loadHome():
    return render_template('index.html')

#@app.route('/sports', methods=['GET'] )
#def getSports():
 #   print("This is executing my first endpoint in the server")
  #  return dictionarySports

#@app.route('/sport/<id>', methods = ['GET'])
#def getSportById ( id ):
 #   sportID= int(id)
  #  for sport in listOfSports:
   #     if sport['id']== sportID:
    #        return "The sport of this id is "+sport['name']
     
     #   return "There is no sport with this id, try another one"



#if __name__ == "__main__":
 #   app.run(debug=True)
    