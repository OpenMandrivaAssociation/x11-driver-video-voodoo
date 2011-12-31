Name: x11-driver-video-voodoo
Version: 1.2.4
Release: 7
Summary: The X.org video driver for Voodoo1 and Voodoo2 video adapters
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-voodoo-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0
Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-voodoo is the X.org video driver for Voodoo1 and Voodoo2
video adapters.

%prep
%setup -qn xf86-video-voodoo-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/voodoo_drv.so
%{_mandir}/man4/voodoo.*

