#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC76BB9FEEAD12EA7 (hpj@cl.no)
#
Name     : desktop-file-utils
Version  : 0.26
Release  : 17
URL      : https://www.freedesktop.org/software/desktop-file-utils/releases/desktop-file-utils-0.26.tar.xz
Source0  : https://www.freedesktop.org/software/desktop-file-utils/releases/desktop-file-utils-0.26.tar.xz
Source1  : desktop-file-utils.tmpfiles
Source2  : mime-update.service
Source3  : https://www.freedesktop.org/software/desktop-file-utils/releases/desktop-file-utils-0.26.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: desktop-file-utils-bin = %{version}-%{release}
Requires: desktop-file-utils-config = %{version}-%{release}
Requires: desktop-file-utils-data = %{version}-%{release}
Requires: desktop-file-utils-license = %{version}-%{release}
Requires: desktop-file-utils-man = %{version}-%{release}
Requires: desktop-file-utils-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(glib-2.0)
Patch1: 0001-update-desktop-database-add-output-option.patch

%description
desktop-file-utils
==================
http://www.freedesktop.org/wiki/Software/desktop-file-utils

%package bin
Summary: bin components for the desktop-file-utils package.
Group: Binaries
Requires: desktop-file-utils-data = %{version}-%{release}
Requires: desktop-file-utils-config = %{version}-%{release}
Requires: desktop-file-utils-license = %{version}-%{release}
Requires: desktop-file-utils-services = %{version}-%{release}

%description bin
bin components for the desktop-file-utils package.


%package config
Summary: config components for the desktop-file-utils package.
Group: Default

%description config
config components for the desktop-file-utils package.


%package data
Summary: data components for the desktop-file-utils package.
Group: Data

%description data
data components for the desktop-file-utils package.


%package license
Summary: license components for the desktop-file-utils package.
Group: Default

%description license
license components for the desktop-file-utils package.


%package man
Summary: man components for the desktop-file-utils package.
Group: Default

%description man
man components for the desktop-file-utils package.


%package services
Summary: services components for the desktop-file-utils package.
Group: Systemd services

%description services
services components for the desktop-file-utils package.


%prep
%setup -q -n desktop-file-utils-0.26
cd %{_builddir}/desktop-file-utils-0.26
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593712682
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/desktop-file-utils
cp %{_builddir}/desktop-file-utils-0.26/COPYING %{buildroot}/usr/share/package-licenses/desktop-file-utils/4cc77b90af91e615a64ae04893fdffa7939db84c
DESTDIR=%{buildroot} ninja -C builddir install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/mime-update.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/desktop-file-utils.conf
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/
ln -s ../mime-update.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/mime-update.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/desktop-file-edit
/usr/bin/desktop-file-install
/usr/bin/desktop-file-validate
/usr/bin/update-desktop-database

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/desktop-file-utils.conf

%files data
%defattr(-,root,root,-)
/usr/share/emacs/site-lisp/desktop-entry-mode.el

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/desktop-file-utils/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/desktop-file-edit.1
/usr/share/man/man1/desktop-file-install.1
/usr/share/man/man1/desktop-file-validate.1
/usr/share/man/man1/update-desktop-database.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/mime-update.service
/usr/lib/systemd/system/update-triggers.target.wants/mime-update.service
