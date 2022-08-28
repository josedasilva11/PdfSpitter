export const t_dict = require('./translated.json')


export function _translate(text) {
    if (t_dict[text])
        return t_dict[text]
    return text
}