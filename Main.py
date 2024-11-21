from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

# Define the LoginScreen
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)
        login_button = Button(text='Login', on_press=self.validate_login)

        layout.add_widget(Label(text='Login to Tuck Shop'))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        self.add_widget(layout)

    def validate_login(self, instance):
        # Replace these credentials with your own logic
        if self.username_input.text == 'admin' and self.password_input.text == 'password':
            self.manager.current = 'tuckshop'
        else:
            self.username_input.text = ''
            self.password_input.text = ''
            self.username_input.hint_text = 'Invalid username, try again'
            self.password_input.hint_text = 'Invalid password'

# Define the TuckShop Screen
class TuckShop(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add buttons for actions
        button_layout = BoxLayout(size_hint_y=None, height=40, padding=5, spacing=5)
        layout.add_widget(button_layout)

        view_button = Button(text='View Items', on_press=self.load_items)
        button_layout.add_widget(view_button)

        back_button = Button(text='Back', on_press=self.go_back)
        button_layout.add_widget(back_button)

        # Welcome label
        welcome_label = Label(text='Welcome to Maelezo University Tuck Shop!', size_hint_y=None, height=40)
        layout.add_widget(welcome_label)

        # Label for items
        item_label = Label(text='Items:', size_hint_y=None, height=40)
        layout.add_widget(item_label)

        # Scrollable list of items
        scroll_view = ScrollView(size_hint=(1, 1))
        self.item_list = BoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        self.item_list.bind(minimum_height=self.item_list.setter('height'))
        scroll_view.add_widget(self.item_list)
        layout.add_widget(scroll_view)

        # Label to show the selected item
        self.selected_item_label = Label(text='Selected item: None', size_hint_y=None, height=40)
        layout.add_widget(self.selected_item_label)

        # Order form
        self.order_form = BoxLayout(orientation='vertical', size_hint_y=None, height=200, padding=10, spacing=10)
        self.name_input = TextInput(hint_text='Your Name', multiline=False)
        self.contact_input = TextInput(hint_text='Contact Information', multiline=False)
        self.place_order_button = Button(text='Place Order', on_press=self.place_order)

        self.order_form.add_widget(Label(text='Place Order'))
        self.order_form.add_widget(self.name_input)
        self.order_form.add_widget(self.contact_input)
        self.order_form.add_widget(self.place_order_button)

        layout.add_widget(self.order_form)

        self.add_widget(layout)

    def load_items(self, instance):
        items = [
            {"name": "Notebook", "price": 100, "stock": 20, "offer": "10% off"},
            {"name": "Pen", "price": 20, "stock": 50, "offer": "Buy 2 Get 1 Free"},
            {"name": "Pencil", "price": 20, "stock": 100, "offer": "No offers"},
            {"name": "Eraser", "price": 25, "stock": 50, "offer": "No offers"},
            {"name": "Sharpener", "price": 30, "stock": 120, "offer": "No offers"},
            {"name": "Ruler", "price": 50, "stock": 80, "offer": "20% off"},
            {"name": "Glue Stick", "price": 130, "stock": 40, "offer": "Buy 1 Get 1 Free"},
            {"name": "Stickynote", "price": 100, "stock": 50, "offer": "15% off"},
            {"name": "Cupcakes", "price": 25, "stock": 30, "offer": "Buy 3 Get 1 Free"},
            {"name": "Chips", "price": 100, "stock": 20, "offer": "Buy 2 Get 1 Free"},
            {"name": "Soda", "price": 50, "stock": 20, "offer": "No offers"},
            {"name": "Chocolate", "price": 70, "stock": 15, "offer": "10% off"},
            {"name": "Candy", "price": 10, "stock": 100, "offer": "Buy 5 Get 2 Free"},
            {"name": "Ice Cream", "price": 50, "stock": 30, "offer": "Buy 1 Get 1 Free"},
            {"name": "Cookies", "price": 100, "stock": 20, "offer": "15% off"}
        ]
        self.item_list.clear_widgets()  # Clear the current list
        for item in items:
            item_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=5, padding=5)
            item_label = Label(text=f"{item['name']} - Price: {item['price']} Ksh, Stock: {item['stock']}, Offer: {item['offer']}")
            select_button = Button(text='Select', size_hint_x=None, width=100)
            select_button.bind(on_press=lambda instance, i=item, b=item_box: self.select_item(i, b))
            item_box.add_widget(item_label)
            item_box.add_widget(select_button)
            self.item_list.add_widget(item_box)

    def select_item(self, item, item_box):
        # Clear selection color from all items
        for child in self.item_list.children:
            child.background_color = (1, 1, 1, 1)  # Reset the background color

        # Highlight the selected item
        item_box.background_color = (0.8, 0.8, 0.8, 1)  # Change the background color to grey

        # Update the selected item label
        self.selected_item_label.text = f"Selected item: {item['name']} - Price: {item['price']} Ksh"

    def place_order(self, instance):
        name = self.name_input.text
        contact = self.contact_input.text
        selected_item = self.selected_item_label.text
        if name and contact and "Selected item: None" not in selected_item:
            print(f"Order placed by {name}, Contact: {contact}, Item: {selected_item}")
            self.selected_item_label.text = 'Selected item: None'
            self.name_input.text = ''
            self.contact_input.text = ''
            for child in self.item_list.children:
                child.background_color = (1, 1, 1, 1)  # Reset the background color
            print('Order placed successfully!')

    def go_back(self, instance):
        self.manager.current = 'login'

# Define the main app
class TuckShopApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(TuckShop(name='tuckshop'))
        return sm

if __name__ == '__main__':
    TuckShopApp().run()
