import json
import pandas as pd
import pandapipes as pp
import numpy as np
import pandapipes.plotting as plot
from rhn_app.services.create_junctions import create_junctions_from_df
from rhn_app.services.create_sources import create_sources_from_df
from rhn_app.services.create_sinks import create_sinks_from_df
from rhn_app.services.create_connections import create_connections_from_df

def calc_pipeflow_from_df(df_heater, df_sink, df_connection, df_nodetype):

    # Prepare blank network for elements
    print("Creating empty network...")
    net = pp.create_empty_network(name="Data", fluid="water")
    
    # Dictionary to store junction references
    junction_dict = {}

    # create junctions
    print("Creating supply and return junctions...")
    create_junctions_from_df(df_heater, df_sink, df_connection, df_nodetype, net, junction_dict)

    # create sources
    print("Creating sources...")
    create_sources_from_df(df_heater, df_sink, df_connection, df_nodetype, net, junction_dict)

    # create sinks
    print("Creating sinks...")
    create_sinks_from_df(df_heater, df_sink, df_connection, df_nodetype, net, junction_dict)

    # create connections
    print("Creating connections...")
    create_connections_from_df(df_heater, df_sink, df_connection, df_nodetype, net, junction_dict)

    # Run the pipeflow simulation
    print("Running pipeflow simulation...")
    pp.pipeflow(net, mode="bidirectional")

    # Extract relevant mass flow rate values
    pipe_flows = {
        "mdot_from": list(net.res_pipe["mdot_from_kg_per_s"]),
        "pipe_names": list(net.pipe.name),
    }

    # Convert to JSON string
    response = json.dumps(pipe_flows)

    return response
