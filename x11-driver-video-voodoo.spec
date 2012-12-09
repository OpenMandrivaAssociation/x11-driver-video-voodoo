Name: x11-driver-video-voodoo
Version: 1.2.5
Release: 9
Summary: The X.org video driver for Voodoo1 and Voodoo2 video adapters
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-voodoo-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
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



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.5-8
+ Revision: 810694
- version update 1.2.5

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.4-8
+ Revision: 787290
- Rebuild for x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.4-7
+ Revision: 748504
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.4-6
+ Revision: 703686
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.2.4-5
+ Revision: 683593
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-4
+ Revision: 671187
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.4-3mdv2011.0
+ Revision: 595725
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.4-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Thu Jul 22 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.4-1mdv2011.0
+ Revision: 557071
- New version: 1.2.4

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2.3-1mdv2010.0
+ Revision: 407746
- new release

* Thu Feb 26 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 345056
- new release
- fix group

  + Colin Guthrie <cguthrie@mandriva.org>
    - Rebuild for new xserver

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.0-3mdv2009.1
+ Revision: 308271
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 266024
- rebuild early 2009.0 package (before pixel changes)
- improved description

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194130
- Update to version 1.2.0.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-4mdv2008.1
+ Revision: 166221
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-3mdv2008.1
+ Revision: 156631
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-2mdv2008.1
+ Revision: 154768
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update to use existing tag xf86-video-voodoo-1.1.1, and add patches up to
  mandriva branch.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-1mdv2008.1
+ Revision: 99040
- new upstream version: 1.1.1
- minor spec cleanup

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2008.0
+ Revision: 75826
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

