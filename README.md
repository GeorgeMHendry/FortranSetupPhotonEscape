As part of my main physics project. I need to run snapshots from the CMacIonize code. This contains a grid set of various properties of the molecular cloud.
Here in particular we are interested in the Number density, but the code I run is in Fortran. 
Fortran has no native way to look at a file directory so would require manual entry of the snapshots. This code creates a param file, which is always named the same.
It is also contained within the directory with the snapshots. Enables the fortran code to just have the directory inputted and then everything else should be
self-contained. 

