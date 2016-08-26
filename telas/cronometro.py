# -*- coding: utf-8 -*-






from kivy.uix.screenmanager import Screen


from kivy.clock import Clock

from datetime import datetime, timedelta
from time import gmtime, strftime, time

import time
from chronograph.chronograph import Chronograph

from kivy.uix.label import Label


class JanelaCronometro (Screen):
    def __init__(self, smanager=None, last_window=None, **kwargs):
        super(JanelaCronometro, self).__init__(**kwargs)
        self.smanager = smanager
        self.last_window = last_window
        
        self.ids.area_laps.bind(minimum_height=self.ids.area_laps.setter('height'))
        
        self.running = None
        self.cg = Chronograph(name="Testing Chronograph")
        
    def on_leave (self):
        self.smanager.remove_widget(self)
        
        
    def do_start (self):
        if self.running:
            #self.timer_refresh # stoppp
                
            self.running = False
            self.ids.butt_start.text = 'Start'
            self.ids.butt_reset.disabled = False
            self.cg.stop()
            
                
            elapsed_time = self.cg.total_elapsed_time
            td = timedelta (seconds=elapsed_time)
            tempo = str(td)[:-3]
            
            wid = Label(text=tempo)
            self.ids.area_laps.add_widget (wid)
            
            self._refresh(0)
            Clock.unschedule(self.timer_refresh )
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
        