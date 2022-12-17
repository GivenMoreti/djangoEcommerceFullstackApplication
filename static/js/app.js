const upButton =document.getElementById('up');
upButton.addEventListener('click', function(){
    window.scrollTo({
        top:0,
        left:0,
        behavior:"smooth"
    })
})
