function select_article() {
    // get article id from selected dropdown option
    var article_id = document.getElementById("article-selection").value;

    // if id is "new", clear the form
    if (article_id == "new") {
        document.getElementById("id").value = "new";
        document.getElementById("title").value = "";
        document.getElementById("content").value = "";
        document.getElementById("content-preview").innerHTML = "";
        return;
    }
    // else send a GET request to the server using an AJAX call
    $.ajax({
        url: "/article-editor/get?id=" + article_id,
        method: "GET",
        success: function(response) {
            // fill the form with the article data
            document.getElementById("id").value = article_id;
            document.getElementById("title").value = response.title;
            document.getElementById("content").value = response.content;
            if (response.premium) {
                document.getElementById("premium").checked = true;
            } else {
                document.getElementById("premium").checked = false;
            }
            preview_markdown();
        },
        // receive error message from flask server
        error: function(response) {
            // reload the page to show the flash message
            location.reload();
        }
    });
}

function delete_article() {
    // get article id from selected dropdown option
    var article_id = document.getElementById("article-selection").value;
    console.log(article_id);
    // send a DELETE request to the server using an AJAX call
    $.ajax({
        url: "/article-editor/delete?id=" + article_id,
        method: "DELETE",
        success: function() {
            // clear the form
            document.getElementById("id").value = "new";
            document.getElementById("title").value = "";
            document.getElementById("content").value = "";
            document.getElementById("content-preview").innerHTML = "";
            // reload the page to show the flash message
            location.reload();
        },
        // receive error message from flask server
        error: function(response) {
            // reload the page to show the flash message
            location.reload();
        }
    });
}

// ---------------------------------------------------------
// ATTENTION: Showdown is required for the markdown preview!

// insert markdown at the cursor position in the textarea
function insert_markdown(markdown) {
    // get the text from the textarea
    var text = document.getElementById("content").value;
    // get the cursor position
    var cursor = document.getElementById("content").selectionStart;
    // get the text before and after the cursor
    var text_before = text.substring(0, cursor);
    var text_after = text.substring(cursor);
    // insert the markdown
    var new_text = text_before + markdown + text_after;
    // set the new text
    document.getElementById("content").value = new_text;
    // set the cursor position after the markdown
    document.getElementById("content").selectionStart = cursor + markdown.length;
    document.getElementById("content").selectionEnd = cursor + markdown.length;
    // focus the textarea
    document.getElementById("content").focus();
    // show the preview
    preview_markdown();
}

// add event listener to the textarea
document.getElementById("content").addEventListener("input", preview_markdown);

// convert markdown to HTML and show the preview
function preview_markdown() {
    // get the text from the textarea
    var text = document.getElementById("content").value;
    // get the preview element
    var preview = document.getElementById("content-preview");
    // convert the markdown to HTML
    var converter = new showdown.Converter();
    var html = converter.makeHtml(text);
    // set the preview HTML
    preview.innerHTML = html;
}

// caller functions for the markdown buttons

function markdown_h1() {
    insert_markdown("# ");
}

function markdown_h2() {
    insert_markdown("## ");
}

function markdown_h3() {
    insert_markdown("### ");
}

function markdown_h4() {
    insert_markdown("#### ");
}

function markdown_bold() {
    insert_markdown("**");
}

function markdown_italic() {
    insert_markdown("*");
}

function markdown_bold_italic() {
    insert_markdown("***");
}

function markdown_unordered_list() {
    insert_markdown("- ");
}

function markdown_ordered_list() {
    insert_markdown("1. ");
}

function markdown_link() {
    insert_markdown("[link text](https://)");
}

function markdown_image() {
    insert_markdown("![image alternative text](https://)");
}

function markdown_blockquote() {
    insert_markdown("> ");
}

function markdown_code() {
    insert_markdown("`code`");
}

function markdown_horizontal_line() {
    insert_markdown("\n---\n");
}

function markdown_escape() {
    insert_markdown("\\");
}