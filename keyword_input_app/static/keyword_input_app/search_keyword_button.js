$(document).ready(function() {
    $('#keyword_button_id').on('click', function(event) {
        var input_text = $("#keyword_textfield_id").val();
        if (input_text.includes('/'))
        {
            alert("Please do not include slash(/) in your keyword.")
        }
        else
        {
            var url="/searched_photos/" + input_text;
            window.location.href = url;
        }
    });
});