$(document).ready(function(){
    $('#searchbtn').on('click', function (e){
        e.preventDefault();
        var searchtext = $('#searchbox').val();
        $.ajax({
            url: '/events?search=' + searchtext,
            type: 'GET',
            sucess: function(resp){
                var newHtml = resp.data.map(d =>{
                    return `<div>
                            <p></p>
                            </div>`
                })
            },
            error: function(xhr, status, error){
                console.error(error);
            }
        })
    });
});