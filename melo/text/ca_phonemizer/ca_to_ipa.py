from .cleaner import catalan_cleaners
from .gruut_wrapper import Gruut

def ca2ipa(text):
    e = Gruut(language="ca-es", keep_puncs=True, keep_stress=True, use_espeak_phonemes=True)
    # text = catalan_cleaners(text)
    phonemes = e.phonemize(text, separator="")
    return phonemes


if __name__ == '__main__':
  print(ca2ipa("Miquel Martí i Pol fou un poeta, escriptor i traductor català, dels més populars del segle xx. És l'autor d'un dels llibres poètics més venuts de la literatura catalana, Estimada Marta"))