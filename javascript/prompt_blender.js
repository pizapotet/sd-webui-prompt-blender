//@ts-check

/**
 * @param {string | undefined} [str]
 * @returns {string}
 */
function onClickGenerate(str) {
    const inputs = getTagInputs()

    // 空の文字列を除いて連結する
    return inputs.filter(str => str.trim() !== "").join(", ");
}

/**
 * @returns {Array<string>}
 */
function getTagInputs() {
    const container = document.getElementById("prompt_blender_input_container");
    const textareaCollection = container?.querySelectorAll('[id^="prompt_blender_input_"] textarea');

    const inputs = Array.from(textareaCollection ?? []).map((textarea) => {
        // @ts-ignore
        var textareaValue = textarea.value;
        return textareaValue
    });

    return inputs
}
