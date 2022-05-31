$("#sendhome").change(function() {
    if ( $(this).is(':checked') ) {
        $("#addressform").show();
    } else {
        $("#addressform").hide();
    }
});