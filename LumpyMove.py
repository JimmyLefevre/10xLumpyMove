#------------------------------------------------------------------------
# Commands:
#   LumpyMoveToPreviousWord
#   LumpyMoveToNextWord
#   LumpyMoveToPreviousParagraph
#   LumpyMoveToNextParagraph
#   LumpySelectToPreviousWord
#   LumpySelectToNextWord
#   LumpySelectToPreviousParagraph
#   LumpySelectToNextParagraph
#------------------------------------------------------------------------
import N10X

def _LumpyIsIdentCharacter(c):
    return c.isalnum() or c == '_'

def _LumpyIsNewlineCharacter(c):
    return c == '\n' or c == '\r'

def _LumpyPrevParagraphY(cursor_index):
    _, y = N10X.Editor.GetCursorPos(cursor_index)
    while y > 0 and N10X.Editor.GetLine(y).isspace():
        y -= 1
    while y > 0 and not N10X.Editor.GetLine(y).isspace():
        y -= 1
    return y

def _LumpyNextParagraphY(cursor_index):
    last_line = N10X.Editor.GetLineCount() - 1
    _, y = N10X.Editor.GetCursorPos(cursor_index)
    while y < last_line and N10X.Editor.GetLine(y).isspace():
        y += 1
    while y < last_line and not N10X.Editor.GetLine(y).isspace():
        y += 1
    return y

def _LumpyUpdateSelection(cursor_index, new_x, new_y, forward):
    orig_x, orig_y = N10X.Editor.GetCursorPos(cursor_index)
    sel_p0, sel_p1 = N10X.Editor.GetCursorSelection(cursor_index)
    if not forward:
        sel_p0, sel_p1 = sel_p1, sel_p0
    if (orig_x == sel_p0[0] and orig_y == sel_p0[1]):
        N10X.Editor.SetSelection(sel_p1, (new_x, new_y), cursor_index)
    else:
        N10X.Editor.SetSelection(sel_p0, (new_x, new_y), cursor_index)

def _LumpyPrevWordXY(cursor_index):
    x, y = N10X.Editor.GetCursorPos(cursor_index)
    line = N10X.Editor.GetLine(y)
    while x > 0 and not _LumpyIsIdentCharacter(line[x-1]):
        x -= 1
    if x == 0:
        if y > 0:
            y -= 1
            line = N10X.Editor.GetLine(y)
            x = len(line) - 1
            while x > 0 and _LumpyIsNewlineCharacter(line[x-1]):
                x -= 1
    else:
        while x > 0 and _LumpyIsIdentCharacter(line[x-1]):
            x -= 1
    return x, y

def _LumpyNextWordXY(cursor_index):
    x, y = N10X.Editor.GetCursorPos(cursor_index)
    line = N10X.Editor.GetLine(y)
    len_line = len(line)
    while x < len_line and _LumpyIsNewlineCharacter(line[x]):
        x += 1
    if x == len_line and (y + 1) < N10X.Editor.GetLineCount():
        y += 1
        x = 0
    else:
        while x < len_line and _LumpyIsIdentCharacter(line[x]):
            x += 1
        while x < len_line and not _LumpyIsIdentCharacter(line[x]):
            x += 1
        while x > 0 and _LumpyIsNewlineCharacter(line[x-1]):
            x -= 1
    return x, y

def _LumpyPrev(extend_selection, paragraph):
    scroll_line = N10X.Editor.GetScrollLine()
    for cursor_index in range(N10X.Editor.GetCursorCount()):
        target_x, target_y = _LumpyPrevWordXY(cursor_index) if not paragraph else (0, _LumpyPrevParagraphY(cursor_index))
        if extend_selection:
            _LumpyUpdateSelection(cursor_index, target_x, target_y, False)
        else:
            N10X.Editor.SetCursorPos((target_x, target_y), cursor_index)
        if cursor_index == 0:
          N10X.Editor.SetScrollLine(min(scroll_line, target_y))

def _LumpyNext(extend_selection, paragraph):
    scroll_line = N10X.Editor.GetScrollLine()
    visible_line_count = N10X.Editor.GetVisibleLineCount()
    for cursor_index in range(N10X.Editor.GetCursorCount()):
        target_x, target_y = _LumpyNextWordXY(cursor_index) if not paragraph else (0, _LumpyNextParagraphY(cursor_index))
        if extend_selection:
            _LumpyUpdateSelection(cursor_index, target_x, target_y, True)
        else:
            N10X.Editor.SetCursorPos((target_x, target_y), cursor_index)
        if cursor_index == 0:
            N10X.Editor.SetScrollLine(max(scroll_line, target_y - visible_line_count + 2))

def LumpyMoveToPreviousParagraph():
    _LumpyPrev(False, True)

def LumpyMoveToNextParagraph():
    _LumpyNext(False, True)

def LumpySelectToPreviousParagraph():
    _LumpyPrev(True, True)

def LumpySelectToNextParagraph():
    _LumpyNext(True, True)

def LumpyMoveToPreviousWord():
    _LumpyPrev(False, False)

def LumpyMoveToNextWord():
    _LumpyNext(False, False)

def LumpySelectToPreviousWord():
    _LumpyPrev(True, False)

def LumpySelectToNextWord():
    _LumpyNext(True, False)
