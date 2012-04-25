This program is not to be resold for profit without the express written permission of the author.

This is a script I wrote for identifying translation memory segments that have multiple translations.  
i.e. if "My name is John" is translated in more than one way.

How to use:
1.) You must have Python 2.7 installed
2.) Run the command "python TM_script.py {filename to check}" (no quotes)
	Example is python TM_script.py client.tmx
3.) The file log.txt will have all of the segments that have more than one translation.

This is a script I wrote for identifying translation memory segments that have multiple translations.  
i.e. if "My name is John" is translated in more than one way.

DISCLAIMERS:
1.) This only works for TMX files and has only been tested against exports for XTM.
2.) This only currently works if en-US (English - United States) is the source language
3.) I will not be held responsible for any problems that arise regarding your TM files.  Use at your own risk.

Bill Blanchard
bill.blanchard@gmail.com
