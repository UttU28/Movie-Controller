import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# from notify_run import Notify
# notify = Notify(endpoint="https://notify.run/R3EV6hx0dLPXxiDF73KD")
# notify.send("Click to control videos!", "http://{}:5000/".format(IPAddr))
import json
from flask import Flask, render_template, request
from defaultFunctions.topFunctions import volumeIncrease,previousTrack,backSeek,pause,forwardSeek,nextTrack,volumeDecrease
from defaultFunctions.homeFunctions import escape,desktop,fullScreen,one,two,three,prevTab,nextTab
from siteFunctions.youTubeFunctions import searchYouTube,newTabYT,escapeYT,volUpYT,startYT,iButtonYT,fullScreenYT,volDownYT,saveMusicYT
from siteFunctions.googleChromeFunctions import searchGoogleChrome,newTabGC,saveLinkGC
from siteFunctions.fMoviesFunctions import searchFMovies,newTabFM,click1FM,volUpFM,startFM,click2FM,fullScreenFM,volDownFM
from siteFunctions.iBommaFunctions import searchIBomma,newTabIB,click1IB,volUpIB,startIB,click2IB,fullScreenIB,volDownIB
from siteFunctions.primeVideosFunctions import searchPrime,newTabAP,volUpAP,startAP,fullScreenAP,volDownAP
from siteFunctions.netflixFunctions import searchNetflix,newTabN,volUpN,skipIntroN,volDownN,fullScreenN
from defaultFunctions.bottomFunctions import scrollUpMain,clickMain,moveUpMain,closeTabMain,refreshMain,scrollDownMain,moveleftMain,movedownMain,moverightMain,moveBackMain
from defaultFunctions.controller import clickMainController,moveupMainController,moveleftMainController,movedownMainController,moverightMainController


with open("controllerFormat.json", "r") as contFile: controllerFormat = json.load(contFile)
with open("controllerData.json", "r") as contFile: controllerData = json.load(contFile)

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        functionName = request.form.get("functionName")
        searchData = request.form.get("searchData")
        
        functionMapping = {"volumeIncrease": volumeIncrease,"previousTrack": previousTrack,"backSeek": backSeek,"pause": pause,"forwardSeek": forwardSeek,"nextTrack": nextTrack,"volumeDecrease": volumeDecrease,"escape": escape,"desktop": desktop,"fullScreen": fullScreen,"prevTab": prevTab,"one": one,"two": two,"three": three,"nextTab": nextTab,"searchYouTube": lambda: searchYouTube(searchData),"newTabYT": newTabYT,"escapeYT": escapeYT,"volUpYT": volUpYT,"startYT": startYT,"iButtonYT": iButtonYT,"fullScreenYT": fullScreenYT,"volDownYT": volDownYT,"saveMusicYT": saveMusicYT,"searchGoogleChrome": lambda: searchGoogleChrome(searchData),"newTabGC": newTabGC,"saveLinkGC": saveLinkGC,"searchFMovies": lambda: searchFMovies(searchData),"newTabFM": newTabFM,"click1FM": click1FM,"volUpFM": volUpFM,"startFM": startFM,"click2FM": click2FM,"fullScreenFM": fullScreenFM,"volDownFM": volDownFM,"searchIBomma": lambda: searchIBomma(searchData),"newTabIB": newTabIB,"click1IB": click1IB,"volUpIB": volUpIB,"startIB": startIB,"click2IB": click2IB,"fullScreenIB": fullScreenIB,"volDownIB": volDownIB,"searchNetflix": lambda: searchNetflix(searchData),"newTabN": newTabN,"volUpN": volUpN,"skipIntroN": skipIntroN,"fullScreenN": fullScreenN,"volDownN": volDownN,"searchPrime": lambda: searchPrime(searchData),"newTabAP": newTabAP,"volUpAP": volUpAP,"startAP": startAP,"fullScreenAP": fullScreenAP,"volDownAP": volDownAP,"scrollUpMain": scrollUpMain,"clickMain": clickMain,"moveUpMain": moveUpMain,"closeTabMain": closeTabMain,"refreshMain": refreshMain,"scrollDownMain": scrollDownMain,"moveleftMain": moveleftMain,"movedownMain": movedownMain,"moverightMain": moverightMain,"moveBackMain": moveBackMain,"clickMainController": clickMainController,"moveupMainController": moveupMainController,"moveleftMainController": moveleftMainController,"movedownMainController": movedownMainController,"moverightMainController": moverightMainController}
        if functionName in functionMapping:
            functionMapping[functionName]()

        print(functionName)
    return render_template("index.html", controllerFormat=controllerFormat, controllerData=controllerData)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0")