import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

from notify_run import Notify
notify = Notify(endpoint="https://notify.run/R3EV6hx0dLPXxiDF73KD")
notify.send("Click to control videos!", "http://{}:5000/".format(IPAddr))


from flask import Flask, render_template, request
from aMainTopFunctions import *
from bHomeFunctions import *
from cYouTubeFunctions import *
from dGoogleChromeFunctions import *
from eFMoviesFunctions import *
from fPrimeVideosFunctions import *
from gNetflixFunctions import *
from hMainBottomFunctions import *


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        functionName = request.form.get("functionName")

        if functionName == "volumeIncrease":
            volumeIncrease()
        elif functionName == "previousTrack":
            previousTrack()
        elif functionName == "backSeek":
            backSeek()
        elif functionName == "pause":
            pause()
        elif functionName == "forwardSeek":
            forwardSeek()
        elif functionName == "nextTrack":
            nextTrack()
        elif functionName == "volumeDecrease":
            volumeDecrease()


        elif functionName == "escape":
            escape()
        elif functionName == "desktop":
            desktop()
        elif functionName == "fullScreen":
            fullScreen()
        elif functionName == "one":
            one()
        elif functionName == "two":
            two()
        elif functionName == "three":
            three()
        elif functionName == "four":
            four()
        elif functionName == "nextTab":
            nextTab()


        elif functionName == "searchYouTube":
            searchData = request.form.get("searchData")
            searchYouTube(searchData)
        elif functionName == "newTabYT":
            newTabYT()
        elif functionName == "escapeYT":
            escapeYT()
        elif functionName == "volUpYT":
            volUpYT()
        elif functionName == "startYT":
            startYT()
        elif functionName == "iButtonYT":
            iButtonYT()
        elif functionName == "fullScreenYT":
            fullScreenYT()
        elif functionName == "volDownYT":
            volDownYT()
        elif functionName == "saveMusicYT":
            saveMusicYT()


        elif functionName == "searchGoogleChrome":
            searchData = request.form.get("searchData")
            searchGoogleChrome(searchData)
        elif functionName == "newTabGC":
            newTabGC()
        elif functionName == "saveLinkGC":
            saveLinkGC()


        elif functionName == "searchFMovies":
            searchData = request.form.get("searchData")
            searchFMovies(searchData)
        elif functionName == "newTabFM":
            newTabFM()
        elif functionName == "click1FM":
            click1FM()
        elif functionName == "volUpFM":
            volUpFM()
        elif functionName == "startFM":
            startFM()
        elif functionName == "click2FM":
            click2FM()
        elif functionName == "fullScreenFM":
            fullScreenFM()
        elif functionName == "volDownFM":
            volDownFM()


        elif functionName == "searchNetflix":
            searchData = request.form.get("searchData")
            searchNetflix(searchData)
        elif functionName == "newTabN":
            newTabN()
        elif functionName == "volUpN":
            volUpN()
        elif functionName == "skipIntroN":
            skipIntroN()
        elif functionName == "fullScreenN":
            fullScreenN()
        elif functionName == "volDownN":
            volDownN()


        elif functionName == "searchPrime":
            searchData = request.form.get("searchData")
            searchPrime(searchData)
        elif functionName == "newTabAP":
            newTabAP()
        elif functionName == "volUpAP":
            volUpAP()
        elif functionName == "startAP":
            startAP()
        elif functionName == "fullScreenAP":
            fullScreenAP()
        elif functionName == "volDownAP":
            volDownAP()


        elif functionName == "scrollUpMain":
            scrollUpMain()
        elif functionName == "clickMain":
            clickMain()
        elif functionName == "moveUpMain":
            moveUpMain()
        elif functionName == "closeTabMain":
            closeTabMain()
        elif functionName == "refreshMain":
            refreshMain()
        elif functionName == "scrollDownMain":
            scrollDownMain()
        elif functionName == "moveleftMain":
            moveleftMain()
        elif functionName == "movedownMain":
            movedownMain()
        elif functionName == "moverightMain":
            moverightMain()
        elif functionName == "goBackMain":
            goBackMain()



        print(functionName)
    return render_template("index.html")


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0")