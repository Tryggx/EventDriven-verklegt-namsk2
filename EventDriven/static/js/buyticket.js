$("#sendhome").change(function() {
    if ( $(this).is(':checked') ) {
        $("#addressform").show();

        $("label[for='id_name']").css('display','inline-block');
        $("#id_name").css('display','inline-block');
        $("label[for='id_address']").css('display','inline-block');
        $("#id_address").css('display','inline-block');
        $("label[for='id_city']").css('display','inline-block');
        $("#id_city").css('display','inline-block');
        $("label[for='id_country']").css('display','inline-block');
        $("#id_country").css('display','inline-block');
        $("label[for='id_zip']").css('display','inline-block');
        $("#id_zip").css('display','inline-block');
        $("#id_name").attr('required', true);
        $("#id_address").attr('required',true);
        $("#id_city").attr('required',true);
        $("#id_country").attr('required',true);
        $("#id_zip").attr('required',true);
    } else {
        $("#addressform").hide()
        $("label[for='id_name']").css('display','none');
        $("#id_name").css('display','none');
        $("label[for='id_address']").css('display','none');
        $("#id_address").css('display','none');
        $("label[for='id_city']").css('display','none');
        $("#id_city").css('display','none');
        $("label[for='id_country']").css('display','none');
        $("#id_country").css('display','none');
        $("label[for='id_zip']").css('display','none');
        $("#id_zip").css('display','none');
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

