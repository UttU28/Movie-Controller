var randomImage = function() {

//     var fileNames = [
//        "image1.png",
//        "image2.jpg",
//        "image3.png",
//    ];
   
// var randomIndex = Math.Round(Math.random() * fileNames.length);

//Change myImage to the id of your image. (example: <img id = "myImage" src = "meme.png"></img>)
    document.getElementById("screenImage").src = "/static/Images/image.jpg"  //filesNames[randomIndex];
    console.log("HI")
};
   
randomImage();

setInterval(randomImage, 1000);