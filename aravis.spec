Name:		aravis		
Version:	0.3.4
Release:	2%{?dist}
Summary:	Aravis digital video camera acquisition library

Group:		Development/Libraries
License:	GPLv2+
URL:		http://live.gnome.org/Aravis
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.3/%{name}-%{version}.tar.xz

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

Source10:	aravis.png

%global fullname %{name}-0.4

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

%description viewer
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently only implements an ethernet camera protocol used for industrial cameras. 

This package contains the simple video viewer application.

%package gstreamer1

Summary:	Aravis digital video camera acquisition library -- GStreamer 1.0 plugin
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gstreamer1-plugins-base

%description gstreamer1
Aravis is a glib/gobject based library for video acquisition using Genicam cameras. It currently only implements an ethernet camera protocol used for industrial cameras. 

This package contains the GStreamer plugin.

%prep
%setup -q

%build
%configure --enable-viewer --enable-gst-plugin
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{fullname}
desktop-file-install --vendor=""						\
       --dir=%{buildroot}%{_datadir}/applications/				\
       %{buildroot}%{_datadir}/applications/arv-viewer.desktop

%files
%{_bindir}/arv-tool-0.4
%{_bindir}/arv-fake-gv-camera-0.4
%{_datadir}/%{fullname}/*.xml
%{_libdir}/lib%{fullname}*
%{_libdir}/girepository-1.0/*
/usr/doc/%{fullname}

%files devel
%{_datadir}/gtk-doc/html/%{fullname}
%{_includedir}/%{fullname}
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/*

%files -f %{fullname}.lang viewer
%{_bindir}/arv-viewer
%{_datadir}/%{fullname}/*.ui
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_datadir}/applications/arv-viewer.desktop
%{_datadir}/appdata/arv-viewer.appdata.xml

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

%files gstreamer1
%{_libdir}/gstreamer-1.0/*

%changelog

* Fri Aug 15 2014 Emmanuel Pacaud <emmanuel@gnome.org> 0.3.4-2
- Fix aravis-viewer dependency
