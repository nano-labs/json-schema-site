// validador
function validate_json(textarea_id) {
    try {
        var conteudo = $(textarea_id).val();
        var valido = JSON.stringify(JSON.parse(conteudo), " ", 4);
        $(textarea_id).val(valido);
        return true;
    } catch (err) {
        validation_error(textarea_id);
        return false;
    }
}
function validation_error(textarea_id) {
    $("error_" + textarea_id).remove();
    var obj = $(textarea_id);
    obj.addClass("error");
    var overlay = $(".error_overlay_base").clone().removeClass("error_overlay_base");
    overlay.addClass("error_" + textarea_id);
    var y = obj.position().top;
    var x = obj.position().left;
    overlay.css("top", y + "px");
    overlay.css("left", x + "px");
    overlay.height(obj.height() + 4);
    overlay.width(obj.width() + 4);
    overlay.hide();
    $(".content").append(overlay);
    // obj.parent().append(overlay);
    overlay.fadeIn();
}
$(document).ready(function () {
    $('#check_json').click(function (event) {
        event.preventDefault();
        var a_ok = validate_json("#json_a");
        var b_ok = validate_json("#json_b");
        if (a_ok && b_ok) {
            $("#input_form").submit();
        }
        return false;
    });
})
$(document.body).on({
    click: function(e){
        e.preventDefault();
        $(this).parent().parent().remove();
        console.log("oi");
    }    
},'.error_message_buttom');