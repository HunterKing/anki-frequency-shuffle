from anki import hooks
from ._version import __version__

# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
from anki._backend import RustBackend as rs
import random

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window

    ## Create our own category of deck.
    #data = mw.col.decks.all_config()

    ## Get review time today for all decks.
    #data = mw.col.studied_today()

    ## Get review time today for arbitrary card.
    # data =

    ## Get list of new cards today.
    data = mw.col.decks.all_names_and_ids()
    # "Japanese": 1636743027696
    # data = mw.col.find_cards("is:learn")
    # data = mw.col.get_card(1675883008174).due
    data = mw.col.find_cards("tag:Structure")
    for card in data:
        target_card = mw.col.get_card(card)
        note = target_card.note()
        note['Frequency'] = str(random.randint(1000, 2000))
        mw.col.update_note(note)

    # 1670458105420, 1675883008174

    ## Get list of review cards today.

    ## Get list of new cards yesterday (or before)?
    ## Get list of reviewed cards yesterday (or before)?

    # show a message box
    showInfo("%s" % data)

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)