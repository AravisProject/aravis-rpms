Name:		aravis
Version:	0.5.7
Release:	1%{?dist}
Summary:	Aravis digital video camera acquisition library

Group:		Development/Libraries
License:	GPLv2+
URL:		http://live.gnome.org/Aravis
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.5/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
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
BuildRequires:	pkgconfig(libcap-ng)
BuildRequires:	pkgconfig(audit)

%global  majorversion 0.6
%global fullname %{name}-%{majorversion}

Requires:	glib2 >= 2.26
Requires:	libxml2

%description
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements the gigabit ethernet and USB3 (Since Aravis 0.5.x) protocols used by industrial cameras. 

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
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements the gigabit ethernet and USB3 (Since Aravis 0.5.x) protocols used by industrial cameras. 

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

%description viewer
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements the gigabit ethernet and USB3 (Since Aravis 0.5.x) protocols used by industrial cameras. 

This package contains the simple video viewer application.

%package static
Summary:	Aravis digital video camera acquisition library -- Static development files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements the gigabit ethernet and USB3 (Since Aravis 0.5.x) protocols used by industrial cameras. 

This package contains the static development files for Aravis.

%package gstreamer1

Summary:	Aravis digital video camera acquisition library -- GStreamer 1.0 plugin
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gstreamer1-plugins-base

%description gstreamer1
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements the gigabit ethernet and USB3 (Since Aravis 0.5.x) protocols used by industrial cameras. 

This package contains the GStreamer plugin.

%prep
%setup -q

%build
%configure --enable-usb --enable-packet-socket --enable-viewer --enable-gst-plugin --disable-gst-0.10-plugin
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{fullname}
desktop-file-install --vendor=""						\
       --dir=%{buildroot}%{_datadir}/applications/				\
       %{buildroot}%{_datadir}/applications/arv-viewer.desktop

# remove .la files
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'

# bug, these should never exist in the first place
rm %{buildroot}%{_datadir}/%{fullname}/arvviewer.h
rm %{buildroot}%{_datadir}/%{fullname}/arvviewertypes.h

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
%{_bindir}/arv-tool-%{majorversion}
%{_bindir}/arv-fake-gv-camera-%{majorversion}
%{_libdir}/lib%{fullname}*.so.*
%{_libdir}/girepository-1.0/*
%{_docdir}/%{name}/%{fullname}
%{_datadir}/%{fullname}/*.xml

%files devel
%{_includedir}/%{fullname}
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/*
%{_datadir}/gtk-doc/html/%{fullname}
%{_libdir}/lib%{fullname}*.so

%files static
%{_libdir}/lib%{fullname}*.a

%files -f %{fullname}.lang viewer
%{_bindir}/arv-viewer
%{_datadir}/%{fullname}/*.ui
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/arv-viewer.desktop
%{_datadir}/appdata/arv-viewer.appdata.xml

%files gstreamer1
%{_libdir}/gstreamer-1.0/*

%changelog
* Tue Feb 21 2017 Mark Harfouche <mark.harfouche@gmail.com> 0.5.7
- New upstream release
- Enabled usb support
- Enabled packet-socket

* Sat Jan 17 2015 Emmanuel Pacaud <emmanuel@gnome.org> 0.3.7.1
- New upstream release
- genicam: fix accuracy of division of integers
- new arv_make_high_priority and arv_make_realtime API
- viewer: make stream thread realtime if possible
- camera: add GigEVision specific API for packet delay, packet size and stream selection
- gst_pugins: add a number of buffers property
- build fixes
- translation updates

* Sat Nov 15 2014 Emmanuel Pacaud <emmanuel@gnome.org> 0.3.6.1
- New upstream release
- camera: new abort_acquisition function
- gv_stream: missing frame detection fix
- buffer: user_data and frame_id accessors
- chunk_parser: bug fixes
- viewer: prevent use of broken coglsink from autovideosink
- translations: updates

* Wed Aug 20 2014 Emmanuel Pacaud <emmanuel@gnome.org> 0.3.5-1
- Update to aravis 0.3.5
- ArvChunkParser API for Chunk Data support
- Make ArvBuffer internal data private

* Fri Aug 15 2014 Emmanuel Pacaud <emmanuel@gnome.org> 0.3.4-2
- Fix aravis-viewer dependency
