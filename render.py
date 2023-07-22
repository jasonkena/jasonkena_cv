import yaml
import jinja2

data = yaml.load(open("data.yaml"), Loader=yaml.FullLoader)
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
