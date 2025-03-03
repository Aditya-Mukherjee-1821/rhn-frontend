from rhn_app.services.constants import *
import pandapipes as pp

def create_junctions_from_df(df_heater, df_sink, df_connection, df_nodetype, net, junction_dict):
    # Get number of nodes from dataframe
    num_nodes = len(df_nodetype)

    # tracker tracks number of junctions created
    junction_tracker = 0

    # Iterate over all nodes to find and create junctions
    for i in range(num_nodes):
        if df_nodetype.at[i, 'Node Type'] == "Junction":
            
            # Replace dashes with underscores to conform with Python naming
            junction_name = str(df_nodetype.at[i, 'Name']).replace("Junction-", "Junction_")
            
            junction_pos_x = float(df_nodetype.at[i, 'X-Coordinate'])
            junction_pos_y = float(df_nodetype.at[i, 'Y-Coordinate'])
            junction_pos_flow = (junction_pos_x, junction_pos_y)
            junction_pos_return = (junction_pos_x, junction_pos_y - 100)

            # Define supply and return flow network junctions
            supply_junction = pp.create_junction(net,
                                                 pn_bar=net_flow_p_bar,
                                                 tfluid_k=t_net_flow_init_k,
                                                 geodata=junction_pos_flow,
                                                 name=junction_name + '_supply')
            return_junction = pp.create_junction(net,
                                                 pn_bar=net_return_p_bar,
                                                 tfluid_k=t_net_return_init_k,
                                                 geodata=junction_pos_return,
                                                 name=junction_name + '_return')

            # Store the junctions in the passed dictionary
            junction_dict[junction_name + '_supply'] = supply_junction
            junction_dict[junction_name + '_return'] = return_junction

            junction_tracker += 2
