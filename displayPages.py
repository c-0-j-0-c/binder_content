import ipywidgets as widgets

def displayPages(page, page_nums, sec_name):
    baseURL = "https://books.google.com.au/books/publisher/"
    begin = '<img src="'
    size = '" height=900>'
    a = widgets.Output()
    with a:
        display(widgets.HTML(value=f"{begin}{baseURL}{page[page_nums[0]]}{size}"))
    s = widgets.IntSlider(
            value=page_nums[0],
            min=page_nums[0],
            max=page_nums[-1],
            step=1,
            description=sec_name,
            disabled=False,
            continuous_update=False,
            orientation='horizontal',
            readout=True,
            readout_format='d'
        )
    #mylink = widgets.jslink((s, 'value'), (im_w, 'height'))

    def handle_slider_change(change):
        a.clear_output()
        with a:
            display(widgets.HTML(value=f"{begin}{baseURL}{page[s.value]}{size}"))


    s.observe(handle_slider_change, names='value')


    w = widgets.VBox([s,a])
    display(w)
