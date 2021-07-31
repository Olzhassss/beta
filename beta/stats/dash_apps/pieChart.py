import dash_core_components as dcc
import dash_html_components as html
from pandas.core.frame import DataFrame
import plotly.express as px
import pandas as pd

from django_plotly_dash import DjangoDash

from main.models import Profile

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('pieChart', external_stylesheets=external_stylesheets)


# df = pd.DataFrame([t.__dict__ for t in Profile.objects.all() ])
# obj = get_object_or_404(Profile, id=app_id)
# obj_dict = dict(map( lambda x: (x.verbose_name, x.value_to_string(obj)), Profile._meta.get_fields()))
# [ t.__dict__ for t in Profile.objects.all() ]

def casual():
    std_list = []
    for instance in Profile.objects.all():
        std_dict = instance.__dict__
        std_dict.pop('_state')
        for field in Profile._meta.get_fields():
            std_dict[field.verbose_name.capitalize()] = std_dict[field.name]
            std_dict.pop(field.name, None)
        std_list.append(std_dict)
    df1 = pd.DataFrame(std_list)
    return

def pand():
    df = pd.DataFrame([t.__dict__ for t in Profile.objects.all()])
    df.drop('_state', axis=1, inplace=True)
    df.columns = [x.verbose_name.capitalize() for x in Profile._meta.get_fields()]
    return df

df = pand()

# std_dict = list(map(lambda x: x.__dict__, Profile.objects.all())
# for row in std_dict:
#     for field in Profile._meta.get_fields():
#         std_dict[row][field.verbose_name] = std_dict[row][field.name]
#         std_dict[row].pop(field.name, None)

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# for field in Profile._meta.get_fields():
#     df.rename()

df['Mailbox'] = df['Email'].str.split('@').str[1]

pie_sex = px.pie(df, names='Sex', title='Division by sex in applications')
pie_email = px.pie(df, names='Mailbox', title='Popularity of certain mailboxes')
app.layout = html.Div([
    html.Div([
        dcc.Graph(
                figure=pie_sex
            )
    ], style={'width':'50%', 'display':'inline-block'}),
    html.Div([
        dcc.Graph(
                figure=pie_email
            )
    ], style={'width':'50%', 'display':'inline-block'})
])

import dash


app = DjangoDash('SimpleExample')

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i,
                  'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
        value='medium'
    ),
    html.Div(id='output-size')

])

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value

@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." %(dropdown_size,
                                                  dropdown_color)