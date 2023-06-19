function sendEmail() {
    console.log(document.getElementById('assunto'))
    window.Email.send({
        Host : "smtp.elasticemail.com",
        Username : "iago.portfolio7@gmail.com",
        Password : "DBBDF11CEAFA77A78E9D79F20AE3E545BB0B",
        To : "iago.portfolio@outlook.com",
        From : "iago.portfolio7@gmail.com",
        Subject : `${ document.getElementById('assunto').value} - ${document.getElementById('email').value}`,
        Body : document.getElementById('mensagem').value,
        Port: '2525'
    }).then(
      message => alert(message)
    );
}