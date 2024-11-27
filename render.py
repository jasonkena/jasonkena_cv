import re
import yaml
import jinja2


def replace_refs(input_string, func):
    # Regex to match REF_{id}
    pattern = r"REF_(\w+)"

    # Function to replace each match
    def replacer(match):
        id = match.group(1)  # Extract the id
        return rf"\hyperlink{{{id}}}{{{func(id)}}}"

    # Substitute all matches in the string
    return re.sub(pattern, replacer, input_string)


def preprocess(data):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tags = {}
    # store publication tags
    for i in range(len(data["publications"])):
        tag = data["publications"][i]["tag"]
        assert tag not in tags
        tags[tag] = alphabet[len(tags)]
        data["publications"][i]["tag_alpha"] = tags[tag]

    for i in range(len(data["patents"])):
        tag = data["patents"][i]["tag"]
        assert tag not in tags
        tags[tag] = alphabet[len(tags)]
        data["patents"][i]["tag_alpha"] = tags[tag]

    for i in range(len(data["research"])):
        for j in range(len(data["research"][i]["misc"])):
            try:
                data["research"][i]["misc"][j] = replace_refs(
                    data["research"][i]["misc"][j],
                    lambda x: f"\\hypertarget{{{x}_back}}{{[{tags[x]}]}}",
                )
            except Exception as e:
                print(data["research"][i]["misc"][j])
                print(e)
                breakpoint()

    return data


data = yaml.load(open("data.yaml"), Loader=yaml.FullLoader)
data = preprocess(data)
template = jinja2.Template(
    open("template.tex").read(),
    # since {} and # are used by latex
    variable_start_string="[[",
    variable_end_string="]]",
    block_start_string="[%",
    block_end_string="%]",
    comment_start_string="[=",
    comment_end_string="=]",
)


output = template.render(**data)
open("main.tex", "w").write(output)
