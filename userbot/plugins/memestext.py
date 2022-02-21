import random

from userbot import devub

from ..core.managers import edit_or_reply
from . import devmemes

plugin_devegory = "fun"


@devub.dev_cmd(
    pattern="congo$",
    command=("congo", plugin_devegory),
    info={
        "header": " Congratulate the people..",
        "usage": "{tr}congo",
    },
)
async def _(e):
    "Congratulate the people."
    txt = random.choice(devmemes.CONGOREACTS)
    await edit_or_reply(e, txt)


@devub.dev_cmd(
    pattern="shg$",
    command=("shg", plugin_devegory),
    info={
        "header": "Shrug at it !!",
        "usage": "{tr}shg",
    },
)
async def shrugger(e):
    "Shrug at it !!"
    txt = random.choice(devmemes.SHGS)
    await edit_or_reply(e, txt)


@devub.dev_cmd(
    pattern="runs$",
    command=("runs", plugin_devegory),
    info={
        "header": "Run, run, RUNNN!.",
        "usage": "{tr}runs",
    },
)
async def runner_lol(e):
    "Run, run, RUNNN!"
    txt = random.choice(devmemes.RUNSREACTS)
    await edit_or_reply(e, txt)


@devub.dev_cmd(
    pattern="noob$",
    command=("noob", plugin_devegory),
    info={
        "header": "Whadya want to know? Are you a NOOB?",
        "usage": "{tr}noob",
    },
)
async def metoo(e):
    "Whadya want to know? Are you a NOOB?"
    txt = random.choice(devmemes.NOOBSTR)
    await edit_or_reply(e, txt)


@devub.dev_cmd(
    pattern="insult$",
    command=("insult", plugin_devegory),
    info={
        "header": "insult someone.",
        "usage": "{tr}insult",
    },
)
async def insult(e):
    "insult someone."
    txt = random.choice(devmemes.INSULT_STRINGS)
    await edit_or_reply(e, txt)


@devub.dev_cmd(
    pattern="hey$",
    command=("hey", plugin_devegory),
    info={
        "header": "start a conversation with people",
        "usage": "{tr}hey",
    },
)
async def hoi(e):
    "start a conversation with people."
    txt = random.choice(devmemes.HELLOSTR)
    await edit_or_reply(e, txt)


@devub.dev_cmd(
    pattern="pro$",
    command=("pro", plugin_devegory),
    info={
        "header": "If you think you're pro, try this.",
        "usage": "{tr}pro",
    },
)
async def proo(e):
    "If you think you're pro, try this."
    txt = random.choice(devmemes.PRO_STRINGS)
    await edit_or_reply(e, txt)


@devub.dev_cmd(
    pattern="react ?([\s\S]*)",
    command=("react", plugin_devegory),
    info={
        "header": "Make your userbot react",
        "types": [
            "happy",
            "think",
            "wave",
            "wtf",
            "love",
            "confused",
            "dead",
            "sad",
            "dog",
        ],
        "usage": ["{tr}react <type>", "{tr}react"],
    },
)
async def _(e):
    "Make your userbot react."
    input_str = e.pattern_match.group(1)
    if input_str in "happy":
        emoticons = devmemes.FACEREACTS[0]
    elif input_str in "think":
        emoticons = devmemes.FACEREACTS[1]
    elif input_str in "wave":
        emoticons = devmemes.FACEREACTS[2]
    elif input_str in "wtf":
        emoticons = devmemes.FACEREACTS[3]
    elif input_str in "love":
        emoticons = devmemes.FACEREACTS[4]
    elif input_str in "confused":
        emoticons = devmemes.FACEREACTS[5]
    elif input_str in "dead":
        emoticons = devmemes.FACEREACTS[6]
    elif input_str in "sad":
        emoticons = devmemes.FACEREACTS[7]
    elif input_str in "dog":
        emoticons = devmemes.FACEREACTS[8]
    else:
        emoticons = devmemes.FACEREACTS[9]
    txt = random.choice(emoticons)
    await edit_or_reply(e, txt)


@devub.dev_cmd(
    pattern="10iq$",
    command=("10iq", plugin_devegory),
    info={
        "header": "You retard !!",
        "usage": "{tr}10iq",
    },
)
async def iqless(e):
    "You retard !!"
    await edit_or_reply(e, "♿")


@devub.dev_cmd(
    pattern="fp$",
    command=("fp", plugin_devegory),
    info={
        "header": "send you face pam emoji!",
        "usage": "{tr}fp",
    },
)
async def facepalm(e):
    "send you face pam emoji!"
    await edit_or_reply(e, "🤦‍♂")


@devub.dev_cmd(
    pattern="bt$",
    command=("bt", plugin_devegory),
    info={
        "header": "Believe me, you will find this useful.",
        "usage": "{tr}bt",
    },
    groups_only=True,
)
async def bluetext(e):
    """Believe me, you will find this useful."""
    await edit_or_reply(
        e,
        "/BLUETEXT /MUST /CLICK.\n"
        "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?",
    )


@devub.dev_cmd(
    pattern="session$",
    command=("session", plugin_devegory),
    info={
        "header": "telethon session error code(fun)",
        "usage": "{tr}session",
    },
)
async def _(event):
    "telethon session error code(fun)."
    mentions = "**telethon.errors.rpcerrorlist.AuthKeyDuplidevedError: The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions (caused by GetMessagesRequest)**"
    await edit_or_reply(event, mentions)
