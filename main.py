from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.color_definitions import colors
from kivy.properties import StringProperty, ObjectProperty
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
class CustomerScreen(Screen): 
    def __init__(self,**kwargs):
        super(CustomerScreen, self).__init__(**kwargs)             
    def set_light(self):        
        self.current_app.theme_cls.theme_style = "Light"
        sql_update = "UPDATE tb_temas SET  tema = 'Light'  WHERE id = '1';"
        self.current_app.cursor.execute(sql_update)
        self.current_app.cnx.commit() 
    def set_dark(self):
        self.current_app.theme_cls.theme_style = "Dark"
        sql_update = """UPDATE tb_temas SET tema = 'Dark' WHERE id = 1;"""
        self.current_app.cursor.execute(sql_update)
        self.current_app.cnx.commit()  
    def on_checkbox_active(self, checkbox, value):                       
        if value:
            #print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')            
            if (checkbox== self.ids['check1']):            
                self.current_app.theme_cls.primary_palette = "Cyan" 
                sql_update = "UPDATE tb_temas SET  paleta = 'Cyan' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.cnx.commit()            
            elif (checkbox== self.ids['check2']):
                self.current_app.theme_cls.primary_palette = "Teal"
                sql_update = "UPDATE tb_temas SET  paleta = 'Teal' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.cnx.commit()            
            elif (checkbox== self.ids['check3']):
                self.current_app.theme_cls.primary_palette = "Blue"
                sql_update = "UPDATE tb_temas SET  paleta = 'Blue' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.cnx.commit()            
            elif (checkbox== self.ids['check4']):
                self.current_app.theme_cls.primary_palette = "Purple"
                sql_update = "UPDATE tb_temas SET  paleta = 'Purple' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.cnx.commit()            
            elif (checkbox== self.ids['check5']):
                self.current_app.theme_cls.primary_palette = "Red"
                sql_update = "UPDATE tb_temas SET  paleta = 'Red' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.cnx.commit()                        
            elif (checkbox== self.ids['check6']):
                self.current_app.theme_cls.primary_palette = "Orange"
                sql_update = "UPDATE tb_temas SET  paleta = 'Orange' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.cnx.commit()            
            elif (checkbox== self.ids['check7']):
                self.current_app.theme_cls.primary_palette = "Amber"
                sql_update = "UPDATE tb_temas SET  paleta = 'Amber' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.cnx.commit()            
            elif (checkbox== self.ids['check8']):
                self.current_app.theme_cls.primary_palette = "Gray"
                sql_update = "UPDATE tb_temas SET  paleta = 'Gray' WHERE id = '1';"
                self.current_app.cursor.execute(sql_update)
                self.current_app.cnx.commit()                        
        else:
            pass
            #print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')       
    def __init__(self, **kw):
        super(CustomerScreen, self).__init__(**kw)
        self.current_app = App.get_running_app()            
class ThemeApp(MDApp):    
    cnx =  sqlite3.connect("data.sql")
    cursor = cnx.cursor() 
    current_tab = ""       
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):                        
        self.current_tab = (tab_text)
        if self.current_tab == "Temas":            
            print(tab_text) # Nome da Guia:
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
            for dt in data:
                tema = dt[0]
                paleta = dt[1]                        
            self.theme_cls.theme_style = tema
            self.theme_cls.primary_palette = paleta
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