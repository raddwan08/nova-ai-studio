def generate_script(
    title,
    idea,
    age,
    language,
    duration
):

    script = f"""
TITLE:
{title}


AGE:
{age}


LANGUAGE:
{language}


DURATION:
{duration}


STORY:

NOVA begins a new adventure.

The children learn about:
{idea}

NOVA explores, discovers,
and shares a fun lesson.

End.
"""

    return script
