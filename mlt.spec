#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v13
# autospec commit: dc0ff31
#
Name     : mlt
Version  : 7.24.0
Release  : 43
URL      : https://github.com/mltframework/mlt/releases/download/v7.24.0/mlt-7.24.0.tar.gz
Source0  : https://github.com/mltframework/mlt/releases/download/v7.24.0/mlt-7.24.0.tar.gz
Summary  : MLT multimedia framework
Group    : Development/Tools
License  : LGPL-2.1 MIT
BuildRequires : SDL2-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : fftw-dev
BuildRequires : glibc-dev
BuildRequires : gtk+-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libarchive-dev
BuildRequires : libxml2-dev
BuildRequires : lua-dev
BuildRequires : mesa-dev
BuildRequires : opencv-dev
BuildRequires : openjdk-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavdevice)
BuildRequires : pkgconfig(libavfilter)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libexif)
BuildRequires : pkgconfig(libswresample)
BuildRequires : pkgconfig(libswscale)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sdl)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(sox)
BuildRequires : pkgconfig(spatialaudio)
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(vorbisfile)
BuildRequires : python3-dev
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : ruby
BuildRequires : sox-dev
BuildRequires : swig
BuildRequires : tcl-dev tk-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
MLT Demo Notes
Before running the demo script, make sure you '. setenv' from the parent
directory. Also, please create clips clip1.dv, clip2.dv, clip3.dv, clip1.mpeg,
clip2.mpeg, clip3.mpeg, and music1.ogg. Please make sure clips are at least 500
frames duration.

%prep
%setup -q -n mlt-7.24.0
cd %{_builddir}/mlt-7.24.0
pushd ..
cp -a mlt-7.24.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720054908
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720054908
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mlt
cp %{_builddir}/mlt-%{version}/COPYING %{buildroot}/usr/share/package-licenses/mlt/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
cp %{_builddir}/mlt-%{version}/src/modules/plus/ebur128/COPYING %{buildroot}/usr/share/package-licenses/mlt/2627ff03833f74ed51a7f43c55d30b249b6a0707 || :
cp %{_builddir}/mlt-%{version}/src/modules/rtaudio/LICENSE %{buildroot}/usr/share/package-licenses/mlt/83fbf4e6e117732a8668feb528722e5b96d69fb5 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
