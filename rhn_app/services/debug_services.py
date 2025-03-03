# while debugging remove any parameters from extract_and_modify_data

from calc_pipeflow import calc_pipeflow_from_df
from data_processor import extract_and_modify_data

df_heater, df_sink, df_connection, df_nodetype = extract_and_modify_data()
calc_pipeflow_from_df(df_heater, df_sink, df_connection, df_nodetype)