#!/bin/sh

#https://github.com/xcir/libvmod-awsrest

if [ "${VMP_PKGTYPE}" = "deb" ]; then
    apt-get -yq install libmhash-dev
else
    dnf -y install libmhash-devel
fi
