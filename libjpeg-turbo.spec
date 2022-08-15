#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7EC2DBB6F4DBF434 (information@libjpeg-turbo.org)
#
Name     : libjpeg-turbo
Version  : 2.1.4
Release  : 70
URL      : https://sourceforge.net/projects/libjpeg-turbo/files/2.1.4/libjpeg-turbo-2.1.4.tar.gz
Source0  : https://sourceforge.net/projects/libjpeg-turbo/files/2.1.4/libjpeg-turbo-2.1.4.tar.gz
Source1  : https://sourceforge.net/projects/libjpeg-turbo/files/2.1.4/libjpeg-turbo-2.1.4.tar.gz.sig
Summary  : A SIMD-accelerated JPEG codec that provides the TurboJPEG API
Group    : Development/Tools
License  : BSD-3-Clause IJG
Requires: libjpeg-turbo-bin = %{version}-%{release}
Requires: libjpeg-turbo-filemap = %{version}-%{release}
Requires: libjpeg-turbo-lib = %{version}-%{release}
Requires: libjpeg-turbo-license = %{version}-%{release}
Requires: libjpeg-turbo-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : nasm
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : yasm

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
Requires: libjpeg-turbo-license = %{version}-%{release}
Requires: libjpeg-turbo-filemap = %{version}-%{release}

%description bin
bin components for the libjpeg-turbo package.


%package dev
Summary: dev components for the libjpeg-turbo package.
Group: Development
Requires: libjpeg-turbo-lib = %{version}-%{release}
Requires: libjpeg-turbo-bin = %{version}-%{release}
Provides: libjpeg-turbo-devel = %{version}-%{release}
Requires: libjpeg-turbo = %{version}-%{release}

%description dev
dev components for the libjpeg-turbo package.


%package dev32
Summary: dev32 components for the libjpeg-turbo package.
Group: Default
Requires: libjpeg-turbo-lib32 = %{version}-%{release}
Requires: libjpeg-turbo-bin = %{version}-%{release}
Requires: libjpeg-turbo-dev = %{version}-%{release}

%description dev32
dev32 components for the libjpeg-turbo package.


%package doc
Summary: doc components for the libjpeg-turbo package.
Group: Documentation
Requires: libjpeg-turbo-man = %{version}-%{release}

%description doc
doc components for the libjpeg-turbo package.


%package filemap
Summary: filemap components for the libjpeg-turbo package.
Group: Default

%description filemap
filemap components for the libjpeg-turbo package.


%package lib
Summary: lib components for the libjpeg-turbo package.
Group: Libraries
Requires: libjpeg-turbo-license = %{version}-%{release}
Requires: libjpeg-turbo-filemap = %{version}-%{release}

%description lib
lib components for the libjpeg-turbo package.


%package lib32
Summary: lib32 components for the libjpeg-turbo package.
Group: Default
Requires: libjpeg-turbo-license = %{version}-%{release}

%description lib32
lib32 components for the libjpeg-turbo package.


%package license
Summary: license components for the libjpeg-turbo package.
Group: Default

%description license
license components for the libjpeg-turbo package.


%package man
Summary: man components for the libjpeg-turbo package.
Group: Default

%description man
man components for the libjpeg-turbo package.


%prep
%setup -q -n libjpeg-turbo-2.1.4
cd %{_builddir}/libjpeg-turbo-2.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660578903
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
%cmake ..
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}"
make  %{?_smp_mflags}

./tjbench testimages/testimgint.jpg
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}"
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build32
pushd clr-build32
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 ..
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../clr-build32;
make test || :
cd ../clr-build-avx2;
make test || :

%install
export SOURCE_DATE_EPOCH=1660578903
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libjpeg-turbo
cp %{_builddir}/libjpeg-turbo-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/libjpeg-turbo/e3f989b72a7dce97f48943ac8c8b5e5ca16653f2
cp %{_builddir}/libjpeg-turbo-%{version}/release/License.rtf %{buildroot}/usr/share/package-licenses/libjpeg-turbo/f0b17b88210d4efef996d99421683315b8ded689
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
## install_append content
[ -d %{buildroot}/usr/lib/ ] && mv %{buildroot}/usr/lib/*so* %{buildroot}/usr/lib32
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cjpeg
/usr/bin/djpeg
/usr/bin/jpegtran
/usr/bin/rdjpgcom
/usr/bin/tjbench
/usr/bin/wrjpgcom
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/jconfig.h
/usr/include/jerror.h
/usr/include/jmorecfg.h
/usr/include/jpeglib.h
/usr/include/turbojpeg.h
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboConfig.cmake
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboConfigVersion.cmake
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboTargets-relwithdebinfo.cmake
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboTargets.cmake
/usr/lib64/glibc-hwcaps/x86-64-v3/libjpeg.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libturbojpeg.so
/usr/lib64/libjpeg.so
/usr/lib64/libturbojpeg.so
/usr/lib64/pkgconfig/libjpeg.pc
/usr/lib64/pkgconfig/libturbojpeg.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/libjpeg-turbo/libjpeg-turboConfig.cmake
/usr/lib32/cmake/libjpeg-turbo/libjpeg-turboConfigVersion.cmake
/usr/lib32/cmake/libjpeg-turbo/libjpeg-turboTargets-relwithdebinfo.cmake
/usr/lib32/cmake/libjpeg-turbo/libjpeg-turboTargets.cmake
/usr/lib32/libjpeg.so
/usr/lib32/libturbojpeg.so
/usr/lib32/pkgconfig/32libjpeg.pc
/usr/lib32/pkgconfig/32libturbojpeg.pc
/usr/lib32/pkgconfig/libjpeg.pc
/usr/lib32/pkgconfig/libturbojpeg.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libjpeg\-turbo/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-libjpeg-turbo

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libjpeg.so.62
/usr/lib64/glibc-hwcaps/x86-64-v3/libjpeg.so.62.3.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libturbojpeg.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libturbojpeg.so.0.2.0
/usr/lib64/libjpeg.so.62
/usr/lib64/libjpeg.so.62.3.0
/usr/lib64/libturbojpeg.so.0
/usr/lib64/libturbojpeg.so.0.2.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libjpeg.so.62
/usr/lib32/libjpeg.so.62.3.0
/usr/lib32/libturbojpeg.so.0
/usr/lib32/libturbojpeg.so.0.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libjpeg-turbo/e3f989b72a7dce97f48943ac8c8b5e5ca16653f2
/usr/share/package-licenses/libjpeg-turbo/f0b17b88210d4efef996d99421683315b8ded689

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cjpeg.1
/usr/share/man/man1/djpeg.1
/usr/share/man/man1/jpegtran.1
/usr/share/man/man1/rdjpgcom.1
/usr/share/man/man1/wrjpgcom.1
