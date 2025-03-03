from rhn_app.services.constants import *
import pandapipes as pp
import pandas as pd

def create_sources_from_df(df_heater, df_sink, df_connection, df_nodetype, net, junction_dict):
    e_flow_conv_ratio = (7 / 0.033 + 40.3 / 0.193) / 2  # = 210.4648
    t_out_c = 90
    t_out_k = t_out_c + 273.15
    source_flow_bar = 10
    pressure_lift = 3
    prod_multiplier = 1

    # Clean up column names
    df_connection['Start Node'] = df_connection['Start Node'].str.strip()
    df_connection['End Node'] = df_connection['End Node'].str.strip()

    for i in range(len(df_heater)):
        if str(df_heater.iloc[i, 0]) != "Ericsson":  # Ericsson special case below
            source_name = str(df_heater.iloc[i, 0])

            for j in range(len(df_connection)):
                start_node = str(df_connection.at[j, 'Start Node']).replace("Junction-", "Junction_")
                end_node = str(df_connection.at[j, 'End Node']).replace("Junction-", "Junction_")

                if start_node == source_name:
                    if end_node + "_supply" not in junction_dict or end_node + "_return" not in junction_dict:
                        print(f"Error: Junction {end_node} not found in junction_dict")
                        continue

                    source_flow = junction_dict[end_node + "_supply"]
                    source_return = junction_dict[end_node + "_return"]

                    pp.create_circ_pump_const_pressure(
                        net,
                        flow_junction=source_flow,
                        return_junction=source_return,
                        plift_bar=pressure_lift,
                        p_flow_bar=source_flow_bar,
                        mdot_flow_kg_per_s=pd.to_numeric(df_heater.iloc[i, 2]) / e_flow_conv_ratio,
                        t_flow_k=t_out_k,
                        name=source_name
                    )

                elif end_node == source_name:
                    if start_node + "_supply" not in junction_dict or start_node + "_return" not in junction_dict:
                        print(f"Error: Junction {start_node} not found in junction_dict")
                        continue

                    source_flow = junction_dict[start_node + "_supply"]
                    source_return = junction_dict[start_node + "_return"]

                    pp.create_circ_pump_const_pressure(
                        net,
                        flow_junction=source_flow,
                        return_junction=source_return,
                        plift_bar=pressure_lift,
                        p_flow_bar=source_flow_bar,
                        mdot_flow_kg_per_s=pd.to_numeric(df_heater.iloc[i, 2]) / e_flow_conv_ratio,
                        t_flow_k=t_out_k,
                        name=source_name
                    )

    # Ericsson special case: Ericsson has only return connections
    junction_dict['Ericsson_connection'] = pp.create_junction(
        net, pn_bar=net_return_p_bar, tfluid_k=t_net_return_init_k, name='Ericsson_connection'
    )
    pp.create_ext_grid(
        net,
        junction=junction_dict['Ericsson_connection'],
        p_bar=net_return_p_bar,
        t_k=t_net_return_init_k,
        name="Ericsson Ext. Grid"
    )

    # Tracker for Ericsson auxiliary junction connections
    e_pipe_tracker = 0

    for i in range(len(df_connection)):
        start_node = str(df_connection.at[i, 'Start Node']).replace("Junction-", "Junction_")
        end_node = str(df_connection.at[i, 'End Node']).replace("Junction-", "Junction_")

        try:
            if start_node == 'Ericsson':
                connection_name = junction_dict.get(end_node + "_return")
            elif end_node == 'Ericsson':
                connection_name = junction_dict.get(start_node + "_return")
            else:
                continue
        except KeyError:
            print(f"Error: Junction {start_node} or {end_node} not found in junction_dict")
            continue

        if connection_name is None:
            print(f"Error: Junction {start_node} or {end_node} not found in junction_dict")
            continue

        pp.create_pipe_from_parameters(
            net,
            from_junction=connection_name,
            to_junction=junction_dict['Ericsson_connection'],
            length_km=float(str(df_connection.at[i, 'Length [m]'])) / 1000,
            diameter_m=float(str(df_connection.at[i, 'Diameter [mm]'])) / 1000,
            k_mm=0.05,
            alpha_w_per_m2k=float(str(df_connection.at[i, 'Heat Transfer Coefficient [W/mK]'])),
            text_k=int(temp_ext_k),
            name='Pipe_E_' + str(e_pipe_tracker)
        )

        e_pipe_tracker += 1
