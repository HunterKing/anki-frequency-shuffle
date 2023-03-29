from anki import hooks
from ._version import __version__

# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect, tooltip
# import all of the Qt GUI library
from aqt.qt import *
from anki._backend import RustBackend as rs
import random


# Fetch the config values.
config = mw.addonManager.getConfig(__name__)

def shuffleFreq() -> None:
    target_tag = "tag:" + config['target_tag']
    target_field = config['target_field']
    max_rank = config['highest_ranking']
    min_rank = config['lowest_ranking']

    data = mw.col.find_cards(target_tag)
    for card in data:
        target_card = mw.col.get_card(card)
        note = target_card.note()
        note[target_field] = str(random.randint(max_rank, min_rank))
        mw.col.update_note(note)
    
    tooltip(
        (f"Finished randomizing {len(data)} cards in {config['target_tag']}")
    )

# create a new menu item, "test"
action = QAction("Generate Random Frequencies", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, shuffleFreq)
# and add it to the tools menu
mw.form.menuTools.addAction(action)