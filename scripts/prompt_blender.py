import gradio as gr
import modules

from modules import script_callbacks


def send_to_buttons_component(image_component, output_result_component):
    try:
        send_to_buttons = modules.generation_parameters_copypaste.create_buttons(
            ["txt2img", "img2img", "inpaint", "extras"])
        for tabname, button in send_to_buttons.items():
            print(tabname)
            params = ParamBinding(paste_button=button, tabname=tabname, source_text_component=output_result_component,
                                  source_image_component=image_component, source_tabname=f"{tabname}_source_tabname")
            modules.generation_parameters_copypaste.register_paste_params_button(
                params)
        return send_to_buttons
    except:
        pass


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Tab("Blend"):
            with gr.Row():
                with gr.Column():
                    # TODO: Output blend result for tags
                    output_result_component = gr.Textbox(
                        label="Prompt", interactive=False
                    )
                    hidden_image_component = gr.Image(
                        type="pil", elem_id="prompt_blender_hidden_image")
                    with gr.Row():
                        send_to_buttons_component(hidden_image_component,
                                                  output_result_component)
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
