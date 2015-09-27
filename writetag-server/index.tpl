<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title></title>
        <meta name="description" content="">

        <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/jstree/3.0.9/themes/default/style.min.css" />
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
        
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/jstree/3.0.9/jstree.min.js"></script>
    </head>
    <body>
        <form method="POST" action="/" class="pure-form pure-form-aligned">
            <fieldset>
                <div class="pure-control-group">
                    <label for="source">Source:</label>
                    <select name="source">
                        % for source in sources:
                            <option value="option">{{source}}</option>
                        % end
                    </select>
                </div>
                <div class="pure-control-group">
                    <label for="source">Select file or folder:</label>
                    <div id="url_select_tree"></div>
                    <script>
                        $(function() {
                            $('#url_select_tree').jstree({
                                "core": {
                                    "data": [{{!tree}}]
                                },
                                "types" : {
                                    "folder" : {
                                      "icon" : "fa fa-folder"
                                    },
                                    "file" : {
                                      "icon" : "fa fa-file-audio-o"
                                    }
                                  },
                                  "plugins" : ["types", "sort"]
                            });
                        });
                    </script>
                </div>
            </fieldset>
        </form>
    </body>
</html>
