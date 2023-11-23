import gradio as gr
import modules
import textwrap

from modules import script_callbacks


def send_to_buttons_component(image_component, output_result_component):
    try:
        send_to_buttons = modules.generation_parameters_copypaste.create_buttons(
            ["txt2img", "img2img", "inpaint", "extras"])
        modules.generation_parameters_copypaste.bind_buttons(
            send_to_buttons, image_component, output_result_component)
        return send_to_buttons
    except:
        pass


def build_prompt():
    tmp_value = """
        (best quality, masterpiece:1.2), ultra detailed
        , BREAK
        , silver hair, emerald eyes, beautiful elf
        """
    return textwrap.dedent(tmp_value)[1:-1]


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Tab("Blend"):
            with gr.Row():
                with gr.Column():
                    output_component = gr.Textbox(
                        label="output", interactive=False
                    )
                    btn = gr.Button("Generate")
                    btn.click(None, [], output_component,
                              _js="(x) => x + 'foo'")
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
