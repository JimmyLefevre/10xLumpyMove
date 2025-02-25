# 10xLumpyMove
Lumpier cursor movement for the 10x editor

This exports 9 commands you can use:
##### `LumpyMoveToPreviousWord`, `LumpyMoveToNextWord`, `LumpySelectToPreviousWord`, `LumpySelectToNextWord`

![20250224_031343](https://github.com/user-attachments/assets/b375b4fc-fe98-46e1-9cfe-e8579884e528)

Movement by word is Delphi-like. It will jump to the start of the previous/next word (ie. string of letters/digits/underscores), with one additional stop at line breaks.
`LumpyDeleteWord` uses the same logic.

##### `LumpyMoveToPreviousParagraph`, `LumpyMoveToNextParagraph`, `LumpySelectToPreviousParagraph`, `LumpySelectToNextParagraph`

![20250224_031034](https://github.com/user-attachments/assets/f280d605-bcf2-496e-8cb1-26347e97b83d)

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
Importantly, it will skip over multiple blank lines in a row.
