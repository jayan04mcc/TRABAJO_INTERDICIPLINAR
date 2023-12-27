document.getElementById('toggleButton').addEventListener('click', function() {
    let infoDiv = document.getElementById('info');
    if (infoDiv.style.display === 'none') {
        infoDiv.style.display = 'block';
    } else {
        infoDiv.style.display = 'none';
    }
});
