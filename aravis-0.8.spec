%global majorversion 0.8
Name:		aravis-%{majorversion}
Version:	0.8.16
Release:	1%{?dist}
Summary:	Aravis digital video camera acquisition library

Group:		Development/Libraries
License:	GPLv2+
URL:		https://github.com/AravisProject/aravis
Source0:	https://github.com/AravisProject/aravis/releases/download/%{version}/aravis-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gtk-doc
BuildRequires:	gobject-introspection-devel
BuildRequires:	pkgconfig(glib-2.0) >= 2.26
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(gstreamer-base-1.0) >= 1.0
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(audit)

Requires:	glib2 >= 2.26
Requires:	libxml2

%description
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements the gigabit ethernet and USB3 protocols used by industrial cameras.

%package devel
Summary:	Aravis digital video camera acquisition library -- Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	pkgconfig(glib-2.0) >= 2.26
Requires:	pkgconfig(gobject-2.0)
Requires:	pkgconfig(gio-2.0)
Requires:	pkgconfig(libxml-2.0)
Requires:	pkgconfig(gthread-2.0)

%description devel
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements the gigabit ethernet and USB3 protocols used by industrial cameras.

This package contains the development files for Aravis.

%package viewer
Summary:	Aravis digital video camera acquisition library -- Viewer
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libnotify
Requires:	gtk3
Requires:	gstreamer1-plugins-base
Requires:	gstreamer1-plugins-good
Requires:	gstreamer1-plugins-bad-free
Obsoletes:	aravis-0.4-viewer <= 0.5

%description viewer
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements the gigabit ethernet and USB3 protocols used by industrial cameras.

This package contains the simple video viewer application.

%package gstreamer1

Summary:	Aravis digital video camera acquisition library -- GStreamer 1.0 plugin
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gstreamer1-plugins-base

%description gstreamer1
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements the gigabit ethernet and USB3 protocols used by industrial cameras.

This package contains the GStreamer plugin.

%prep
%setup -q -n aravis-%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

desktop-file-install --vendor=""						\
       --dir=%{buildroot}%{_datadir}/applications/				\
       %{buildroot}%{_datadir}/applications/arv-viewer-%{majorversion}.desktop

%post viewer
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun viewer
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%files
%{_bindir}/arv-tool-*
%{_bindir}/arv-camera-test-*
%{_bindir}/arv-fake-gv-camera-*
%{_bindir}/arv-test-*
%{_libdir}/lib%{name}*.so.*
%{_libdir}/girepository-1.0/*
%{_mandir}/man1/arv-tool-0.8.1.gz

%files devel
%{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/*
%{_libdir}/lib%{name}.so

%files -f %{name}.lang viewer
%{_bindir}/arv-viewer-*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/arv-viewer-*.desktop
%{_datadir}/metainfo/arv-viewer-*.appdata.xml
%{_mandir}/man1/arv-viewer-*.1.gz

%files gstreamer1
%{_libdir}/gstreamer-1.0/*

%changelog
* Fri Jul 30 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.16-1
New upstream release

  * ci: use Github actions for linux and macOS (Emmanuel)
  * ci: minGW support (Václav)
  * gigevision: use proper broadcast addressese during discovery (Václav)
  * camera: accessor to float feature increment (Emmanuel)
  * camera: make set_trigger more robust (Emmanuel)
  * camera: fallback to Continuous mode if SingleFrame is not available
    (Emmanuel)
  * viewer: allow to save a snapshot as png or jpeg image (Emmanuel)
  * viewer: display all pixel formats in selector (Emmanuel)
  * simulator: now works on Windows and macOS (Václav, Emmanuel)
  * debug: fix output on Windows (Václav)
  * doc: Windows build documentation (Václav)
  * tests: new arv-test application for automated testing (Emmanuel)

* Tue Jul 20 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.15-1
New upstream release

  * gigevision: only disable packet resend after a packet unavailable error
  * gigevision: add a new packet timeout for first packet resend request
  * doc: improve GvStream property documentation
  * code cleanup

* Tue Jul 13 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.14-1
New upstream release

 * debug: fix debug timestamp on older platforms (Emmanuel)

* Tue Jul 13 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.13-1
New upstream release

  * viewer: fix incorrect bandwith and frame rate computation

* Tue Jul 13 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.12-1
New upstream release

  * usb3vision: initialize stream infos

* Tue Jul 13 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.11-1
New upstream release

  * stream: add an extensible info API (Emmanuel)
  * gvstream: improve packet resend request behaviour in case of unordered gvsp
    packets (Emmanuel)
  * gvstream: wait for thread setup during ArvGvStream initialization (Emmanuel)
  * gigevision: use MAC as serial number fallback (Emmanuel)
  * genicam: fix arv_exposure_mode_to_string (Martin)
  * usb3vision: improve error reporting in case of libsub error (Emmanuel)
  * usb3vision: automatically detach kernel driver (Emmanuel)
  * cameratest: add a test duration parameter (Emmanuel)
  * misc: rename internal ArvStatistic to ArvHistogram (Emmanuel)

* Wed May 12 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.10-1
New upstream release

  * arv-tool: make device enumeration faster (Emmanuel)
  * debug: rework debug log levels (Emmanuel)
  * fakegvcamera: improve streaming reliability - partly fix #499 (Emmanuel)
  * gvstream: fix use after reference release - fix #504 (Emmanuel)
  * genicam: String node support - fix #507 (Emmanuel)

* Thu Apr 22 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.9-1
New upstream release

  * windows: build fix (Emmanuel)

* Wed Apr 21 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.8-1
New upstream release

  * arv-camera-test: promote to installed application (Emmanuel)
  * applications: fix policy parameter consistency (Emmanuel)
  * debug: timestamped and modernized output (Emmanuel)
  * genicam: add a range check debug mode (Emmanuel)
  * gvdevice: faster finalization (Emmanuel)
  * camera: new DeviceSerialNumber getter (Emmanuel)

* Sun Mar 28 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.7-1
New upstream release

  * camera: ignore Acquisitiontart feature setting failure (Emmanuel)
  * camera: fix trigger setting for Basler cameras (Casperoo)
  * camera: add set_exposure API (Emmanuel)
  * gigevision: Windows support (Václav)
  * usb3vision: better error packet handling (Emmanuel)
  * genicam: allow get/set float from an int node (Emmanuel)
  * genicam: allow multiple pIndex property nodes (Emmanuel)

* Sun Mar 28 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.6-1
New upstream release

  * camera: handle GainRaw also as a float feature
  * camera: add arv_camera_new_with_device()
  * camera: ignore error on TriggerSelector and TriggerMode setting in arv_camera_set_trigger()
  * gigevision: fail quicker if a device is not found at ArvGvDevice instantiation
  * fakegvcamera: fix interface selection
  * genicam: implement optional range check for integer and float node values, as a runtime option
  * genicam: fix min/max computation for StructEntry and MaskedIntReg nodes
  * gstplugin: don't fail camera init if gain or exposure features are not available

* Sun Mar 28 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.5-1
New upstream release

  * macOS: build fix
  * travis:enable macOS

* Sun Mar 28 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.4-1
New upstream release

  * all: s/adjustement/adjustment/

* Sun Mar 28 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.3-1
New upstream release

  * gigevision: automatically adjust packet size if needed (Emmanuel)
  * gstreamer: don't try to set frame rate if feature is not available (Emmanuel)
  * genicam: fix pVariable name with dot (Arrigo)
  * genicam: fix parsing of genicam data url (Emmanuel)
  * buffer: add arv_buffer_set_frame_id API (Russel)
  * usb3vision: add Dahua Technology USB id (H.F)
  * build: preparatory work for windows compilation (Eudoxos)

* Sun Mar 28 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.2-1
New upstream release

  * gvdevice: fix timeout race (casperoo)
  * fakecamera: implement Mono16 pixel format (Hinko)
  * Enable ppc64le in CI pipeline (nagesh)

* Sun Mar 28 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.1-1
New upstream release

  * build: add more compilation warnings and fix them (Emmanuel)

* Sun Mar 28 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.8.0-1
New upstream release

  * gigevision: ExtendedIds support (Hendrick, Emmanuel)
  * gigevision: add get_control_access API (casperoo)
  * genicam: implement proper AccessMode and ImposedAccessMode support (Siim)
  * genicam: add or extend support for Representation, Unit, DisplayNotation and DisplayPrecision proerties (Siim)
  * genicam: extend GcRregisterDescriptionNode API (Siim)
  * genicam: improve String register (Siim)
  * genicam: implement arv_gc_feature_get_name_space() (Siim)
  * gst-plugin: don't shadow GstBaseSrc num-buffers property (Marko)
  * usb3vision: add Daheng Imaging descriptors (Jakob)

* Sun Mar 28 2021 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.7.5-1
New upstream release

  * gst-plugin: error handling and lock fixes (Marko)
  * build: fix when aravis is used as a subproject (Rihards)
  * build: fix viewer build without libusb (Guillaume)
  * fake camera: implement bayer pixel formats (Bernardo)
  * gcregister: don't try to read WO registers (Stefan)
  * viewer: fix buffer leak (Emmanuel)
  * gvstream: correctly handle resend request limit (Emmanuel)
  * stream: device reference leak fix (Emmanuel)

* Mon Apr 20 2020 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.7.4-1
New upstream release

  * camera/device/stream: add an error parameter to object intantiation functions (Emmanuel)
  * camera: fix node type mismatch error in set_frame_rate (Arkadiusz)
  * gigevision: ignore duplicated packets (Joris)
  * build: make build of tests optional (Edgar)
  * all: use gobject macros for class declarations (Emmanuel)
  * camera: add a GError parameter to most functions (Emmanuel)
  * python: add python tests in test suite (Emmanuel)
  * usb3vision: improve reliability of camera connection (Dmitry)
  * introspection: fix PixefFormat type (Léo, Maarten)

* Fri Oct 18 2019 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.7.2-1
New upstream release

  * gigevision: support for ImageExtendedChunkPayload (Nathan)
  * chunkparser: add a GError parameter to the getters (Emmanuel)
  * chunkparser: add a boolean accessor (Emmanuel)
  * arvtool: new `values` command that show the values of all available features (Emmanuel)
  * gcport: don't try to read a register when the port is an event (Emmanuel)
  * genicam: pSelect support (Emmanuel)
  * genicam: remove value_type property, replaced by ARV_IS_GC_(FLOAT|INTEGER`BOOLEAN|STRING|ENUMERATION) (Emmanuel)
  * genicam: simplify read/write feature values as/from string (Emmanuel)
  * genicam: fix min/max of non 64 bit integers
  * genicam: Float and Integer now get their min/max also from pValue (Emmanuel)
  * gigevision: correctly detect access denied errors

* Mon Sep 09 2019 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.7.0-1
New upstream release

* Tue May 28 2019 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.6.3-1
New upstream release

  * device: fix get_status return value
  * gigevision: add more pixel format enums

* Thu Apr 25 2019 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.6.2-1
New upstream release

  * stream: add stop/start thread API
  * gigevision: allow to discover more devices
  * gigevision: stop stream thread quicker
  * genicam: add <Register> element support
  * genicam: let float node point to integer node
  * usb3vision: sanity checks during device initialization

* Tue Feb 05 2019 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.6.1-1
New upstream release

  * gigevision: auto-packet size negociation improvements
  * gigevision: interface addess assignment improvement
  * usb3vision: memory leak fixes
  * usb3vision: payload size computation fixes
  * camera: avoid clashes in device id generation
  * genicam: signedness and endianness related fix
  * usb3vision: chunk data support
  * camera: matrix vision device support
  * camera: PointGrey / FLIR renaming support
  * i18n: czech and slovak translations
  * build: remove libcap-ng dependency

* Fri Nov 10 2017 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.5.10-1
New upstream release

* Thu Mar 16 2017 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.5.7-2
Make viewer package obsolete 0.4 version

* Wed Feb 22 2017 Mark Harfouche <mark.harfouche@gmail.com> 0.5.7-1
New upstream release

  * Changing the name to aravis-0.6
  * Enabled usb support
  * Enabled packet-socket

* Wed Feb 22 2017 Mark Harfouche <mark.harfouche@gmail.com> 0.4.1-2
Changing the name to aravis-0.4

* Sat Jan 17 2015 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.3.7-1
New upstream release

  * genicam: fix accuracy of division of integers
  * new arv_make_high_priority and arv_make_realtime API
  * viewer: make stream thread realtime if possible
  * camera: add GigEVision specific API for packet delay, packet size and stream selection
  * gst_pugins: add a number of buffers property
  * build fixes
  * translation updates

* Sat Nov 15 2014 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.3.6-1
New upstream release

  * camera: new abort_acquisition function
  * gv_stream: missing frame detection fix
  * buffer: user_data and frame_id accessors
  * chunk_parser: bug fixes
  * viewer: prevent use of broken coglsink from autovideosink
  * translations: updates

* Wed Aug 20 2014 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.3.5-1
Update to aravis 0.3.5

  * ArvChunkParser API for Chunk Data support
  * Make ArvBuffer internal data private

* Fri Aug 15 2014 Emmanuel Pacaud <emmanuel.pacaud@free.fr> 0.3.4-2
Fix aravis-viewer dependency
