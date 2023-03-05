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

    dpg.add_drag_float(label="Ripple Vin, mV", width=150, pos=[10, 200], tag="ripple_vin", min_value=1, max_value=10000, default_value=500, format='%.0f')
    dpg.add_drag_float(label="Ripple Vout, mV", width=150, pos=[10, 225], tag="ripple_vout", min_value=1, max_value=10000, default_value=25, format='%.0f')

    dpg.add_drag_float(label="V gate, V", width=150, pos=[10, 265], tag="v_gate_driver", min_value=0, max_value=100, default_value=2, format='%.1f')
    dpg.add_drag_float(label="I gate, A", width=150, pos=[10, 290], tag="i_gate_driver", min_value=0, max_value=100, default_value=2, format='%.1f')
    dpg.add_drag_float(label="Inductor DCR, mOhms", width=150, pos=[10, 315], tag="inductor_dcr", min_value=0, max_value=100000, default_value=3, format='%.1f')

    dpg.add_drag_float(label="VT1 Rds_on, mOhms", width=150, pos=[10, 355], tag="vt1_r_channel", min_value=0, max_value=10000, default_value=4, format='%.1f')
    dpg.add_drag_float(label="VT1 Qgs, nC", width=150, pos=[10, 380], tag="vt1_qgs", min_value=0, max_value=10000, default_value=2, format='%.1f')
    dpg.add_drag_float(label="VT1 Qgd, nC", width=150, pos=[10, 405], tag="vt1_qgd", min_value=0, max_value=10000, default_value=1, format='%.1f')
    dpg.add_drag_float(label="VT1 Qrr, nC", width=150, pos=[10, 430], tag="vt1_qrr", min_value=0, max_value=10000, default_value=4, format='%.1f')
    dpg.add_drag_float(label="VT1 Qg, nC", width=150, pos=[10, 455], tag="vt1_qg", min_value=0, max_value=10000, default_value=4, format='%.1f')
    
    dpg.add_drag_float(label="VT2 Rds_on, mOhms", width=150, pos=[10, 495], tag="vt2_r_channel", min_value=0, max_value=10000, default_value=4, format='%.1f')
    dpg.add_drag_float(label="VT2 Qgs, nC", width=150, pos=[10, 520], tag="vt2_qgs", min_value=0, max_value=10000, default_value=2, format='%.1f')
    dpg.add_drag_float(label="VT2 Qgd, nC", width=150, pos=[10, 545], tag="vt2_qgd", min_value=0, max_value=10000, default_value=1, format='%.1f')
    dpg.add_drag_float(label="VT2 Qrr, nC", width=150, pos=[10, 570], tag="vt2_qrr", min_value=0, max_value=10000, default_value=4, format='%.1f')
    dpg.add_drag_float(label="VT2 Qg, nC", width=150, pos=[10, 595], tag="vt2_qg", min_value=0, max_value=10000, default_value=4, format='%.1f')

    dpg.add_drag_float(label="Pout, W", width=150, pos=[450, 430], tag="p_out", min_value=0, max_value=50000, default_value=0, format='%.1f')
    dpg.add_drag_float(label="Efficiency, %", width=150, pos=[450, 455], tag="efficiency", min_value=0, max_value=100, format='%.1f')

    dpg.add_drag_float(label="VT1 loss, W", width=150, pos=[450, 495], tag="vt1_loss", min_value=0, max_value=100, format='%.1f')
    dpg.add_drag_float(label="VT2 loss, W", width=150, pos=[450, 520], tag="vt2_loss", min_value=0, max_value=100, format='%.1f')
    dpg.add_drag_float(label="Inductor loss, W", width=150, pos=[450, 545], tag="inductor_loss", min_value=0, max_value=100, format='%.1f')
    dpg.add_drag_float(label="Capacitor loss, W", width=150, pos=[450, 570], tag="cout_loss", min_value=0, max_value=100, format='%.1f')
    dpg.add_drag_float(label="Total loss, W", width=150, pos=[450, 595], tag="total_loss", min_value=0, max_value=100, format='%.1f')

    dpg.add_drag_float(label="L (min), uH", width=150, pos=[820, 430], tag="l_min", min_value=0, max_value=50000, default_value=0, format='%.1f')
    dpg.add_drag_float(label="L (nom), uH", width=150, pos=[820, 455], tag="l_nom", min_value=0, max_value=50000, default_value=0, format='%.1f')

    dpg.add_drag_float(label="Cin, uF", width=150, pos=[820, 495], tag="c_in", min_value=0, max_value=50000, default_value=0, format='%.1f')
    dpg.add_drag_float(label="Cin (ripple), A", width=150, pos=[820, 520], tag="i_ripple_cin", min_value=0, max_value=1000, default_value=0, format='%.1f')

    dpg.add_drag_float(label="Cout, uF", width=150, pos=[820, 570], tag="c_out", min_value=0, max_value=50000, default_value=0, format='%.1f')
    dpg.add_drag_float(label="ESR (min), mOhms", width=150, pos=[820, 595], tag="esr", min_value=0, max_value=50000, default_value=0, format='%.1f')

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