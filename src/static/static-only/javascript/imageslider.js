var myImage = document.getElementById("image");
var arrayImage = images;
var imageIndex = 0;

function chnageImage(){
  myImage.setAttribute("src", arrayImage[imageIndex]);
  imageIndex++;

  if(imageIndex >= arrayImage.length){
      imageIndex = 0;
  }


}

setInterval(changeImage, 3000);
