from rhn_app.services.constants import *
import pandapipes as pp
import pandas as pd

def create_sinks_from_df(df_heater, df_sink, df_connection, df_nodetype, net, junction_dict):
    t_return_c = t_net_return_init_c + 5
    t_return_k = t_return_c + 273.15
    num_sinks = len(df_sink)
    num_connections = len(df_connection)
    sink_tracker = 0

    for i in range(num_sinks):
        sink_get = str(df_sink.at[i, 'Name'])

        for j in range(num_sinks):
            if df_sink.at[j, 'Name'] == sink_get:
                sink_type = str(df_sink.at[j, 'Category'])
                sink_priority = int(str(df_sink.at[j, 'Priority']))
                sink_demand_kW = float(str(df_sink.at[j, 'Base Demand [kW]']))
                mdot_kg_per_s_demand = float(str(df_sink.at[j, 'Base Demand [kg/s]']))
                sink_x = float(str(df_sink.at[j, 'X-Coordinate']))
                sink_y = float(str(df_sink.at[j, 'Y-Coordinate']))

        # Get connecting junction and pipe diameter
        for k in range(num_connections):
            if df_connection.at[k, "End Node"] == sink_get:
                key_supply = str(df_connection.at[k, 'Start Node']).replace("Junction-", "Junction_") + '_supply'
                key_return = str(df_connection.at[k, 'Start Node']).replace("Junction-", "Junction_") + '_return'
            elif df_connection.at[k, "Start Node"] == sink_get:
                key_supply = str(df_connection.at[k, 'End Node']).replace("Junction-", "Junction_") + '_supply'
                key_return = str(df_connection.at[k, 'End Node']).replace("Junction-", "Junction_") + '_return'
            else:
                continue

            # Fetch junctions from junction_dict
            sink_source = junction_dict.get(key_supply, None)
            sink_return = junction_dict.get(key_return, None)

            if sink_source is None or sink_return is None:
                print(f"Warning: {key_supply} or {key_return} not found in junction_dict. Skipping sink {sink_get}.")
                continue

            connection_d_mm = float(str(df_connection.at[k, 'Diameter [mm]']))
            mdot_kg_per_s_capacity = float(str(df_connection.at[k, 'Capacity [kg/s]']))

            sink_name = sink_get.replace("Junction-", "Sink_")

            # Define sink
            pp.create_heat_consumer(net,
                                    from_junction=sink_source,
                                    to_junction=sink_return,
                                    diameter_m=connection_d_mm / 1000,
                                    qext_w=sink_demand_kW * 1000,
                                    controlled_mdot_kg_per_s=mdot_kg_per_s_demand,
                                    name=sink_name, type=sink_type,
                                    x=sink_x, y=sink_y)

            sink_tracker += 1
