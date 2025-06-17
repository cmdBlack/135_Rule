

class DataFilter:
    def __init__(self):
        self.SYNOPTIC_STATIONS = ['98134', '98223', '98232', '98325', '98328', '98336',
                                 '98429', '98430', '98431', '98440', '98444', '98526',
                                 '98531', '98536', '98543', '98618', '98630', '98646',
                                 '98653', '98741', '98753', '98755', '98836', '98132',
                                 '98133', '98222', '98233', '98324', '98327', '98334',
                                 '98426', '98427', '98428', '98432', '98433', '98434',
                                 '98435', '98446', '98538', '98546', '98548', '98553',
                                 '98558', '98642', '98644', '98648', '98746', '98751',
                                 '98752', '98851', '98329', '98332', '98422', '98425',
                                 '98437', '98545', '98550', '98602', '98643', '98748']
    def filter_synoptic_data(self):
        with open("SMPH01_RPMM_150000.txt") as data:
            for line in data:
                if str(line[0:5]) in self.SYNOPTIC_STATIONS:
                    with open("Synoptic_Observations.txt", "a") as new_data:
                        new_data.write(line)

    def filter_with_cloud_group(self):
        with open("Synoptic_Observations.txt") as data:
            for line in data:
                data_per_station = line.split(" ")
                try:
                    index_guide = data_per_station.index("333")
                    print(index_guide)
                except ValueError:
                    pass







