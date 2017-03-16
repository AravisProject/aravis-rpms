%global majorversion 0.4
Name:		aravis-%{majorversion}
Version:	0.4.1
Release:	2%{?dist}
Summary:	Aravis digital video camera acquisition library

Obsoletes: aravis < 0.4.1-2
Obsoletes: aravis-debuginfo < 0.4.1-2

Group:		Development/Libraries
License:	GPLv2+
URL:		http://live.gnome.org/Aravis
Source0:	http://ftp.gnome.org/pub/gnome/sources/aravis/0.4/aravis-%{version}.tar.xz

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

Requires:	glib2 >= 2.26
Requires:	libxml2

%description
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently only implements an ethernet camera protocol used for industrial cameras.

%package devel
Summary:	Aravis digital video camera acquisition library -- Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	pkgconfig(glib-2.0) >= 2.26
Requires:	pkgconfig(gobject-2.0)
Requires:	pkgconfig(gio-2.0)
Requires:	pkgconfig(libxml-2.0)
Requires:	pkgconfig(gthread-2.0)
Obsoletes: aravis-devel < 0.4.1-2

%description devel
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently only implements an ethernet camera protocol used for industrial cameras.

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
Obsoletes: aravis-viewer < 0.4.1-2

%description viewer
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently only implements an ethernet camera protocol used for industrial cameras.

This package contains the simple video viewer application.

%package static
Summary:	Aravis digital video camera acquisition library -- Static development files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently implements an ethernet protocol used by industrial cameras.

This package contains the static development files for Aravis.

%package gstreamer1

Summary:	Aravis digital video camera acquisition library -- GStreamer 1.0 plugin
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gstreamer1-plugins-base
Obsoletes: aravis-gstreamer1 < 0.4.1-2

%description gstreamer1
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently only implements an ethernet camera protocol used for industrial cameras.

This package contains the GStreamer plugin.

%prep
%setup -q -n aravis-%{version}

%build
%configure --enable-viewer --enable-gst-plugin --disable-gst-0.10-plugin
make %{?_smp_mflags}


%install
%make_install
# I think this is fixed in 0.5
mv %{buildroot}/usr/doc %{buildroot}%{_docdir}
%find_lang %{name}
desktop-file-install --vendor=""						\
       --dir=%{buildroot}%{_datadir}/applications/				\
       %{buildroot}%{_datadir}/applications/arv-viewer.desktop

# remove .la files
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'

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
%{_datadir}/%{name}/*.xml
%{_libdir}/lib%{name}*.so.*
%{_libdir}/girepository-1.0/*
%{_docdir}/%{name}

%files devel
%{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/*
%{_libdir}/lib%{name}*.so

%files static
%{_libdir}/lib%{name}*.a

%files -f %{name}.lang viewer
%{_bindir}/arv-viewer
%{_datadir}/%{name}/*.ui
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/arv-viewer.desktop
%{_datadir}/appdata/arv-viewer.appdata.xml

%files gstreamer1
%{_libdir}/gstreamer-1.0/*

%changelog
* Wed Feb 22 2017 Mark Harfouche <mark.harfouche@gmail.com> - 0.4.1-2
- Changing the name to aravis-0.4

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
