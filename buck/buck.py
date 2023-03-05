import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Buck. Power supply', width=1280, height=720, resizable=False)
dpg.setup_dearpygui()


img_buck_width, img_buck_height, img_buck_channels, img_buck_data = dpg.load_image("img/buck.png")

def callback_button_calculate():
    print("Calculate......")
    dpg.set_value("p_out", 146.2)

with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=img_buck_width, height=img_buck_height, default_value=img_buck_data, tag="texture_buck")

with dpg.font_registry():
    default_font = dpg.add_font("couriernew.ttf", 14)
    second_font = dpg.add_font("couriernew.ttf", 20)

with dpg.window(tag="MainWindow"):
    dpg.bind_font(default_font)
    dpg.add_image("texture_buck", pos=[450,10])

    dpg.add_button(label="Calculate", width=200, height=40, pos=[1050, 630], tag="button_result", callback=callback_button_calculate)
    dpg.bind_item_font("button_result", second_font)
    
    dpg.add_drag_float(label="Vin (min), V", width=150, pos=[10, 10], tag="voltage_input_min", min_value=0.1, max_value=10000, default_value=15, format='%.1f')
    dpg.add_drag_float(label="Vin (max), V", width=150, pos=[10, 35], tag="voltage_input_max", min_value=0.1, max_value=10000, default_value=60, format='%.1f')
    dpg.add_drag_float(label="Vout, V", width=150, pos=[10, 60], tag="voltage_output", min_value=0.1, max_value=10000, default_value=12, format='%.2f')
    dpg.add_drag_float(label="Iout, A", width=150, pos=[10, 85], tag="input_output", min_value=0.1, max_value=10000, default_value=20, format='%.2f')
    dpg.add_drag_float(label="Fsw, kHz", width=150, pos=[10, 110], tag="frequency", min_value=0, max_value=10000, default_value=250, format='%.0f')
    dpg.add_drag_float(label="Ripple current, %", width=150, pos=[10, 135], tag="ripple_current", min_value=1, max_value=100, default_value=30, format='%.0f')
    dpg.add_drag_float(label="N phase", width=150, pos=[10, 160], tag="quantity_phase", min_value=1, max_value=256, default_value=1, format='%.0f')

    dpg.add_drag_float(label="Ripple Vin, mV", width=150, pos=[10, 220], tag="ripple_vin", min_value=1, max_value=10000, default_value=500, format='%.0f')
    dpg.add_drag_float(label="Ripple Vout, mV", width=150, pos=[10, 245], tag="ripple_vout", min_value=1, max_value=10000, default_value=25, format='%.0f')

    dpg.add_drag_float(label="I gate, A", width=150, pos=[10, 305], tag="i_gate_driver", min_value=0, max_value=100, default_value=2, format='%.1f')
    dpg.add_drag_float(label="Inductor DCR, mOhms", width=150, pos=[10, 330], tag="inductor_dcr", min_value=0, max_value=100000, default_value=3, format='%.1f')

    dpg.add_drag_float(label="VT1 Rds_on, mOhms", width=150, pos=[10, 390], tag="vt1_r_channel", min_value=0, max_value=10000, default_value=4, format='%.1f')
    dpg.add_drag_float(label="VT1 Qgs, nC", width=150, pos=[10, 415], tag="vt1_qgs", min_value=0, max_value=10000, default_value=2, format='%.1f')
    dpg.add_drag_float(label="VT1 Qgd, nC", width=150, pos=[10, 440], tag="vt1_qgd", min_value=0, max_value=10000, default_value=1, format='%.1f')
    dpg.add_drag_float(label="VT1 Qrr, nC", width=150, pos=[10, 465], tag="vt1_qrr", min_value=0, max_value=10000, default_value=4, format='%.1f')
    
    dpg.add_drag_float(label="VT2 Rds_on, mOhms", width=150, pos=[10, 525], tag="vt2_r_channel", min_value=0, max_value=10000, default_value=4, format='%.1f')
    dpg.add_drag_float(label="VT2 Qgs, nC", width=150, pos=[10, 550], tag="vt2_qgs", min_value=0, max_value=10000, default_value=2, format='%.1f')
    dpg.add_drag_float(label="VT2 Qgd, nC", width=150, pos=[10, 575], tag="vt2_qgd", min_value=0, max_value=10000, default_value=1, format='%.1f')
    dpg.add_drag_float(label="VT2 Qrr, nC", width=150, pos=[10, 600], tag="vt2_qrr", min_value=0, max_value=10000, default_value=4, format='%.1f')

    dpg.add_drag_float(label="Pout, W", width=150, pos=[450, 440], tag="p_out", min_value=0, max_value=50000, default_value=0, format='%.1f')
    dpg.add_drag_float(label="Efficiency, %", width=150, pos=[450, 465], tag="efficiency", min_value=0, max_value=100, format='%.1f')



dpg.show_viewport()
dpg.set_primary_window("MainWindow", True)
dpg.start_dearpygui()
dpg.destroy_context()

##########################################################################

'''
dpg.add_drag_int(label="test", width=200, tag="temp")



dpg.add_combo(items=['9600','19200','38400','57600','115200','250000','460800'], default_value="460800", label="Speed", width=120, tag="speed")

    with dpg.menu_bar():
        with dpg.menu(label="Files"):
            dpg.add_menu_item(label="Open")
            dpg.add_menu_item(label="Save")
            dpg.add_menu_item(label="Close")

    with dpg.menu_bar():
        with dpg.menu(label="Themes"):
            dpg.add_menu_item(label="Dark")
            dpg.add_menu_item(label="Light")
            dpg.add_menu_item(label="Classic")
'''