# Aravis spec file

This is a spec file for building aravis rpms on a Fedora installation.

Aravis is split in 4 RPMs:

* aravis and aravis-devel, which contain respectively the library and the development files
* aravis-gstreamer1 provides a GStreamer 1.x plugin
* aravis-viewer embeds the viewer, and depends on gtk

Built RPMs are available on Fedora's Copr:

https://copr.fedorainfracloud.org/coprs/emmanuelp/Aravis/

### Srpm build 

rpmbuild -ba aravis.spec

### Mock

mock -r fedora-24-x86_64 rebuild aravis-x.y.z-a.srpm
