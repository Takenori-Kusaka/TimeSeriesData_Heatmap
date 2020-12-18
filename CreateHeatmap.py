import pandas as pd
import plotly.graph_objects as go
from PIL import Image

def create_graph(filepath_list: list, target_col: str, sampling_rate: str, graph_title: str, xaxis_title: str, yaxis_title: str, background_image_path: str, output_filepath: str):

    df_list = []
    for f in filepath_list:
        df_list.append(pd.read_csv(f, index_col=0, parse_dates=[0]).resample(sampling_rate).mean().interpolate(method="linear"))
    df = df_list[0].join([df_list[1], df_list[2]], how='left')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['x'], y=df['y'],
                             mode='markers',
                             marker=dict(
                                 size=3,
                                 color=df[target_col],
                                 colorscale='RdYlGn',
                                 showscale=True
                             ),
                             name=target_col))
    fig.update_layout(title_text=graph_title,
                      xaxis_title=xaxis_title,
                      yaxis_title=yaxis_title,
                      xaxis_range=[0, 800],
                      yaxis_range=[0, 600])
    img = Image.open(background_image_path)
    fig.add_layout_image(
        dict(
            source=img,
            xref="x",
            yref="y",
            x=0,
            y=600,
            sizex=800,
            sizey=600,
            sizing="stretch",
            opacity=0.5,
            layer="below")
    )
    fig.write_html(output_filepath + '.html', auto_open=False)
    fig.write_image(output_filepath + '.png', width=1920, height=1080)
    fig.show()

if __name__ == "__main__":
    create_graph(['map_log.csv', 'signal_level_log.csv', 'throughput_log.csv'],
                 'signal_level',
                 '200ms',
                 'WifiSignalLevel',
                 'X座標',
                 'Y座標',
                 './map_google_embed.png',
                 './heatmap_px')