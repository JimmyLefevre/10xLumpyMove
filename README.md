# 10xLumpyMove
Lumpier cursor movement for the 10x editor

This exports 8 commands you can use:
##### `LumpyMoveToPreviousWord`, `LumpyMoveToNextWord`, `LumpySelectToPreviousWord`, `LumpySelectToNextWord`
Movement by word is Delphi-like. It will jump to the start of the previous/next word (ie. string of letters/digits/underscores), with one additional stop at line breaks.
##### `LumpyMoveToPreviousParagraph`, `LumpyMoveToNextParagraph`, `LumpySelectToPreviousParagraph`, `LumpySelectToNextParagraph`
Movement by paragraph is similar to Vim `{` `}`, or to the following VSCode command:
  ```json
  {
    "command": "cursorMove",
    "args": {
      "by": "line",
      "to": "prevBlankLine", // or nextBlankLine
    }
  }
  ```
Importantly, it will skip over multiple blank lines.
