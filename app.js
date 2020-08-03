const container = document.getElementById('video-container');
const button = document.getElementById('get-video');
var form = document.getElementById("myForm");

function handleForm(event) { 
    event.preventDefault(); 
}

form.addEventListener('submit', handleForm);

function textOverlay() {
    $("p").remove(".name");
    const name = document.createElement("p");
    name.classList.add("name")
    name.append(document.createTextNode(document.getElementById('content').value));
    container.append(name);

    // Clear out textarea after submitting
    $('#content').val('');

    return false;
}

button.addEventListener('click', () => {
  Twilio.Video.createLocalVideoTrack().then(track => {
    container.append(track.attach());
    button.remove();
    document.getElementById("inputSec").style.display = 'block';
  });
})