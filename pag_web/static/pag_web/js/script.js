function register() {
    var name = document.getElementById('name').value;
    var university = document.getElementById('university').value;

    if (name && university) {
        alert('¡Gracias por registrarte, ' + name + ' de ' + university + '!');
    } else {
        alert('Por favor, completa todos los campos.');
    }
}
