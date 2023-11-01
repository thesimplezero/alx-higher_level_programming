// jQuery script
$(document).ready(function() {

    // Select the div by ID
    const redHeaderDiv = $('DIV#red_header');

    // Add an event handler
    redHeaderDiv.click(function() {
        // Find the header
        const headerElement = $('header');

        // Check if header was found
        if (headerElement) {
            // Use css to set colour
            headerElement.css('color', '#FF0000');
        } else {
            console.error('Header elemnet not found');
        }
    });
});