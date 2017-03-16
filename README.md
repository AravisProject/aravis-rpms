# Aravis spec file

This is a set of spec files for building aravis rpms on a Fedora installation.

Aravis is split in 5 RPMs:

* aravis-0.x and aravis-0.x-devel, which contain respectively the library and the development files
* aravis-0.x-gstreamer1 provides a GStreamer 1.x plugin
* aravis-0.x-viewer embeds the viewer, and depends on gtk
* aravis-0.x-static which contains the static library

Built RPMs are available on Fedora's Copr:

https://copr.fedorainfracloud.org/coprs/emmanuelp/Aravis/

### Srpm build

```
rpmbuild -ba aravis-0.4.spec
rpmbuild -ba aravis-0.6.spec
```

### Mock

```
mock -r fedora-24-x86_64 rebuild aravis-0.4-x.y.z-a.srpm
mock -r fedora-24-x86_64 rebuild aravis-0.6-x.y.z-a.srpm
```
