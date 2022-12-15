%define _disable_ld_no_undefined 1

Summary:	The X.org video driver for Voodoo1 and Voodoo2 video adapters
Name:		x11-driver-video-voodoo
Version:	1.2.6
Release:	1
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-voodoo-%{version}.tar.xz
Patch1:		U_don-t-use-PCITAG-in-struct-anymore.patch
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-voodoo is the X.org video driver for Voodoo1 and Voodoo2
video adapters.

%prep
%setup -qn xf86-video-voodoo-%{version}
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/voodoo_drv.so
%{_mandir}/man4/voodoo.*

