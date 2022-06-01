$(document).ready(function(){
    $('#searchbtn').on('click', function (e){
        e.preventDefault();
        var searchtext = $('#searchbox').val();
        $.ajax({
            url: '/events?search=' + searchtext,
            type: 'GET',
            success: function(resp){
                var newHtml = resp.data.map(d => {
                    return `
                            <div class="item">
                                <a href="/events/${ d.id }" style="width:200px">
                                <!--<a href="#eventmodal${ d.id }"  data-bs-toggle="modal" data-bs-target="#eventmodal${ d.id }" style="width:200px">-->
                                <img  src="${ d.poster_image }"  alt="...">
                                </a>
                            </div>
                    `
                })
                let returnHtml = `<div class="wrapper" style="height: 90vh;"><div id="searchsection">` + newHtml.join('') + `</div> </div>`
                $('#eventContainer').html(returnHtml);
                $('#searchbox').val('');
            },
            error: function(xhr, status, error){
                console.error(error);
            }
        })
    });
    $('#searchbox').keypress(
        function(event){
            if (event.which == '13') {
                event.preventDefault();
                $('#searchbtn').click();
            }
        });

});