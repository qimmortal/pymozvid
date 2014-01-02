#name of the second display
#TODO - find it automatically
dname=r'\\.\DISPLAY2'
window_offset=(150,32) # bottom left corner of window from bottom left of screen!
#list of touples (name:string, settings:dict)
modes = [('Home - CRT on Top',
          {'PelsHeight':1024L,
           'PelsWidth':1280L,
           'BitsPerPel':32L,
           'DisplayFrequency':85L,
           'Position_x':-256,
           'Position_y':-1024}),      
         ('Home - CRT on Left',
          {'PelsHeight':1024L,
           'PelsWidth':1280L,
           'BitsPerPel':32L,
           'DisplayFrequency':85L,
           'Position_x':-1280,
           'Position_y':0}),
         ('Work - LCD on Left',
          {'PelsHeight':1024L,
           'PelsWidth':1280L,
           'BitsPerPel':32L,
           'DisplayFrequency':60L,
           'Position_x':-1280,
           'Position_y':-256})

         ]