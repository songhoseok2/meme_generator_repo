$(document).ready(function()
{
    $('#input_text_button_id').on('click', function(event)
    {
        var input_text = $('#text_textfield_id').val();
        var input_font_size = $('#font_size_textfield_id').val();
        var input_font_red = $('#font_red_textfield_id').val();
        var input_font_green = $('#font_green_textfield_id').val();
        var input_font_blue = $('#font_blue_textfield_id').val();
        var selected_URL = $('#url_textfield_id').val();

        if (input_text.includes('/'))
        {
            alert('Please do not include slash(/) in your text.');
        }
        else if(input_text === '' || selected_URL === '' || input_font_size === '' ||
            input_font_red === '' || input_font_green === '' || input_font_blue === '')
        {
            alert('Please fill out all fields.');
        }
        else if(isNaN(input_font_size) || isNaN(input_font_red) || isNaN(input_font_green) || isNaN(input_font_blue))
        {
            alert('Please enter numbers only for the font size and color values.');
        }
        else if(input_font_size.includes('-') || input_font_red.includes('-') || input_font_green.includes('-') || input_font_blue.includes('-'))
        {
            alert('Please enter positive numbers only for the font size and color values.');
        }
        else if(!(0 <= input_font_red && input_font_red <= 255) ||
                !(0 <= input_font_green && input_font_green <= 255) ||
                !(0 <= input_font_blue && input_font_blue <= 255))
        {
            alert('Please enter numbers from 0 to 255 (inclusive) for color values.')
        }

        else
        {
            selected_URL = selected_URL.replace('https://', '');
            selected_URL = selected_URL.replace('.staticflickr.com', '');
            input_text = input_text.replace('?', '%3F');
            input_text = input_text.replace('#', '%23');
            input_text = input_text.replace('\\', '%5C');
            var url='/final_result/' + input_text + '/' + input_font_size + '/' + input_font_red + '/' + input_font_green + '/' + input_font_blue + '/' + selected_URL;
            window.location.href = url;
        }
    });
});

