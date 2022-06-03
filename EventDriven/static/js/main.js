$(document).ready(function(){
    $('#searchbtn').on('click', function (e){
        e.preventDefault();
        var searchtext = $('#searchbox').val();
        window.location = '/events?search=' + searchtext
    });
    $('#searchbox').keypress(
        function(event){
            if (event.which == '13') {
                event.preventDefault();
                $('#searchbtn').click();
            }
        });

});