import gradio as gr

from modules import script_callbacks

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            gr.Markdown(
                """
                # Hello World!
                Start typing below to see the output.
                """
            )
        return [(ui_component, "Prompt Blender", "prompt_blender")]

script_callbacks.on_ui_tabs(on_ui_tabs)