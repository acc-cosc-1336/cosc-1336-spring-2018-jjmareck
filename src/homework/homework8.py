'''
Write a function named add_inventory with a widgets parameter of type dictionary, widget_name, and quantity

The function will add the widget to the dictionary if it doesn't exist.
If the widget exists it will update the quantity of the widgets.

    :param widgets:    a dictionary of widgets. Key is widget name, value is quantity
    :param widget_name: Widget name
    :param quantity:    Running count of inventory on hand
    :return:

    
'''
def add_inventory(widgets,widget_name,quantity):

    try:
        previous_quantity = widgets[widget_name]
    except:
        previous_quantity = 0
    finally:
        quantity += previous_quantity
    
    widgets[widget_name] = quantity
    

'''
Write a function named remove_inventory_widget with a widget_name parameter.

The function will remove the widget_name if it exists and return 'Record deleted'
Otherwise it returns 'Item not found'

    :param widgets:
    :param widget_name:
    :return:
'''
def remove_inventory_widget(widgets,widget_name):
    
    try:
        del widgets[widget_name]
        return 'Record deleted'
    except:
        return 'Item not found'
