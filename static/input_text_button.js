$(document).ready(function() {
    $('#input_text_button_id').on('click', function(event) {
        var input_text = $("#text_textfield_id").val();
        var selected_URL = $("#url_textfield_id").val();
        if (input_text.includes('/'))
        {
            alert("Please do not include slash(/) in your text.");
        }
        else if(input_text === '')
        {
            alert("Please enter a keyword.");
        }
        else if(selected_URL === '')
        {
            alert("Please copy a URL.");
        }
        else
        {
            selected_URL = selected_URL.replace("https://", "");
            selected_URL = selected_URL.replace(".staticflickr.com", "");
            var url="/final_result/" + input_text + '/' + selected_URL;
            window.location.href = url;
        }
    });
});

