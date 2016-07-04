from IPython.display import display, HTML
import jinja2
import os
import pandas as pd

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class twoAxesLineChart(object):

    def __init__(self):
        pass

    def draw(self, dataframe, **kwarg):

        df_json = dataframe.to_json(orient='records')
        templates_var = {'data': df_json}

        pyd3_js_url = "files/d3.pyd3.js"
        d3_js_url ="files/d3.v3.min.js"
        css_url = "files/d3.pyd3.css"

        display(HTML('''<link media="all" href="%s" type="text/css"
                      rel="stylesheet"/>''' % (css_url)))
        display(HTML('<script src="%s"></script>' % (d3_js_url)))
        display(HTML('<script src="%s"></script>' % (pyd3_js_url)))
        display(HTML('<script src="%s"></script>' % (d3_js_url)))

        TEMPLATE_FILE = "twoAxesLineChart.html"
        template = jinja_environment.get_template( TEMPLATE_FILE )

        html = template.render(templates_var)

        display(HTML(html))
