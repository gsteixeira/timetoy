# -*- coding: utf-8 -*-






from kivy.uix.screenmanager import Screen


from kivy.clock import Clock

from datetime import datetime, timedelta
from time import gmtime, strftime, time

import time
from chronograph.chronograph import Chronograph




class JanelaCronometro (Screen):
    def __init__(self, smanager=None, last_window=None, **kwargs):
        super(JanelaCronometro, self).__init__(**kwargs)
        self.smanager = smanager
        self.last_window = last_window
        
        self.running = False
        self.cg = Chronograph(name="Testing Chronograph")
        
    def on_leave (self):
        self.smanager.remove_widget(self)
        
        
    def do_start (self):
        if self.running:
            #self.timer_refresh # stoppp
            Clock.unschedule(self.timer_refresh )
            self.cg.stop()
            self.running = False
            self.ids.butt_start.text = 'Start'
            self.ids.butt_reset.disabled = False
        else:
            self.running = True
            self.timer_refresh = Clock.schedule_interval( self._refresh, 0.1)
            self.cg.start()
            self.ids.butt_start.text = 'Stop'
            self.ids.butt_reset.disabled = True
        
    
    def do_reset (self):
        self.cg.reset()
        self._refresh(0)
        
    
    def _refresh(self, dt):
        elapsed_time = self.cg.total_elapsed_time
        #readable = strftime("%H:%M:%S", elapsed_time)
        
        td = timedelta (seconds=elapsed_time)
        
        self.ids.tx_clock.text = str(td)[:-3]
        