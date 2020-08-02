// var video = document.querySelector('#videoElement');

// if(navigator.mediaDevices.getUserMedia) {
//     navigator.mediaDevices.getUserMedia({video:true})
//     .then(function (stream) {
//         video.srcObject = stream;
//     })
//     .catch(function(error){
//         console.log("Something went wrong!")
//     })
// }

const container = document.getElementById('video-container');
const button = document.getElementById('get-video');
var form = document.getElementById("myForm");

function handleForm(event) { 
    event.preventDefault(); 
}

//You can then call the function with something like what i have below.

form.addEventListener('submit', handleForm);

function doSomething() {
    $("p").remove(".name");
    const name = document.createElement("p");
    name.classList.add("name")
    name.append(document.createTextNode(document.getElementById('content').value));
    container.append(name);
    return false;
}

button.addEventListener('click', () => {
  Twilio.Video.createLocalVideoTrack().then(track => {
    container.append(track.attach());
    button.remove();
  });
})