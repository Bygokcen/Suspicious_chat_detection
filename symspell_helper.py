from symspellpy.symspellpy import SymSpell
import importlib.resources as pkg_resources

# SymSpell initializasyonu
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Frekans sözlüğünü yükle
dictionary_path = pkg_resources.path("symspellpy", "frequency_dictionary_en_82_765.txt")
bigram_path = pkg_resources.path("symspellpy", "frequency_bigramdictionary_en_243_342.txt")

with dictionary_path as dp, bigram_path as bp:
    sym_spell.load_dictionary(dp, term_index=0, count_index=1)
    sym_spell.load_bigram_dictionary(bp, term_index=0, count_index=2)

def correct_text(text):
    suggestions = sym_spell.lookup_compound(text, max_edit_distance=2)
    return suggestions[0].term if suggestions else text
