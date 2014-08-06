from gi.repository import GObject, Gtk, Gedit



UI_XML = """<ui>
<menubar name="MenuBar">
  <placeholder name="ExtraMenu_3">
    <menu name="SQLMenu" action="SQL">
      <menuitem action="NewDataBase"/>
      <menuitem action="CreateTable"/>
    </menu>
  </placeholder>
</menubar>
</ui>"""



class SQLCommand(GObject.Object, Gedit.WindowActivatable):

    __gtype_name__ = "ExamplePlugin04"

    window = GObject.property(type=Gedit.Window)

  

    def __init__(self):

        GObject.Object.__init__(self)



    def _add_ui(self):

        manager = self.window.get_ui_manager()

        self._actions = Gtk.ActionGroup("Example04Actions")

        self._actions.add_actions([
            ('SQL', None, "_SQLCommand", None, None, None), 
            ('NewDataBase', None, "Create Data Base",None, None,self.create_database),
            ('CreateTable', None, "Create Data Base",None, None,self.create_table),
        ])

        manager.insert_action_group(self._actions)

        self._ui_merge_id = manager.add_ui_from_string(UI_XML)

        manager.ensure_update()

    

    def do_activate(self):

        self._add_ui()



    def do_deactivate(self):

        self._remove_ui()



    def do_update_state(self):

        pass



    def create_database(self, action, data=None):

        view = self.window.get_active_view()

        if view:

            view.get_buffer().insert_at_cursor("Hola mundo!!")


    def create_table(self, action, data=None):

        view = self.window.get_active_view()

        if view:

            view.get_buffer().insert_at_cursor("Creando una tabla mysql")


    def _remove_ui(self):

        manager = self.window.get_ui_manager()

        manager.remove_ui(self._ui_merge_id)

        manager.remove_action_group(self._actions)

        manager.ensure_update()

