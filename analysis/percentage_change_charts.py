import plotly
import plotly.graph_objs as go
import styles
import sys

def create_change_in_percentage_chart(data, name, labelx, labely, title, titlex, titley, limit):
    print('Creating plot...')
    series = [(float(d[labelx]), float(d[labely]), d["symbol"]) for d in data if d[labelx] != None and d[labely] != None and int(d["rank"]) < limit]

    series_q1 = [(x,y,z) for (x,y,z) in series if x > 0 and y > 0]
    series_q2 = [(x,y,z) for (x,y,z) in series if x < 0 and y < 0]
    series_q3 = [(x,y,z) for (x,y,z) in series if (x > 0 and y < 0) or (x < 0 and y > 0)]

    x1, y1, z1 = zip(*series_q1)
    x2, y2, z2 = zip(*series_q2)
    x3, y3, z3 = zip(*series_q3)

    trace0 = go.Scatter(
        x = x1,
        y = y1,
        mode = 'markers+text',
        name = 'Symbols',
        text = z1,
        marker = styles.marker_open_circle_green,
        textposition='top'
    )

    trace1 = go.Scatter(
        x = x2,
        y = y2,
        mode = 'markers+text',
        name = 'Symbols',
        text = z2,
        marker = styles.marker_open_circle_red,
        textposition='top'
    )

    trace2 = go.Scatter(
        x = x3,
        y = y3,
        mode = 'markers+text',
        name = 'Symbols',
        text = z3,
        marker = styles.marker_open_circle_gray,
        textposition='top'
    )

    data = [trace0,trace1,trace2]

    layout = go.Layout(
        title = title,
        titlefont = dict(size=28),
        hovermode='closest',        
        xaxis=dict(
            title=titlex
        ),
        yaxis=dict(
            title=titley
        ),
        showlegend = False
    )

    fig = go.Figure(data=data, layout=layout)
    #py.image.save_as(fig, filename='plot.png')

    print('Uploading plot...')
    #py.plot(fig, filename=name, auto_open=False)
    return plotly.offline.plot(fig, include_plotlyjs=False, output_type='div').replace('"showLink": true', '"showLink": false')

