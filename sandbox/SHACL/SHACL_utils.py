from rdflib import Graph
from pyshacl import validate
from glob import glob
import os

from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def parse_folder_to_single_graph(path_to_folder: str, file_extension: str, recurse: bool = True) -> Graph:
    output = Graph()
    files = [f for f in glob(f"{path_to_folder}/**/*.{file_extension}", recursive=recurse) if os.path.isfile(f)]
    print(f"Parsing {len(files)} {file_extension} files")
    for filename in files:
        print(f"Parsing {filename}")
        output.parse(filename)
    return output


def plot_graph(graph: Graph) -> None:
    G = rdflib_to_networkx_multidigraph(graph)

    # Plot Networkx instance of RDF Graph
    pos = nx.spring_layout(G, scale=2)
    edge_labels = nx.get_edge_attributes(G, 'r')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, with_labels=True)


    plt.show()
    return


def search_df_word(dataframe: pd.DataFrame, keyword: str) -> pd.DataFrame:
    mask = dataframe.apply(lambda row: row.astype(str).str.contains(keyword, case=False)).any(axis=1)
    filtered_dataframe = dataframe[mask]
    return filtered_dataframe


def drop_nan_cols(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.dropna(axis=1, how='all')


def drop_nan_rows_with_keyword(dataframe: pd.DataFrame, keyword: str) -> pd.DataFrame:
    # Get the columns containing the keyword
    columns_with_keyword = [col for col in dataframe.columns if keyword in col]
    # Drop rows with NaN values in columns containing the keyword
    dataframe = dataframe.dropna(subset=columns_with_keyword, thresh=1)
    return dataframe


def column_value_counts(dataframe: pd.DataFrame, keyword: str) -> pd.DataFrame:
    value_counts = dataframe[keyword].value_counts()
    return value_counts


def plot_value_counts_pie_chart(value_counts: pd.DataFrame) -> None:
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.0f')
    plt.title(f'Value Counts for {value_counts.index.name}')
    plt.show()
    return



def main() -> None:
    # Person Example
    # equipment = parse_folder_to_single_graph("example_person\data", "rdf")
    # shacl = parse_folder_to_single_graph("example_person\shapes", "rdf")

    equipment = parse_folder_to_single_graph("cgmes_threedotzero", "xml")
    shacl = parse_folder_to_single_graph("SHACL", "rdf")
    plot_graph(equipment)
    r = validate(data_graph=equipment, shacl_graph=shacl)
    conforms, results_graph, results_text = r
    print(results_text)


if __name__ == "__main__":
    main()
    print("Done")