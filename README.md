# Cyclic Space
 
A type of cellular automata called cyclic space was discovered by David Griffeath of the University of Wisconsin at Madison in 1990. Cyclic Space is described in  [The Magic Machine A Handbook of Computer Sorcery](https://www.amazon.com/Magic-Machine-Handbook-Computer-Sorcery/dp/0716721252/ref=sr_1_1?crid=2N7PKFJOVUI49&dib=eyJ2IjoiMSJ9.NTLdsrNDLEk1x3LeOBQyww.nWfU52fpvLMdRJsWOJv1BBOrNoiGSeZ0rMMVjCoi1Ns&dib_tag=se&keywords=the+magic+machine+a.k.+dewdney&qid=1729741595&sprefix=the+magic+machine+a.k.+dewdnet%2Caps%2C169&sr=8-1) by A.K. Dewdeny.
 This page is a cyclic space simulator I wrote to explore these automata and a mimi project to brush up on my Python coding and to try out [streamlit](https://streamlit.io/) . 
 Cyclic Space is a grid of cells where each cell has one of n possible values, numbered 0 through n-1. Cyclic spaces are most interesting when n is fairly small. In each generation any cell with a value k will eat any neighboring cell that has value k-1. Cells is the 0 state will eat cells in the n-1 state thus allowing loops of state changes.  Choose any image to load. You can then choose the number of colors to color-reduce the image into an image with n colors. The cyclic algorithm will then run successive generations of the cyclic space. You can also scale the image. Smaller images animate faster. Watch for the "Demons" of cyclic space to appear. These crystal seeds will continue to grow. 
 
 
## Link to App
 
 
TODO: **Add link to Streamlit Community hosted App**

## Usage
 
TODO: Write usage instructions
 
## Contributing
 
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
 
## History
 
Version 0.1 (2024-10-31) - adding load image by url
 
## Credits
 
Software Artist - David S Maynard (@dmaynard)

## License
 
The MIT License (MIT)

Copyright (c) 2024 David S Maynard

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.