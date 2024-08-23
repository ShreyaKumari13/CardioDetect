// Initialize Firebase
var config = {
        apiKey: "AIzaSyDnmQFMztgoIYwuOLoOWUIIb8zpKZxs2eM",
        authDomain: "contactform-c6a0c.firebaseapp.com",
        databaseURL: "https://contactform-c6a0c-default-rtdb.firebaseio.com",
        projectId: "contactform-c6a0c",
        storageBucket: "contactform-c6a0c.appspot.com",
        messagingSenderId: "644611779374",
        appId: "1:644611779374:web:b6e6b1210497ca8ef3e8bf"
    
    
};
firebase.initializeApp(config);

//Reference messages collection
let messagesRef = firebase.database().ref('messages');

//listen to form
document.getElementById('contactForm').addEventListener('submit', submitForm);

function submitForm(e){
    e.preventDefault();

    // get Values
    let first_name = getInputVal('name');
    let last_name= getInputVal('company');
    let email = getInputVal('email');
    let phone = getInputVal('phone');
    let message = getInputVal('message');

    //save message

    saveMessage(first_name, last_name, email, phone, message);

    //show alert
    document.querySelector('.alert').style.display='block';

    //Hide alert after 3 s
    setTimeout(function(){
        document.querySelector('.alert').style.display='none';
    }, 3000)
    //clear form
    document.getElementById('contactForm').reset();
}
//function to get form values

function getInputVal(id){
    return document.getElementById(id).value;
}

//save message to firebase
function saveMessage(first_name, last_name, email, phone, message){
    let newMessageRef = messagesRef.push();
    newMessageRef.set({
       first_name: first_name,
        last_name: last_name,
        email: email,
        phone: phone,
        message: message
    })
}
// JavaScript for canvas animation
var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var particles = [];

function createParticle() {
  var particle = {
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    radius: Math.random() * 2 + 1,
    color: 'white',
    // Decreased speed values to make movement slower
    speedX: (Math.random() - 0.5) * 0.5,
    speedY: (Math.random() - 0.5) * 0.5
  };
  particles.push(particle);
}

function update() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (var i = 0; i < particles.length; i++) {
    var p = particles[i];
    p.x += p.speedX;
    p.y += p.speedY;

    if (p.x < 0 || p.x > canvas.width || p.y < 0 || p.y > canvas.height) {
      p.x = Math.random() * canvas.width;
      p.y = Math.random() * canvas.height;
    }

    ctx.beginPath();
    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
    ctx.fillStyle = p.color;
    ctx.fill();
  }

  requestAnimationFrame(update);
}

for (var i = 0; i < 100; i++) {
  createParticle();
}

update();