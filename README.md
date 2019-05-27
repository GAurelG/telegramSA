# TelegramSA

I am trying to build a Sentiment analysis pipeline to analyse data from a telegram chat and estimate my mood over the different days.
I will use the export function provided in the Telegram client, it outputs html files.
Two other method that could work to get the data and might provide another format:

    - using a telagram terminal client
    - creating a telegramBot:
        + good = could have real time analysis
        + bof = would need to have the bot in the chat = could get privacy questions depending on my skills of processing things securely.

## Pre-processing the chat data

[] parsing the html files to extract username, date, time
[] store the data (probably in some kind of database, could play with timeserie database to learn, even if it seems overscaled for such a small amount of data

Some things that might be problematic:
    - handle voice message
    - handle handle pictures or video (if it is in the actual extract)
    - maybe detect the language of the message as they can vary (and how to handle mix of languages in one message (could split per sentence but need to detect that case)
    - handle emoji (might actually be ok, more problematic for the sentiment analysis

## Sentiment scoring

I plan on using BERT from google as a base. I need more reading to be specific on the final training of the model, and how to set the data processing for multiple languages, for the handling of emojis and how to store the info back

## Sentiment analysis

I could use the data to see sentiment over the day, over the months, compare sentiment of the different participants (could do correlation).
Could try prediction of the mood considering the last X periode of time mood.
If I can get info from emojis, could look to see if the message sentiment is correlating with the use of emojis or not, or if there is a difference in frequency of emoji considering the mood.
One interresting feature could be to have the number of message considering the mood in a given period of time. the difficulty with that, is that in the example chat, we would be chatting during work hours, and depending on workload, there would be or not more activity;
