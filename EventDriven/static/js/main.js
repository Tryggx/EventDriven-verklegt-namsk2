$(document).ready(function(){
    $('#testbtn').on('click', function (e){
        e.preventDefault();
        $.ajax({
            url: '/events/eventjson/1',
            type: 'GET',
            sucess: function(resp){
                var newHtml = resp.data.map(d =>{
                    return `<div>
                            <p></p>
                            </div>`
                })
            },
            error: function(xhr, status, error){
                console.error(error)
            }
        })
    });
});