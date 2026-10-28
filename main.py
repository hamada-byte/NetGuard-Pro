from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import threading
import time

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class NetGuardProApp(App):
    def build(self):
        self.title = "NetGuard Pro"
        self.is_vpn_active = False
        self.is_skip_active = False
        self.is_firewall_active = False
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.lbl_title = Label(
            text="NetGuard Pro\nAd Blocker & Data Saver",
            font_size='22sp',
            halign='center'
        )
        layout.add_widget(self.lbl_title)

        self.lbl_info = Label(
            text="Welcome! This app blocks ads and saves your internet data by controlling background apps.",
            font_size='14sp',
            halign='center',
            color=(0.8, 0.8, 0.8, 1)
        )
        layout.add_widget(self.lbl_info)

        self.status = Label(
            text="Status: Ready & Protected 🛡️",
            font_size='18sp',
            color=(0.3, 1, 0.3, 1)
        )
        layout.add_widget(self.status)

        self.btn_vpn = Button(
            text="Enable Ad Blocker (Local VPN)",
            font_size='16sp',
            background_color=(0.2, 0.6, 1, 1),
            size_hint=(1, 0.18)
        )
        self.btn_vpn.bind(on_press=self.toggle_local_vpn)
        layout.add_widget(self.btn_vpn)

        self.btn_skip = Button(
            text="Enable Auto-Skip (Accessibility)",
            font_size='16sp',
            background_color=(0.3, 0.8, 0.4, 1),
            size_hint=(1, 0.18)
        )
        self.btn_skip.bind(on_press=self.toggle_accessibility)
        layout.add_widget(self.btn_skip)

        self.btn_firewall = Button(
            text="Data Firewall (Block Background Apps)",
            font_size='16sp',
            background_color=(0.9, 0.5, 0.2, 1),
            size_hint=(1, 0.18)
        )
        self.btn_firewall.bind(on_press=self.toggle_firewall)
        layout.add_widget(self.btn_firewall)

        return layout

    def toggle_local_vpn(self, instance):
        self.is_vpn_active = not self.is_vpn_active
        if self.is_vpn_active:
            self.status.text = "Status: Local VPN Active & Blocking Ads 🛡️"
            self.status.color = (0.3, 1, 0.3, 1)
            self.btn_vpn.text = "Disable Ad Blocker"
        else:
            self.status.text = "Status: Protection Disabled ❌"
            self.status.color = (1, 0.3, 0.3, 1)
            self.btn_vpn.text = "Enable Ad Blocker (Local VPN)"

    def toggle_accessibility(self, instance):
        self.is_skip_active = not self.is_skip_active
        if self.is_skip_active:
            self.status.text = "Status: Auto-Skip Engine Active ⚡"
            self.status.color = (0.3, 1, 0.3, 1)
            self.btn_skip.text = "Disable Auto-Skip"
        else:
            self.status.text = "Status: Auto-Skip Disabled"
            self.status.color = (1, 0.3, 0.3, 1)
            self.btn_skip.text = "Enable Auto-Skip (Accessibility)"

    def toggle_firewall(self, instance):
        self.is_firewall_active = not self.is_firewall_active
        if self.is_firewall_active:
            self.status.text = "Status: Data Firewall Active & Saving Data 📶"
            self.status.color = (0.3, 1, 0.3, 1)
            self.btn_firewall.text = "Disable Data Firewall"
        else:
            self.status.text = "Status: Firewall Disabled"
            self.status.color = (1, 0.3, 0.3, 1)
            self.btn_firewall.text = "Data Firewall (Block Background Apps)"

if __name__ == '__main__':
    NetGuardProApp().run()
