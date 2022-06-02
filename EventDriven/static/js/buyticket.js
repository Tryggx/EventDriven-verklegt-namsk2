$("#sendhome").change(function() {
    if ( $(this).is(':checked') ) {
        $("#addressform").show();

        $("label[for='id_name']").show();
        $("#id_name").show();
        $("label[for='id_address']").show();
        $("#id_address").show();
        $("label[for='id_city']").show();
        $("#id_city").show();
        $("label[for='id_country']").show();
        $("#id_country").show();
        $("label[for='id_zip']").show();
        $("#id_zip").show();
        $("#id_name").attr('required', true);
        $("#id_address").attr('required',true);
        $("#id_city").attr('required',true);
        $("#id_country").attr('required',true);
        $("#id_zip").attr('required',true);
    } else {
        $("#addressform").hide()
        $("label[for='id_name']").hide();
        $("#id_name").hide();
        $("label[for='id_address']").hide();
        $("#id_address").hide();
        $("label[for='id_city']").hide();
        $("#id_city").hide();
        $("label[for='id_country']").hide();
        $("#id_country").hide();
        $("label[for='id_zip']").hide();
        $("#id_zip").hide();
        $("#id_name").removeAttr('required');
        $("#id_address").removeAttr('required');
        $("#id_city").removeAttr('required');
        $("#id_country").removeAttr('required');
        $("#id_zip").removeAttr('required');
    }
});


$("#btnadd").on('click', function (e){
    e.preventDefault();
    var amount = parseInt($("#ticketnum").text())
})


$('.btn-number').click(function(e){
    e.preventDefault();
    fieldName = $(this).attr('data-field');
    type      = $(this).attr('data-type');
    var input = $(".input-number");
    var currentVal = parseInt(input.val());
    if (!isNaN(currentVal)) {

        if(type == 'minus') {
            $(".btn-number[data-type='plus']").removeAttr('disabled')

            if (currentVal > input.attr('min')) {
                input.val(currentVal - 1).change();
            }
            if (parseInt(input.val()) == input.attr('min')) {
                $(this).attr('disabled', true);
            }

            } else if (type == 'plus') {
            $(".btn-number[data-type='minus']").removeAttr('disabled')

            if (currentVal < input.attr('max')) {
                input.val(currentVal + 1).change();
            }
            if (parseInt(input.val()) == input.attr('max')) {
                $(this).attr('disabled', true);
            }
        }
    } else {
        input.val(0);
    }
});

$('.input-number').change(function() {

    minValue =  parseInt($(this).attr('min'));
    maxValue =  parseInt($(this).attr('max'));
    valueCurrent = parseInt($(this).val());

    $('#num_tickets').val(valueCurrent);
    $('#price').text(valueCurrent*singleTicketPrice);
    $('#total_price').val(valueCurrent*singleTicketPrice);
    name = $(this).attr('name');
    if(valueCurrent >= minValue) {
        $(".btn-number[data-type='minus'][data-field='"+name+"']").removeAttr('disabled')
    } else {
        //alert('Sorry, the minimum value was reached');
        $(this).val('1');
        $(".btn-number[data-type='plus']").removeAttr('disabled')
        $(".btn-number[data-type='minus']").attr('disabled', true);
    }
    if(valueCurrent <= maxValue) {
        $(".btn-number[data-type='plus'][data-field='"+name+"']").removeAttr('disabled')
    } else {
        //alert('Sorry, the maximum value was reached');
        $(this).val('10');
        $(".btn-number[data-type='minus']").removeAttr('disabled')
        $(".btn-number[data-type='plus']").attr('disabled', true);
    }


});
$(".input-number").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
             // Allow: Ctrl+A
            (e.keyCode == 65 && e.ctrlKey === true) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });

$("#id_cardnumber").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
             // Allow: Ctrl+A
            (e.keyCode == 65 && e.ctrlKey === true) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }

        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
});

$("#exp").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
             // Allow: Ctrl+A
            (e.keyCode == 65 && e.ctrlKey === true) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        if( $('#exp').val().length == 2 ) {
            $('#exp').val( $('#exp').val() +"/");
        }
        // Ensure that it is a number and stop the keypress
        if (((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105))) {
            e.preventDefault();
        }
});

$("#id_cvc").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
             // Allow: Ctrl+A
            (e.keyCode == 65 && e.ctrlKey === true) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if (((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) || document.getElementById('id_cvc').value.length >= 4) {
            e.preventDefault();
        }
});

