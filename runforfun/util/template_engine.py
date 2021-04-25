from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


def render_run_plan(workout, routes, sunrise_sunset, forecast, dress):
    template = env.get_template('run_plan.html')
    return template.render(workout=workout, routes=routes, sunrise_sunset=sunrise_sunset,
                           forecast=forecast, dress=dress)