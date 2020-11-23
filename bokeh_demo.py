# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:37:31 2020

@author: Gurpal Singh
"""

# Imports
from bokeh.io import curdoc
from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.layouts import widgetbox, row
from bokeh.models import Slider, TextInput

# Define callback function for text input
def update_plot_text(attr, old, new): 
    
    # Debug
    print('update_plot_text funtion called with value: ', text_input.value)

    # Check if integer format
    if text_input.value.isdigit():
        
        # Clear current doc 
        curdoc().clear() 
       
        # Cast to int
        num_input = int(text_input.value)
        
        # Regenerate X and Y values 
        x = [x for x in range(0,num_input)]
        y = x 

        # Create figure plot
        plot = figure(title='Title', plot_height=500, plot_width=1000,
                      x_range=(0,100+num_input), y_range=(0,100+num_input),
                      tools=[HoverTool(tooltips=[('X','@x'),('Y','@y')],mode='mouse')])

        # Adding glyphs to plot
        plot.circle(x,y)

        # Add the widgets and plot to doc
        layout = row(widgetbox(slider,text_input), plot)
        
        # Update current doc
        curdoc().add_root(layout)
        
    # Error     
    else:
        print('User input is not valid')
        
# Define the callback function for slider
def update_plot_slider(attr, old, new): 
    
    # Clear the current doc
    curdoc().clear()
    
    print('update_plot_slider function called with value: ',slider.value)
    
    # Regenerate X and Y values 
    x = [x for x in range(0,slider.value)]
    y = x 

    # Create figure plot
    plot = figure(title='Title', plot_height=500, plot_width=1000,
                  x_range=(0,100), y_range=(0,100),
              tools=[HoverTool(tooltips=[('X','@x'),('Y','@y')],mode='mouse')])

    # Adding glyphs
    plot.circle(x,y)

    # Add the plot to current document and add a title
    layout = row(widgetbox(slider,text_input), plot)
    curdoc().add_root(layout)
    
    
# Default Plot at start
    
# Generate dummy data
x = [x for x in range(0,100)]
y = x

# Make a slider object: slider
slider = Slider(title = 'X Range', start = 0, end = 100, step =1, value = 100)

# Attach the callback to the 'value' property of slider
slider.on_change('value',update_plot_slider)

# Make a text intput object: text_input
text_input = TextInput(value='100', title='X Range: ')

# Attach the callback to the 'value' property of text_input
text_input.on_change("value", update_plot_text)

# Create figure plot
plot = figure(title='Title', plot_height=500, plot_width=1000,
              x_range=(0,100), y_range=(0,100),
              tools=[HoverTool(tooltips=[('X','@x'),('Y','@y')],mode='mouse')])

# Adding glyphs
plot.circle(x,y)

# Add the plot and widgets to layout
layout = row(widgetbox(slider,text_input), plot)

# Add layout to current doc
curdoc().add_root(layout)
curdoc().title = 'Bokeh Demo'
