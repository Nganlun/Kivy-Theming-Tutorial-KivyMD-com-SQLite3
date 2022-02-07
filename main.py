import kivy
import sqlite3
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.theming import ThemeManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFillRoundFlatButton
Builder.load_file("gui.kv")
class Tab(MDFloatLayout, MDTabsBase):    
    pass
class ScManager(ScreenManager):
    pass                                                          
class ThemeApp(Screen):        
    def __init__(self, **kwargs):
        super(ThemeApp, self).__init__(**kwargs)
        self.current_app = MDApp.get_running_app()                  
    def on_pre_enter(self, *args):        
        sql_theme = "SELECT palette FROM tb_themes WHERE id = '1';"
        self.current_app.cursor.execute(sql_theme)
        row = self.current_app.cursor.fetchone()
        print("ids", self.ids)
        if row[0] == "Cyan":
            self.ids['check1'].active = True
        elif row[0] == "Teal":
            self.ids['check2'].active = True
        elif row[0] == "Blue":
            self.ids['check3'].active = True
        elif row[0] == "Purple":
            self.ids['check4'].active = True
        elif row[0] == "Red":
            self.ids['check5'].active = True
        elif row[0] == "Orange":
            self.ids['check6'].active = True
        elif row[0] == "Amber":
            self.ids['check7'].active = True
        elif row[0] == "Gray":
            self.ids['check8'].active = True
    def set_light(self):        
        self.current_app.theme_cls.theme_style = "Light"
        sql_update = "UPDATE tb_themes SET  theme = 'Light'  WHERE id = '1';"
        self.current_app.cursor.execute(sql_update)
        self.current_app.connection.commit() 
    def set_dark(self):
        self.current_app.theme_cls.theme_style = "Dark"
        sql_update = """UPDATE tb_themes SET theme = 'Dark' WHERE id = 1;"""
        self.current_app.cursor.execute(sql_update)
        self.current_app.connection.commit()  
    def on_checkbox_active(self, checkbox, value):                       
        if value:            
            if (checkbox== self.ids['check1']):            
                self.current_app.theme_cls.primary_palette = "Cyan" 
                sql_update = "UPDATE tb_themes SET  palette = 'Cyan' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.connection.commit()                 
            elif (checkbox== self.ids['check2']):
                self.current_app.theme_cls.primary_palette = "Teal"
                sql_update = "UPDATE tb_themes SET  palette = 'Teal' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.connection.commit()           
            elif (checkbox== self.ids['check3']):
                self.current_app.theme_cls.primary_palette = "Blue"
                sql_update = "UPDATE tb_themes SET  palette = 'Blue' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.connection.commit()           
            elif (checkbox== self.ids['check4']):
                self.current_app.theme_cls.primary_palette = "Purple"
                sql_update = "UPDATE tb_themes SET  palette = 'Purple' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.connection.commit()           
            elif (checkbox== self.ids['check5']):
                self.current_app.theme_cls.primary_palette = "Red"
                sql_update = "UPDATE tb_themes SET  palette = 'Red' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.connection.commit()                       
            elif (checkbox== self.ids['check6']):
                self.current_app.theme_cls.primary_palette = "Orange"
                sql_update = "UPDATE tb_themes SET  palette = 'Orange' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.connection.commit()          
            elif (checkbox== self.ids['check7']):
                self.current_app.theme_cls.primary_palette = "Amber"
                sql_update = "UPDATE tb_themes SET  palette = 'Amber' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.connection.commit()           
            elif (checkbox== self.ids['check8']):
                self.current_app.theme_cls.primary_palette = "Gray"
                sql_update = "UPDATE tb_themes SET  palette = 'Gray' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.connection.commit()                      
        else:
            pass          
class Theming_App(MDApp):
    MDApp.title = "Theming App"    
    connection=  sqlite3.connect("data.db")
    cursor = connection.cursor()     
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = ThemeApp()
    def insert_theme(self):
        sql_inicio = "INSERT INTO tb_themes(id, theme, palette) VALUES ('1', 'Light', 'Blue');"    
        self.cursor.execute(sql_inicio)
        self.connection.commit()
    def create_table(self):
        sql_tabela = """CREATE TABLE IF NOT EXISTS tb_themes(
        id integer PRIMARY KEY,
        theme text NOT NULL,
        palette text NOT NULL)"""
        self.connection.execute(sql_tabela)        
        self.cursor.execute("SELECT * FROM tb_themes")
        data = self.cursor.fetchall()
        if len(data)==0 or data==None:
            self.insert_theme()                                
    def apply_theme(self):
        sql_theme = "SELECT theme, palette  FROM tb_themes WHERE id = '1';"    
        self.cursor.execute(sql_theme)
        data =  self.cursor.fetchall()
        if len(data)==0 or data==None:
            self.insert_theme()            
        else:
            for dt in data:
                theme = dt[0]
                palette = dt[1]                        
            self.theme_cls.theme_style = theme
            self.theme_cls.primary_palette = palette              
    def build(self):        
        self.sm = ScManager()
        self.create_table()                
        self.apply_theme()        
        self.sm.add_widget(ThemeApp(name='theme_app'))        
        return self.sm     
if __name__ == "__main__":
    Theming_App().run()
