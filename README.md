# FM Player Rater

A way of quickly and objectively rating players in Football Manager based upon
attribute testing performed by
[FM-Arena](https://fm-arena.com/table/18-attribute-testing/). These results
were used to create weightings for each attribute such that a weighted total
rating based on players' attributes could be calculated if exported from
Football Manager.

## How to Use

Use of the FM Player Rater requires that the "Disable Player Attribute Masking"
option was selected on starting your game save.

In addition, FM Player Rater functionality requires export of the following data
by creating a custom player search view containing the following columns:
- Player Name
- ALL Technical attributes
- ALL Mental attributes
- ALL Physical attributes

Once the custom player search view is set up, you can export player data from
within Football Manager by:
- Clicking on the "FM" icon to the top-right of the UI
- Pressing the "Print Screen" button
- Selecting the "Web Page" option, and saving the HTML file to a known location
- Opening the HTML file within Excel, and saving the file in "CSV UTF-8" format
- Moving the new CSV file to the same folder as the Player Rater
