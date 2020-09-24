#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mlt
Version  : 6.22.1
Release  : 14
URL      : https://github.com/mltframework/mlt/releases/download/v6.22.1/mlt-6.22.1.tar.gz
Source0  : https://github.com/mltframework/mlt/releases/download/v6.22.1/mlt-6.22.1.tar.gz
Summary  : MLT multimedia framework
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: mlt-bin = %{version}-%{release}
Requires: mlt-data = %{version}-%{release}
Requires: mlt-lib = %{version}-%{release}
Requires: mlt-license = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-cpan
BuildRequires : buildreq-qmake
BuildRequires : fftw-dev
BuildRequires : gtk+-dev
BuildRequires : libxml2-dev
BuildRequires : opencv-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : sox-dev

%description
--------------------
Written by Charles Yates <charles.yates@pandora.be>
and Dan Dennedy <dan@dennedy.org>

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


%prep
%setup -q -n mlt-6.22.1
cd %{_builddir}/mlt-6.22.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596469320
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --enable-gpl3 \
--enable-opencv
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1596469320
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mlt
cp %{_builddir}/mlt-6.22.1/COPYING %{buildroot}/usr/share/package-licenses/mlt/3704f4680301a60004b20f94e0b5b8c7ff1484a9
cp %{_builddir}/mlt-6.22.1/src/modules/plus/ebur128/COPYING %{buildroot}/usr/share/package-licenses/mlt/2627ff03833f74ed51a7f43c55d30b249b6a0707
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/melt

%files data
%defattr(-,root,root,-)
/usr/share/mlt/core/consumer_multi.yml
/usr/share/mlt/core/data_fx.properties
/usr/share/mlt/core/filter_audiomap.yml
/usr/share/mlt/core/filter_audiowave.yml
/usr/share/mlt/core/filter_brightness.yml
/usr/share/mlt/core/filter_channelcopy.yml
/usr/share/mlt/core/filter_crop.yml
/usr/share/mlt/core/filter_data_show.yml
/usr/share/mlt/core/filter_fieldorder.yml
/usr/share/mlt/core/filter_gamma.yml
/usr/share/mlt/core/filter_greyscale.yml
/usr/share/mlt/core/filter_luma.yml
/usr/share/mlt/core/filter_mask_apply.yml
/usr/share/mlt/core/filter_mask_start.yml
/usr/share/mlt/core/filter_mirror.yml
/usr/share/mlt/core/filter_mono.yml
/usr/share/mlt/core/filter_obscure.yml
/usr/share/mlt/core/filter_panner.yml
/usr/share/mlt/core/filter_region.yml
/usr/share/mlt/core/filter_rescale.yml
/usr/share/mlt/core/filter_resize.yml
/usr/share/mlt/core/filter_transition.yml
/usr/share/mlt/core/filter_watermark.yml
/usr/share/mlt/core/loader.dict
/usr/share/mlt/core/loader.ini
/usr/share/mlt/core/producer_colour.yml
/usr/share/mlt/core/producer_consumer.yml
/usr/share/mlt/core/producer_hold.yml
/usr/share/mlt/core/producer_loader.yml
/usr/share/mlt/core/producer_melt.yml
/usr/share/mlt/core/producer_melt_file.yml
/usr/share/mlt/core/producer_noise.yml
/usr/share/mlt/core/producer_timewarp.yml
/usr/share/mlt/core/producer_tone.yml
/usr/share/mlt/core/transition_composite.yml
/usr/share/mlt/core/transition_luma.yml
/usr/share/mlt/core/transition_matte.yml
/usr/share/mlt/core/transition_mix.yml
/usr/share/mlt/core/transition_region.yml
/usr/share/mlt/decklink/consumer_decklink.yml
/usr/share/mlt/decklink/producer_decklink.yml
/usr/share/mlt/feeds/NTSC/data_fx.properties
/usr/share/mlt/feeds/NTSC/etv.properties
/usr/share/mlt/feeds/NTSC/obscure.properties
/usr/share/mlt/feeds/PAL/border.properties
/usr/share/mlt/feeds/PAL/data_fx.properties
/usr/share/mlt/feeds/PAL/etv.properties
/usr/share/mlt/feeds/PAL/example.properties
/usr/share/mlt/feeds/PAL/obscure.properties
/usr/share/mlt/gdk/filter_rescale.yml
/usr/share/mlt/gdk/producer_pango.yml
/usr/share/mlt/gdk/producer_pixbuf.yml
/usr/share/mlt/kdenlive/filter_boxblur.yml
/usr/share/mlt/kdenlive/filter_freeze.yml
/usr/share/mlt/kdenlive/filter_wave.yml
/usr/share/mlt/kdenlive/producer_framebuffer.yml
/usr/share/mlt/metaschema.yaml
/usr/share/mlt/oldfilm/dust1.svg
/usr/share/mlt/oldfilm/dust2.svg
/usr/share/mlt/oldfilm/dust3.svg
/usr/share/mlt/oldfilm/dust4.svg
/usr/share/mlt/oldfilm/dust5.svg
/usr/share/mlt/oldfilm/fdust.svg
/usr/share/mlt/oldfilm/filter_dust.yml
/usr/share/mlt/oldfilm/filter_grain.yml
/usr/share/mlt/oldfilm/filter_lines.yml
/usr/share/mlt/oldfilm/filter_oldfilm.yml
/usr/share/mlt/oldfilm/filter_tcolor.yml
/usr/share/mlt/oldfilm/filter_vignette.yml
/usr/share/mlt/oldfilm/grain.svg
/usr/share/mlt/oldfilm/lines.svg
/usr/share/mlt/oldfilm/oldfilm.svg
/usr/share/mlt/oldfilm/tcolor.svg
/usr/share/mlt/oldfilm/vignette.svg
/usr/share/mlt/plus/consumer_blipflash.yml
/usr/share/mlt/plus/filter_affine.yml
/usr/share/mlt/plus/filter_charcoal.yml
/usr/share/mlt/plus/filter_dance.yml
/usr/share/mlt/plus/filter_dynamic_loudness.yml
/usr/share/mlt/plus/filter_dynamictext.yml
/usr/share/mlt/plus/filter_fft.yml
/usr/share/mlt/plus/filter_invert.yml
/usr/share/mlt/plus/filter_lift_gamma_gain.yml
/usr/share/mlt/plus/filter_loudness.yml
/usr/share/mlt/plus/filter_loudness_meter.yml
/usr/share/mlt/plus/filter_lumakey.yml
/usr/share/mlt/plus/filter_rgblut.yml
/usr/share/mlt/plus/filter_sepia.yml
/usr/share/mlt/plus/filter_spot_remover.yml
/usr/share/mlt/plus/filter_text.yml
/usr/share/mlt/plus/filter_timer.yml
/usr/share/mlt/plus/producer_blipflash.yml
/usr/share/mlt/plus/producer_count.yml
/usr/share/mlt/plus/transition_affine.yml
/usr/share/mlt/presets/consumer/avformat/AAC
/usr/share/mlt/presets/consumer/avformat/ALAC
/usr/share/mlt/presets/consumer/avformat/FLAC
/usr/share/mlt/presets/consumer/avformat/Flash
/usr/share/mlt/presets/consumer/avformat/GIF
/usr/share/mlt/presets/consumer/avformat/MJPEG
/usr/share/mlt/presets/consumer/avformat/MP3
/usr/share/mlt/presets/consumer/avformat/MPEG-2
/usr/share/mlt/presets/consumer/avformat/MPEG-4
/usr/share/mlt/presets/consumer/avformat/MPEG-4-ASP
/usr/share/mlt/presets/consumer/avformat/Slide-Deck-H264
/usr/share/mlt/presets/consumer/avformat/Slide-Deck-HEVC
/usr/share/mlt/presets/consumer/avformat/Sony-PSP
/usr/share/mlt/presets/consumer/avformat/Vorbis
/usr/share/mlt/presets/consumer/avformat/WAV
/usr/share/mlt/presets/consumer/avformat/WMA
/usr/share/mlt/presets/consumer/avformat/WMV
/usr/share/mlt/presets/consumer/avformat/XDCAM-HD422
/usr/share/mlt/presets/consumer/avformat/YouTube
"/usr/share/mlt/presets/consumer/avformat/alpha/Quicktime Animation"
"/usr/share/mlt/presets/consumer/avformat/alpha/Ut Video"
/usr/share/mlt/presets/consumer/avformat/alpha/vp8
/usr/share/mlt/presets/consumer/avformat/alpha/vp9
/usr/share/mlt/presets/consumer/avformat/atsc_1080i_50/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_1080i_5994/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_1080p_2398/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_1080p_24/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_1080p_25/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_1080p_2997/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_1080p_30/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_1080p_50/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_1080p_5994/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_1080p_60/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_720p_2398/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_720p_50/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_720p_5994/DNxHD
/usr/share/mlt/presets/consumer/avformat/atsc_720p_60/DNxHD
/usr/share/mlt/presets/consumer/avformat/dv_ntsc/D10
/usr/share/mlt/presets/consumer/avformat/dv_ntsc/DV
/usr/share/mlt/presets/consumer/avformat/dv_ntsc/DVCPRO50
/usr/share/mlt/presets/consumer/avformat/dv_ntsc/DVD
/usr/share/mlt/presets/consumer/avformat/dv_ntsc_wide/D10
/usr/share/mlt/presets/consumer/avformat/dv_ntsc_wide/DV
/usr/share/mlt/presets/consumer/avformat/dv_ntsc_wide/DVCPRO50
/usr/share/mlt/presets/consumer/avformat/dv_ntsc_wide/DVD
/usr/share/mlt/presets/consumer/avformat/dv_pal/D10
/usr/share/mlt/presets/consumer/avformat/dv_pal/DV
/usr/share/mlt/presets/consumer/avformat/dv_pal/DVCPRO50
/usr/share/mlt/presets/consumer/avformat/dv_pal/DVD
/usr/share/mlt/presets/consumer/avformat/dv_pal_wide/D10
/usr/share/mlt/presets/consumer/avformat/dv_pal_wide/DV
/usr/share/mlt/presets/consumer/avformat/dv_pal_wide/DVCPRO50
/usr/share/mlt/presets/consumer/avformat/dv_pal_wide/DVD
/usr/share/mlt/presets/consumer/avformat/hdv_1080_25p/HDV
/usr/share/mlt/presets/consumer/avformat/hdv_1080_30p/HDV
/usr/share/mlt/presets/consumer/avformat/hdv_1080_50i/HDV
/usr/share/mlt/presets/consumer/avformat/hdv_1080_60i/HDV
/usr/share/mlt/presets/consumer/avformat/hdv_720_25p/HDV
/usr/share/mlt/presets/consumer/avformat/hdv_720_30p/HDV
/usr/share/mlt/presets/consumer/avformat/hdv_720_50p/HDV
/usr/share/mlt/presets/consumer/avformat/hdv_720_60p/HDV
/usr/share/mlt/presets/consumer/avformat/intermediate/DNxHR-HQ
/usr/share/mlt/presets/consumer/avformat/intermediate/MJPEG
/usr/share/mlt/presets/consumer/avformat/intermediate/MPEG-2
/usr/share/mlt/presets/consumer/avformat/intermediate/MPEG-4
/usr/share/mlt/presets/consumer/avformat/intermediate/ProRes
"/usr/share/mlt/presets/consumer/avformat/intermediate/ProRes HQ"
/usr/share/mlt/presets/consumer/avformat/intermediate/ProRes-Kostya
/usr/share/mlt/presets/consumer/avformat/lossless/FFV1
/usr/share/mlt/presets/consumer/avformat/lossless/H.264
/usr/share/mlt/presets/consumer/avformat/lossless/HuffYUV
"/usr/share/mlt/presets/consumer/avformat/lossless/Ut Video"
/usr/share/mlt/presets/consumer/avformat/stills/BMP
/usr/share/mlt/presets/consumer/avformat/stills/DPX
/usr/share/mlt/presets/consumer/avformat/stills/JPEG
/usr/share/mlt/presets/consumer/avformat/stills/PNG
/usr/share/mlt/presets/consumer/avformat/stills/PPM
/usr/share/mlt/presets/consumer/avformat/stills/TGA
/usr/share/mlt/presets/consumer/avformat/stills/TIFF
/usr/share/mlt/presets/consumer/avformat/vp9
/usr/share/mlt/presets/consumer/avformat/webm
/usr/share/mlt/presets/consumer/avformat/webm-pass1
/usr/share/mlt/presets/consumer/avformat/x264-medium
/usr/share/mlt/presets/consumer/avformat/x264-medium-baseline
/usr/share/mlt/presets/consumer/avformat/x264-medium-main
/usr/share/mlt/presets/consumer/avformat/x264-medium-pass1
/usr/share/mlt/presets/consumer/avformat/x265-medium
/usr/share/mlt/presets/consumer/avformat/x265-medium-pass1
/usr/share/mlt/presets/filter/brightness/from_black
/usr/share/mlt/presets/filter/brightness/to_black
/usr/share/mlt/presets/filter/movit.blur/blur_in
/usr/share/mlt/presets/filter/movit.blur/blur_in_out
/usr/share/mlt/presets/filter/movit.blur/blur_out
/usr/share/mlt/presets/filter/movit.opacity/fade_in
/usr/share/mlt/presets/filter/movit.opacity/fade_in_out
/usr/share/mlt/presets/filter/movit.opacity/fade_out
/usr/share/mlt/presets/filter/volume/fade_in
/usr/share/mlt/presets/filter/volume/fade_out
/usr/share/mlt/profiles/atsc_1080i_50
/usr/share/mlt/profiles/atsc_1080i_5994
/usr/share/mlt/profiles/atsc_1080i_60
/usr/share/mlt/profiles/atsc_1080p_2398
/usr/share/mlt/profiles/atsc_1080p_24
/usr/share/mlt/profiles/atsc_1080p_25
/usr/share/mlt/profiles/atsc_1080p_2997
/usr/share/mlt/profiles/atsc_1080p_30
/usr/share/mlt/profiles/atsc_1080p_50
/usr/share/mlt/profiles/atsc_1080p_5994
/usr/share/mlt/profiles/atsc_1080p_60
/usr/share/mlt/profiles/atsc_720p_2398
/usr/share/mlt/profiles/atsc_720p_24
/usr/share/mlt/profiles/atsc_720p_25
/usr/share/mlt/profiles/atsc_720p_2997
/usr/share/mlt/profiles/atsc_720p_30
/usr/share/mlt/profiles/atsc_720p_50
/usr/share/mlt/profiles/atsc_720p_5994
/usr/share/mlt/profiles/atsc_720p_60
/usr/share/mlt/profiles/cif_15
/usr/share/mlt/profiles/cif_ntsc
/usr/share/mlt/profiles/cif_pal
/usr/share/mlt/profiles/cvd_ntsc
/usr/share/mlt/profiles/cvd_pal
/usr/share/mlt/profiles/dv_ntsc
/usr/share/mlt/profiles/dv_ntsc_wide
/usr/share/mlt/profiles/dv_pal
/usr/share/mlt/profiles/dv_pal_wide
/usr/share/mlt/profiles/hdv_1080_25p
/usr/share/mlt/profiles/hdv_1080_30p
/usr/share/mlt/profiles/hdv_1080_50i
/usr/share/mlt/profiles/hdv_1080_60i
/usr/share/mlt/profiles/hdv_720_25p
/usr/share/mlt/profiles/hdv_720_30p
/usr/share/mlt/profiles/hdv_720_50p
/usr/share/mlt/profiles/hdv_720_60p
/usr/share/mlt/profiles/qcif_15
/usr/share/mlt/profiles/qcif_ntsc
/usr/share/mlt/profiles/qcif_pal
/usr/share/mlt/profiles/qhd_1440p_2398
/usr/share/mlt/profiles/qhd_1440p_24
/usr/share/mlt/profiles/qhd_1440p_25
/usr/share/mlt/profiles/qhd_1440p_2997
/usr/share/mlt/profiles/qhd_1440p_30
/usr/share/mlt/profiles/qhd_1440p_50
/usr/share/mlt/profiles/qhd_1440p_5994
/usr/share/mlt/profiles/qhd_1440p_60
/usr/share/mlt/profiles/quarter_15
/usr/share/mlt/profiles/quarter_ntsc
/usr/share/mlt/profiles/quarter_ntsc_wide
/usr/share/mlt/profiles/quarter_pal
/usr/share/mlt/profiles/quarter_pal_wide
/usr/share/mlt/profiles/sdi_486i_5994
/usr/share/mlt/profiles/sdi_486p_2398
/usr/share/mlt/profiles/square_1080p_30
/usr/share/mlt/profiles/square_1080p_60
/usr/share/mlt/profiles/square_ntsc
/usr/share/mlt/profiles/square_ntsc_wide
/usr/share/mlt/profiles/square_pal
/usr/share/mlt/profiles/square_pal_wide
/usr/share/mlt/profiles/svcd_ntsc
/usr/share/mlt/profiles/svcd_ntsc_wide
/usr/share/mlt/profiles/svcd_pal
/usr/share/mlt/profiles/svcd_pal_wide
/usr/share/mlt/profiles/uhd_2160p_2398
/usr/share/mlt/profiles/uhd_2160p_24
/usr/share/mlt/profiles/uhd_2160p_25
/usr/share/mlt/profiles/uhd_2160p_2997
/usr/share/mlt/profiles/uhd_2160p_30
/usr/share/mlt/profiles/uhd_2160p_50
/usr/share/mlt/profiles/uhd_2160p_5994
/usr/share/mlt/profiles/uhd_2160p_60
/usr/share/mlt/profiles/vcd_ntsc
/usr/share/mlt/profiles/vcd_pal
/usr/share/mlt/profiles/vertical_hd_30
/usr/share/mlt/profiles/vertical_hd_60
/usr/share/mlt/rtaudio/consumer_rtaudio.yml
/usr/share/mlt/sdl2/consumer_sdl2.yml
/usr/share/mlt/sdl2/consumer_sdl2_audio.yml
/usr/share/mlt/sox/filter_sox.yml
/usr/share/mlt/sox/filter_sox_effect.yml
/usr/share/mlt/vmfx/filter_chroma.yml
/usr/share/mlt/vmfx/filter_chroma_hold.yml
/usr/share/mlt/vmfx/filter_mono.yml
/usr/share/mlt/vmfx/filter_shape.yml
/usr/share/mlt/vmfx/producer_pgm.yml
/usr/share/mlt/xml/consumer_xml.yml
/usr/share/mlt/xml/mlt-xml.dtd
/usr/share/mlt/xml/producer_xml-nogl.yml
/usr/share/mlt/xml/producer_xml-string.yml
/usr/share/mlt/xml/producer_xml.yml

%files dev
%defattr(-,root,root,-)
/usr/include/mlt++/Mlt.h
/usr/include/mlt++/MltAnimation.h
/usr/include/mlt++/MltAudio.h
/usr/include/mlt++/MltConfig.h
/usr/include/mlt++/MltConsumer.h
/usr/include/mlt++/MltDeque.h
/usr/include/mlt++/MltEvent.h
/usr/include/mlt++/MltFactory.h
/usr/include/mlt++/MltField.h
/usr/include/mlt++/MltFilter.h
/usr/include/mlt++/MltFilteredConsumer.h
/usr/include/mlt++/MltFilteredProducer.h
/usr/include/mlt++/MltFrame.h
/usr/include/mlt++/MltGeometry.h
/usr/include/mlt++/MltMultitrack.h
/usr/include/mlt++/MltParser.h
/usr/include/mlt++/MltPlaylist.h
/usr/include/mlt++/MltProducer.h
/usr/include/mlt++/MltProfile.h
/usr/include/mlt++/MltProperties.h
/usr/include/mlt++/MltPushConsumer.h
/usr/include/mlt++/MltRepository.h
/usr/include/mlt++/MltService.h
/usr/include/mlt++/MltTokeniser.h
/usr/include/mlt++/MltTractor.h
/usr/include/mlt++/MltTransition.h
/usr/include/mlt/framework/mlt.h
/usr/include/mlt/framework/mlt_animation.h
/usr/include/mlt/framework/mlt_audio.h
/usr/include/mlt/framework/mlt_cache.h
/usr/include/mlt/framework/mlt_consumer.h
/usr/include/mlt/framework/mlt_deque.h
/usr/include/mlt/framework/mlt_events.h
/usr/include/mlt/framework/mlt_factory.h
/usr/include/mlt/framework/mlt_field.h
/usr/include/mlt/framework/mlt_filter.h
/usr/include/mlt/framework/mlt_frame.h
/usr/include/mlt/framework/mlt_geometry.h
/usr/include/mlt/framework/mlt_log.h
/usr/include/mlt/framework/mlt_luma_map.h
/usr/include/mlt/framework/mlt_multitrack.h
/usr/include/mlt/framework/mlt_parser.h
/usr/include/mlt/framework/mlt_playlist.h
/usr/include/mlt/framework/mlt_pool.h
/usr/include/mlt/framework/mlt_producer.h
/usr/include/mlt/framework/mlt_profile.h
/usr/include/mlt/framework/mlt_properties.h
/usr/include/mlt/framework/mlt_property.h
/usr/include/mlt/framework/mlt_repository.h
/usr/include/mlt/framework/mlt_service.h
/usr/include/mlt/framework/mlt_slices.h
/usr/include/mlt/framework/mlt_tokeniser.h
/usr/include/mlt/framework/mlt_tractor.h
/usr/include/mlt/framework/mlt_transition.h
/usr/include/mlt/framework/mlt_types.h
/usr/include/mlt/framework/mlt_version.h
/usr/lib64/libmlt++.so
/usr/lib64/libmlt.so
/usr/lib64/pkgconfig/mlt++.pc
/usr/lib64/pkgconfig/mlt-framework.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmlt++.so.3
/usr/lib64/libmlt++.so.6.22.1
/usr/lib64/libmlt.so.6
/usr/lib64/libmlt.so.6.22.1
/usr/lib64/mlt/libmltcore.so
/usr/lib64/mlt/libmltdecklink.so
/usr/lib64/mlt/libmltgdk.so
/usr/lib64/mlt/libmltkdenlive.so
/usr/lib64/mlt/libmltoldfilm.so
/usr/lib64/mlt/libmltplus.so
/usr/lib64/mlt/libmltrtaudio.so
/usr/lib64/mlt/libmltsdl2.so
/usr/lib64/mlt/libmltsox.so
/usr/lib64/mlt/libmltvmfx.so
/usr/lib64/mlt/libmltxml.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mlt/2627ff03833f74ed51a7f43c55d30b249b6a0707
/usr/share/package-licenses/mlt/3704f4680301a60004b20f94e0b5b8c7ff1484a9
