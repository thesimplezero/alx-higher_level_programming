// jQuery script
$(document).ready(function() {

    const redHeaderDiv = $('DIV#red_header');

    redHeaderDiv.click(function() {
        // Find the header
        const headerElement = $('header');

        // Check if header was found
        if (headerElement) {
            // Use addClass method
            headerElement.addClass('red');
        } else {
            console.error('Header elemnet not found');
        }
    });
});
