class Translation(object):

    START_TEXT = """Hello මචං,

මම Telegram URL Upload Bot!

<b>මට ඕනි Direct download URL link එකක් එවන්න, මම ඒක File හෝ Video විදියට upload කරන්නම්</b>

උදවු සදහා /help ..

Film group - @film_with_review
"""

    HELP_USER = """මම URL Uploader bot..
    
1.  url එක එවන්න (Link | New Name with Extension).
2. Send Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots

Support Group : @film_with_review
"""

    FORMAT_SELECTION = """ඔයාට ඕනි format එක තෝරන්න: <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    DOWNLOAD_START = "Downloading 👿👿👿"
    
    UPLOAD_START = "Uploading now..👻👻👻"
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds. මාව hospital දාන්න අයියෝ."

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nමේ හුත්තො Telegram එකට upload කරන්න පුළුවන් උපරිම 1.96 GB "

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "මේකෙ මුකුත් නෑ හුත්තෝ \n<b>YouTubeDL</b> said: {}"
