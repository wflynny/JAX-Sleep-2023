#!/usr/bin/env bash

wget -O visium/GSE203424.tar https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE203424&format=file
cd visium && tar -xvf GSE203424.tar && cd -

wget -O xenium/mouse_brain.zip https://cf.10xgenomics.com/samples/xenium/1.0.2/Xenium_V1_FF_Mouse_Brain_MultiSection_1/Xenium_V1_FF_Mouse_Brain_MultiSection_1_outs.zip

wget -O singlecell/mouse_brain_filtered_feature_bc_matrix.h5 https://cf.10xgenomics.com/samples/cell-exp/7.0.0/5k_mouse_brain_CNIK_3pv3/5k_mouse_brain_CNIK_3pv3_filtered_feature_bc_matrix.h5
