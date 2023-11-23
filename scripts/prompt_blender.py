import gradio as gr

from modules import script_callbacks


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Tab("Blend"):
            with gr.Row():
                with gr.Column():
                    # TODO: Output blend result for tags
                    output_result_component = gr.Textbox(
                        label="Prompt", interactive=False
                    )
                with gr.Column():
                    # TODO: Input tags
                    gr.Markdown(
                        """
                        # Hello World!
                        Start typing below to see the output.
                        """
                    )
        with gr.Tab("Management"):
            with gr.Row():
                # TODO: Edit and Serch tags
                gr.Markdown(
                    """
                        # Hello World!
                        Start typing below to see the output.
                        """
                )
        return [(ui_component, "Prompt Blender", "prompt_blender")]


script_callbacks.on_ui_tabs(on_ui_tabs)
