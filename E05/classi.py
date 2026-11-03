import numpy as np

class PET:
    def __init__(self,raggio_anello,numero_pixel,ris_temporale_ns):
        self.raggio_anello = raggio_anello
        self.numero_pixel = numero_pixel
        self.ris_temporale_ns = ris_temporale_ns
        
    def __lt__(self,other):
            return self.raggio_anello < other.raggio_anello
    
    def __gt__(self,other):
	    return self.raggio_anello > other.raggio_anello