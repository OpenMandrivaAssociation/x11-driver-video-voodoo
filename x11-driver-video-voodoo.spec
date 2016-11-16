%define _disable_ld_no_undefined 1

Summary:	The X.org video driver for Voodoo1 and Voodoo2 video adapters
Name:		x11-driver-video-voodoo
Version:	1.2.5
Release:	24
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-voodoo-%{version}.tar.bz2
Patch0:		xf86-video-voodoo-1.2.5-remove-miInitializeBackingStore.patch
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
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/voodoo_drv.so
%{_mandir}/man4/voodoo.*

