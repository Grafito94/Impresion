function changeImg(){

    var changeImage = document.getElementById("img");


    if(changeImage.src === "http://127.0.0.1:5000/static/images/img1.jpeg"){
        changeImage.src = "static/images/img2.jpeg";
    }else{
        changeImage.src = "static/images/img1.jpeg";
    }
    console.log(changeImage.src);
}



