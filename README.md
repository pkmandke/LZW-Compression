# LZW compression of utf-8 text files

This repository studies the variability of the compression ratio of utf-8 text files. The files, however, are not general text files but synthetic ones. More specifically, each file contains characters sampled from a specific probability distribution function. As of now, 4 probability distribution functions have being targeted:

* Poisson
* Gaussian
* Uniform
* Exponential

The [lzw](https://github.com/pytholic97/LZW-Text-File-Compression) package is used to achieve the compression and decompression of the text files.


# Author

[Prathamesh Mandke](https://www.linkedin.com/in/prathamesh-mandke-866866168/)

# To Do

* [ ] Plot compression time along with ratios using sns.
* [ ] Target the various atypical databases for data compression as enlisted [here](http://corpus.canterbury.ac.nz/descriptions/).
