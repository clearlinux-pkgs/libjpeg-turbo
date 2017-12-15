#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x85C7044E033FDE16 (information@libjpeg-turbo.org)
#
Name     : libjpeg-turbo
Version  : 1.5.2
Release  : 35
URL      : http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-1.5.2.tar.gz
Source0  : http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-1.5.2.tar.gz
Source99 : http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-1.5.2.tar.gz.sig
Summary  : A SIMD-accelerated JPEG codec that provides the TurboJPEG API
Group    : Development/Tools
License  : BSD-3-Clause IJG
Requires: libjpeg-turbo-bin
Requires: libjpeg-turbo-lib
Requires: libjpeg-turbo-doc
BuildRequires : cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : nasm
BuildRequires : yasm
Patch1: cve-2017-15232.patch

%description
TurboJPEG Java Wrapper
======================
The TurboJPEG shared library can optionally be built with a Java Native
Interface wrapper, which allows the library to be loaded and used directly from
Java applications.  The Java front end for this is defined in several classes
located under org/libjpegturbo/turbojpeg.  The source code for these Java
classes is licensed under a BSD-style license, so the files can be incorporated
directly into both open source and proprietary projects without restriction.  A
Java archive (JAR) file containing these classes is also shipped with the
"official" distribution packages of libjpeg-turbo.

%package bin
Summary: bin components for the libjpeg-turbo package.
Group: Binaries

%description bin
bin components for the libjpeg-turbo package.


%package dev
Summary: dev components for the libjpeg-turbo package.
Group: Development
Requires: libjpeg-turbo-lib
Requires: libjpeg-turbo-bin
Provides: libjpeg-turbo-devel

%description dev
dev components for the libjpeg-turbo package.


%package dev32
Summary: dev32 components for the libjpeg-turbo package.
Group: Default
Requires: libjpeg-turbo-lib32
Requires: libjpeg-turbo-bin
Requires: libjpeg-turbo-dev

%description dev32
dev32 components for the libjpeg-turbo package.


%package doc
Summary: doc components for the libjpeg-turbo package.
Group: Documentation

%description doc
doc components for the libjpeg-turbo package.


%package lib
Summary: lib components for the libjpeg-turbo package.
Group: Libraries

%description lib
lib components for the libjpeg-turbo package.


%package lib32
Summary: lib32 components for the libjpeg-turbo package.
Group: Default

%description lib32
lib32 components for the libjpeg-turbo package.


%prep
%setup -q -n libjpeg-turbo-1.5.2
%patch1 -p1
pushd ..
cp -a libjpeg-turbo-1.5.2 build32
popd
pushd ..
cp -a libjpeg-turbo-1.5.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513308180
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" %configure --disable-static
make  %{?_smp_mflags}

./tjbench testimages/testimgint.jpg
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" %configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static    --libdir=/usr/lib64/haswell --bindir=/usr/bin/haswell
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1513308180
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install
popd
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/haswell/pkgconfig/libjpeg.pc
/usr/lib64/haswell/pkgconfig/libturbojpeg.pc

%files bin
%defattr(-,root,root,-)
/usr/bin/cjpeg
/usr/bin/djpeg
/usr/bin/haswell/cjpeg
/usr/bin/haswell/djpeg
/usr/bin/haswell/jpegtran
/usr/bin/haswell/rdjpgcom
/usr/bin/haswell/tjbench
/usr/bin/haswell/wrjpgcom
/usr/bin/jpegtran
/usr/bin/rdjpgcom
/usr/bin/tjbench
/usr/bin/wrjpgcom

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/haswell/libjpeg.so
/usr/lib64/haswell/libturbojpeg.so
/usr/lib64/libjpeg.so
/usr/lib64/libturbojpeg.so
/usr/lib64/pkgconfig/libjpeg.pc
/usr/lib64/pkgconfig/libturbojpeg.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libjpeg.so
/usr/lib32/libturbojpeg.so
/usr/lib32/pkgconfig/32libjpeg.pc
/usr/lib32/pkgconfig/32libturbojpeg.pc
/usr/lib32/pkgconfig/libjpeg.pc
/usr/lib32/pkgconfig/libturbojpeg.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libjpeg\-turbo/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libjpeg.so.62
/usr/lib64/haswell/libjpeg.so.62.2.0
/usr/lib64/haswell/libturbojpeg.so.0
/usr/lib64/haswell/libturbojpeg.so.0.1.0
/usr/lib64/libjpeg.so.62
/usr/lib64/libjpeg.so.62.2.0
/usr/lib64/libturbojpeg.so.0
/usr/lib64/libturbojpeg.so.0.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libjpeg.so.62
/usr/lib32/libjpeg.so.62.2.0
/usr/lib32/libturbojpeg.so.0
/usr/lib32/libturbojpeg.so.0.1.0
