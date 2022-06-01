$("#sendhome").change(function() {
    if ( $(this).is(':checked') ) {
        $("#addressform").show();
    } else {
        $("#addressform").hide();
    }
});

$("#btnadd").on('click', function (e){
    e.preventDefault();
    var amount = parseInt($("#ticketnum").text())
})