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
                            <div class="section">
                            <div class="item">
                                <a href="/events/{{ event.id }}" style="width:200px">
                                <!--<a href="#eventmodal${ d.id }"  data-bs-toggle="modal" data-bs-target="#eventmodal${ d.id }" style="width:200px">-->
                                <img  src="${ d.poster_image }"  alt="...">
                                </a>
                            </div>
                    </div>`
                })
                $('#eventContainer').html(newHtml.join(''));
                $('#searchbox').val('');
            },
            error: function(xhr, status, error){
                console.error(error);
            }
        })
    });
});