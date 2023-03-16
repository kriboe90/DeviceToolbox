import pandas as pd

class LEDSpectrum:
    def __init__(self):
        self.data = None
        self.spectrum = None
        self.sample_names = None

    def read_data(self, file):
        ''''
        read spectrum txt as DataFrame
        '''
        self.data = pd.read_csv(file, sep='\t', index_col=0, encoding = 'unicode_escape')
        spectrum_start = self.data.index.get_loc('wavelength /nm') + 1
        self.spectrum = self.data[spectrum_start:spectrum_start+471].apply(pd.to_numeric)
        self.sample_names = self.data.loc['comment']
        self.spectrum.columns = self.sample_names
        self.spectrum.index = self.spectrum.index.astype('float')
    def get_spectrum(self, filter=None):
        if filter:
            return self.spectrum.filter(regex=filter, axis=1)
        return self.spectrum

    def get_peak_wl(self, filter=None):
        peak_wl = self.data.loc['peak wavelength'].apply(pd.to_numeric)
        peak_wl.index = self.sample_names
        if filter:
            return peak_wl.filter(regex=filter, axis=0)
        return peak_wl

    def get_peak_power(self, filter=None):
        peak_power = self.data.loc['peak power'].apply(pd.to_numeric)
        peak_power.index = self.sample_names
        if filter:
            return peak_power.filter(regex=filter, axis=0)
        return peak_power

    def get_num_leds(self):
        return self.sample_names.str.findall(pat="\.*LED_\d*").apply(', '.join).drop_duplicates().count()


    def get_num_samples(self):
        return self.spectrum.shape[1]

    def get_num_runs(self):
        return self.sample_names.str.findall(pat="\.*Run_\d*").apply(', '.join).drop_duplicates().count()
