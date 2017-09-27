import re
def clearScintillaCallbacks():
    editor.clearCallbacks([SCINTILLANOTIFICATION.DOUBLECLICK, SCINTILLANOTIFICATION.INDICATORCLICK]) 
clearScintillaCallbacks()
    
def clearIndicators():
    text_end_position1 = editor1.getLength()
    text_end_position2 = editor2.getLength()
    editor1.setIndicatorCurrent(8)
    editor1.indicatorClearRange(0, text_end_position1)
    editor2.setIndicatorCurrent(8)
    editor2.indicatorClearRange(0, text_end_position2)

def toggleview():
    # 0 = main_view
    # 1 = second_view
    current_doc_index_main_view = notepad.getCurrentDocIndex(0)
    current_doc_index_second_view = notepad.getCurrentDocIndex(1)
    if notepad.getCurrentView() == 0:
        notepad.activateIndex(1, current_doc_index_second_view)
    else:
        notepad.activateIndex(0, current_doc_index_main_view)

def colorize():
    selected_text = editor.getSelText()
    clearIndicators()
    toggleview()
    matches = []
    editor.research('{0}'.format(selected_text), lambda m: matches.append(m.span(0)),re.IGNORECASE)
    for match in matches:
        editor.indicSetStyle(8,INDICATORSTYLE.ROUNDBOX)
        editor.indicSetFore(8,(117,217,117))
        editor.indicSetAlpha(8,255)
        editor.indicSetOutlineAlpha(8,255)
        editor.indicSetUnder(8,True)
        editor.setIndicatorCurrent(8)
        editor.indicatorFillRange(match[0], match[1] - match[0])
    toggleview()
    
def sci_callback_DOUBLECLICK(args):
    if editor2:
        colorize()
    else:
        clearScintillaCallbacks()

def sci_callback_INDICATORCLICK(args):
    clearIndicators()
editor.callback(sci_callback_DOUBLECLICK, [SCINTILLANOTIFICATION.DOUBLECLICK])
editor.callback(sci_callback_INDICATORCLICK, [SCINTILLANOTIFICATION.INDICATORCLICK])