Opens a file (HTML) in the specified browser (Firefox) and changes the filename (C:\inetpub\wwwroot\...) to an URL (http://localhost/...)

## Installation
Put the files into a directory in your {sublime}\Data\Packages\ folder

## Usage
Consider editing a HTML file and you want to open that file in your webbrowser. Well, that's easy but you want to open the file as a URL. You have edited it in the folder of your webserver application (C:\inetpub\wwwroot\... for example) and it should open it as the URL http://localhost/....

This package does the right thing. All is done in the run_in_browser.py. To customize you can change the following:

- Change the replace path: url = url.replace('C:/inetpub/wwwroot', 'http://localhost'). In detail:
- Change the path to your webserver (here: C:\inetpub\wwwroot) to the path where your webpages are.
- Change the host (here: http://localhost) that replaces this part in the webbrowser.
- Change the call of your favorite webbrowser (here: "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe").
- Change the shortcut: The package defines a keyboard shortcut CTRL-F11 (like in Eclipse) to open the file in the webbrowser. You can change/remove the shortcut in the Default (Windows).sublime-keymap file in the package itself. I haven't set any keymaps for Linux or OSX.



## Link
https://github.com/AxxL/sublime-run-in-browser