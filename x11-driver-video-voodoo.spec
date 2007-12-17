Name: x11-driver-video-voodoo
Version: 1.1.1
Release: %mkrel 2
Summary: The X.org video driver for Voodoo1 and Voodoo2 video adapters
Group: Development/X11
URL: http://xorg.freedesktop.org

########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-voodoo  xorg/drivers/xf86-video-voodoo
# cd xorg/drivers/xf86-video/voodoo
# git-archive --format=tar --prefix=xf86-video-voodoo-1.1.1/ master | bzip2 -9 > xf86-video-voodoo-1.1.1.tar.bz2
########################################################################
Source0: xf86-video-voodoo-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
The X.org video driver for Voodoo1 and Voodoo2 video adapters.

%prep
%setup -q -n xf86-video-voodoo-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/voodoo_drv.la
%{_libdir}/xorg/modules/drivers/voodoo_drv.so
%{_mandir}/man4/voodoo.*

