function delete_account() {
    // send a POST request (keeps password private) to the server using an AJAX call
    $.ajax({
        url: "/account/delete",
        method: "POST",
        data: {
            password: document.getElementById("password-confirm").value
        },
        success: function(data) {
            // redirect to the home page
            window.location.href = "/";
        },
        error: function(data) {
            // reload the page to show the flash message
            location.reload();
        }
    });
}