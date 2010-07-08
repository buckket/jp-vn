
init:
    
    python hide:
 
        def overlay():

            if not config.developer:
                return

            import os.path
            filename, line = renpy.get_filename_line()
            filename = os.path.basename(filename)

            ui.text("%s:%d" % (filename, line),
                    xanchor=1.0,yanchor=1.0,xpos=1.0,ypos=1.0,
                    size=14)
                    
        config.overlay_functions.append(overlay)
