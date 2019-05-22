import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window()
window.push_handlers(pyglet.window.event.WindowEventLogger())

music = pyglet.resource.media("Cros'.wav")
music.play()

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
