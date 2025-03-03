from rhn_app.services.constants import *
import pandapipes as pp
import pandas as pd

def create_connections_from_df(df_heater, df_sink, df_connection, df_nodetype, net, junction_dict):
    # Concatenate source and sink names into a single NumPy array
    np_heaters_sinks = pd.concat([df_heater[['Name']], df_sink[['Name']]]).to_numpy()
    
    pipe_tracker = 0  # Initialize pipe tracker

    for i in range(len(df_connection)):
        
        pipe_get = str(df_connection.at[i, 'Name']).replace("-", "_")

        start_node = str(df_connection.at[i, 'Start Node'])
        end_node = str(df_connection.at[i, 'End Node'])

        supply_line = str(df_connection.at[i, 'Has Supply Line']) == 'True'
        return_line = str(df_connection.at[i, 'Has Return Line']) == 'True'

        # Exclude source and sink node connections (defined earlier)
        if start_node not in np_heaters_sinks and end_node not in np_heaters_sinks:
                
            # Create supply line pipe
            if supply_line:
                key_from = start_node.replace("Junction-", "Junction_") + '_supply'
                key_to = end_node.replace("Junction-", "Junction_") + '_supply'

                if key_from in junction_dict and key_to in junction_dict:
                    pp.create_pipe_from_parameters(
                        net,
                        from_junction=junction_dict[key_from],
                        to_junction=junction_dict[key_to],
                        length_km=float(df_connection.at[i, 'Length [m]']) / 1000,
                        diameter_m=float(df_connection.at[i, 'Diameter [mm]']) / 1000,
                        k_mm=.05,
                        u_w_per_m2k=float(df_connection.at[i, 'Heat Transfer Coefficient [W/mK]']),  # W/mK from raw data
                        sections=5,
                        text_k=int(temp_ext_k),
                        name=pipe_get + '_supply'
                    )
                    pipe_tracker += 1
                else:
                    print(f"Warning: Supply junctions {key_from} or {key_to} not found in junction_dict.")

            # Create return line pipe
            if return_line:
                key_from = end_node.replace("Junction-", "Junction_") + '_return'
                key_to = start_node.replace("Junction-", "Junction_") + '_return'

                if key_from in junction_dict and key_to in junction_dict:
                    pp.create_pipe_from_parameters(
                        net,
                        from_junction=junction_dict[key_from],
                        to_junction=junction_dict[key_to],
                        length_km=float(df_connection.at[i, 'Length [m]']) / 1000,
                        diameter_m=float(df_connection.at[i, 'Diameter [mm]']) / 1000,
                        k_mm=.05,
                        u_w_per_m2k=float(df_connection.at[i, 'Heat Transfer Coefficient [W/mK]']),  # W/mK from raw data
                        sections=5,
                        text_k=int(temp_ext_k),
                        name=pipe_get + '_return'
                    )
                    pipe_tracker += 1
                else:
                    print(f"Warning: Return junctions {key_from} or {key_to} not found in junction_dict.")
