# DriveDirect in Python (GUI)
Get a Direct Download Link to a Google Drive file through Python

### Get the command line version [here](https://github.com/ThisIsNoahEvans/DriveDirect-CMD)

## How It Works
Once launched, the program requests a Google Drive sharing link. This can be found through the Link Sharing feature of Google Drive. It doesn't work with Google Docs files - only actual files with a visible file extension in Google Drive. (for example: .png files, .pdf documents, or .mp4 videos)

The program then adjusts the URL to the direct download format - like when you click the Download button in Google Drive - and will print that URL to the screen. It'll also copy the URL to your clipboard, replacing what was there before (which was probably the original non-direct URL).

The GUI version of this tool runs using Tkinter.

*Note: I adapted the Tkinter code from [here](https://datatofish.com/entry-box-tkinter) so the code may not be 100% efficient as it could be.*

## Enjoy!
If you have any issues, post an issue here on GitHub or [email me.](mailto:programming@itsnoahevans.co.uk)
