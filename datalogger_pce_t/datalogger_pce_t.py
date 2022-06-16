import pandas as pd
import numpy as np

class DataLogger:
    def __init__(self, file, delimiter=";"):
        self.datasets = None
        self.start_times = None
        self.end_times = None
        self.delimiter = delimiter
        self._read_datasets_from_file(file)
        self.get_metadata()

    def _read_datasets_from_file(self, file):
        self.datasets = []
        data = pd.read_csv(file, decimal=',', header=0, comment='#', delimiter=self.delimiter)
        sep_indices = data.index[data['Place'] == 'Place'].tolist()
        sep_indices.insert(0,0)
        sep_indices.append(len(data))
        for i in range(len(sep_indices)-1):
            dataset = data.iloc[sep_indices[i]+1 : sep_indices[i + 1]].copy()
            dataset = dataset.astype({"Value": float,
                                    "Value.1": float,
                                    "Value.2": float,
                                    "Value.3": float,
                                    "Value.4": float,
                                    "Value.5": float,
                                    "Value.6": float,
                                    "Value.7": float,
                                    "Value.8": float,
                                    "Value.9": float,
                                    "Value.10": float,
                                    "Value.11": float,
                                      })
            dataset["DateTime"] = pd.to_datetime(dataset["Date"] + ' ' + dataset["Time"])
            dataset["ExpTime"] = (dataset["DateTime"] - dataset["DateTime"].iloc[0])// np.timedelta64(1, 's')
            dataset.rename(columns={"Value": "Channel_1",
                                    "Value.1": "Channel_2",
                                    "Value.2": "Channel_3",
                                    "Value.3": "Channel_4",
                                    "Value.4": "Channel_5",
                                    "Value.5": "Channel_6",
                                    "Value.6": "Channel_7",
                                    "Value.7": "Channel_8",
                                    "Value.8": "Channel_9",
                                    "Value.9": "Channel_10",
                                    "Value.10": "Channel_11",
                                    "Value.11": "Channel_12"
                                    }, inplace=True)
            dataset.rename(columns={"Unit": "Unit_1",
                                    "Unit.1": "Unit_2",
                                    "Unit.2": "Unit_3",
                                    "Unit.3": "Unit_4",
                                    "Unit.4": "Unit_5",
                                    "Unit.5": "Unit_6",
                                    "Unit.6": "Unit_7",
                                    "Unit.7": "Unit_8",
                                    "Unit.8": "Unit_9",
                                    "Unit.9": "Unit_10",
                                    "Unit.10": "Unit_11",
                                    "Unit.11": "Unit_12"
                                    }, inplace=True)
            self.datasets.append(dataset)

    def get_metadata(self):
        self.start_times = []
        self.end_times = []
        for dataset in self.datasets:
            self.start_times.append(dataset['DateTime'].iloc[0])
            self.end_times.append(dataset['DateTime'].iloc[-1])

    def show_info(self):
        for i, (start_time, end_time), in enumerate(zip(self.start_times, self.end_times)):
            print(f"Dataset {i}")
            print(f"Date: {start_time.strftime('%d.%m.%Y')}")
            print(f"Start Time: {start_time.strftime('%H:%M')}")
            print(f"End Time: {end_time.strftime('%H:%M')}")
            print(f"Duration: {pd.Timedelta(end_time-start_time).seconds} s")
            print("----------------------")
    def get_data(self, dataset_index):
        return self.datasets[dataset_index]