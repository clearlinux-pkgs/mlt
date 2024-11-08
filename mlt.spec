#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: eaa4f711da30
#
Name     : mlt
Version  : 7.22.0
Release  : 51
URL      : https://github.com/mltframework/mlt/releases/download/v7.22.0/mlt-7.22.0.tar.gz
Source0  : https://github.com/mltframework/mlt/releases/download/v7.22.0/mlt-7.22.0.tar.gz
Summary  : MLT multimedia framework
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: mlt-bin = %{version}-%{release}
Requires: mlt-data = %{version}-%{release}
Requires: mlt-lib = %{version}-%{release}
Requires: mlt-license = %{version}-%{release}
Requires: mlt-man = %{version}-%{release}
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
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(vorbisfile)
BuildRequires : python3-dev
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtsvg-dev
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

%package bin
Summary: bin components for the mlt package.
Group: Binaries
Requires: mlt-data = %{version}-%{release}
Requires: mlt-license = %{version}-%{release}

%description bin
bin components for the mlt package.


%package data
Summary: data components for the mlt package.
Group: Data

%description data
data components for the mlt package.


%package dev
Summary: dev components for the mlt package.
Group: Development
Requires: mlt-lib = %{version}-%{release}
Requires: mlt-bin = %{version}-%{release}
Requires: mlt-data = %{version}-%{release}
Provides: mlt-devel = %{version}-%{release}
Requires: mlt = %{version}-%{release}

%description dev
dev components for the mlt package.


%package lib
Summary: lib components for the mlt package.
Group: Libraries
Requires: mlt-data = %{version}-%{release}
Requires: mlt-license = %{version}-%{release}

%description lib
lib components for the mlt package.


%package license
Summary: license components for the mlt package.
Group: Default

%description license
license components for the mlt package.


%package man
Summary: man components for the mlt package.
Group: Default

%description man
man components for the mlt package.


%prep
%setup -q -n mlt-7.22.0
cd %{_builddir}/mlt-7.22.0
pushd ..
cp -a mlt-7.22.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725554799
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
export SOURCE_DATE_EPOCH=1725554799
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

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/melt-7
/usr/bin/melt
/usr/bin/melt-7

%files data
%defattr(-,root,root,-)
/usr/share/mlt-7/avformat/blacklist.txt
/usr/share/mlt-7/avformat/consumer_avformat.yml
/usr/share/mlt-7/avformat/filter_avcolour_space.yml
/usr/share/mlt-7/avformat/filter_avdeinterlace.yml
/usr/share/mlt-7/avformat/filter_swresample.yml
/usr/share/mlt-7/avformat/filter_swscale.yml
/usr/share/mlt-7/avformat/link_avdeinterlace.yml
/usr/share/mlt-7/avformat/link_swresample.yml
/usr/share/mlt-7/avformat/producer_avformat.yml
/usr/share/mlt-7/avformat/resolution_scale.yml
/usr/share/mlt-7/avformat/yuv_only.txt
/usr/share/mlt-7/chain_normalizers.ini
/usr/share/mlt-7/core/consumer_multi.yml
/usr/share/mlt-7/core/consumer_null.yml
/usr/share/mlt-7/core/filter_audiochannels.yml
/usr/share/mlt-7/core/filter_audioconvert.yml
/usr/share/mlt-7/core/filter_audiomap.yml
/usr/share/mlt-7/core/filter_audioseam.yml
/usr/share/mlt-7/core/filter_audiowave.yml
/usr/share/mlt-7/core/filter_autofade.yml
/usr/share/mlt-7/core/filter_box_blur.yml
/usr/share/mlt-7/core/filter_brightness.yml
/usr/share/mlt-7/core/filter_channelcopy.yml
/usr/share/mlt-7/core/filter_choppy.yml
/usr/share/mlt-7/core/filter_crop.yml
/usr/share/mlt-7/core/filter_fieldorder.yml
/usr/share/mlt-7/core/filter_gamma.yml
/usr/share/mlt-7/core/filter_greyscale.yml
/usr/share/mlt-7/core/filter_imageconvert.yml
/usr/share/mlt-7/core/filter_luma.yml
/usr/share/mlt-7/core/filter_mask_apply.yml
/usr/share/mlt-7/core/filter_mask_start.yml
/usr/share/mlt-7/core/filter_mirror.yml
/usr/share/mlt-7/core/filter_mono.yml
/usr/share/mlt-7/core/filter_obscure.yml
/usr/share/mlt-7/core/filter_panner.yml
/usr/share/mlt-7/core/filter_pillar_echo.yml
/usr/share/mlt-7/core/filter_rescale.yml
/usr/share/mlt-7/core/filter_resize.yml
/usr/share/mlt-7/core/filter_transition.yml
/usr/share/mlt-7/core/filter_watermark.yml
/usr/share/mlt-7/core/link_timeremap.yml
/usr/share/mlt-7/core/loader.dict
/usr/share/mlt-7/core/loader.ini
/usr/share/mlt-7/core/producer_abnormal.yml
/usr/share/mlt-7/core/producer_blank.yml
/usr/share/mlt-7/core/producer_colour.yml
/usr/share/mlt-7/core/producer_consumer.yml
/usr/share/mlt-7/core/producer_hold.yml
/usr/share/mlt-7/core/producer_loader-nogl.yml
/usr/share/mlt-7/core/producer_loader.yml
/usr/share/mlt-7/core/producer_melt.yml
/usr/share/mlt-7/core/producer_melt_file.yml
/usr/share/mlt-7/core/producer_noise.yml
/usr/share/mlt-7/core/producer_timewarp.yml
/usr/share/mlt-7/core/producer_tone.yml
/usr/share/mlt-7/core/transition_composite.yml
/usr/share/mlt-7/core/transition_luma.yml
/usr/share/mlt-7/core/transition_matte.yml
/usr/share/mlt-7/core/transition_mix.yml
/usr/share/mlt-7/decklink/consumer_decklink.yml
/usr/share/mlt-7/decklink/producer_decklink.yml
/usr/share/mlt-7/gdk/filter_rescale.yml
/usr/share/mlt-7/gdk/producer_pango.yml
/usr/share/mlt-7/gdk/producer_pixbuf.yml
/usr/share/mlt-7/jackrack/consumer_jack.yml
/usr/share/mlt-7/kdenlive/filter_boxblur.yml
/usr/share/mlt-7/kdenlive/filter_freeze.yml
/usr/share/mlt-7/kdenlive/filter_wave.yml
/usr/share/mlt-7/kdenlive/producer_framebuffer.yml
/usr/share/mlt-7/metaschema.yaml
/usr/share/mlt-7/normalize/filter_audiolevel.yml
/usr/share/mlt-7/normalize/filter_volume.yml
/usr/share/mlt-7/oldfilm/dust1.svg
/usr/share/mlt-7/oldfilm/dust2.svg
/usr/share/mlt-7/oldfilm/dust3.svg
/usr/share/mlt-7/oldfilm/dust4.svg
/usr/share/mlt-7/oldfilm/dust5.svg
/usr/share/mlt-7/oldfilm/fdust.svg
/usr/share/mlt-7/oldfilm/filter_dust.yml
/usr/share/mlt-7/oldfilm/filter_grain.yml
/usr/share/mlt-7/oldfilm/filter_lines.yml
/usr/share/mlt-7/oldfilm/filter_oldfilm.yml
/usr/share/mlt-7/oldfilm/filter_tcolor.yml
/usr/share/mlt-7/oldfilm/filter_vignette.yml
/usr/share/mlt-7/oldfilm/grain.svg
/usr/share/mlt-7/oldfilm/lines.svg
/usr/share/mlt-7/oldfilm/oldfilm.svg
/usr/share/mlt-7/oldfilm/tcolor.svg
/usr/share/mlt-7/oldfilm/vignette.svg
/usr/share/mlt-7/plus/consumer_blipflash.yml
/usr/share/mlt-7/plus/filter_affine.yml
/usr/share/mlt-7/plus/filter_charcoal.yml
/usr/share/mlt-7/plus/filter_chroma.yml
/usr/share/mlt-7/plus/filter_chroma_hold.yml
/usr/share/mlt-7/plus/filter_dance.yml
/usr/share/mlt-7/plus/filter_dynamic_loudness.yml
/usr/share/mlt-7/plus/filter_dynamictext.yml
/usr/share/mlt-7/plus/filter_fft.yml
/usr/share/mlt-7/plus/filter_invert.yml
/usr/share/mlt-7/plus/filter_lift_gamma_gain.yml
/usr/share/mlt-7/plus/filter_loudness.yml
/usr/share/mlt-7/plus/filter_loudness_meter.yml
/usr/share/mlt-7/plus/filter_lumakey.yml
/usr/share/mlt-7/plus/filter_rgblut.yml
/usr/share/mlt-7/plus/filter_sepia.yml
/usr/share/mlt-7/plus/filter_shape.yml
/usr/share/mlt-7/plus/filter_spot_remover.yml
/usr/share/mlt-7/plus/filter_strobe.yml
/usr/share/mlt-7/plus/filter_text.yml
/usr/share/mlt-7/plus/filter_threshold.yml
/usr/share/mlt-7/plus/filter_timer.yml
/usr/share/mlt-7/plus/producer_blipflash.yml
/usr/share/mlt-7/plus/producer_count.yml
/usr/share/mlt-7/plus/producer_pgm.yml
/usr/share/mlt-7/plus/transition_affine.yml
/usr/share/mlt-7/plusgpl/consumer_cbrts.yml
/usr/share/mlt-7/plusgpl/filter_burningtv.yml
/usr/share/mlt-7/plusgpl/filter_lumaliftgaingamma.yml
/usr/share/mlt-7/plusgpl/filter_rotoscoping.yml
/usr/share/mlt-7/presets/consumer/avformat/AAC
/usr/share/mlt-7/presets/consumer/avformat/ALAC
/usr/share/mlt-7/presets/consumer/avformat/AV1
/usr/share/mlt-7/presets/consumer/avformat/FLAC
/usr/share/mlt-7/presets/consumer/avformat/Flash
/usr/share/mlt-7/presets/consumer/avformat/GIF
/usr/share/mlt-7/presets/consumer/avformat/MJPEG
/usr/share/mlt-7/presets/consumer/avformat/MP3
/usr/share/mlt-7/presets/consumer/avformat/MPEG-2
/usr/share/mlt-7/presets/consumer/avformat/MPEG-4
/usr/share/mlt-7/presets/consumer/avformat/MPEG-4-ASP
/usr/share/mlt-7/presets/consumer/avformat/Slide-Deck-H264
/usr/share/mlt-7/presets/consumer/avformat/Slide-Deck-HEVC
/usr/share/mlt-7/presets/consumer/avformat/Sony-PSP
/usr/share/mlt-7/presets/consumer/avformat/Vorbis
/usr/share/mlt-7/presets/consumer/avformat/WAV
/usr/share/mlt-7/presets/consumer/avformat/WMA
/usr/share/mlt-7/presets/consumer/avformat/WMV
/usr/share/mlt-7/presets/consumer/avformat/XDCAM-HD422
/usr/share/mlt-7/presets/consumer/avformat/YouTube
"/usr/share/mlt-7/presets/consumer/avformat/alpha/Quicktime Animation"
"/usr/share/mlt-7/presets/consumer/avformat/alpha/Ut Video"
/usr/share/mlt-7/presets/consumer/avformat/alpha/vp8
/usr/share/mlt-7/presets/consumer/avformat/alpha/vp9
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080i_50/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080i_5994/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080p_2398/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080p_24/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080p_25/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080p_2997/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080p_30/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080p_50/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080p_5994/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_1080p_60/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_720p_2398/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_720p_50/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_720p_5994/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/atsc_720p_60/DNxHD
/usr/share/mlt-7/presets/consumer/avformat/dv_ntsc/D10
/usr/share/mlt-7/presets/consumer/avformat/dv_ntsc/DV
/usr/share/mlt-7/presets/consumer/avformat/dv_ntsc/DVCPRO50
/usr/share/mlt-7/presets/consumer/avformat/dv_ntsc/DVD
/usr/share/mlt-7/presets/consumer/avformat/dv_ntsc_wide/D10
/usr/share/mlt-7/presets/consumer/avformat/dv_ntsc_wide/DV
/usr/share/mlt-7/presets/consumer/avformat/dv_ntsc_wide/DVCPRO50
/usr/share/mlt-7/presets/consumer/avformat/dv_ntsc_wide/DVD
/usr/share/mlt-7/presets/consumer/avformat/dv_pal/D10
/usr/share/mlt-7/presets/consumer/avformat/dv_pal/DV
/usr/share/mlt-7/presets/consumer/avformat/dv_pal/DVCPRO50
/usr/share/mlt-7/presets/consumer/avformat/dv_pal/DVD
/usr/share/mlt-7/presets/consumer/avformat/dv_pal_wide/D10
/usr/share/mlt-7/presets/consumer/avformat/dv_pal_wide/DV
/usr/share/mlt-7/presets/consumer/avformat/dv_pal_wide/DVCPRO50
/usr/share/mlt-7/presets/consumer/avformat/dv_pal_wide/DVD
/usr/share/mlt-7/presets/consumer/avformat/hdv_1080_25p/HDV
/usr/share/mlt-7/presets/consumer/avformat/hdv_1080_30p/HDV
/usr/share/mlt-7/presets/consumer/avformat/hdv_1080_50i/HDV
/usr/share/mlt-7/presets/consumer/avformat/hdv_1080_60i/HDV
/usr/share/mlt-7/presets/consumer/avformat/hdv_720_25p/HDV
/usr/share/mlt-7/presets/consumer/avformat/hdv_720_30p/HDV
/usr/share/mlt-7/presets/consumer/avformat/hdv_720_50p/HDV
/usr/share/mlt-7/presets/consumer/avformat/hdv_720_60p/HDV
/usr/share/mlt-7/presets/consumer/avformat/intermediate/DNxHR-HQ
/usr/share/mlt-7/presets/consumer/avformat/intermediate/MJPEG
/usr/share/mlt-7/presets/consumer/avformat/intermediate/MPEG-2
/usr/share/mlt-7/presets/consumer/avformat/intermediate/MPEG-4
/usr/share/mlt-7/presets/consumer/avformat/intermediate/ProRes
"/usr/share/mlt-7/presets/consumer/avformat/intermediate/ProRes HQ"
/usr/share/mlt-7/presets/consumer/avformat/intermediate/ProRes-Kostya
/usr/share/mlt-7/presets/consumer/avformat/lossless/FFV1
/usr/share/mlt-7/presets/consumer/avformat/lossless/H.264
/usr/share/mlt-7/presets/consumer/avformat/lossless/HuffYUV
"/usr/share/mlt-7/presets/consumer/avformat/lossless/Ut Video"
/usr/share/mlt-7/presets/consumer/avformat/stills/BMP
/usr/share/mlt-7/presets/consumer/avformat/stills/DPX
/usr/share/mlt-7/presets/consumer/avformat/stills/JPEG
/usr/share/mlt-7/presets/consumer/avformat/stills/PNG
/usr/share/mlt-7/presets/consumer/avformat/stills/PPM
/usr/share/mlt-7/presets/consumer/avformat/stills/TGA
/usr/share/mlt-7/presets/consumer/avformat/stills/TIFF
/usr/share/mlt-7/presets/consumer/avformat/stills/webp
/usr/share/mlt-7/presets/consumer/avformat/ten_bit/AV1
/usr/share/mlt-7/presets/consumer/avformat/ten_bit/DNxHR-HQ
/usr/share/mlt-7/presets/consumer/avformat/ten_bit/FFV1
"/usr/share/mlt-7/presets/consumer/avformat/ten_bit/ProRes 422"
"/usr/share/mlt-7/presets/consumer/avformat/ten_bit/ProRes 444"
"/usr/share/mlt-7/presets/consumer/avformat/ten_bit/ProRes HQ"
/usr/share/mlt-7/presets/consumer/avformat/ten_bit/x264-high10
/usr/share/mlt-7/presets/consumer/avformat/ten_bit/x265-main10
/usr/share/mlt-7/presets/consumer/avformat/vp9
/usr/share/mlt-7/presets/consumer/avformat/webm
/usr/share/mlt-7/presets/consumer/avformat/webm-pass1
/usr/share/mlt-7/presets/consumer/avformat/webp
/usr/share/mlt-7/presets/consumer/avformat/x264-medium
/usr/share/mlt-7/presets/consumer/avformat/x264-medium-baseline
/usr/share/mlt-7/presets/consumer/avformat/x264-medium-main
/usr/share/mlt-7/presets/consumer/avformat/x264-medium-pass1
/usr/share/mlt-7/presets/consumer/avformat/x265-medium
/usr/share/mlt-7/presets/consumer/avformat/x265-medium-pass1
/usr/share/mlt-7/presets/filter/brightness/from_black
/usr/share/mlt-7/presets/filter/brightness/to_black
/usr/share/mlt-7/presets/filter/movit.blur/blur_in
/usr/share/mlt-7/presets/filter/movit.blur/blur_in_out
/usr/share/mlt-7/presets/filter/movit.blur/blur_out
/usr/share/mlt-7/presets/filter/movit.opacity/fade_in
/usr/share/mlt-7/presets/filter/movit.opacity/fade_in_out
/usr/share/mlt-7/presets/filter/movit.opacity/fade_out
/usr/share/mlt-7/presets/filter/volume/fade_in
/usr/share/mlt-7/presets/filter/volume/fade_out
/usr/share/mlt-7/profiles/atsc_1080i_50
/usr/share/mlt-7/profiles/atsc_1080i_5994
/usr/share/mlt-7/profiles/atsc_1080i_60
/usr/share/mlt-7/profiles/atsc_1080p_2398
/usr/share/mlt-7/profiles/atsc_1080p_24
/usr/share/mlt-7/profiles/atsc_1080p_25
/usr/share/mlt-7/profiles/atsc_1080p_2997
/usr/share/mlt-7/profiles/atsc_1080p_30
/usr/share/mlt-7/profiles/atsc_1080p_50
/usr/share/mlt-7/profiles/atsc_1080p_5994
/usr/share/mlt-7/profiles/atsc_1080p_60
/usr/share/mlt-7/profiles/atsc_720p_2398
/usr/share/mlt-7/profiles/atsc_720p_24
/usr/share/mlt-7/profiles/atsc_720p_25
/usr/share/mlt-7/profiles/atsc_720p_2997
/usr/share/mlt-7/profiles/atsc_720p_30
/usr/share/mlt-7/profiles/atsc_720p_50
/usr/share/mlt-7/profiles/atsc_720p_5994
/usr/share/mlt-7/profiles/atsc_720p_60
/usr/share/mlt-7/profiles/cif_15
/usr/share/mlt-7/profiles/cif_ntsc
/usr/share/mlt-7/profiles/cif_pal
/usr/share/mlt-7/profiles/cvd_ntsc
/usr/share/mlt-7/profiles/cvd_pal
/usr/share/mlt-7/profiles/dv_ntsc
/usr/share/mlt-7/profiles/dv_ntsc_wide
/usr/share/mlt-7/profiles/dv_pal
/usr/share/mlt-7/profiles/dv_pal_wide
/usr/share/mlt-7/profiles/hdv_1080_25p
/usr/share/mlt-7/profiles/hdv_1080_30p
/usr/share/mlt-7/profiles/hdv_1080_50i
/usr/share/mlt-7/profiles/hdv_1080_60i
/usr/share/mlt-7/profiles/hdv_720_25p
/usr/share/mlt-7/profiles/hdv_720_30p
/usr/share/mlt-7/profiles/hdv_720_50p
/usr/share/mlt-7/profiles/hdv_720_60p
/usr/share/mlt-7/profiles/qcif_15
/usr/share/mlt-7/profiles/qcif_ntsc
/usr/share/mlt-7/profiles/qcif_pal
/usr/share/mlt-7/profiles/qhd_1440p_2398
/usr/share/mlt-7/profiles/qhd_1440p_24
/usr/share/mlt-7/profiles/qhd_1440p_25
/usr/share/mlt-7/profiles/qhd_1440p_2997
/usr/share/mlt-7/profiles/qhd_1440p_30
/usr/share/mlt-7/profiles/qhd_1440p_50
/usr/share/mlt-7/profiles/qhd_1440p_5994
/usr/share/mlt-7/profiles/qhd_1440p_60
/usr/share/mlt-7/profiles/quarter_15
/usr/share/mlt-7/profiles/quarter_ntsc
/usr/share/mlt-7/profiles/quarter_ntsc_wide
/usr/share/mlt-7/profiles/quarter_pal
/usr/share/mlt-7/profiles/quarter_pal_wide
/usr/share/mlt-7/profiles/sdi_486i_5994
/usr/share/mlt-7/profiles/sdi_486p_2398
/usr/share/mlt-7/profiles/square_1080p_30
/usr/share/mlt-7/profiles/square_1080p_60
/usr/share/mlt-7/profiles/square_ntsc
/usr/share/mlt-7/profiles/square_ntsc_wide
/usr/share/mlt-7/profiles/square_pal
/usr/share/mlt-7/profiles/square_pal_wide
/usr/share/mlt-7/profiles/svcd_ntsc
/usr/share/mlt-7/profiles/svcd_ntsc_wide
/usr/share/mlt-7/profiles/svcd_pal
/usr/share/mlt-7/profiles/svcd_pal_wide
/usr/share/mlt-7/profiles/uhd_2160p_2398
/usr/share/mlt-7/profiles/uhd_2160p_24
/usr/share/mlt-7/profiles/uhd_2160p_25
/usr/share/mlt-7/profiles/uhd_2160p_2997
/usr/share/mlt-7/profiles/uhd_2160p_30
/usr/share/mlt-7/profiles/uhd_2160p_50
/usr/share/mlt-7/profiles/uhd_2160p_5994
/usr/share/mlt-7/profiles/uhd_2160p_60
/usr/share/mlt-7/profiles/vcd_ntsc
/usr/share/mlt-7/profiles/vcd_pal
/usr/share/mlt-7/profiles/vertical_hd_30
/usr/share/mlt-7/profiles/vertical_hd_60
/usr/share/mlt-7/qt/filter_audiolevelgraph.yml
/usr/share/mlt-7/qt/filter_audiospectrum.yml
/usr/share/mlt-7/qt/filter_audiowaveform.yml
/usr/share/mlt-7/qt/filter_gpsgraphic.yml
/usr/share/mlt-7/qt/filter_gpstext.yml
/usr/share/mlt-7/qt/filter_lightshow.yml
/usr/share/mlt-7/qt/filter_qtblend.yml
/usr/share/mlt-7/qt/filter_qtcrop.yml
/usr/share/mlt-7/qt/filter_qtext.yml
/usr/share/mlt-7/qt/filter_typewriter.yml
/usr/share/mlt-7/qt/producer_kdenlivetitle.yml
/usr/share/mlt-7/qt/producer_qimage.yml
/usr/share/mlt-7/qt/producer_qtext.yml
/usr/share/mlt-7/qt/transition_qtblend.yml
/usr/share/mlt-7/qt/transition_vqm.yml
/usr/share/mlt-7/resample/filter_resample.yml
/usr/share/mlt-7/resample/link_resample.yml
/usr/share/mlt-7/rtaudio/consumer_rtaudio.yml
/usr/share/mlt-7/sdl/consumer_sdl.yml
/usr/share/mlt-7/sdl/consumer_sdl_audio.yml
/usr/share/mlt-7/sdl/consumer_sdl_preview.yml
/usr/share/mlt-7/sdl/consumer_sdl_still.yml
/usr/share/mlt-7/sdl2/consumer_sdl2.yml
/usr/share/mlt-7/sdl2/consumer_sdl2_audio.yml
/usr/share/mlt-7/sox/filter_sox.yml
/usr/share/mlt-7/sox/filter_sox_effect.yml
/usr/share/mlt-7/vorbis/producer_vorbis.yml
/usr/share/mlt-7/xine/filter_deinterlace.yml
/usr/share/mlt-7/xine/link_deinterlace.yml
/usr/share/mlt-7/xml/consumer_xml.yml
/usr/share/mlt-7/xml/mlt-xml.dtd
/usr/share/mlt-7/xml/producer_xml-nogl.yml
/usr/share/mlt-7/xml/producer_xml-string.yml
/usr/share/mlt-7/xml/producer_xml.yml

%files dev
%defattr(-,root,root,-)
/usr/include/mlt-7/framework/mlt.h
/usr/include/mlt-7/framework/mlt_animation.h
/usr/include/mlt-7/framework/mlt_audio.h
/usr/include/mlt-7/framework/mlt_cache.h
/usr/include/mlt-7/framework/mlt_chain.h
/usr/include/mlt-7/framework/mlt_consumer.h
/usr/include/mlt-7/framework/mlt_deque.h
/usr/include/mlt-7/framework/mlt_events.h
/usr/include/mlt-7/framework/mlt_factory.h
/usr/include/mlt-7/framework/mlt_field.h
/usr/include/mlt-7/framework/mlt_filter.h
/usr/include/mlt-7/framework/mlt_frame.h
/usr/include/mlt-7/framework/mlt_image.h
/usr/include/mlt-7/framework/mlt_link.h
/usr/include/mlt-7/framework/mlt_log.h
/usr/include/mlt-7/framework/mlt_luma_map.h
/usr/include/mlt-7/framework/mlt_multitrack.h
/usr/include/mlt-7/framework/mlt_parser.h
/usr/include/mlt-7/framework/mlt_playlist.h
/usr/include/mlt-7/framework/mlt_pool.h
/usr/include/mlt-7/framework/mlt_producer.h
/usr/include/mlt-7/framework/mlt_profile.h
/usr/include/mlt-7/framework/mlt_properties.h
/usr/include/mlt-7/framework/mlt_property.h
/usr/include/mlt-7/framework/mlt_repository.h
/usr/include/mlt-7/framework/mlt_service.h
/usr/include/mlt-7/framework/mlt_slices.h
/usr/include/mlt-7/framework/mlt_tokeniser.h
/usr/include/mlt-7/framework/mlt_tractor.h
/usr/include/mlt-7/framework/mlt_transition.h
/usr/include/mlt-7/framework/mlt_types.h
/usr/include/mlt-7/framework/mlt_version.h
/usr/include/mlt-7/mlt++/Mlt.h
/usr/include/mlt-7/mlt++/MltAnimation.h
/usr/include/mlt-7/mlt++/MltAudio.h
/usr/include/mlt-7/mlt++/MltChain.h
/usr/include/mlt-7/mlt++/MltConfig.h
/usr/include/mlt-7/mlt++/MltConsumer.h
/usr/include/mlt-7/mlt++/MltDeque.h
/usr/include/mlt-7/mlt++/MltEvent.h
/usr/include/mlt-7/mlt++/MltFactory.h
/usr/include/mlt-7/mlt++/MltField.h
/usr/include/mlt-7/mlt++/MltFilter.h
/usr/include/mlt-7/mlt++/MltFilteredConsumer.h
/usr/include/mlt-7/mlt++/MltFilteredProducer.h
/usr/include/mlt-7/mlt++/MltFrame.h
/usr/include/mlt-7/mlt++/MltImage.h
/usr/include/mlt-7/mlt++/MltLink.h
/usr/include/mlt-7/mlt++/MltMultitrack.h
/usr/include/mlt-7/mlt++/MltParser.h
/usr/include/mlt-7/mlt++/MltPlaylist.h
/usr/include/mlt-7/mlt++/MltProducer.h
/usr/include/mlt-7/mlt++/MltProfile.h
/usr/include/mlt-7/mlt++/MltProperties.h
/usr/include/mlt-7/mlt++/MltPushConsumer.h
/usr/include/mlt-7/mlt++/MltRepository.h
/usr/include/mlt-7/mlt++/MltService.h
/usr/include/mlt-7/mlt++/MltTokeniser.h
/usr/include/mlt-7/mlt++/MltTractor.h
/usr/include/mlt-7/mlt++/MltTransition.h
/usr/lib64/cmake/Mlt7/Mlt7Config.cmake
/usr/lib64/cmake/Mlt7/Mlt7ConfigVersion.cmake
/usr/lib64/cmake/Mlt7/Mlt7Targets-relwithdebinfo.cmake
/usr/lib64/cmake/Mlt7/Mlt7Targets.cmake
/usr/lib64/libmlt++-7.so
/usr/lib64/libmlt-7.so
/usr/lib64/pkgconfig/mlt++-7.pc
/usr/lib64/pkgconfig/mlt-framework-7.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmlt++-7.so.7.22.0
/V3/usr/lib64/libmlt-7.so.7.22.0
/V3/usr/lib64/mlt-7/libmltavformat.so
/V3/usr/lib64/mlt-7/libmltcore.so
/V3/usr/lib64/mlt-7/libmltdecklink.so
/V3/usr/lib64/mlt-7/libmltgdk.so
/V3/usr/lib64/mlt-7/libmltjackrack.so
/V3/usr/lib64/mlt-7/libmltkdenlive.so
/V3/usr/lib64/mlt-7/libmltnormalize.so
/V3/usr/lib64/mlt-7/libmltoldfilm.so
/V3/usr/lib64/mlt-7/libmltplus.so
/V3/usr/lib64/mlt-7/libmltplusgpl.so
/V3/usr/lib64/mlt-7/libmltqt.so
/V3/usr/lib64/mlt-7/libmltresample.so
/V3/usr/lib64/mlt-7/libmltrtaudio.so
/V3/usr/lib64/mlt-7/libmltsdl.so
/V3/usr/lib64/mlt-7/libmltsdl2.so
/V3/usr/lib64/mlt-7/libmltsox.so
/V3/usr/lib64/mlt-7/libmltvorbis.so
/V3/usr/lib64/mlt-7/libmltxine.so
/V3/usr/lib64/mlt-7/libmltxml.so
/usr/lib64/libmlt++-7.so.7
/usr/lib64/libmlt++-7.so.7.22.0
/usr/lib64/libmlt-7.so.7
/usr/lib64/libmlt-7.so.7.22.0
/usr/lib64/mlt-7/libmltavformat.so
/usr/lib64/mlt-7/libmltcore.so
/usr/lib64/mlt-7/libmltdecklink.so
/usr/lib64/mlt-7/libmltgdk.so
/usr/lib64/mlt-7/libmltjackrack.so
/usr/lib64/mlt-7/libmltkdenlive.so
/usr/lib64/mlt-7/libmltnormalize.so
/usr/lib64/mlt-7/libmltoldfilm.so
/usr/lib64/mlt-7/libmltplus.so
/usr/lib64/mlt-7/libmltplusgpl.so
/usr/lib64/mlt-7/libmltqt.so
/usr/lib64/mlt-7/libmltresample.so
/usr/lib64/mlt-7/libmltrtaudio.so
/usr/lib64/mlt-7/libmltsdl.so
/usr/lib64/mlt-7/libmltsdl2.so
/usr/lib64/mlt-7/libmltsox.so
/usr/lib64/mlt-7/libmltvorbis.so
/usr/lib64/mlt-7/libmltxine.so
/usr/lib64/mlt-7/libmltxml.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mlt/2627ff03833f74ed51a7f43c55d30b249b6a0707
/usr/share/package-licenses/mlt/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/mlt/83fbf4e6e117732a8668feb528722e5b96d69fb5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/melt-7.1
