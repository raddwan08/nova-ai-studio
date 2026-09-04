import gradio as gr


def generate_script(title, idea, age, language, duration):

    return f"""
🌟 NOVA KIDS STORY

Title:
{title}

Age:
{age}

Language:
{language}

Duration:
{duration}


Story:

NOVA starts a new adventure.

Today children learn about:

{idea}

Through fun exploration,
NOVA teaches a positive lesson.

The End ✨
"""


demo = gr.Interface(
    fn=generate_script,
    inputs=[
        gr.Textbox(label="Video Title"),
        gr.Textbox(label="Video Idea"),
        gr.Textbox(label="Age Group"),
        gr.Textbox(label="Language"),
        gr.Textbox(label="Duration")
    ],
    outputs=gr.Textbox(
        label="Generated Script"
    ),
    title="🌟 NOVA AI STUDIO",
    description="Create safe educational kids stories"
)


demo.launch()
