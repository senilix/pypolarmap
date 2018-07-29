## Setup

### Prerequisites

[Intel Fortran Redist for Parallel XE 2015 Compiler](https://software.intel.com/en-us/articles/redistributables-for-intel-parallel-studio-xe-2015-composer-edition-for-windows) provides libmmd.dll and libifcoremmd.ddl

### Testing Fortran 

install mingw fortran compiler 
add to path

to compile a test dll

    gfortran -shared -static -fPIC Test.f90 -o Test.dll

### Create venv

32bit python is required, with conda this means:

    set CONDA_SUBDIR=win-32
    conda create -n scanner32 numpy matplotlib colorcet qtawesome pyqt5
    activate scanner32
    conda info

## TODO 

* multi chart doesn't always redraw properly
* graph limits aren't updating properly in the multi chart
* polar chart ylim is not correct
* draw the actual window shape not a line