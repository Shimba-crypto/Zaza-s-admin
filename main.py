from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import random

class ZazaAdmin(App):
    def build(self):
        # Main Layout
        self.root_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # --- Header ---
        header = Label(text="[b]ZAZA ADMIN V1.0[/b]", markup=True, size_hint_y=0.1, font_size='28sp')
        self.root_layout.add_widget(header)

        # --- Stats Grid ---
        stats_grid = GridLayout(cols=2, spacing=10, size_hint_y=0.3)
        self.cpu_label = Label(text="CPU: 0%", color=(0, 1, 0, 1))
        self.mem_label = Label(text="MEM: 0%", color=(0, 1, 0, 1))
        self.zmw_label = Label(text="ZMW/USD: 26.40", color=(1, 0.8, 0, 1))
        self.net_label = Label(text="Status: Secure", color=(0, 1, 1, 1))
        
        for widget in [self.cpu_label, self.mem_label, self.zmw_label, self.net_label]:
            stats_grid.add_widget(widget)
        self.root_layout.add_widget(stats_grid)

        # --- Control Buttons ---
        controls = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.2)
        
        refresh_btn = Button(text="Refresh Stats", background_color=(0.2, 0.6, 1, 1))
        refresh_btn.bind(on_press=self.update_stats)
        
        panic_btn = Button(text="PANIC LOCKDOWN", background_color=(1, 0, 0, 1))
        panic_btn.bind(on_press=self.trigger_panic)
        
        controls.add_widget(refresh_btn)
        controls.add_widget(panic_btn)
        self.root_layout.add_widget(controls)

        # --- Console Logs ---
        self.console = Label(text="[Initializing Zaza Kernel...]\n[Systems Check: OK]", 
                             valign='top', halign='left', size_hint_y=0.4, markup=True)
        self.console.bind(size=self.console.setter('text_size'))
        self.root_layout.add_widget(self.console)

        # Update stats automatically every 3 seconds
        Clock.schedule_interval(self.update_stats, 3)
        
        return self.root_layout

    def update_stats(self, *args):
        self.cpu_label.text = f"CPU: {random.randint(10, 85)}%"
        self.mem_label.text = f"MEM: {random.randint(20, 60)}%"
        self.log_to_console("System status heartbeat checked.")

    def trigger_panic(self, instance):
        self.log_to_console("[!] CRITICAL: Panic Mode Activated!")
        self.root_layout.canvas.before.clear()
        # Visual feedback for panic mode
        self.net_label.text = "Status: LOCKED"
        self.net_label.color = (1, 0, 0, 1)

    def log_to_console(self, message):
        lines = self.console.text.split('\n')
        lines.append(f"> {message}")
        if len(lines) > 6: lines.pop(0)
        self.console.text = '\n'.join(lines)

if __name__ == "__main__":
    ZazaAdmin().run()
