import webbrowser
import time
import random
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class ZazaAdminV2(App):
    def build(self):
        self.tp = TabbedPanel(do_default_tab=False, background_color=(0.05, 0.05, 0.05, 1))

        # --- TAB 1: SYSTEMS MONITOR ---
        tab1 = TabbedPanelItem(text='Systems')
        layout1 = BoxLayout(orientation='vertical', padding=15, spacing=10)
        self.time_label = Label(text="00:00:00", font_size='36sp', color=(0, 1, 0.5, 1), size_hint_y=0.2)
        layout1.add_widget(self.time_label)
        
        stats_grid = GridLayout(cols=2, spacing=10, size_hint_y=0.3)
        self.cpu_label = Label(text="CPU: 0%", color=(0.2, 0.8, 1, 1))
        self.mem_label = Label(text="MEM: 0%", color=(0.2, 0.8, 1, 1))
        self.zmw_label = Label(text="ZMW/USD: 26.42", color=(1, 0.8, 0, 1))
        self.status_label = Label(text="SECURE", color=(0, 1, 0, 1))
        for lbl in [self.cpu_label, self.mem_label, self.zmw_label, self.status_label]:
            stats_grid.add_widget(lbl)
        layout1.add_widget(stats_grid)

        controls = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.5)
        lock_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        lock_box.add_widget(Label(text="GLOBAL LOCKDOWN"))
        self.lock_switch = Switch(active=False)
        self.lock_switch.bind(active=self.on_lockdown)
        lock_box.add_widget(self.lock_switch)
        controls.add_widget(lock_box)
        
        update_btn = Button(text="CHECK FOR UPDATES", background_color=(0, 0.4, 0.8, 1))
        update_btn.bind(on_press=self.open_github)
        controls.add_widget(update_btn)
        layout1.add_widget(controls)
        tab1.add_widget(layout1)

        # --- TAB 2: THE CREW ---
        tab2 = TabbedPanelItem(text='The Crew')
        crew_scroll = ScrollView()
        crew_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
        crew_layout.bind(minimum_height=crew_layout.setter('height'))
        for member in ["Jojo", "Biggi Elijah", "Perfect Kaputo", "Yango Tate", "Kutemwa"]:
            crew_layout.add_widget(Button(text=f"{member} [ONLINE]", size_hint_y=None, height=60, background_color=(0.1, 0.3, 0.1, 1)))
        crew_scroll.add_widget(crew_layout)
        tab2.add_widget(crew_scroll)

        # --- TAB 3: ZAZA TERMINAL ---
        tab3 = TabbedPanelItem(text='Terminal')
        term_layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        # Scrollable area for history
        self.term_scroll = ScrollView(size_hint=(1, 0.8), bar_width=10)
        self.history_label = Label(text="[color=00FF00]Zaza Terminal v1.0 Initialized...[/color]\nType 'help' for commands.", 
                                   markup=True, size_hint_y=None, valign='top', halign='left')
        self.history_label.bind(size=self.history_label.setter('text_size'), 
                                texture_size=self.history_label.setter('height'))
        self.term_scroll.add_widget(self.history_label)
        term_layout.add_widget(self.term_scroll)

        # Input box
        self.cmd_input = TextInput(multiline=False, size_hint=(1, 0.2), background_color=(0, 0, 0, 1), 
                                   foreground_color=(0, 1, 0, 1), font_name='Roboto', hint_text="Enter command...")
        self.cmd_input.bind(on_text_validate=self.process_command)
        term_layout.add_widget(self.cmd_input)
        
        tab3.add_widget(term_layout)

        # Add all tabs
        self.tp.add_widget(tab1)
        self.tp.add_widget(tab2)
        self.tp.add_widget(tab3)

        Clock.schedule_interval(self.update_ui, 1)
        return self.tp

    def process_command(self, instance):
        cmd = instance.text.strip().lower()
        instance.text = "" # Clear input
        response = ""

        if cmd == "help":
            response = "Available: help, status, crew, clear, exit"
        elif cmd == "status":
            response = f"System: {self.status_label.text} | CPU: {self.cpu_label.text}"
        elif cmd == "crew":
            response = "Members Online: Jojo, Biggi, Perfect, Yango, Kutemwa"
        elif cmd == "clear":
            self.history_label.text = "[color=00FF00]Terminal Cleared.[/color]"
            return
        elif cmd == "":
            return
        else:
            response = f"Unknown command: '{cmd}'"

        self.history_label.text += f"\n[color=00FF00]> {cmd}[/color]\n{response}"
        # Scroll to bottom
        Clock.schedule_once(lambda dt: setattr(self.term_scroll, 'scroll_y', 0))

    def update_ui(self, *args):
        self.time_label.text = time.strftime("%H:%M:%S")
        if not self.lock_switch.active:
            self.cpu_label.text = f"CPU: {random.randint(12, 65)}%"
            self.mem_label.text = f"MEM: {random.randint(30, 55)}%"

    def on_lockdown(self, instance, value):
        msg = "LOCKED" if value else "SECURE"
        self.status_label.text = msg
        self.status_label.color = (1, 0, 0, 1) if value else (0, 1, 0, 1)

    def open_github(self, instance):
        webbrowser.open("https://github.com/Shimba-crypto/Zaza-s-admin/releases")

if __name__ == "__main__":
    ZazaAdminV2().run()
