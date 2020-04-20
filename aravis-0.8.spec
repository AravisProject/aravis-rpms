%global majorversion 0.8
Name:		aravis-%{majorversion}
Version:	0.7.4
Release:	1%{?dist}
Summary:	Aravis digital video camera acquisition library

Group:		Development/Libraries
License:	GPLv2+
URL:		https://github.com/AravisProject/aravis
Source0:	https://ftp.gnome.org/pub/gnome/sources/aravis/0.7/aravis-%{version}.tar.xz

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
%{_bindir}/arv-fake-gv-camera-*
%{_datadir}/%{name}/*.xml
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
* Mon Apr 20 2020 Emmanuel Pacaud <emmanuel@gnome.org> 0.7.4-1
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

* Fri Oct 18 2019 Emmanuel Pacaud <emmanuel@gnome.org> 0.7.2-1
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

* Mon Sep 09 2019 Emmanuel Pacaud <emmanuel@gnome.org> 0.7.0-1
New upstream release

* Tue May 28 2019 Emmanuel Pacaud <emmanuel@gnome.org> 0.6.3-1
New upstream release

  * device: fix get_status return value
  * gigevision: add more pixel format enums

* Thu Apr 25 2019 Emmanuel Pacaud <emmanuel@gnome.org> 0.6.2-1
New upstream release

  * stream: add stop/start thread API
  * gigevision: allow to discover more devices
  * gigevision: stop stream thread quicker
  * genicam: add <Register> element support
  * genicam: let float node point to integer node
  * usb3vision: sanity checks during device initialization

* Tue Feb 05 2019 Emmanuel Pacaud <emmanuel@gnome.org> 0.6.1-1
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

* Fri Nov 10 2017 Emmanuel Pacaud <emmanuel@gnome.org> 0.5.10-1
New upstream release

* Thu Mar 16 2017 Emmanuel Pacaud <emmanuel@gnome.org> 0.5.7-2
Make viewer package obsolete 0.4 version

* Wed Feb 22 2017 Mark Harfouche <mark.harfouche@gmail.com> 0.5.7-1
New upstream release

  * Changing the name to aravis-0.6
  * Enabled usb support
  * Enabled packet-socket

* Wed Feb 22 2017 Mark Harfouche <mark.harfouche@gmail.com> 0.4.1-2
Changing the name to aravis-0.4

* Sat Jan 17 2015 Emmanuel Pacaud <emmanuel@gnome.org> 0.3.7-1
New upstream release

  * genicam: fix accuracy of division of integers
  * new arv_make_high_priority and arv_make_realtime API
  * viewer: make stream thread realtime if possible
  * camera: add GigEVision specific API for packet delay, packet size and stream selection
  * gst_pugins: add a number of buffers property
  * build fixes
  * translation updates

* Sat Nov 15 2014 Emmanuel Pacaud <emmanuel@gnome.org> 0.3.6-1
New upstream release

  * camera: new abort_acquisition function
  * gv_stream: missing frame detection fix
  * buffer: user_data and frame_id accessors
  * chunk_parser: bug fixes
  * viewer: prevent use of broken coglsink from autovideosink
  * translations: updates

* Wed Aug 20 2014 Emmanuel Pacaud <emmanuel@gnome.org> 0.3.5-1
Update to aravis 0.3.5

  * ArvChunkParser API for Chunk Data support
  * Make ArvBuffer internal data private

* Fri Aug 15 2014 Emmanuel Pacaud <emmanuel@gnome.org> 0.3.4-2
Fix aravis-viewer dependency