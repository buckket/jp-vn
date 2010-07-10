
init:
    
    python:
    
        def jumpToLabel():
            ui.vbox(xanchor=0.5,yanchor=0.5,xpos=0.5,ypos=0.5)
            ui.text("Name des Labels:")
            ui.input("")
            ui.close()
            
            label = ui.interact()
            
            if renpy.has_label(label):
                nvl_clear()
                renpy.music.stop()
                renpy.jump(label)
            else:
                ui.vbox(xanchor=0.5,yanchor=0.5,xpos=0.5,ypos=0.5)
                ui.text("Label nicht gefunden.")
                ui.button(clicked=ui.returns(True),xpos=0.5,xanchor=0.5)
                ui.text("OK")
                ui.close()
            
                ok = ui.interact()
                
                jumpToLabel()
 
        def overlay():

            if not config.developer:
                return

            import os.path
            filename, line = renpy.get_filename_line()
            filename = os.path.basename(filename)

            ui.text("%s:%d" % (filename, line),
                    xanchor=1.0,yanchor=1.0,xpos=1.0,ypos=1.0,
                    size=14)
                    
            ui.button(xanchor=0.0, yanchor=1.0, xpos=0.0, ypos=1.0, clicked=jumpToLabel)
            ui.text("Springe zu...", size = 14)
                    
        config.overlay_functions.append(overlay)
