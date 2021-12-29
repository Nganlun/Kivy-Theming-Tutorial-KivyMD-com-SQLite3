from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.color_definitions import colors
from kivy.properties import StringProperty
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.lang.builder import Builder
import sqlite3
Builder.load_file("customer_sc.kv")
class ScManager(ScreenManager):
    pass
class Tab(MDFloatLayout, MDTabsBase):    
    content_text = StringProperty("")
class MyToggleButton(MDFillRoundFlatButton, MDToggleButton):    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light
class CustomerScreen(Screen):  
    def set_light(self):        
        self.current_app.theme_cls.theme_style = "Light"
        sql_update = "UPDATE tb_temas SET  tema = 'Light'  WHERE id = '1';"
        self.current_app.cursor.execute(sql_update)
    def set_dark(self):
        self.current_app.theme_cls.theme_style = "Dark"
        sql_update = """UPDATE tb_temas SET tema = 'Dark' WHERE id = 1;"""
        self.current_app.cursor.execute(sql_update)
    def toggle_palette(self):          
        if self.ids['check1'].active == True:            
            self.current_app.theme_cls.primary_palette = "Cyan" 
            sql_update = "UPDATE tb_temas SET  paleta = 'Cyan' WHERE id = '1';"
            self.current_app.cursor.execute(sql_update)
            self.current_app.cnx.commit()            
        if self.ids['check2'].active == True:
            self.current_app.theme_cls.primary_palette = "Teal"
            sql_update = "UPDATE tb_temas SET  paleta = 'Teal' WHERE id = '1';"
            self.current_app.cursor.execute(sql_update)
            self.current_app.cnx.commit()            
        if self.ids['check3'].active == True:
            self.current_app.theme_cls.primary_palette = "Blue"
            sql_update = "UPDATE tb_temas SET  paleta = 'Blue' WHERE id = '1';"
            self.current_app.cursor.execute(sql_update)
            self.current_app.cnx.commit()            
        if self.ids['check4'].active == True:
            self.current_app.theme_cls.primary_palette = "Purple"
            sql_update = "UPDATE tb_temas SET  paleta = 'Purple' WHERE id = '1';"
            self.current_app.cursor.execute(sql_update)
            self.current_app.cnx.commit()            
        if self.ids['check5'].active == True:
            self.current_app.theme_cls.primary_palette = "Red"
            sql_update = "UPDATE tb_temas SET  paleta = 'Red' WHERE id = '1';"
            self.current_app.cursor.execute(sql_update)
            self.current_app.cnx.commit()            
        if self.ids['check6'].active == True:
            self.current_app.theme_cls.primary_palette = "Orange"
            sql_update = "UPDATE tb_temas SET  paleta = 'Orange' WHERE id = '1';"
            self.current_app.cursor.execute(sql_update)
            self.current_app.cnx.commit()            
        if self.ids['check7'].active == True:
            self.current_app.theme_cls.primary_palette = "Amber"
            sql_update = "UPDATE tb_temas SET  paleta = 'Amber' WHERE id = '1';"
            self.current_app.cursor.execute(sql_update)
            self.current_app.cnx.commit()            
        if self.ids['check8'].active == True:
            self.current_app.theme_cls.primary_palette = "Gray"
            sql_update = "UPDATE tb_temas SET  paleta = 'Gray' WHERE id = '1';"
            self.current_app.cursor.execute(sql_update)
            self.current_app.cnx.commit()            
        if self.current_app.theme_cls.theme_style == "Dark":
            self.set_dark()
        else:
            self.set_light()
    def __init__(self, **kw):
        super(CustomerScreen, self).__init__(**kw)
        self.current_app = App.get_running_app()        
    def on_touch_down(self, touch):
        self.toggle_palette()                            
        return super(CustomerScreen, self).on_touch_down(touch)
class ThemeApp(MDApp):
    cnx =  sqlite3.connect("data.sql")
    cursor = cnx.cursor()  
    def inserir_tema(self):
        sql_inicio = "INSERT INTO tb_temas (id, tema, paleta) VALUES ('1', 'Light', 'Cyan');"    
        self.cursor.execute(sql_inicio)
        self.cnx.commit()
    def criar_tabela(self):
        sql_tabela = """CREATE TABLE IF NOT EXISTS tb_temas (
        id integer PRIMARY KEY,
        tema text NOT NULL,
        paleta text NOT NULL)"""
        self.cnx.execute(sql_tabela)        
        self.cursor.execute("SELECT * FROM tb_temas")
        data = self.cursor.fetchall()
        if len(data)==0 or data==None:
            self.inserir_tema()
            print("Tema inserido na base de dados.")
    def aplicar_tema(self):
        sql_tema = "SELECT tema, paleta  FROM tb_temas WHERE id = '1';"    
        self.cursor.execute(sql_tema)
        data =  self.cursor.fetchall()
        if len(data)==0 or data==None:
            self.inserir_tema()
            print("Tema inserido na base de dados.")
        else:
            for d in data:                      
                self.theme_cls.primary_palette = str(d[1])
                self.theme_cls.theme_style = str(d[0])
    def fechar_app(self):
        self.stop() 
    def build(self):
        self.criar_tabela()
        self.aplicar_tema()
        scm = ScManager()
        scm.current = "customer"
        return scm
if __name__ == "__main__":
    ThemeApp().run()
