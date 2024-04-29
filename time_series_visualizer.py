import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
bottom_25 = df['value'] >= df['value'].quantile(0.025) 
top_25 = df['value'] <= df['value'].quantile(0.975)
df = df[bottom_25 & top_25]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(19, 7))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    graph = sns.lineplot(data=df, x=df.index, y=df['value'], color='red')
    fig = graph.figure
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['Month'] = df.index.month_name()
    df_01 = df.groupby(['year', 'month', 'Month'])['value'].agg(['mean']).reset_index()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    fig, ax = plt.subplots(figsize=(14, 7))
    graph = sns.barplot(data=df_01, x='year', y='mean', hue='Month', palette='bright', hue_order=month_order)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    fig = graph.figure
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(ncols=2, figsize=(24, 9))
    # plot 01
    sns.boxplot(data=df_box, x='year', y='value', ax=axs[0])
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')
    axs[0].set_title('Year-wise Box Plot (Trend)')
    # plot 02 
    sns.boxplot(data=df_box, x='month', y='value',  ax=axs[1], order=month_order)
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    plt.savefig('box_plot.png')
    return fig
