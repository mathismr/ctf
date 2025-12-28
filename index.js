var pass = 'f067c12e26bfaabd97dcf23d95e5d054d7e65d8a0f6c9411222738f50168e42e'

var formpass = document.getElementById('passwd')

function encryptString(str) {
    var hash = CryptoJS.SHA256(str);
    var hashString = hash.toString(CryptoJS.enc.Hex);
  
    return hashString;
  }

function send() {
    if (encryptString(formpass) === pass) {
        alert("Access granted")
    }
}