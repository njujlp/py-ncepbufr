import ncepbufr
lunit = 7
ncepbufr.openbf('prepbufr',lunit,'IN',lunit)
ncepbufr.dxdump('prepbufr.table',lunit,lunit+1)
